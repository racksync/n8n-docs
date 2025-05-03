---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการตั้งค่า Zoom credentials
description: วิธีตั้งค่า Zoom credentials เพื่อเชื่อมต่อและยืนยันตัวตนกับ Zoom ใน n8n
contentType: [integration, reference]
---

# Zoom credentials

คุณสามารถใช้ credentials นี้เพื่อ authenticate กับ node เหล่านี้:

- [Zoom](/integrations/builtin/app-nodes/n8n-nodes-base.zoom.md)

## Prerequisites

สมัคร [Zoom](https://zoom.us/){:target=_blank .external-link} ให้เรียบร้อยก่อน โดย account ของคุณต้องมีสิทธิ์อย่างใดอย่างหนึ่งต่อไปนี้:

- Account owner
- Account admin
- Zoom for developers role

## Supported authentication methods

- API JWT token
- OAuth2

/// warning | API JWT token deprecation
Zoom ยกเลิกการรองรับ JWT access tokens ตั้งแต่เดือนมิถุนายน 2023 ต้องใช้ OAuth2 สำหรับ credentials ใหม่เท่านั้น
///

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Zoom's API documentation](https://developers.zoom.us/docs/api/){:target=_blank .external-link}

## Using API JWT token

วิธีนี้ถูก Zoom ยกเลิกการใช้งานแล้ว ไม่ควรสร้าง credentials ใหม่ด้วยวิธีนี้

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **JWT token**: สร้าง JWT token ได้โดยสร้าง JWT app ใหม่ใน [Zoom App Marketplace](https://marketplace.zoom.us/){:target=_blank .external-link}

## Using OAuth2

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Client ID**: ได้จากการสร้าง OAuth app ใน Zoom App Marketplace
- **Client Secret**: ได้จากการสร้าง OAuth app

สร้าง **Client ID** และ **Client Secret** ได้โดย [สร้าง OAuth app](https://developers.zoom.us/docs/integrations/create/){:target=_blank .external-link}

ตั้งค่า OAuth app ตามนี้:

- เลือก **User-managed app** ใน **Select how the app is managed**
- คัดลอก **OAuth Callback URL** จาก n8n ไปใส่ใน Zoom เป็น **OAuth Redirect URL**
- ถ้า credential ใน n8n มี **Whitelist URL** ให้ใส่ URL นั้นเป็น **OAuth Redirect URL** ใน Zoom ด้วย
- ใส่ **Scopes** ตามที่ต้องการใช้งาน สำหรับใช้ทุกฟีเจอร์ใน [Zoom](/integrations/builtin/app-nodes/n8n-nodes-base.zoom.md) node ให้เลือก:
    - `meeting:read`
    - `meeting:write`
    - ดูรายละเอียด scope เพิ่มเติมที่ [OAuth scopes | Meeting scopes](https://developers.zoom.us/docs/integrations/oauth-scopes/#meeting-scopes){:target=_blank .external-link}
- คัดลอก **Client ID** และ **Client Secret** จาก Zoom app ไปใส่ใน n8n credential
