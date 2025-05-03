---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Environment Variables สำหรับ User Management SMTP และ 2FA
description: Environment Variables สำหรับตั้งค่า User Management และ Email
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# User management SMTP, and two-factor authentication environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการตั้งค่า user management และ email ได้ที่ [User management](/hosting/configuration/user-management-self-hosted.md)
<!-- vale off -->
| Variable | Type | Default | Description |
| :------- | :--- | :------ | :---------- |
| `N8N_EMAIL_MODE` | String | `smtp` | เปิด email |
| `N8N_SMTP_HOST` | String | - | _ชื่อ SMTP server ของคุณ_ |
| `N8N_SMTP_PORT` | Number | - | _port ของ SMTP server ของคุณ_ |
| `N8N_SMTP_USER` | String | - | _username SMTP ของคุณ_ |
| `N8N_SMTP_PASS` | String | - | _password SMTP ของคุณ_ |
| `N8N_SMTP_OAUTH_SERVICE_CLIENT` | String | - | ถ้าใช้ 2LO กับ service account ใส่ client ID ตรงนี้ |
| `N8N_SMTP_OAUTH_PRIVATE_KEY` | String | - | ถ้าใช้ 2LO กับ service account ใส่ private key ตรงนี้ |
| `N8N_SMTP_SENDER` | String | - | อีเมลผู้ส่ง (ใส่ชื่อผู้ส่งได้ด้วย) ตัวอย่าง: _N8N `<contact@n8n.com>`_ |
| `N8N_SMTP_SSL` | Boolean | `true` | ใช้ SSL กับ SMTP หรือไม่ (true/false) |
| `N8N_SMTP_STARTTLS` | Boolean | `true` | ใช้ STARTTLS กับ SMTP หรือไม่ (true/false) |
| `N8N_UM_EMAIL_TEMPLATES_INVITE` | String | - | path เต็มของ HTML email template ถ้าต้องการ override template สำหรับ invite |
| `N8N_UM_EMAIL_TEMPLATES_PWRESET` | String | - | path เต็มของ HTML email template ถ้าต้องการ override template สำหรับ reset password |
| `N8N_UM_EMAIL_TEMPLATES_WORKFLOW_SHARED` | String | - | override HTML template สำหรับแจ้งเตือนเวลามีคนแชร์ workflow ให้ ใส่ path เต็มของ template |
| `N8N_UM_EMAIL_TEMPLATES_CREDENTIALS_SHARED` | String | - | override HTML template สำหรับแจ้งเตือนเวลามีคนแชร์ credential ให้ ใส่ path เต็มของ template |
| `N8N_USER_MANAGEMENT_JWT_SECRET` | String | - | กำหนด JWT secret เอง (ถ้าไม่กำหนด n8n จะ generate ให้เองตอน start) |
| `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS` | Number | 168 | อายุ JWT (ชั่วโมง) |
| `N8N_USER_MANAGEMENT_JWT_REFRESH_TIMEOUT_HOURS` | Number | 0 | เวลาก่อน JWT หมดอายุที่จะ refresh อัตโนมัติ 0 = 25% ของ `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS` -1 = ไม่ refresh เลย (user ต้อง login ใหม่หลังหมดอายุ) |
| `N8N_MFA_ENABLED` | Boolean | `true` | เปิด 2FA (true) หรือปิด (false) n8n จะไม่สนใจถ้า user เดิมเปิด 2FA อยู่แล้ว |
<!-- vale on -->
