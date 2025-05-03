---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลเข้าสู่ระบบ X (Twitter เดิม)
description: คู่มือการตั้งค่า credentials สำหรับเชื่อมต่อ X (Twitter) กับ n8n เพื่อใช้งาน workflow automation
contentType: [integration, reference]
priority: medium
---

# X (formerly Twitter) credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [X (formerly Twitter)](/integrations/builtin/app-nodes/n8n-nodes-base.twitter.md)

## Prerequisites

- สร้าง [X developer](https://developer.x.com/en){:target=_blank .external-link} account ขึ้นมาก่อน
- สร้าง [Twitter app](https://developer.x.com/en/docs/apps){:target=_blank .external-link} หรือจะใช้ project และ app ที่ถูกสร้างให้อัตโนมัติเมื่อสมัคร developer portal ก็ได้ ดูรายละเอียดการตั้งค่า app เพิ่มเติมในแต่ละ authentication method ด้านล่าง

## Supported authentication methods

- OAuth2

/// note | Deprecation warning
n8n เคยรองรับวิธี **OAuth** authentication ที่ใช้ X's [OAuth 1.0a](https://developer.x.com/en/docs/authentication/oauth-1-0a){:target=_blank .external-link} authentication method มาก่อน แต่ n8n ได้ยกเลิกวิธีนี้ตั้งแต่ปล่อย V2 ของ X node ใน n8n เวอร์ชัน [0.236.0](/release-notes/0-x.md#n8n02360)
///

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [X's API documentation](https://developer.x.com/en/docs/twitter-api){:target=_blank .external-link} และดูข้อมูลเกี่ยวกับการยืนยันตัวตนได้ที่ [X's API authentication documentation](https://developer.x.com/en/docs/authentication/overview){:target=_blank .external-link}

ดูข้อมูลเกี่ยวกับ app-only authentication ได้ที่ [Application-only Authentication](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only){:target=_blank .external-link}

## Using OAuth2

ใช้วิธีนี้ถ้าคุณใช้ n8n เวอร์ชัน 0.236.0 ขึ้นไป

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Client ID**
- **Client Secret**

วิธีสร้าง Client ID และ Client Secret:

1. เข้าไปที่ [developer portal](https://developer.x.com/en/portal/dashboard){:target=_blank .external-link} ของ Twitter แล้วเปิด project ของคุณ
2. ที่แท็บ **Overview** ของ project ให้หา section **Apps** แล้วเลือก **Add App**
3. ตั้งชื่อ app ในช่อง **Name** แล้วกด **Next**
1. ไปที่ **App Settings**
4. ใน **User authentication settings** ให้เลือก **Set Up**
1. ตั้งค่า **App permissions** เลือก **Read and write and Direct message** ถ้าต้องการใช้ฟังก์ชันทั้งหมดของ n8n X node
5. ใน section **Type of app** ให้เลือก **Web App, Automated App or Bot**
1. ใน n8n ให้ copy **OAuth Redirect URL**
7. ใน X app ให้หา section **App Info** แล้ววาง URL ที่ copy มาในช่อง **Callback URI / Redirect URL**
7. เพิ่ม **Website URL**
8. กดบันทึกการเปลี่ยนแปลง
1. copy **Client ID** และ **Client Secret** ที่แสดงใน X แล้วนำไปใส่ในช่องที่เกี่ยวข้องใน n8n credential

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน OAuth 2.0 ได้ที่ [OAuth 2.0 Authentication documentation](https://developer.x.com/en/docs/authentication/oauth-2-0){:target=_blank .external-link}

/// note | X rate limits
credential นี้ใช้ OAuth 2.0 Bearer Token authentication method ดังนั้นจะมีข้อจำกัด rate limit ตามที่ X กำหนด ดูรายละเอียดเพิ่มเติมได้ที่ [X rate limits](#x-rate-limits) ด้านล่าง
///

## X rate limits

X จะมีการจำกัดจำนวนการใช้งาน (rate limit) ต่อ endpoint ตามระดับ access plan ของ developer แต่ละคน โดย X จะคำนวณ rate limit ของ app และ user แยกจากกัน ดูรายละเอียด rate limit และวิธีหลีกเลี่ยงได้ที่ [Rate limits](https://developer.x.com/en/docs/twitter-api/rate-limits){:target=_blank .external-link}

แนวทางการคำนวณ rate limit:

- ถ้าใช้ OAuth แบบเก่า (deprecated) จะใช้ user rate limit คือจำกัดตาม access token ของแต่ละ user ในแต่ละช่วงเวลา
- ถ้า [Using OAuth2](#using-oauth2) จะใช้ app rate limit คือจำกัดตาม app ในแต่ละช่วงเวลา

X จะคำนวณ user rate limit และ app rate limit แยกจากกัน

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ rate limit แต่ละประเภทได้ที่ [Rate limits and authentication methods](https://developer.x.com/en/docs/twitter-api/rate-limits#auth){:target=_blank .external-link}
