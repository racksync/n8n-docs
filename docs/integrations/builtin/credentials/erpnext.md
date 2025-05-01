---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ERPNext credentials
description: Documentation for ERPNext credentials. Use these credentials to authenticate ERPNext in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# ERPNext credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [ERPNext](/integrations/builtin/app-nodes/n8n-nodes-base.erpnext.md)

## Prerequisites

- มี instance ของ [ERPNext](https://erpnext.com/){:target=_blank .external-link} ที่เข้าถึงได้
- สร้างบัญชีผู้ใช้บน instance นั้น

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [ERPNext's API documentation](https://frappeframework.com/docs/v13/user/en/guides/integration/rest_api){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **URL** ของ ERPNext instance ของคุณ เช่น `https://example.erpnext.com`
- **API Key**: สร้าง API key ผ่าน ERPNext ดูคำแนะนำได้ที่ [ERPNext API Access documentation](https://frappeframework.com/docs/v13/user/en/guides/integration/rest_api/token_based_auth){:target=_blank .external-link}
- **API Secret**: สร้างพร้อมกับ API key

