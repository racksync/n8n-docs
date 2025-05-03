---
title: ข้อมูลเข้าสู่ระบบ SendGrid
description: คู่มือการตั้งค่า SendGrid credentials สำหรับเชื่อมต่อ SendGrid กับ n8n
contentType: [integration, reference]
priority: medium
---

# SendGrid credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [SendGrid](/integrations/builtin/app-nodes/n8n-nodes-base.sendgrid.md)

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [SendGrid's API documentation](https://www.twilio.com/docs/sendgrid/api-reference){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credentials นี้ คุณจะต้องมี [SendGrid](https://sendgrid.com){:target=_blank .external-link} account และ:

- **API Key**

วิธีสร้าง API key:

1. ใน Twilio SendGrid app ไปที่ **Settings >** [**API Keys**](https://app.sendgrid.com/settings/api_keys){:target=_blank .external-link}
2. เลือก **Create API Key**
3. ตั้งชื่อ API key เช่น `n8n integration`
4. เลือก **Full Access**
5. เลือก **Create & View**
6. คัดลอก key แล้วนำไปใส่ใน n8n credential ของคุณ

ดูรายละเอียดเพิ่มเติมได้ที่ [Create API Keys](https://www.twilio.com/docs/sendgrid/api-reference/api-keys/create-api-keys){:target=_blank .external-link}
