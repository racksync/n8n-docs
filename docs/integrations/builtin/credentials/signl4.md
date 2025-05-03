---
title: ข้อมูลเข้าสู่ระบบ SIGNL4
description: คู่มือการตั้งค่า SIGNL4 credentials สำหรับเชื่อมต่อ SIGNL4 กับ n8n
contentType: [integration, reference]
---

# SIGNL4 credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [SIGNL4](/integrations/builtin/app-nodes/n8n-nodes-base.signl4.md)

## Prerequisites

สมัคร [SIGNL4](https://www.signl4.com/){:target=_blank .external-link} account ก่อนใช้งาน

## Supported authentication methods

- Webhook secret

## Related resources

ดูรายละเอียดเพิ่มเติมได้ที่ [SIGNL4's Inbound Webhook documentation](https://connect.signl4.com/webhook/docs/index.html){:target=_blank .external-link}

## Using webhook secret

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Team Secret**: SIGNL4 จะส่ง secret นี้ในอีเมล "✅ Sign up complete" เป็นส่วนท้ายของ webhook URL เช่น ถ้า URL คือ `https://connect.signl4.com/webhook/helloworld` team secret คือ `helloworld`

