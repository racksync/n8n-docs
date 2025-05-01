---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Invoice Ninja credentials
description: Documentation for Invoice Ninja credentials. Use these credentials to authenticate Invoice Ninja in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Invoice Ninja credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Invoice Ninja](/integrations/builtin/app-nodes/n8n-nodes-base.invoiceninja.md)
- [Invoice Ninja Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.invoiceninjatrigger.md)

## Prerequisites

สร้างบัญชี [Invoice Ninja](https://www.invoiceninja.com/){:target=_blank .external-link} เฉพาะแผน Pro และ Enterprise เท่านั้นที่รองรับการรวม API

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับ API ได้ที่ [v4 API documentation](https://invoice-ninja.readthedocs.io/en/latest/api.html){:target=_blank .external-link} และ [v5 API documentation](https://api-docs.invoicing.co/){:target=_blank .external-link} ของ Invoice Ninja

## Using API key

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **URL**: หาก Invoice Ninja host การติดตั้งของคุณ ให้ใช้ URL เริ่มต้นที่กล่าวถึง หากคุณ self-hosting การติดตั้งของคุณ ให้ใช้ URL ของ Invoice Ninja instance ของคุณ
- **API Token**: สร้าง API token ใน **Settings > Account Management > API Tokens**
- **Secret** (ไม่บังคับ): มีให้สำหรับผู้ใช้ API v5 เท่านั้น

