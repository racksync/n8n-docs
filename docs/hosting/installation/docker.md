---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Docker Installation

[Docker](https://www.docker.com/){:target=_blank .external-link} มีข้อดีดังนี้:

* ติดตั้ง n8n ใน environment ที่สะอาด
* ตั้งค่าฐานข้อมูลที่คุณต้องการได้ง่ายขึ้น
* ลดปัญหาเรื่องความแตกต่างของระบบปฏิบัติการ เพราะ Docker ให้ environment ที่เหมือนกัน
* ลดปัญหา compatibility ที่เกิดจากความแตกต่างของ OS และเครื่องมือ
* ช่วยให้ย้ายไปยัง host หรือ environment ใหม่ได้ง่ายขึ้น

คุณสามารถใช้ n8n กับ Docker ร่วมกับ [Docker Compose](/hosting/installation/server-setups/docker-compose.md) ได้ด้วย โดยสามารถดูตัวอย่างไฟล์ Docker Compose สำหรับสถาปัตยกรรมต่างๆ ได้ที่ [n8n-hosting repository](https://github.com/n8n-io/n8n-hosting)

--8<-- "_snippets/self-hosting/warning.md"

## Prerequisites

ก่อนเริ่มต้น ให้ติดตั้ง [Docker Desktop](https://docs.docker.com/get-docker/){:target=_blank .external-link}

/// note | Linux Users
Docker Desktop มีให้สำหรับ Mac และ Windows ส่วน Linux ต้องติดตั้ง [Docker Engine](https://docs.docker.com/engine/install/) และ [Docker Compose](https://docs.docker.com/compose/install/) แยกเองตาม distro ของคุณ
///

--8<-- "_snippets/self-hosting/installation/latest-next-version.md"

## Starting n8n

เปิด terminal แล้วรัน:

```sh
docker volume create n8n_data

docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

คำสั่งนี้จะสร้าง volume สำหรับเก็บข้อมูลถาวร, ดาวน์โหลด image n8n ที่ต้องใช้ และเริ่ม container โดยเปิด port `5678` ให้คุณเข้าใช้งานได้ และ mount docker volume `n8n_data` เพื่อเก็บข้อมูลของคุณไว้ระหว่างที่ container ถูกรีสตาร์ท

เมื่อ container ทำงานแล้ว คุณสามารถเข้าใช้งาน n8n ได้ที่:
[http://localhost:5678](http://localhost:5678)

## Using with PostgreSQL

โดยปกติ n8n จะใช้ SQLite ในการเก็บ [credentials](/glossary.md#credential-n8n), execution ที่ผ่านมา และ workflow ต่างๆ แต่ n8n ก็รองรับ PostgreSQL ด้วย โดยตั้งค่าผ่าน environment variable ตามตัวอย่างด้านล่าง

ถ้าใช้ PostgreSQL ก็ยังควร mount ข้อมูลในโฟลเดอร์ `/home/node/.n8n` ไว้เหมือนเดิม เพราะมีข้อมูล user ของ n8n และที่สำคัญคือ encryption key สำหรับ credentials รวมถึงชื่อ webhook ถ้าใช้ [n8n tunnel](#n8n-with-tunnel)

ถ้า n8n หาโฟลเดอร์ `/home/node/.n8n` ไม่เจอตอนเริ่มต้น มันจะสร้างใหม่ให้เอง ซึ่งจะทำให้ credentials เดิมที่เข้ารหัสด้วย key อันเก่าใช้ไม่ได้

/// note | Keep in mind
แม้จะใช้ PostgreSQL ก็ยังแนะนำให้ mount `/home/node/.n8n` ไว้ แต่ถ้าไม่ mount ก็สามารถกำหนด encryption key เองได้โดยใช้ [`N8N_ENCRYPTION_KEY` environment variable](/hosting/configuration/environment-variables/deployment.md) ตอนสั่งรัน container
///

ถ้าต้องการใช้ n8n กับ PostgreSQL ให้รันคำสั่งนี้ (แทนที่ค่าต่างๆ ใน <> ด้วยค่าจริงของคุณ):

```sh
docker volume create n8n_data

docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e DB_TYPE=postgresdb \
 -e DB_POSTGRESDB_DATABASE=<POSTGRES_DATABASE> \
 -e DB_POSTGRESDB_HOST=<POSTGRES_HOST> \
 -e DB_POSTGRESDB_PORT=<POSTGRES_PORT> \
 -e DB_POSTGRESDB_USER=<POSTGRES_USER> \
 -e DB_POSTGRESDB_SCHEMA=<POSTGRES_SCHEMA> \
 -e DB_POSTGRESDB_PASSWORD=<POSTGRES_PASSWORD> \
 -v n8n_data:/home/node/.n8n \
 docker.n8n.io/n8nio/n8n
```

สามารถดูตัวอย่างไฟล์ `docker-compose` สำหรับ PostgreSQL ได้ที่ [n8n hosting repository](https://github.com/n8n-io/n8n-hosting/tree/main/docker-compose/withPostgres)

## Setting timezone

ถ้าต้องการกำหนด timezone ที่ n8n จะใช้ ให้ตั้งค่า [`GENERIC_TIMEZONE` environment variable](/hosting/configuration/environment-variables/timezone-localization.md) node ที่เกี่ยวกับ schedule เช่น [Schedule Trigger node](/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/index.md) จะใช้ค่านี้ในการกำหนด timezone ที่ถูกต้อง

ถ้าต้องการตั้ง timezone ของระบบ (เช่นเวลาที่แสดงในคำสั่ง `date`) ให้ใช้ environment variable `TZ`

ตัวอย่างนี้ตั้ง timezone ให้ทั้งสองตัวแปร:

```sh
docker volume create n8n_data

docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -e GENERIC_TIMEZONE="Europe/Berlin" \
 -e TZ="Europe/Berlin" \
 -v n8n_data:/home/node/.n8n \
 docker.n8n.io/n8nio/n8n
```

## Updating

ถ้าต้องการอัปเดต n8n ใน Docker Desktop ให้ไปที่แท็บ **Images** แล้วเลือก **Pull** จาก context menu เพื่อดาวน์โหลด image n8n เวอร์ชันล่าสุด

![Docker Desktop](/_images/hosting/installation/docker/docker_desktop.png)

หรือจะใช้ command line เพื่อ pull เวอร์ชันล่าสุดหรือเวอร์ชันที่ต้องการก็ได้:

```sh
# ดึงเวอร์ชันล่าสุด (stable)
docker pull docker.n8n.io/n8nio/n8n

# ดึงเวอร์ชันที่ต้องการ
docker pull docker.n8n.io/n8nio/n8n:1.81.0

# ดึงเวอร์ชัน next (unstable)
docker pull docker.n8n.io/n8nio/n8n:next
```

หลังจาก pull image ใหม่แล้ว ให้หยุด container n8n เดิมแล้วสั่งรันใหม่อีกครั้ง สามารถใช้ command line ได้ โดยแทนที่ `<container_id>` ด้วย container ID ที่ได้จากคำสั่งแรก:

```sh
# ดู container ID
docker ps -a

# หยุด container ที่ต้องการ
docker stop <container_id>

# ลบ container ที่ต้องการ
docker rm <container_id>

# สั่งรัน container ใหม่
docker run --name=<container_name> [options] -d docker.n8n.io/n8nio/n8n
```

### Updating Docker Compose

--8<-- "_snippets/self-hosting/installation/docker-compose-updating.md"

## Further reading

ดูข้อมูลเพิ่มเติมเกี่ยวกับการตั้งค่า Docker ได้ที่ README ของ [Docker image](https://github.com/n8n-io/n8n/tree/master/docker/images/n8n)

--8<-- "_snippets/self-hosting/installation/tunnel.md"

เริ่ม n8n ด้วย `--tunnel` โดยรัน:

```sh
docker volume create n8n_data

docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -v n8n_data:/home/node/.n8n \
 docker.n8n.io/n8nio/n8n \
 start --tunnel
```

## Next steps

--8<-- "_snippets/self-hosting/installation/server-setups-next-steps.md"
