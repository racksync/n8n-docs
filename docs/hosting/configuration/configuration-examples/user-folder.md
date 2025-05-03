---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ระบุ path ของ user folder
description: ระบุตำแหน่งโฟลเดอร์สำหรับเก็บข้อมูลเฉพาะ user
contentType: howto
---

# Specify user folder path

n8n จะเก็บข้อมูล user เฉพาะ เช่น encryption key, ไฟล์ SQLite database, และ tunnel ID (ถ้าใช้) ไว้ใน subfolder `.n8n` ของ user ที่รัน n8n คุณสามารถเปลี่ยน path ของ user-folder ได้ด้วย environment variable

```bash
export N8N_USER_FOLDER=/home/jim/n8n
```
ดูรายละเอียดตัวแปรนี้เพิ่มเติมได้ที่ [Environment variables reference](/hosting/configuration/environment-variables/deployment.md)
