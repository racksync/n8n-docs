---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Mandrill credentials
description: Documentation for Mandrill credentials. Use these credentials to authenticate Mandrill in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Mandrill credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Mandrill](/integrations/builtin/app-nodes/n8n-nodes-base.mandrill.md)

## Prerequisites

- สร้างบัญชี Mailchimp [Transactional email account](https://mailchimp.com/features/transactional-email-infrastructure/){:target=_blank .external-link}
- เข้าสู่ระบบ [Mandrill](https://mandrillapp.com/login/){:target=_blank .external-link} ด้วยบัญชี Mailchimp ของคุณ

หากคุณมีบัญชี Mailchimp ที่มีแผน Standard หรือสูงกว่าอยู่แล้ว ให้เปิดใช้งาน [Transactional Emails](https://mailchimp.com/help/add-or-remove-transactional-email){:target=_blank .external-link} ภายในบัญชีนั้นเพื่อใช้ Mandrill

## Supported authentication methods

- API key

## Related resources

อ้างอิง [Mailchimp's Transactional API documentation](https://mailchimp.com/developer/transactional/api/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**: สร้าง API key จาก [Settings](https://mandrillapp.com/settings){:target=_blank .external-link} ของ Mandrill อ้างอิงเอกสาร Mailchimp's [Generate your API key documentation](https://mailchimp.com/developer/transactional/guides/quick-start/#generate-your-api-key){:target=_blank .external-link} สำหรับคำแนะนำโดยละเอียดเพิ่มเติม

