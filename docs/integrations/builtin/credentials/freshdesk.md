---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Freshdesk credentials
description: Documentation for Freshdesk credentials. Use these credentials to authenticate Freshdesk in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Freshdesk credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Freshdesk](/integrations/builtin/app-nodes/n8n-nodes-base.freshdesk.md)

## Prerequisites

สร้างบัญชี [Freshdesk](https://freshdesk.com/){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Freshdesk's API documentation](https://developers.freshdesk.com/api/){:target=_blank .external-link}

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**: ดูคำแนะนำโดยละเอียดเกี่ยวกับการรับ API key ของคุณได้ที่ [Freshdesk API authenticaton documentation](https://developers.freshdesk.com/api/#authentication){:target=_blank .external-link}
- Freshdesk **Domain**: ใช้ subdomain ของบัญชี Freshdesk ของคุณ นี่เป็นส่วนหนึ่งของ URL ตัวอย่างเช่น `https://<subdomain>.freshdesk.com` ดังนั้น หากคุณเข้าถึง Freshdesk ผ่าน `https://n8n.freshdesk.com` ให้ป้อน `n8n` เป็น **Domain** ของคุณ

