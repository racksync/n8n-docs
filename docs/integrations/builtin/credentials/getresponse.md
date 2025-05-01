---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: GetResponse credentials
description: Documentation for GetResponse credentials. Use these credentials to authenticate GetResponse in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# GetResponse credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [GetResponse](/integrations/builtin/app-nodes/n8n-nodes-base.getresponse.md)
- [GetResponse Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.getresponsetrigger.md)

## Prerequisites

สร้างบัญชี [GetResponse](https://www.getresponse.com/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API key
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [GetResponse's API documentation](https://apidocs.getresponse.com/v3){:target=_blank .external-link}

## Using API key

ถ้าต้องการตั้งค่า credential นี้ คุณจะต้องมี:

- **API Key**: ดูหรือสร้าง API key ได้ที่ **Integrations and API > API** ดูวิธีการโดยละเอียดได้ที่ [GetResponse Help Center](https://www.getresponse.com/help/where-do-i-find-the-api-key.html){:target=_blank .external-link}

## Using OAuth2

ถ้าต้องการตั้งค่า credential นี้ คุณจะต้องมี:

- **Client ID**: สร้างขึ้นเมื่อคุณ [register your application](https://apidocs.getresponse.com/v3/authentication/oauth2){:target=_blank .external-link}
- **Client Secret**: สร้างขึ้นเมื่อคุณ [register your application](https://apidocs.getresponse.com/v3/authentication/oauth2){:target=_blank .external-link} ในชื่อ **Client Secret Key**

ตอนที่คุณ register application ให้ copy **OAuth Redirect URL** จาก n8n ไปใส่ใน **Redirect URL** ของ GetResponse

/// note | Redirect URL with localhost
Redirect URL ควรเป็น URL ใน domain ของคุณเอง เช่น `https://mytemplatemaker.example.com/gr_callback` GetResponse ไม่รองรับ callback URL ที่เป็น localhost ดู [FAQs](#configure-oauth2-credentials-for-a-local-environment) สำหรับการตั้งค่า credentials ใน local environment
///

## Configure OAuth2 credentials for a local environment

GetResponse ไม่รองรับ callback URL ที่เป็น localhost ทำตามขั้นตอนนี้เพื่อ config OAuth credentials สำหรับ local environment:
1. ใช้ [ngrok](https://ngrok.com/){:target=_blank .external-link} เพื่อ expose server ที่รันอยู่บน port `5678` ไปยังอินเทอร์เน็ต ใน terminal ให้รันคำสั่งนี้:
```sh
ngrok http 5678
```
2. เปิด terminal ใหม่แล้วรันคำสั่งนี้ โดยแทนที่ `<YOUR-NGROK-URL>` ด้วย URL ที่ได้จากขั้นตอนก่อนหน้า
```sh
export WEBHOOK_URL=<YOUR-NGROK-URL>
```
3. ทำตามขั้นตอนใน [Using OAuth2](#using-oauth2) เพื่อ config credentials โดยใช้ URL นี้เป็น **Redirect URL**

