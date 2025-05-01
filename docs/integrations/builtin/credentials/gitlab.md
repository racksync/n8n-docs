---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: GitLab credentials
description: Documentation for GitLab credentials. Use these credentials to authenticate GitLab in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# GitLab credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [GitLab](/integrations/builtin/app-nodes/n8n-nodes-base.gitlab.md)
- [GitLab Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger.md)

## Supported authentication methods

- API access token
- OAuth2 (แนะนำ)

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [GitLab's API documentation](https://docs.gitlab.com/ee/api/rest/){:target=_blank .external-link}

## Using API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [GitLab](https://gitlab.com/){:target=_blank .external-link} และ:

- URL ของ **GitLab Server** ของคุณ
- **Access Token**

วิธีตั้งค่า credential:

1. ใน GitLab เลือก avatar ของคุณ จากนั้นเลือก **Edit profile**
2. ในแถบด้านข้างซ้าย เลือก **Access tokens**
3. เลือก **Add new token**
4. ป้อน **Name** สำหรับ token เช่น `n8n integration`
5. ป้อน **expiry date** สำหรับ token หากคุณไม่ป้อนวันหมดอายุ GitLab จะตั้งค่าโดยอัตโนมัติเป็น 365 วันหลังจากวันที่ปัจจุบัน
    - token จะหมดอายุในวันหมดอายุนั้น ณ เวลาเที่ยงคืน UTC
6. เลือก **Scopes** ที่ต้องการ สำหรับ node [GitLab](/integrations/builtin/app-nodes/n8n-nodes-base.gitlab.md) ให้ใช้ scope `api` เพื่อให้สิทธิ์เข้าถึงฟังก์ชันทั้งหมดของ node ได้อย่างง่ายดาย หรือดูที่ [Personal access token scopes](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes){:target=_blank .external-link} เพื่อเลือก scopes สำหรับฟังก์ชันที่คุณต้องการใช้
7. เลือก **Create personal access token**
8. คัดลอก access token ที่สร้างขึ้นนี้และป้อนลงใน credential ของ n8n เป็น **Access Token**
9. ป้อน URL ของ **GitLab Server** ของคุณใน credential ของ n8n

ดูข้อมูลเพิ่มเติมได้ที่ [Create a personal access token documentation](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token){:target=_blank .external-link} ของ GitLab

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณ [self-hosting](/hosting/index.md) n8n คุณจะต้องมีบัญชี [GitLab](https://gitlab.com/){:target=_blank .external-link} จากนั้นสร้าง GitLab application ใหม่:

1. ใน GitLab เลือก avatar ของคุณ จากนั้นเลือก **Edit profile**
2. ในแถบด้านข้างซ้าย เลือก **Applications**
3. เลือก **Add new application**
4. ป้อน **Name** สำหรับ application ของคุณ เช่น `n8n integration`
5. ใน n8n คัดลอก **OAuth Redirect URL** ป้อนเป็น **Redirect URI** ของ GitLab
6. เลือก **Scopes** ที่ต้องการ สำหรับ node [GitLab](/integrations/builtin/app-nodes/n8n-nodes-base.gitlab.md) ให้ใช้ scope `api` เพื่อให้สิทธิ์เข้าถึงฟังก์ชันทั้งหมดของ node ได้อย่างง่ายดาย หรือดูที่ [Personal access token scopes](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes){:target=_blank .external-link} เพื่อเลือก scopes สำหรับฟังก์ชันที่คุณต้องการใช้
6. เลือก **Save application**
7. คัดลอก **Application ID** และป้อนเป็น **Client ID** ใน credential ของ n8n
8. คัดลอก **Secret** และป้อนเป็น **Client Secret** ใน credential ของ n8n

ดูข้อมูลเพิ่มเติมได้ที่เอกสาร [Configure GitLab as an OAuth 2.0 authentication identity provider](https://docs.gitlab.com/ee/integration/oauth_provider.html){:target=_blank .external-link} ของ GitLab ดูข้อมูลเพิ่มเติมเกี่ยวกับ OAuth2 และ GitLab ได้ที่ [GitLab OAuth 2.0 identity provider API documentation](https://docs.gitlab.com/ee/api/oauth2.html){:target=_blank .external-link}
