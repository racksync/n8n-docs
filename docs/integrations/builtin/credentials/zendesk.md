---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการตั้งค่า Zendesk credentials
description: วิธีตั้งค่า Zendesk credentials เพื่อเชื่อมต่อและยืนยันตัวตนกับ Zendesk ใน n8n
contentType: [integration, reference]
---

# Zendesk credentials

คุณสามารถใช้ credentials นี้เพื่อ authenticate กับ node เหล่านี้:

- [Zendesk](/integrations/builtin/app-nodes/n8n-nodes-base.zendesk.md)
- [Zendesk Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.zendesktrigger.md)

## Prerequisites

- สมัคร [Zendesk](https://zendesk.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน
- ถ้าจะใช้ API token authentication ให้เปิด token access ที่ Admin Center ใน **Apps and integrations > APIs > Zendesk APIs**

## Supported authentication methods

- API token
- OAuth2

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Zendesk's API documentation](https://developer.zendesk.com/api-reference/){:target=_blank .external-link}

## Using API token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Subdomain**: subdomain ของ Zendesk คือส่วนของ URL ที่อยู่ระหว่าง `https://` กับ `.zendesk.com` เช่นถ้า URL คือ `https://n8n-example.zendesk.com/agent/dashboard` subdomain คือ `n8n-example`
- **Email**: ใส่อีเมลที่ใช้ login Zendesk
- **API Token**: สร้าง API token ได้ที่ **Apps and integrations > APIs > Zendesk API** ดูรายละเอียดที่ [API token](https://developer.zendesk.com/api-reference/introduction/security-and-auth/#api-token){:target=_blank .external-link}

## Using OAuth2

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Client ID**: ได้จากการสร้าง OAuth client ใหม่
- **Client Secret**: ได้จากการสร้าง OAuth client ใหม่
- **Subdomain**: subdomain ของ Zendesk คือส่วนของ URL ที่อยู่ระหว่าง `https://` กับ `.zendesk.com` เช่นถ้า URL คือ `https://n8n-example.zendesk.com/agent/dashboard` subdomain คือ `n8n-example`

สร้าง OAuth client ใหม่ได้ที่ **Apps and integrations > APIs > Zendesk API > OAuth Clients**

ตั้งค่าตามนี้:

 - คัดลอก **OAuth Redirect URL** จาก n8n ไปใส่ใน **Redirect URL** ของ OAuth client
 - คัดลอก **Unique identifier** ของ Zendesk client ไปใส่เป็น **Client ID** ใน n8n
 - คัดลอก **Secret** จาก Zendesk ไปใส่เป็น **Client Secret** ใน n8n
 
ดูรายละเอียดเพิ่มเติมที่ [Registering your application with Zendesk](https://support.zendesk.com/hc/en-us/articles/4408845965210-Using-OAuth-authentication-with-your-application#topic_s21_lfs_qk){:target=_blank .external-link}

