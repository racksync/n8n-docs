---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Configure webhook URLs with reverse proxy
description: Customize n8n webhook URLs for compatibility with reverse proxy setups.
contentType: howto
---

# Configure n8n webhooks with reverse proxy

n8n จะสร้าง webhook URL โดยเอา `N8N_PROTOCOL`, `N8N_HOST` และ `N8N_PORT` มาต่อกัน ถ้า n8n รันอยู่หลัง reverse proxy วิธีนี้จะใช้ไม่ได้ เพราะ n8n รันใน port 5678 แต่ reverse proxy เปิดให้เข้าจากข้างนอกที่ port 443 ดังนั้นต้องตั้ง webhook URL เอง เพื่อให้ n8n แสดง URL ที่ถูกต้องใน Editor UI และ register webhook กับ external service ได้ถูกต้อง

```bash
export WEBHOOK_URL=https://n8n.example.com/
```
ดูรายละเอียดตัวแปรนี้เพิ่มเติมได้ที่ [Environment variables reference](/hosting/configuration/environment-variables/endpoints.md)
