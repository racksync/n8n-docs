---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Mailjet
description: เอกสารสำหรับ Mailjet credentials ใช้เพื่อเชื่อมต่อ Mailjet ใน n8n
contentType: [integration, reference]
---

# Mailjet credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Mailjet](/integrations/builtin/app-nodes/n8n-nodes-base.mailjet.md)
- [Mailjet Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.mailjettrigger.md)

## Prerequisites

สร้างบัญชี [Mailjet](https://www.mailjet.com/){:target=_blank .external-link}

## Supported authentication methods

- Email API key: สำหรับใช้กับ Email API ของ Mailjet
- SMS token: สำหรับใช้กับ SMS API ของ Mailjet

## Related resources

อ้างอิง [Mailjet's Email API documentation](https://dev.mailjet.com/email/guides/){:target=_blank .external-link} และ [Mailjet's SMS API documentation](https://dev.mailjet.com/sms/guides/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับแต่ละบริการ

## Using Email API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**: ดูและสร้าง API keys ในหน้า [API Key Management](https://app.mailjet.com/account/api_keys){:target=_blank .external-link} ของ Mailjet
- **Secret Key**: ดู API Secret Keys ของคุณในหน้า [API Key Management](https://app.mailjet.com/account/api_keys){:target=_blank .external-link} ของ Mailjet
- _Optional:_ เลือกว่าจะใช้ **Sandbox Mode** สำหรับการเรียก API ที่ทำโดยใช้ credential นี้หรือไม่ เมื่อเปิดใช้งาน การเรียก API ทั้งหมดจะใช้ Sandbox mode: API จะยังคงตรวจสอบ payloads แต่จะไม่ส่งข้อความจริง ซึ่งมีประโยชน์ในการแก้ไขปัญหาข้อผิดพลาดของ payload โดยไม่ต้องส่งข้อความจริง อ้างอิงเอกสาร [Sandbox Mode documentation](https://dev.mailjet.com/email/guides/send-api-v31/#sandbox-mode){:target=_blank .external-link} ของ Mailjet สำหรับข้อมูลเพิ่มเติม

สำหรับ credential นี้ คุณสามารถใช้:

- API key และ secret key หลักของ Mailjet
- API key และ secret key ของ subaccount

อ้างอิงเอกสาร [How to create a subaccount (or additional API key) documentation](https://documentation.mailjet.com/hc/en-us/articles/360042561974-How-to-create-a-subaccount-or-additional-API-Key){:target=_blank .external-link} ของ Mailjet สำหรับคำแนะนำโดยละเอียดในการสร้าง API keys เพิ่มเติม อ้างอิงหน้า [What are subaccounts and how does it help me?](https://documentation.mailjet.com/hc/en-us/articles/360042561854-What-are-subaccounts-and-how-does-it-help-me){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ subaccounts ของ Mailjet และเมื่อใดที่คุณอาจต้องการใช้

## Using SMS Token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Token** การเข้าถึง: สร้าง token ใหม่จาก [SMS Dashboard](https://app.mailjet.com/sms){:target=_blank .external-link} ของ Mailjet อ้างอิงคู่มือ [SMS API Getting Started guide](https://dev.mailjet.com/sms/guides/getting-started/){:target=_blank .external-link} สำหรับคำแนะนำโดยละเอียดเพิ่มเติม

