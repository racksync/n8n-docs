---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Execute Command
description: Documentation for the Execute Command node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: high
---

# Execute Command

Execute Command node ใช้สำหรับรัน shell command บนเครื่องที่รัน n8n อยู่

/// note | Which shell runs the command?
node นี้จะรัน command ใน shell หลักของเครื่องที่รัน n8n เช่น `cmd` บน Windows หรือ `zsh` บน macOS

ถ้าคุณรัน n8n ด้วย Docker command จะถูกรันใน container ของ n8n ไม่ใช่บน Docker host
///

/// note | Not available on Cloud
node นี้ไม่สามารถใช้ได้บน n8n Cloud
///

## Node parameters

ตั้งค่า node นี้ด้วย parameter ต่อไปนี้

### Execute Once

เลือกว่าจะให้ node นี้รันแค่ครั้งเดียว (เปิด) หรือรันตามจำนวน item ที่รับเข้ามา (ปิด)

### Command

ใส่ command ที่ต้องการรันบนเครื่องที่รัน n8n ดูตัวอย่างการรัน [multiple commands](#run-multiple-commands) และ [cURL commands](#run-curl-command) ด้านล่าง

#### Run multiple commands

มี 2 วิธีในการรันหลาย command ใน Execute Command node เดียว:

* ใส่แต่ละ command ในบรรทัดเดียวกันโดยคั่นด้วย `&&` เช่น จะเปลี่ยน directory (cd) แล้ว list ไฟล์ (ls) ก็ใช้ `&&` ได้

    ```bash
    cd bin && ls
    ```

* ใส่แต่ละ command ในบรรทัดใหม่ เช่น เขียน ls ต่อจาก cd ในบรรทัดถัดไป

    ```bash
    cd bin
    ls
    ```

#### Run cURL command

คุณสามารถใช้ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) node เพื่อส่ง cURL request ได้เช่นกัน

ถ้าต้องการรัน curl command ใน Execute Command node ต้อง build Docker image ใหม่จาก image n8n เดิม โดย image n8n ปกติใช้ Alpine Linux ต้องติดตั้ง curl เพิ่ม

1. สร้างไฟล์ชื่อ `Dockerfile`
2. ใส่โค้ดนี้ใน Dockerfile

    ```shell
    FROM docker.n8n.io/n8nio/n8n
    USER root
    RUN apk --update add curl
    USER node
    ```

3. ในโฟลเดอร์เดียวกัน ให้รันคำสั่งนี้เพื่อ build Docker image

    ```shell
    docker build -t n8n-curl
    ```

4. เปลี่ยน Docker image ที่ใช้รัน n8n เดิม เช่น จาก `docker.n8n.io/n8nio/n8n` เป็น `n8n-curl`
5. รัน Docker image ใหม่ที่สร้างไว้ จะสามารถใช้ ssh ผ่าน Execute Command Node ได้แล้ว

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'execute-command') ]]

## Common issues

สำหรับคำถามหรือปัญหาที่เจอบ่อยและแนวทางแก้ไข ดูที่ [Common Issues](/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues.md)
