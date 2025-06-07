---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
description: ติดตั้งและรัน n8n ด้วย Docker Compose
---

# Docker-Compose

ถ้าคุณติดตั้ง Docker กับ Docker-Compose ไว้แล้ว สามารถข้ามไปเริ่มที่ [step 3](#3-dns-setup) ได้เลย

ดูตัวอย่าง Docker Compose สำหรับสถาปัตยกรรมต่าง ๆ ได้ที่ [n8n-hosting repository](https://github.com/n8n-io/n8n-hosting)

--8<-- "_snippets/self-hosting/warning.md"

--8<-- "_snippets/self-hosting/installation/latest-next-version.md"

## 1. Install Docker and Docker Compose

วิธีติดตั้ง Docker และ Docker Compose จะแตกต่างกันไปตาม Linux distribution ที่ใช้ ดูรายละเอียดได้ที่ [Docker](https://docs.docker.com/engine/install/) และ [Docker Compose](https://docs.docker.com/compose/install/) ตัวอย่างนี้สำหรับ Ubuntu:

```bash
# ลบ Docker เวอร์ชันเก่าหรือที่ไม่เข้ากันออกก่อน
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
# ติดตั้งแพ็กเกจที่จำเป็น
sudo apt-get update
sudo apt-get install ca-certificates curl
# ดาวน์โหลด repo signing key
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
# ตั้งค่า repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# อัปเดตและติดตั้ง Docker กับ Docker Compose
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

ตรวจสอบว่า Docker กับ Docker Compose ใช้งานได้ด้วยคำสั่ง:

```bash
docker --version
docker compose version
```

## 2. Optional: Non-root user access

สามารถตั้งค่าให้ user ปกติรัน Docker ได้โดยไม่ต้องใช้ `sudo`

ถ้าจะให้ user ที่ล็อกอินอยู่ (และมีสิทธิ์ sudo) ใช้ Docker ได้ ให้รัน:

```bash
sudo usermod -aG docker ${USER}
# ลงทะเบียน group docker กับ session ปัจจุบันโดยไม่ต้องเปลี่ยน primary group
exec sg docker newgrp
```

ถ้าจะให้ user อื่นใช้ Docker ได้ ให้รัน (แทนที่ `<USER_TO_RUN_DOCKER>` ด้วยชื่อ user):

```bash
sudo usermod -aG docker <USER_TO_RUN_DOCKER>
```

ต้องรัน `exec sg docker newgrp` ใน session ของ user นั้นเพื่อให้สิทธิ์ใหม่มีผล

ตรวจสอบว่า session ปัจจุบันเห็น group docker หรือยัง ด้วยคำสั่ง:

```bash
groups
```

## 3. DNS setup

ถ้าจะให้ n8n ใช้งานผ่าน network หรือออนไลน์ ให้สร้าง subdomain แล้วชี้ไปที่ server ของคุณ

เพิ่ม A record แบบนี้:

* **Type**: A
* **Name**: `n8n` (หรือ subdomain ที่ต้องการ)
* **IP address**: (IP ของ server คุณ)

## 4. Create an `.env` file

สร้าง project directory สำหรับเก็บไฟล์ config ของ n8n และ Docker Compose แล้วเข้าไปในโฟลเดอร์นั้น:

```bash
mkdir n8n-compose
cd n8n-compose
```

ในโฟลเดอร์ `n8n-compose` สร้างไฟล์ `.env` เพื่อกำหนดค่าต่าง ๆ ของ n8n ตัวอย่างเช่น:

```bash title=".env file"
# DOMAIN_NAME กับ SUBDOMAIN จะเป็นที่อยู่ที่ใช้เข้าถึง n8n
# กำหนด top level domain
DOMAIN_NAME=example.com

# กำหนด subdomain
SUBDOMAIN=n8n

# ตัวอย่างนี้จะเข้า n8n ได้ที่: https://n8n.example.com

# ตั้ง timezone (ใช้กับ Cron และ node scheduling อื่น ๆ)
# ถ้าไม่ตั้งจะใช้ New York เป็นค่า default
GENERIC_TIMEZONE=Asia/Bangkok

# อีเมลที่ใช้สร้าง TLS/SSL certificate
SSL_EMAIL=user@example.com
```

## 5. Create local files directory

ใน project directory ให้สร้างโฟลเดอร์ `local-files` สำหรับแชร์ไฟล์ระหว่าง n8n กับ host (เช่น ใช้กับ [Read/Write Files from Disk node](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md)):

```bash
mkdir local-files
```

Docker Compose file ด้านล่างจะสร้างโฟลเดอร์นี้ให้อัตโนมัติ แต่สร้างเองจะได้สิทธิ์และ owner ถูกต้อง

## 6. Create Docker Compose file

สร้างไฟล์ `docker-compose.yml` แล้ววางเนื้อหานี้ลงไป:

```yaml title="docker-compose.yml file"
services:
  traefik:
    image: "traefik"
    restart: always
    command:
      - "--api=true"
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.web.http.redirections.entryPoint.to=websecure"
      - "--entrypoints.web.http.redirections.entrypoint.scheme=https"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.mytlschallenge.acme.tlschallenge=true"
      - "--certificatesresolvers.mytlschallenge.acme.email=${SSL_EMAIL}"
      - "--certificatesresolvers.mytlschallenge.acme.storage=/letsencrypt/acme.json"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - traefik_data:/letsencrypt
      - /var/run/docker.sock:/var/run/docker.sock:ro

  n8n:
    image: docker.n8n.io/n8nio/n8n
    restart: always
    ports:
      - "127.0.0.1:5678:5678"
    labels:
      - traefik.enable=true
      - traefik.http.routers.n8n.rule=Host(`${SUBDOMAIN}.${DOMAIN_NAME}`)
      - traefik.http.routers.n8n.tls=true
      - traefik.http.routers.n8n.entrypoints=web,websecure
      - traefik.http.routers.n8n.tls.certresolver=mytlschallenge
      - traefik.http.middlewares.n8n.headers.SSLRedirect=true
      - traefik.http.middlewares.n8n.headers.STSSeconds=315360000
      - traefik.http.middlewares.n8n.headers.browserXSSFilter=true
      - traefik.http.middlewares.n8n.headers.contentTypeNosniff=true
      - traefik.http.middlewares.n8n.headers.forceSTSHeader=true
      - traefik.http.middlewares.n8n.headers.SSLHost=${DOMAIN_NAME}
      - traefik.http.middlewares.n8n.headers.STSIncludeSubdomains=true
      - traefik.http.middlewares.n8n.headers.STSPreload=true
      - traefik.http.routers.n8n.middlewares=n8n@docker
    environment:
      - N8N_HOST=${SUBDOMAIN}.${DOMAIN_NAME}
      - N8N_PORT=5678
      - N8N_PROTOCOL=https
      - NODE_ENV=production
      - WEBHOOK_URL=https://${SUBDOMAIN}.${DOMAIN_NAME}/
      - GENERIC_TIMEZONE=${GENERIC_TIMEZONE}
    volumes:
      - n8n_data:/home/node/.n8n
      - ./local-files:/files

volumes:
  n8n_data:
  traefik_data:
```

Docker Compose file นี้จะสร้าง 2 container: n8n กับ [traefik](https://github.com/traefik/traefik) (proxy สำหรับจัดการ TLS/SSL และ routing)

จะมีการสร้างและ mount [Docker Volumes](https://docs.docker.com/engine/storage/volumes/) 2 ตัว และ bind โฟลเดอร์ `local-files` ที่สร้างไว้:

   | Name            | Type                                                        | Container mount   | Description                                                                                                                         |
   |-----------------|-------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|
   | `n8n_data`      | [Volume](https://docs.docker.com/engine/storage/volumes/)   | `/home/node/.n8n` | ที่เก็บ SQLite database และ encryption key ของ n8n                                            |
   | `traefik_data`  | [Volume](https://docs.docker.com/engine/storage/volumes/)   | `/letsencrypt`    | ที่เก็บข้อมูล TLS/SSL certificate ของ traefik                                                |
   | `./local-files` | [Bind](https://docs.docker.com/engine/storage/bind-mounts/) | `/files`          | โฟลเดอร์ local ที่แชร์กับ n8n ใช้ path `/files` ใน n8n เพื่ออ่าน/เขียนไฟล์นี้                |

## 7. Start Docker Compose

เริ่มรัน n8n ด้วยคำสั่ง:

```bash
sudo docker compose up -d
```

ถ้าจะหยุด container ให้ใช้:

```bash
sudo docker compose stop
```

## 8. Done

ตอนนี้สามารถเข้าใช้งาน n8n ได้ที่ subdomain + domain ที่ตั้งไว้ใน `.env` ตัวอย่างเช่น `https://n8n.example.com`

n8n จะเข้าได้เฉพาะผ่าน HTTPS เท่านั้น

## Next steps

--8<-- "_snippets/self-hosting/installation/server-setups-next-steps.md"
