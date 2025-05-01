---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Asana credentials
description: Documentation for Asana credentials. Use these credentials to authenticate Asana in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Asana credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Asana](/integrations/builtin/app-nodes/n8n-nodes-base.asana.md)
- [Asana Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.asanatrigger.md)

## Supported authentication methods

- Access token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับบริการได้ที่ [Asana's Developer Guides](https://developers.asana.com/docs/overview){:target=_blank .external-link}

## Using Access token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [Asana](https://asana.com/){:target=_blank .external-link} และ:

- Personal **Access Token** (PAT)

วิธีรับ PAT ของคุณ:

1. เปิด Asana [developer console](https://app.asana.com/0/my-apps){:target=_blank .external-link}
2. ในส่วน **Personal access tokens** เลือก **Create new token**
3. ป้อน **Token name** เช่น `n8n integration`
4. ทำเครื่องหมายในช่องเพื่อยอมรับ **Asana API terms**
5. เลือก **Create token**
6. คัดลอก token และป้อนเป็น **Access Token** ใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมได้ที่ [Asana Quick start guide](https://developers.asana.com/docs/quick-start#setup){:target=_blank .external-link}

## Using OAuth2

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [Asana](https://asana.com/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณ [self-hosting](/hosting/index.md) n8n คุณจะต้องลงทะเบียน application เพื่อตั้งค่า OAuth:

1. เปิด Asana [developer console](https://app.asana.com/0/my-apps){:target=_blank .external-link}
2. ในส่วน **My apps** เลือก **Create new app**
3. ป้อน **App name** สำหรับ application ของคุณ เช่น `n8n integration`
4. เลือกวัตถุประสงค์สำหรับ app ของคุณ
5. ทำเครื่องหมายในช่องเพื่อยอมรับ **Asana API terms**
6. เลือก **Create app** หน้าจะเปิดไปที่ **Basic Information** ของ app
7. เลือก **OAuth** จากเมนูด้านซ้าย
8. ใน n8n คัดลอก **OAuth Redirect URL**
9. ใน Asana เลือก **Add redirect URL** และป้อน URL ที่คุณคัดลอกมาจาก n8n
7. คัดลอก **Client ID** จาก Asana และป้อนลงใน n8n credential ของคุณ
8. คัดลอก **Client Secret** จาก Asana และป้อนลงใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมได้ที่ [Asana OAuth register an application documentation](https://developers.asana.com/docs/oauth#register-an-application){:target=_blank .external-link}
