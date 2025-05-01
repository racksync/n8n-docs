---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Formstack Trigger credentials
description: Documentation for Formstack Trigger credentials. Use these credentials to authenticate Formstack Trigger in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Formstack Trigger credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Formstack Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.formstacktrigger.md)

## Prerequisites

สร้างบัญชี [Formstack](https://www.formstack.com/){:target=_blank .external-link}

## Supported authentication methods

- API access token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Formstack's API documentation](https://developers.formstack.com/reference/api-overview){:target=_blank .external-link}

## Using API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- API **Access Token**: หากต้องการสร้าง Access Token ให้ [create a new application](https://www.formstack.com/admin/apiKey/main){:target=_blank .external-link} ใน Formstack โดยใช้รายละเอียดต่อไปนี้:
    * **Redirect URI**: สำหรับ n8n instances บนคลาวด์ ให้ป้อน `https://oauth.n8n.cloud/oauth2/callback`
        - สำหรับ n8n instances ที่ self-hosted ให้ป้อน OAuth callback URL สำหรับ n8n instance ของคุณในรูปแบบ `https://<n8n_url>/rest/oauth2-credential/callback` ตัวอย่างเช่น `https://localhost:5678/rest/oauth2-credential/callback`
    * **Platform**: เลือก **Website**

เมื่อคุณสร้าง application แล้ว ให้คัดลอก access token จากรายการ applications หรือโดยการเลือก application เพื่อดูรายละเอียด

ดูคำแนะนำโดยละเอียดเพิ่มเติมได้ที่ [Formstack's API Authorization documentation](https://developers.formstack.com/reference/api-overview#obtaining-an-api-key-oauth2-access-token){:target=_blank .external-link}

/// note | Access token permissions
Formstack ผูก access tokens กับผู้ใช้ Formstack Access tokens เป็นไปตามสิทธิ์ของผู้ใช้ Formstack (ในแอป)
///

## Using OAuth2

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Client ID**
- **Client Secret**

หากต้องการสร้างทั้งสองอย่างนี้ ให้ [create a new application](https://www.formstack.com/admin/apiKey/main){:target=_blank .external-link} ใน Formstack โดยใช้รายละเอียดต่อไปนี้:

- **Redirect URI**: คัดลอก **OAuth Redirect URL** จาก n8n credential เพื่อป้อนที่นี่
    - สำหรับ n8n instances ที่ self-hosted ให้ป้อน OAuth callback URL สำหรับ n8n instance ของคุณในรูปแบบ `https://<n8n_url>/rest/oauth2-credential/callback` ตัวอย่างเช่น `https://localhost:5678/rest/oauth2-credential/callback`
- **Platform**: เลือก **Website**

เมื่อคุณสร้าง application แล้ว ให้เลือกจากรายการ applications เพื่อดู **Application Details** คัดลอก **Client ID** และ **Client Secret** แล้วเพิ่มลงใน n8n เมื่อคุณเพิ่มทั้งสองอย่างแล้ว ให้เลือกปุ่ม **Connect my account** เพื่อเริ่มขั้นตอน OAuth2 และกระบวนการ authorization

ดูคำแนะนำโดยละเอียดเพิ่มเติมได้ที่ [Formstack's API Authorization documentation](https://developers.formstack.com/reference/api-overview#obtaining-an-api-key-oauth2-access-token){:target=_blank .external-link}

/// note | Access token permissions
Formstack ผูก access tokens กับผู้ใช้ Formstack Access tokens เป็นไปตามสิทธิ์ของผู้ใช้ Formstack (ในแอป)
///

