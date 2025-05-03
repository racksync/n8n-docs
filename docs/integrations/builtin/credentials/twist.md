---
title: คู่มือ Twist credentials
description: คู่มือการตั้งค่า Twist credentials สำหรับเชื่อมต่อ Twist กับ n8n
contentType: [integration, reference]
---

# Twist credentials

คุณสามารถใช้ credentials นี้เพื่อ authenticate กับ node เหล่านี้:

- [Twist](/integrations/builtin/app-nodes/n8n-nodes-base.twist.md)

## Prerequisites

- สมัคร [Twist](https://twist.com/){:target=_blank .external-link} ให้เรียบร้อย
- [สร้าง general integration](https://twist.com/app_console/create_app){:target=_blank .external-link} แล้วตั้งค่า OAuth Redirect URL ให้ถูกต้อง ดูรายละเอียดที่ [Using OAuth2](#usinkg-oauth2)

## Supported authentication methods

- OAuth2

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Twist's API documentation](https://developer.twist.com/v3/#authorization){:target=_blank .external-link}

## Using OAuth2
ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Client ID**: ได้จากการสร้าง general integration
- **Client Secret**: ได้จากการสร้าง general integration

สร้าง Client ID และ Client Secret ได้โดย [สร้าง general integration](https://twist.com/app_console/create_app){:target=_blank .external-link}

ตั้งค่า integration สำหรับ **OAuth Authentication** แบบนี้:

- คัดลอก **OAuth Redirect URL** จาก n8n ไปใส่ใน Twist เป็น **OAuth 2 redirect URL**
    
    /// note | OAuth Redirect URL for self-hosted n8n
    Twist ไม่อนุญาตให้ใช้ Redirect URL ที่เป็น `localhost` ต้องใช้ URL ที่เป็น domain จริง เช่น `https://mytemplatemaker.example.com/gr_callback` ถ้า OAuth Redirect URL ของ n8n เป็น localhost ดูวิธีด้านล่างที่ [Local environment redirect URL](#local-environment-redirect-url) เพื่อสร้าง URL ที่ Twist ยอมรับ
    ///

- กด **Update OAuth settings** เพื่อบันทึก
- คัดลอก **Client ID** และ **Client Secret** จาก Twist ไปใส่ใน n8n

### Local environment redirect URL

Twist ไม่อนุญาตให้ใช้ callback URL ที่เป็น localhost ทำตามนี้เพื่อ setup OAuth credentials สำหรับ local environment:

1. ใช้ [ngrok](https://ngrok.com/) เพื่อ expose server ที่รันอยู่บน port `5678` ขึ้นอินเทอร์เน็ต เปิด terminal แล้วรันคำสั่งนี้:
```sh
ngrok http 5678
```
2. เปิด terminal ใหม่แล้วรันคำสั่งนี้ โดยแทนที่ `<YOUR-NGROK-URL>` ด้วย URL ที่ได้จากขั้นตอนก่อนหน้า
```sh
export WEBHOOK_URL=<YOUR-NGROK-URL>
```
3. ใช้ URL ที่ได้เป็น **OAuth 2 redirect URL** ใน Twist

