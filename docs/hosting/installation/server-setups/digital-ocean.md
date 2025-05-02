---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Hosting n8n on DigitalOcean

คู่มือนี้จะสอนวิธีติดตั้ง n8n แบบ self-host บน DigitalOcean droplet โดยใช้:

* [Caddy](https://caddyserver.com){:target="_blank" .external-link} (reverse proxy) สำหรับเปิดให้เข้าถึง n8n จากอินเทอร์เน็ต และจัดการ SSL/TLS certificate ให้อัตโนมัติ
* [Docker Compose](https://docs.docker.com/compose/){:target="_blank" .external-link} สำหรับจัดการ container ของแต่ละ service

--8<-- "_snippets/self-hosting/warning.md"

--8<-- "_snippets/self-hosting/installation/latest-next-version.md"

## Create a Droplet

1. [Log in](https://cloud.digitalocean.com/login){:target=_blank .external-link} เข้า DigitalOcean
2. เลือก project ที่จะใช้ หรือ [สร้าง project ใหม่](https://docs.digitalocean.com/products/projects/how-to/create/){:target=_blank .external-link}
3. ใน project ของคุณ เลือก **Droplets** จากเมนู **Manage**
4. [สร้าง Droplet ใหม่](https://docs.digitalocean.com/products/droplets/how-to/create/){:target=_blank .external-link} โดยเลือก [Docker image](https://marketplace.digitalocean.com/apps/docker){:target="_blank" .external-link} จากแท็บ **Marketplace**

/// note | Droplet resources
ตอนสร้าง Droplet จะมีให้เลือก plan สำหรับการใช้งานทั่วไป เลือกแบบ shared CPU ธรรมดาก็พอ
///
/// note | SSH key or Password
DigitalOcean ให้เลือกได้ว่าจะใช้ SSH key หรือ password-based authentication แนะนำให้ใช้ SSH key เพราะปลอดภัยกว่า
///
## Log in to your Droplet and create new user

ขั้นตอนต่อไปต้อง SSH เข้าไปที่ Droplet ผ่าน terminal ดูวิธีได้ที่ [How to Connect to Droplets with SSH](https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/){:target="_blank" .external-link}

แนะนำให้สร้าง user ใหม่ ไม่ควรใช้ root

1. ล็อกอินเป็น root
2. สร้าง user ใหม่:
	```shell
	adduser <username>
	```
3. ทำตามขั้นตอนใน CLI เพื่อสร้าง user ให้เสร็จ
4. ให้สิทธิ์ admin กับ user ใหม่:
	```shell
	usermod -aG sudo <username>
	```
	จากนี้จะใช้ `sudo` สั่งงานแบบ admin ได้
5. ตั้งค่า SSH ให้ user ใหม่: [Add Public Key Authentication](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04#step-four-add-public-key-authentication-recommended){:target=_blank .external-link}
5. logout ออกจาก droplet
6. login ใหม่ด้วย SSH เป็น user ที่สร้าง

## Clone configuration repository

Docker Compose, n8n, และ Caddy ต้องใช้ไฟล์ config หลายไฟล์ สามารถ clone repo ตัวอย่างจาก [ที่นี่](https://github.com/n8n-io/n8n-docker-caddy){:target=_blank .external-link} ไปไว้ใน home folder ของ user ที่ล็อกอินอยู่

รันคำสั่งนี้เพื่อ clone:

```shell
git clone https://github.com/n8n-io/n8n-docker-caddy.git
```

แล้วเข้าไปที่โฟลเดอร์ที่ clone มา:

```shell
cd n8n-docker-caddy
```

## Default folders and files

ฝั่ง host (Droplet) จะมี 2 โฟลเดอร์หลักที่ใช้กับ Docker container:

- `caddy_config`: เก็บไฟล์ config ของ Caddy
- `local_files`: สำหรับไฟล์ที่อัปโหลดหรือเพิ่มผ่าน n8n

### Create Docker volumes

สร้าง Docker volume สำหรับ cache ของ Caddy เพื่อให้ start เร็วขึ้น:

```shell
sudo docker volume create caddy_data
```

สร้าง Docker volume สำหรับข้อมูล n8n:

```shell
sudo docker volume create n8n_data
```

## Set up DNS

โดยปกติ n8n จะรันบน subdomain ให้สร้าง DNS record ชนิด "A" ชี้ subdomain ไปที่ IP ของ Droplet วิธีการขึ้นกับผู้ให้บริการ DNS ของคุณ ดูข้อมูลพื้นฐานได้ที่ [An Introduction to DNS Terminology, Components, and Concepts](https://www.digitalocean.com/community/tutorials/an-introduction-to-dns-terminology-components-and-concepts){:target="_blank" .external-link}

## Open ports

n8n เป็น web app ต้องเปิด port 80 (HTTP) และ 443 (HTTPS) ให้เข้าถึงได้

เปิด firewall ด้วยคำสั่ง:

```shell
sudo ufw allow 80
sudo ufw allow 443
```

## Configure n8n

n8n ต้องการ environment variable บางตัวใน container ตัวอย่างไฟล์ `.env` มี placeholder ให้แก้ไข

เปิดไฟล์ด้วย:

```shell
nano .env
```

ในไฟล์จะมี comment อธิบายว่าต้องแก้ตรงไหน

ดูรายละเอียด environment variable เพิ่มเติมได้ที่ [Environment variables](/hosting/configuration/environment-variables/index.md)

## The Docker Compose file

ไฟล์ Docker Compose (`docker-compose.yml`) จะกำหนด service ที่ต้องใช้ (Caddy กับ n8n)

- Caddy: กำหนด port และ volume ที่จะ mount
- n8n: กำหนด port, environment variable (บางตัวมาจาก `.env`), และ volume ที่ต้องใช้

โดยปกติไม่ต้องแก้ไขไฟล์นี้ แต่ถ้าอยากดูให้รัน:

```shell
nano docker-compose.yml
```

## Configure Caddy

Caddy ต้องรู้ว่าจะ serve domain ไหน และเปิด port อะไร แก้ไขไฟล์ `Caddyfile` ในโฟลเดอร์ `caddy_config`

```shell
nano caddy_config/Caddyfile
```

เปลี่ยน subdomain ที่เป็น placeholder ให้เป็นของคุณเอง เช่น ถ้าใช้ `n8n.example.com` ให้แก้ตามนี้ ส่วน `n8n` ใน `reverse_proxy` หมายถึง service ที่กำหนดไว้ใน `docker-compose.yml`:

```text
n8n.<domain>.<suffix> {
    reverse_proxy n8n:5678 {
      flush_interval -1
    }
}
```

ถ้าใช้ `automate.example.com` ก็จะเป็นแบบนี้:

```text
automate.example.com {
    reverse_proxy n8n:5678 {
      flush_interval -1
    }
}
```

## Start Docker Compose

เริ่มรัน n8n กับ Caddy ด้วยคำสั่ง:

```shell
sudo docker compose up -d
```

อาจใช้เวลาสักครู่

## Test your setup

เปิด browser แล้วเข้า URL ที่ตั้งไว้ใน DNS ใส่ username/password ที่ตั้งไว้ ก็จะเข้าใช้งาน n8n ได้

## Stop n8n and Caddy

หยุด n8n กับ Caddy ด้วยคำสั่ง:

```shell
sudo docker compose stop
```
## Updating

--8<-- "_snippets/self-hosting/installation/docker-compose-updating.md"

## Next steps

--8<-- "_snippets/self-hosting/installation/server-setups-next-steps.md"
