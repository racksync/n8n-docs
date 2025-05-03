---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Mailgun
description: เอกสารสำหรับ Mailgun credentials ใช้เพื่อเชื่อมต่อ Mailgun ใน n8n
contentType: [integration, reference]
---

# Mailgun credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Mailgun](/integrations/builtin/app-nodes/n8n-nodes-base.mailgun.md)

## Prerequisites

- สร้างบัญชี [Mailgun](https://www.mailgun.com/){:target=_blank .external-link}
- [เพิ่มและยืนยัน domain](https://help.mailgun.com/hc/en-us/articles/360026833053-Domain-Verification-Setup-Guide){:target=_blank .external-link} ใน Mailgun หรือใช้ sandbox domain ที่ให้มาสำหรับการทดสอบ

## Supported authentication methods

- API key

## Related resources

อ้างอิง [Mailgun's API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/intro/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Domain**: หากบัญชี Mailgun ของคุณอยู่ในยุโรป ให้เลือก **api.eu.mailgun.net** มิฉะนั้น ให้เลือก **api.mailgun.net** อ้างอิง [Mailgun Base URLs](https://documentation.mailgun.com/docs/mailgun/api-reference/intro/#base-url){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
- **Email Domain**: ป้อน email sending domain ที่คุณกำลังทำงานด้วย หากคุณมี sending domains หลายรายการ อ้างอิง [Working with multiple email domains](#working-with-multiple-email-domains) สำหรับข้อมูลเพิ่มเติม
- **API Key**: ดู API key ของคุณใน **Settings > API Keys** อ้างอิงเอกสาร [Mailgun's API Authentication documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/authentication/){:target=_blank .external-link} สำหรับคำแนะนำโดยละเอียดเพิ่มเติม

## Working with multiple email domains

หากบัญชี Mailgun ของคุณมี sending domains หลายรายการ ให้สร้าง credential แยกต่างหากสำหรับแต่ละ email domain ที่คุณกำลังทำงานด้วย
