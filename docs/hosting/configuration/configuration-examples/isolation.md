---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: แยก n8n ออกจากระบบภายนอก
description: ป้องกันไม่ให้ n8n instance เชื่อมต่อกับ server ของ n8n
contentType: howto
---

# Isolate n8n

โดยปกติ n8n ที่รันแบบ self-hosted จะส่งข้อมูลบางอย่างกลับไปที่ server ของ n8n เช่น แจ้งเตือน update, workflow templates, และ diagnostics

ถ้าอยากป้องกันไม่ให้ n8n เชื่อมต่อกับ server ของ n8n ให้ตั้ง environment variables เหล่านี้เป็น false:

```
N8N_DIAGNOSTICS_ENABLED=false
N8N_VERSION_NOTIFICATIONS_ENABLED=false
N8N_TEMPLATES_ENABLED=false
```

และ unset config diagnostics ของ n8n:

```
EXTERNAL_FRONTEND_HOOKS_URLS=
N8N_DIAGNOSTICS_CONFIG_FRONTEND=
N8N_DIAGNOSTICS_CONFIG_BACKEND=
```

ดูรายละเอียดตัวแปรเหล่านี้เพิ่มเติมได้ที่ [Environment variables reference](/hosting/configuration/environment-variables/deployment.md)
