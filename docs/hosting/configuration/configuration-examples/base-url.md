---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ตั้งค่า Base URL สำหรับการเข้าถึง front end ของ n8n
description: ตั้งค่า environment variable Base URL เพื่อกำหนด path การเข้าถึง REST API ของ back end จาก front end
contentType: howto
---

# Configure the Base URL for n8n's front end access

/// warning | Requires manual UI build
กรณีนี้ต้องตั้งค่า environment variable `VUE_APP_URL_BASE_API` ซึ่งต้อง build `n8n-editor-ui` ด้วยตัวเอง ไม่สามารถใช้กับ Docker image ของ n8n ที่ตั้งค่า default เป็น `/` (ใช้ root-domain) ได้
///

คุณสามารถตั้งค่า Base URL ที่ front end ของ n8n จะใช้เชื่อมต่อกับ backend REST API ได้ เหมาะกับกรณีที่ต้องการแยก host front end กับ back end ของ n8n ออกจากกัน

```bash
export VUE_APP_URL_BASE_API=https://n8n.example.com/
```
ดูรายละเอียดตัวแปรนี้เพิ่มเติมได้ที่ [Environment variables reference](/hosting/configuration/environment-variables/deployment.md)
