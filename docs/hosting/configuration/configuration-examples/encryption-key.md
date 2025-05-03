---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ตั้งค่า encryption key เอง
description: ตั้งค่า encryption key เองเพื่อให้ n8n เข้ารหัส credential อย่างปลอดภัย
contentType: howto
---

# Set a custom encryption key

n8n จะสร้าง encryption key แบบสุ่มให้อัตโนมัติเมื่อรันครั้งแรก แล้วเก็บไว้ใน `~/.n8n` โดยใช้ key นี้สำหรับ encrypt credentials ก่อนบันทึกลง database ถ้า key ยังไม่มีใน settings file คุณสามารถตั้งค่าเองผ่าน environment variable เพื่อให้ n8n ใช้ key ที่คุณกำหนดเอง แทนที่จะสร้างใหม่

ถ้าใช้ [queue mode](/hosting/scaling/queue-mode.md) ต้องตั้ง environment variable นี้ให้กับ worker ทุกตัวด้วย

```bash
export N8N_ENCRYPTION_KEY=<SOME RANDOM STRING>
```
ดูรายละเอียดตัวแปรนี้เพิ่มเติมได้ที่ [Environment variables reference](/hosting/configuration/environment-variables/deployment.md)
