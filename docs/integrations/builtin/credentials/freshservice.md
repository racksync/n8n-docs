---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Freshservice credentials
description: Documentation for Freshservice credentials. Use these credentials to authenticate Freshservice in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Freshservice credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Freshservice](/integrations/builtin/app-nodes/n8n-nodes-base.freshservice.md)

## Prerequisites

สร้างบัญชี [Freshservice](https://freshservice.com/){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Freshservice's API documentation](https://api.freshservice.com/v2/){:target=_blank .external-link}

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**: ดูคำแนะนำโดยละเอียดเกี่ยวกับการรับ API key ของคุณได้ที่ [Freshservice API authenticaton documentation](https://api.freshservice.com/v2/#authentication){:target=_blank .external-link}
- Freshservice **Domain** ของคุณ: ใช้ subdomain ของบัญชี Freshservice ของคุณ นี่เป็นส่วนหนึ่งของ URL ตัวอย่างเช่น `https://<subdomain>.freshservice.com` ดังนั้น หากคุณเข้าถึง Freshservice ผ่าน `https://n8n.freshservice.com` ให้ป้อน `n8n` เป็น **Domain** ของคุณ

