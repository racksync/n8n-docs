---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Paddle
description: เอกสารสำหรับข้อมูลยืนยันตัวตน Paddle ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Paddle ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# Paddle credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Paddle](/integrations/builtin/app-nodes/n8n-nodes-base.paddle.md)

## Prerequisites

สร้าง [Paddle](https://paddle.com/){:target=_blank .external-link} account

## Supported authentication methods

- API access token (Classic)

/// warning | Paddle Classic API
credential นี้ทำงานร่วมกับ API ของ Paddle Classic หากคุณเข้าร่วม Paddle หลังเดือนสิงหาคม 2023 คุณกำลังใช้ [Paddle Billing API](https://developer.paddle.com/api-reference/overview){:target=_blank .external-link} และ credential นี้อาจไม่ทำงานสำหรับคุณ
///

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Paddle Classic's API documentation](https://developer.paddle.com/classic/api-reference/1384a288aca7a-api-reference){:target=_blank .external-link}

## Using API access token (Classic)

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Vendor Auth Code**: สร้างขึ้นเมื่อคุณสร้าง API key
- **Vendor ID**: แสดงเมื่อคุณสร้าง API key
- **Use Sandbox Environment API**: เมื่อเปิดใช้งาน node ที่ใช้ credential นี้จะเรียกใช้ Sandbox API endpoint แทน live API endpoint

หากต้องการสร้าง auth code และดู Vendor ID ของคุณ ให้ไปที่ **Paddle > Developer Tools > Authentication > Generate Auth Code** เลือก **Reveal Auth Code** เพื่อแสดง Auth Code ดูข้อมูลเพิ่มเติมที่ [API Authentication](https://developer.paddle.com/classic/api-reference/zg9joji1mzuzotg5-api-authentication){:target=_blank .external-link}
