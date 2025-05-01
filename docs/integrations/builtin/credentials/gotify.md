---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Gotify credentials
description: Documentation for Gotify credentials. Use these credentials to authenticate Gotify in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Gotify credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Gotify](/integrations/builtin/app-nodes/n8n-nodes-base.gotify.md)

## Prerequisites

ติดตั้ง [Gotify](https://gotify.net/docs/install){:target=_blank .external-link} บนเซิร์ฟเวอร์ของคุณ

## Supported authentication methods

- API token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Gotify's API documentation](https://gotify.net/api-docs){:target=_blank .external-link}

## Using API token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **App API Token**: จำเป็นเฉพาะเมื่อคุณจะใช้ credential นี้เพื่อสร้างข้อความ หากต้องการสร้าง App API token ให้สร้าง application จากเมนู **Apps** ดูข้อมูลเพิ่มเติมได้ที่ [Gotify's Push messages documentation](https://gotify.net/docs/pushmsg){:target=_blank .external-link}
- **Client API Token**: จำเป็นสำหรับการดำเนินการอื่นๆ ทั้งหมดนอกเหนือจากการสร้างข้อความ (เช่น การลบหรือการดึงข้อความ) หากต้องการสร้าง Client API token ให้สร้าง client จากเมนู **Clients**
- **URL** ของ Gotify host

