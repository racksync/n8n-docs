---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Mailchimp credentials
description: Documentation for Mailchimp credentials. Use these credentials to authenticate Mailchimp in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Mailchimp credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Mailchimp](/integrations/builtin/app-nodes/n8n-nodes-base.mailchimp.md)
- [Mailchimp Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.mailchimptrigger.md)

## Prerequisites

สร้างบัญชี [Mailchimp](https://www.mailchimp.com/){:target=_blank .external-link}

## Supported authentication methods

- API key
- OAuth2

อ้างอิง [Selecting an authentication method](#selecting-an-authentication-method) สำหรับคำแนะนำเกี่ยวกับวิธีที่จะใช้

## Related resources

อ้างอิง [Mailchimp's API documentation](https://mailchimp.com/developer/marketing/api/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**: สร้าง API key ในส่วน [API keys section](https://us1.admin.mailchimp.com/account/api/){:target=_blank .external-link} ของบัญชี Mailchimp ของคุณ อ้างอิงเอกสาร [Mailchimp's Generate your API key documentation](https://mailchimp.com/developer/marketing/guides/quick-start/#generate-your-api-key){:target=_blank .external-link} สำหรับคำแนะนำโดยละเอียดเพิ่มเติม

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณต้องการกำหนดค่า OAuth2 ตั้งแต่ต้น ให้ [register an application](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/#register-your-application){:target=_blank .external-link} อ้างอิงเอกสาร [Mailchimp OAuth2 documentation](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Selecting an authentication method

Mailchimp แนะนำให้ใช้ API key หากคุณเข้าถึงข้อมูลบัญชี Mailchimp ของคุณเองเท่านั้น:

> ใช้ API key หากคุณกำลังเขียนโค้ดที่เชื่อมโยงข้อมูลแอปพลิเคชัน _ของคุณ_ กับข้อมูลบัญชี Mailchimp _ของคุณ_ อย่างแน่นหนา หากคุณต้องการเข้าถึงข้อมูลบัญชี Mailchimp _ของผู้อื่น_ คุณควรใช้ OAuth 2 ([source](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/#when-not-to-use-oauth-2){:target=_blank .external-link})

