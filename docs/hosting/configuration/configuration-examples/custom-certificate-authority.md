---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ตั้งค่า n8n ให้ใช้ certificate authority ของคุณเอง
description: ปรับแต่ง n8n container ให้ทำงานกับ self signed certificate เมื่อเชื่อมต่อ service
contentType: howto
---

# Configure n8n to use your own certificate authority or self-signed certificate

คุณสามารถเพิ่ม certificate authority (CA) หรือ self-signed certificate ของตัวเองให้กับ n8n ได้ หมายความว่าคุณสามารถเลือก trust SSL certificate เฉพาะที่ต้องการ แทนที่จะ trust ทุก certificate ที่ไม่ถูกต้อง (ซึ่งเสี่ยงเรื่อง security)

/// note | Available in version 1.42.0
ฟีเจอร์นี้ใช้ได้เฉพาะใน n8n เวอร์ชัน 1.42.0 ขึ้นไปเท่านั้น
///

ถ้าจะใช้ฟีเจอร์นี้ ให้นำ certificate ไปไว้ในโฟลเดอร์ แล้ว mount โฟลเดอร์นั้นเข้าไปที่ `/opt/custom-certificates` ใน container

## Docker

ตัวอย่างด้านล่างนี้ สมมติว่าคุณมีโฟลเดอร์ชื่อ `pki` ที่เก็บ certificate อยู่ใน directory เดียวกับที่รันคำสั่ง หรืออยู่ข้าง ๆ ไฟล์ docker compose

### Docker CLI
ถ้าใช้ CLI ให้ใช้ flag `-v` แบบนี้:

```bash
docker run -it --rm \
 --name n8n \
 -p 5678:5678 \
 -v ./pki:/opt/custom-certificates \
 docker.n8n.io/n8nio/n8n
```

### Docker Compose

```yaml
name: n8n
services:
    n8n:
        volumes:
            - ./pki:/opt/custom-certificates
        container_name: n8n
        ports:
            - 5678:5678
        image: docker.n8n.io/n8nio/n8n
```

ควรตั้ง permission ให้ cert ที่ import เข้าไปด้วย สามารถสั่งใน container ได้เลย (สมมติชื่อ container คือ n8n):

```bash
docker exec --user 0 n8n chown -R 1000:1000 /opt/custom-certificates
```
