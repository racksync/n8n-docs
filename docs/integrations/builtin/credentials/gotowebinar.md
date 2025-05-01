---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: GoToWebinar credentials
description: Documentation for GoToWebinar credentials. Use these credentials to authenticate GoToWebinar in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# GoTo Webinar credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [GoToWebinar](/integrations/builtin/app-nodes/n8n-nodes-base.gotowebinar.md)

## Prerequisites

สร้างบัญชี [GoToWebinar](https://www.goto.com/webinar){:target=_blank .external-link} พร้อมสิทธิ์เข้าถึง [Developer Center](https://developer.goto.com/){:target=_blank .external-link}

## Supported authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับการยืนยันตัวตนกับบริการนี้ได้ที่ [GoToWebinar's API documentation](https://developer.goto.com/GoToWebinarV2){:target=_blank .external-link}

## Using OAuth2

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Client ID**: ได้รับเมื่อคุณสร้าง OAuth client
- **Client Secret**: ได้รับเมื่อคุณสร้าง OAuth client

ดูคำแนะนำโดยละเอียดเกี่ยวกับการสร้าง OAuth client ได้ที่ [Create an OAuth client documentation](https://developer.goto.com/guides/Get%20Started/02_HOW_createClient/){:target=_blank .external-link} คัดลอก **OAuth Callback URL** จาก n8n เพื่อใช้เป็น **Redirect URI** ใน OAuth client ของคุณ Client ID และ Client secret จะได้รับเมื่อคุณตั้งค่า client เสร็จสิ้น

