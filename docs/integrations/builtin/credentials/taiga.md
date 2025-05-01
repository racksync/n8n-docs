---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Taiga credentials
description: Documentation for Taiga credentials. Use these credentials to authenticate Taiga in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Taiga credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Taiga](/integrations/builtin/app-nodes/n8n-nodes-base.taiga.md)
- [Taiga Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.taigatrigger.md)

## Prerequisites

สร้างบัญชี [Taiga](https://taiga.io/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- Basic auth

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Taiga's API documentation](https://docs.taiga.io/api.html){:target=_blank .external-link}

## Using basic auth

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Username**: กรอก username หรืออีเมลของคุณ ดูรายละเอียดได้ที่ [Normal login](https://docs.taiga.io/api.html#auth-normal-login){:target=_blank .external-link}
- **Password**: กรอกรหัสผ่านของคุณ
- **Environment**: เลือก **Cloud** หรือ **Self-Hosted** ถ้าเลือก **Self-Hosted** จะต้องกรอก:
    - **URL**: กรอก URL ของ Taiga instance ของคุณ

