---
title: ข้อมูลเข้าสู่ระบบ Strava
description: คู่มือการตั้งค่า Strava credentials สำหรับเชื่อมต่อ Strava กับ n8n
contentType: [integration, reference]
---

# Strava credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Strava](/integrations/builtin/app-nodes/n8n-nodes-base.strava.md)
- [Strava Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.stravatrigger.md)

## Prerequisites

- สร้างบัญชี [Strava](https://strava.com){:target=_blank .external-link}
- สร้างแอป Strava ใน [**Settings > API**](https://www.strava.com/settings/api){:target=_blank .external-link} ดูรายละเอียดเพิ่มเติมที่ [Using OAuth2](#using-oauth2)

## Supported authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Strava's API documentation](https://developers.strava.com/docs/reference/){:target=_blank .external-link}

## Using OAuth2

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Client ID**: ได้จากการ [สร้างแอป Strava](https://developers.strava.com/docs/getting-started/#account){:target=_blank .external-link}
- **Client Secret**: ได้จากการ [สร้างแอป Strava](https://developers.strava.com/docs/getting-started/#account){:target=_blank .external-link}

ตั้งค่าดังนี้ในแอป Strava ของคุณ:

- ใน n8n ให้คัดลอก **OAuth Callback URL** แล้วนำไปวางใน **Authorization Callback Domain** ของแอป Strava
- ลบ protocol (`https://` หรือ `http://`) และ relative URL (`/oauth2/callback` หรือ `/rest/oauth2-credential/callback`) ออกจาก **Authorization Callback Domain** เช่น ถ้า OAuth Redirect URL เดิมคือ `https://oauth.n8n.cloud/oauth2/callback` ให้ใช้ `oauth.n8n.cloud` เป็น **Authorization Callback Domain**
- คัดลอก **Client ID** และ **Client Secret** จากแอป แล้วนำไปใส่ใน n8n credential

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ OAuth flow ได้ที่ [Authentication](https://developers.strava.com/docs/authentication/){:target=_blank .external-link}
