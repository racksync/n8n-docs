---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ClickUp credentials
description: Documentation for ClickUp credentials. Use these credentials to authenticate ClickUp in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# ClickUp credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [ClickUp](/integrations/builtin/app-nodes/n8n-nodes-base.clickup.md)
- [ClickUp Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger.md)

## Supported authentication methods

- API access token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [ClickUp's documentation](https://clickup.com/api/){:target=_blank .external-link}

## Using API access token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [ClickUp](https://www.clickup.com/){:target=_blank .external-link} และ:

- Personal API **Access Token**

วิธีรับ personal API token ของคุณ:

1. หากคุณใช้ ClickUp 2.0 ให้เลือก avatar ของคุณที่มุมล่างซ้ายแล้วเลือก **Apps** หากคุณใช้ ClickUp 3.0 ให้เลือก avatar ของคุณที่มุมบนขวา เลือก **Settings** แล้วเลื่อนลงมาเลือก **Apps** ในแถบด้านข้าง
2. ใต้ **API Token** เลือก **Generate**
3. คัดลอก **Personal API token** ของคุณแล้วป้อนลงใน n8n credential เป็น **Access Token**

ดูข้อมูลเพิ่มเติมได้ที่ [ClickUp's Personal Token documentation](https://clickup.com/api/developer-portal/authentication#personal-token){:target=_blank .external-link}

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณ [self-hosting](/hosting/index.md) n8n คุณจะต้องสร้าง OAuth app:

1. ใน ClickUp เลือก avatar ของคุณแล้วเลือก **Integrations**
2. เลือก **ClickUp API**
3. เลือก **Create an App**
4. ป้อน **Name** สำหรับ app ของคุณ
5. ใน n8n คัดลอก **OAuth Redirect URL** ป้อน URL นี้เป็น **Redirect URL** ของ ClickUp app ของคุณ
6. เมื่อคุณสร้าง app แล้ว ให้คัดลอก **client_id** และ **secret** แล้วป้อนลงใน n8n credential ของคุณ
7. เลือก **Connect my account** และทำตามคำแนะนำบนหน้าจอเพื่อเชื่อมต่อ credential ให้เสร็จสิ้น

 ดูข้อมูลเพิ่มเติมได้ที่ [ClickUp Oauth flow documentation](https://clickup.com/api/developer-portal/authentication#oauth-flow){:target=_blank .external-link}
