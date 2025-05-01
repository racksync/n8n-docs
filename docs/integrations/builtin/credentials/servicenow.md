---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ServiceNow credentials
description: Documentation for ServiceNow credentials. Use these credentials to authenticate ServiceNow in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# ServiceNow credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [ServiceNow](/integrations/builtin/app-nodes/n8n-nodes-base.servicenow.md)

## Prerequisites

สมัคร [ServiceNow](https://developer.servicenow.com/dev.do#!/reference){:target=_blank .external-link} developer account ก่อนใช้งาน

## Supported authentication methods

- Basic auth
- OAuth2

## Related resources

ดูรายละเอียดเพิ่มเติมได้ที่ [ServiceNow's API documentation](https://developer.servicenow.com/dev.do#!/reference/api/washingtondc/rest/){:target=_blank .external-link}

## Using basic auth

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **User** name: ใส่ชื่อผู้ใช้ ServiceNow ของคุณ
- **Password**: ใส่รหัสผ่าน ServiceNow ของคุณ
- **Subdomain**: subdomain ของ instance คุณจะอยู่ใน URL: `https://<subdomain>.service-now.com/` เช่น ถ้า URL คือ `https://dev99890.service-now.com` subdomain คือ `dev99890`

## Using OAuth2

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Client ID**: ได้หลังจาก register app ใหม่
- **Client Secret**: ได้หลังจาก register app ใหม่
- **Subdomain**: subdomain ของ instance คุณจะอยู่ใน URL: `https://<subdomain>.service-now.com/` เช่น ถ้า URL คือ `https://dev99890.service-now.com` subdomain คือ `dev99890`

วิธีสร้าง **Client ID** และ **Client Secret** ให้ไปที่ **System OAuth > Application Registry > New > Create an OAuth API endpoint for external clients** แล้วใช้ค่าต่อไปนี้:

- คัดลอก **Client ID** แล้วนำไปใส่ใน n8n credential
- ใส่ **Client Secret** หรือปล่อยว่างไว้เพื่อให้ระบบสร้าง secret อัตโนมัติ แล้วนำ secret นี้ไปใส่ใน n8n credential
- คัดลอก **OAuth Redirect URL** จาก n8n แล้วนำไปใส่ใน **Redirect URL**

ดูรายละเอียดเพิ่มเติมได้ที่ [How to setup OAuth2 authentication for RESTMessageV2 integrations](https://www.servicenow.com/community/in-other-news/how-to-setup-oauth2-authentication-for-restmessagev2/ba-p/2271823){:target=_blank .external-link}

