---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Medium credentials
description: Documentation for Medium credentials. Use these credentials to authenticate Medium in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Medium credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Medium](/integrations/builtin/app-nodes/n8n-nodes-base.medium.md)

/// warning | Medium API no longer supported
Medium ได้หยุดสนับสนุน Medium API แล้ว credentials เหล่านี้ยังคงปรากฏใน n8n แต่คุณไม่สามารถกำหนดค่า integrations ใหม่โดยใช้ credentials เหล่านี้ได้
///

## Prerequisites

- สร้างบัญชีบน [Medium](https://www.medium.com/){:target=_blank .external-link}
- สำหรับ OAuth2 ให้ขอสิทธิ์เข้าถึง credentials โดยส่งอีเมลไปที่ [yourfriends@medium.com](mailto:yourfriends@medium.com)

## Supported authentication methods

- API access token
- OAuth2

## Related resources

อ้างอิง [Medium's API documentation](https://github.com/Medium/medium-api-docs){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Access Token** ของ API: สร้าง token ใน **Settings >** [**Security and apps**](https://medium.com/me/settings/security){:target=_blank .external-link} **> Integration tokens** ใช้ integration token ที่สร้างขึ้นนี้เป็น **Access Token** ของ n8n

อ้างอิงเอกสาร Medium API [Self-issued access tokens documentation](https://github.com/Medium/medium-api-docs?tab=readme-ov-file#21-self-issued-access-tokens){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Using OAuth2

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Client ID**
- **Client Secret**

วิธีสร้าง **Client ID** และ **Client Secret** คุณจะต้องเข้าถึงเมนู **Developers** จากนั้น สร้างแอปพลิเคชันใหม่เพื่อสร้าง Client ID และ Secret

ใช้การตั้งค่าเหล่านี้สำหรับแอปพลิเคชันใหม่ของคุณ:

- เลือก **OAuth 2** เป็น **Authorization Protocol**
- คัดลอก **OAuth Callback URL** จาก n8n และใช้เป็น **Callback URL** ใน Medium
