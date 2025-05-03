---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ตั้งค่า User Management สำหรับ n8n Self-hosted
description: ตั้งค่า User Management สำหรับ n8n Self-hosted
contentType: howto
---

# Configure self-hosted n8n for user management

User management ใน n8n ช่วยให้คุณสามารถเชิญคนอื่น ๆ มาทำงานร่วมกันใน instance ของ n8n ได้

หน้านี้จะอธิบายวิธีตั้งค่า instance ของ n8n เพื่อรองรับ user management และขั้นตอนการเริ่มเชิญผู้ใช้งาน

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งานได้ที่ [User management](/user-management/index.md) เช่น

* [Managing users](/user-management/manage-users.md)
* [Account types](/user-management/account-types.md)
* [Best practices](/user-management/best-practices.md)

ถ้าต้องการตั้งค่า LDAP ดูได้ที่ [LDAP](/user-management/ldap.md)

ถ้าต้องการตั้งค่า SAML ดูได้ที่ [SAML](/user-management/saml/index.md)

/// note | Basic auth and JWT removed
n8n เอา support สำหรับ basic auth และ JWT ออกตั้งแต่เวอร์ชัน 1.0 แล้วนะ
///

## Setup

การตั้งค่า user management ใน n8n มี 3 ขั้นตอนหลัก ๆ คือ

1. ตั้งค่า instance ของ n8n ให้ใช้ SMTP server ของคุณ
2. เริ่มต้น n8n และทำตามขั้นตอน setup ในแอป
3. เชิญผู้ใช้งาน

### Step one: SMTP

n8n แนะนำให้ตั้งค่า SMTP server เพื่อใช้สำหรับส่ง invite และ reset password ให้ผู้ใช้งาน

/// note | Optional from 0.210.1
ตั้งแต่เวอร์ชัน 0.210.1 ขึ้นไป ขั้นตอนนี้เป็น optional แล้ว คุณสามารถเลือก copy ลิงก์ invite ไปส่งเองแทนการตั้งค่า SMTP ก็ได้ แต่ถ้าไม่ตั้ง SMTP ผู้ใช้จะ reset password ไม่ได้
///

ข้อมูลที่ต้องขอจากผู้ให้บริการ SMTP:

* Server name
* SMTP username
* SMTP password
* SMTP sender name

การตั้งค่า SMTP กับ n8n ให้กำหนด environment variables สำหรับ SMTP ใน instance ของ n8n ดูวิธีตั้งค่า environment variables ได้ที่ [Configuration](/hosting/configuration/configuration-methods.md)
<!-- vale off -->
| Variable | Type | Description | Required? |
| -------- | ---- | ----------- | --------- |
| `N8N_EMAIL_MODE` | string | `smtp` | Required |
| `N8N_SMTP_HOST` | string | _your_SMTP_server_name_ | Required |
| `N8N_SMTP_PORT` | number | _your_SMTP_server_port_ ค่า default คือ `465`.| Optional |
| `N8N_SMTP_USER` | string | _your_SMTP_username_ | Optional |
| `N8N_SMTP_PASS` | string | _your_SMTP_password_ | Optional |
| `N8N_SMTP_OAUTH_SERVICE_CLIENT` | string | _your_OAuth_service_client_ | Optional |
| `N8N_SMTP_OAUTH_PRIVATE_KEY` | string | _your_OAuth_private_key_ | Optional |
| `N8N_SMTP_SENDER` | string | อีเมลผู้ส่ง สามารถใส่ชื่อผู้ส่งด้วยก็ได้ เช่น _N8N `<contact@n8n.com>`_ | Required |
| `N8N_SMTP_SSL` | boolean | จะใช้ SSL กับ SMTP หรือไม่ (true/false) ค่า default คือ `true` | Optional | 
| `N8N_UM_EMAIL_TEMPLATES_INVITE` | string | path เต็มของไฟล์ HTML email template ถ้าต้องการ override template สำหรับ invite | Optional |
| `N8N_UM_EMAIL_TEMPLATES_PWRESET` | string | path เต็มของไฟล์ HTML email template ถ้าต้องการ override template สำหรับ reset password | Optional |
| `N8N_UM_EMAIL_TEMPLATES_WORKFLOW_SHARED` | String | override template HTML สำหรับแจ้งเตือนเวลามีคนแชร์ credential ให้ ใส่ path เต็มของ template | Optional |
| `N8N_UM_EMAIL_TEMPLATES_CREDENTIALS_SHARED` | String | override template HTML สำหรับแจ้งเตือนเวลามีคนแชร์ credential ให้ ใส่ path เต็มของ template | Optional |

<!-- vale on-->
ถ้า instance ของ n8n รันอยู่แล้ว ต้อง restart ใหม่เพื่อให้ตั้งค่า SMTP มีผล

/// note | More configuration options
ยังมี environment variables อื่น ๆ ให้ตั้งค่าได้อีก ดูรายละเอียดทั้งหมดได้ที่ [Environment variables](/hosting/configuration/environment-variables/index.md) เช่น ปิด tag, workflow templates, หรือแบบสอบถาม personalization ถ้าไม่อยากให้ user เห็น
///

/// note | New to SMTP?
ถ้าไม่คุ้นกับ SMTP ลองอ่าน [blog post ของ SendGrid](https://sendgrid.com/blog/what-is-an-smtp-server/) สำหรับแนะนำเบื้องต้น หรือดู [Wikipedia: Simple Mail Transfer Protocol](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) สำหรับรายละเอียดเชิงเทคนิค
///

### Step two: In-app setup

--8<-- "_snippets/user-management/in-app-setup.md"

### Step three: Invite users

--8<-- "_snippets/user-management/invite-users.md"
