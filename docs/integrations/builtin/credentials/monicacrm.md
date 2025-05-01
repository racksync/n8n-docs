---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Monica CRM credentials
description: Documentation for Monica CRM credentials. Use these credentials to authenticate Monica CRM in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Monica CRM credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Monica CRM](/integrations/builtin/app-nodes/n8n-nodes-base.monicacrm.md)

## Prerequisites

ลงทะเบียนบัญชี [Monica CRM](https://www.monicahq.com/){:target=_blank .external-link} หรือ self-host instance

## Supported authentication methods

- API token

## Related resources

อ้างอิง [Monica's API documentation](https://www.monicahq.com/api){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Environment** ของคุณ:
    - เลือก **Cloud-Hosted** หากคุณเข้าถึง instance Monica ของคุณผ่าน Monica
    - เลือก **Self-Hosted** หากคุณ self-host Monica บนเซิร์ฟเวอร์ของคุณเอง ระบุ **Self-Hosted Domain** ของคุณ
- **API Token**: สร้าง token ใน **Settings > API**

