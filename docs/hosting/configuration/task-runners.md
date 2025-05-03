---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Task Runners
description: วิธีตั้งค่า Task Runners เพื่อรัน Task โดยใช้ Process ภายในหรือภายนอก
contentType: howto
---

# Task runners

Task runners คือกลไกกลางที่ใช้สำหรับรัน task ต่าง ๆ ให้ปลอดภัยและมีประสิทธิภาพ โดยจะใช้สำหรับรัน JavaScript ที่ผู้ใช้เขียนเองใน [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md)

หน้านี้จะอธิบายว่า task runners ทำงานยังไง และวิธีตั้งค่าใช้งาน

## How it works

Task runner จะประกอบด้วย 3 ส่วนหลัก ๆ คือ task runner, task broker, และ task requester

![Task runner overview](/_images/hosting/configuration/task-runner-concept.png)

Task runner จะเชื่อมต่อกับ task broker ผ่าน websocket ส่วน task requester จะส่งคำขอ task ไปที่ broker แล้ว task runner ที่ว่างจะมารับไปประมวลผล

runner จะรัน task แล้วส่งผลลัพธ์กลับไปที่ task requester โดยมี task broker เป็นตัวกลางประสานงานระหว่าง runner กับ requester

instance ของ n8n (ทั้ง main และ worker) จะทำหน้าที่เป็น broker ส่วน Code node จะเป็น task requester

## Task runner modes

Task runner มี 2 โหมดให้เลือกใช้: internal และ external

### Internal mode

ในโหมด internal ตัว n8n จะเป็นคนสั่งรัน task runner เป็น child process โดย n8n จะคอยดูแลและจัดการ lifecycle ของ task runner process นี้ ซึ่ง process จะใช้ `uid` และ `gid` เดียวกับ n8n

### External mode

ในโหมด external จะให้ orchestrator ภายนอก (เช่น Kubernetes) เป็นคนสั่งรัน task runner แทน n8n ปกติจะตั้งให้ task runner รันเป็น side-car container คู่กับ n8n

![Task runner deployed as a side-car container](/_images/hosting/configuration/task-runner-external-mode.png)

ในโหมดนี้ orchestrator จะเป็นคนดูแล lifecycle ของ task runner container เอง ทำให้ task runner แยกขาดจาก instance ของ n8n

ถ้าใช้ [Queue mode](/hosting/scaling/queue-mode.md) แต่ละ container ของ n8n (main และ worker) ต้องมี task runner ของตัวเอง

## Setting up external mode

รายละเอียดการตั้งค่า task runner ใน external mode มีดังนี้

### Configuring n8n instance in external mode

ตั้งค่า n8n ให้ใช้ external task runner โดยกำหนด environment variables เหล่านี้

| Environment variables                                  | Description                                                |
|--------------------------------------------------------|------------------------------------------------------------|
| `N8N_RUNNERS_ENABLED=true`                             | เปิดใช้งาน task runners                                   |
| `N8N_RUNNERS_MODE=external`                            | ใช้ task runners ในโหมด external                          |
| `N8N_RUNNERS_AUTH_TOKEN=<random secure shared secret>` | shared secret ที่ task runner ใช้เชื่อมต่อกับ broker      |
| `N8N_RUNNERS_BROKER_LISTEN_ADDRESS=0.0.0.0` | ปกติ task broker จะฟังแค่ localhost ถ้าใช้หลาย container (เช่น Docker Compose) ต้องตั้งให้รับ connection จากข้างนอกได้ |

ดู environment variables ทั้งหมดได้ที่ [task runner environment variables](/hosting/configuration/environment-variables/task-runners.md)

### Configuring task runners in external mode

task runner จะถูกรวมมาใน Docker image ของ n8n อยู่แล้ว และมี launcher สำหรับ task runner ด้วย

launcher จะสั่งรัน runner ตามต้องการ ทำให้ใช้ memory ต่ำถ้าไม่มีงาน และจะมี delay เล็กน้อย (หลักร้อย ms) ตอน cold-start launcher จะคอย monitor และ restart runner ถ้าเกิด infinite loop หรือปัญหาอื่น ๆ

สั่งรัน task runner container จาก Docker image ของ n8n โดยตั้งค่าดังนี้

| Configuration   | Description                                             |
|-----------------|---------------------------------------------------------|
| `command`       | `["/usr/local/bin/task-runner-launcher", "javascript"]` |
| `livenessProbe` | `GET /healthz`, port `5680`                             |

ตั้ง environment variables สำหรับ container ตามนี้ (ปรับตามที่ต้องการ):

| Environment variables | Description |
| ------ | ----- |
| `N8N_RUNNERS_AUTH_TOKEN=<random secure shared secret>` | shared secret ที่ task runner ใช้เชื่อมต่อกับ broker |
| `N8N_RUNNERS_MAX_CONCURRENCY=5` | จำนวน task ที่ runner จะรันพร้อมกันได้ |
| `N8N_RUNNERS_TASK_BROKER_URI=localhost:5679` | address ของ task broker server ใน instance ของ n8n |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT=15` | เวลารอ (วินาที) ถ้าไม่มีงานจะปิด process runner อัตโนมัติ launcher จะสั่งรันใหม่ถ้ามีงานเข้า ตั้งเป็น `0` เพื่อปิดฟีเจอร์นี้ |
| `NODE_OPTIONS=--max-old-space-size=<limit>` | จำกัด memory ของ process Node.js ที่ใช้รัน task runner ควรตั้งให้ต่ำกว่า limit ของ container เพื่อให้ runner เด้งก่อน container จะตาย launcher จะได้ monitor ได้ |
| `GENERIC_TIMEZONE` | [timezone เริ่มต้นเดียวกับที่ตั้งใน n8n instance](/hosting/configuration/environment-variables/timezone-localization.md) |

ดู environment variables ทั้งหมดได้ที่ [task runner environment variables](/hosting/configuration/environment-variables/task-runners.md)
