---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน MailerLite
description: เอกสารสำหรับ MailerLite credentials ใช้เพื่อเชื่อมต่อ MailerLite ใน n8n
contentType: [integration, reference]
---

# MailerLite credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [MailerLite](/integrations/builtin/app-nodes/n8n-nodes-base.mailerlite.md)
- [MailerLite Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.mailerlitetrigger.md)

## Prerequisites

สร้างบัญชี [MailerLite](https://www.mailerlite.com/){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

อ้างอิง [MailerLite's API documentation](https://developers.mailerlite.com/docs/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**: สร้าง API key จากเมนู **Integrations** อ้างอิงเอกสาร [API Authentication documentation](https://developers.mailerlite.com/docs/#authentication){:target=_blank .external-link} สำหรับคำแนะนำโดยละเอียดเพิ่มเติม

เปิดใช้งานสวิตช์ **Classic API** หาก API key สำหรับบัญชี MailerLite Classic แทนที่จะเป็นประสบการณ์ MailerLite ที่ใหม่กว่า

/// note
บัญชี MailerLite ใหม่ส่วนใหญ่และบัญชีฟรีทั้งหมดควรปิดใช้งานสวิตช์ **Classic API** คุณสามารถค้นหา [which version of MailerLite you are using](https://www.mailerlite.com/help/which-version-of-mailerlite-am-i-using) และเรียนรู้เพิ่มเติมเกี่ยวกับความแตกต่างระหว่างทั้งสองใน [MailerLite FAQ](https://www.mailerlite.com/help/new-mailerlite-faq)
///
