---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Freshworks CRM credentials
description: Documentation for Freshworks CRM credentials. Use these credentials to authenticate Freshworks CRM in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Freshworks CRM credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Freshworks CRM](/integrations/builtin/app-nodes/n8n-nodes-base.freshworkscrm.md)

## Prerequisites

สร้างบัญชี [Freshworks CRM](https://www.freshworks.com/freshsales-crm/){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Freshworks CRM's API documentation](https://developers.freshworks.com/crm/api/){:target=_blank .external-link}

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**: ดูคำแนะนำโดยละเอียดเกี่ยวกับการรับ API key ของคุณได้ที่ [Freshworks CRM API authenticaton documentation](https://developers.freshworks.com/crm/api/#authentication){:target=_blank .external-link}
- Freshworks CRM **Domain** ของคุณ: ใช้ subdomain ของบัญชี Freshworks CRM ของคุณ นี่เป็นส่วนหนึ่งของ URL ตัวอย่างเช่น `https://<subdomain>.myfreshworks.com` ดังนั้น หากคุณเข้าถึง Freshworks CRM ผ่าน `https://n8n.myfreshworks.com` ให้ป้อน `n8n` เป็น **Domain** ของคุณ

