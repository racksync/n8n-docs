---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Pushbullet
description: เอกสารสำหรับข้อมูลยืนยันตัวตน Pushbullet ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Pushbullet ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# Pushbullet credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Pushbullet](/integrations/builtin/app-nodes/n8n-nodes-base.pushbullet.md)

## Prerequisites

สร้าง [Pushbullet](https://www.pushbullet.com/){:target=_blank .external-link} account

## Supported authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Pushbullet's API documentation](https://docs.pushbullet.com/){:target=_blank .external-link}

## Using OAuth2

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Client ID**: สร้างขึ้นเมื่อคุณสร้าง Pushbullet app หรือที่เรียกว่า OAuth client
- **Client Secret**: สร้างขึ้นเมื่อคุณสร้าง Pushbullet app หรือที่เรียกว่า OAuth client

หากต้องการสร้าง **Client ID** และ **Client Secret** ให้ไปที่หน้า [create client](https://www.pushbullet.com/create-client) คัดลอก **OAuth Redirect URL** จาก n8n และเพิ่มเป็น **redirect_uri** สำหรับ app/client ใช้ **client_id** และ **client_secret** จาก OAuth Client ใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมที่ [OAuth2 Guide](https://docs.pushbullet.com/#oauth2) ของ Pushbullet

/// note | Pushbullet OAuth test link
Pushbullet มี test link ในระหว่างกระบวนการสร้าง client ที่อธิบายไว้ข้างต้น ลิงก์นี้ไม่สามารถใช้งานร่วมกับ n8n ได้ หากต้องการตรวจสอบว่าการยืนยันตัวตนใช้งานได้ ให้ใช้ปุ่ม **Connect my account** ใน n8n
///

