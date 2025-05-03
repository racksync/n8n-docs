---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Linear
description: เอกสารสำหรับ Linear credentials ใช้เพื่อเชื่อมต่อ Linear ใน n8n
contentType: [integration, reference]
---

# Linear credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

* [Linear Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.lineartrigger.md)
* [Linear](/integrations/builtin/app-nodes/n8n-nodes-base.linear.md)

## Prerequisites

สร้างบัญชี [Linear](https://linear.app/){:target=_blank .external-link}

## Supported authentication methods

- API key
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Linear's API documentation](https://developers.linear.app/docs/graphql/working-with-the-graphql-api){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **API Key** ส่วนตัว: สร้าง API key ใน [**Settings > API**](https://linear.app/n8n/settings/api){:target=_blank .external-link} ดูข้อมูลเพิ่มเติมได้ที่ [Linear Personal API keys documentation](https://developers.linear.app/docs/graphql/working-with-the-graphql-api#personal-api-keys){:target=_blank .external-link}

## Using OAuth2

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Client ID**: สร้างขึ้นเมื่อคุณสร้าง OAuth2 application ใหม่
- **Client Secret**: สร้างขึ้นเมื่อคุณสร้าง OAuth2 application ใหม่
- เลือก **Actor**: actor กำหนดว่า OAuth2 application ควรสร้าง issues, comments และการเปลี่ยนแปลงอื่นๆ อย่างไร ตัวเลือกได้แก่:
    - **User** (ค่าเริ่มต้นของ Linear): application สร้าง resources ในฐานะผู้ใช้ที่ให้สิทธิ์ ใช้ตัวเลือกนี้หากคุณต้องการให้ผู้ใช้แต่ละคนทำการยืนยันตัวตนของตนเอง
    - **Application**: application สร้าง resources ในฐานะตัวมันเอง ใช้ตัวเลือกนี้หากคุณมีผู้ใช้เพียงคนเดียว (เช่น admin) ที่ให้สิทธิ์ application
- หากต้องการใช้ credential นี้กับ node [Linear Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.lineartrigger.md) คุณต้องเปิดใช้งาน toggle **Include Admin Scope**

ดูคำแนะนำและคำอธิบายโดยละเอียดเพิ่มเติมได้ที่ [Linear OAuth2 Authentication documentation](https://developers.linear.app/docs/oauth/authentication){:target=_blank .external-link} ใช้ **OAuth Redirect URL** ของ n8n เป็น **Redirect callback URL** ใน Linear OAuth2 application ของคุณ
