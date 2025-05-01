---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Typeform credentials
description: Documentation for Typeform credentials. Use these credentials to authenticate Typeform in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Typeform credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Typeform Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.typeformtrigger.md)

## Supported authentication methods

- API token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Typeform's API documentation](https://www.typeform.com/developers/get-started/){:target=_blank .external-link}

## Using API token

ในการตั้งค่า credentials นี้ คุณจะต้องมีบัญชี [Typeform](https://typeform.com/){:target=_blank .external-link} และ:

- **Access Token** ส่วนตัว

วิธีขอ personal access token:

1. เข้าสู่ระบบบัญชี Typeform ของคุณ
2. เลือก avatar มุมขวาบน แล้วไปที่ **Account > Your settings >** [**Personal Tokens**](https://admin.typeform.com/user/tokens){:target=_blank .external-link}
3. เลือก **Generate a new token**
4. ตั้งชื่อ token เช่น `n8n integration`
5. สำหรับ **Scopes** ให้เลือก **Custom scopes** แล้วเลือก scope เหล่านี้:
    - Forms: Read
    - Webhooks: Read, Write
6. เลือก **Generate token**
7. คัดลอก token แล้วนำไปใส่ใน n8n credential

ดูรายละเอียดเพิ่มเติมได้ที่ [Personal access token documentation](https://www.typeform.com/developers/get-started/personal-access-token/){:target=_blank .external-link}

## Using OAuth2

ในการตั้งค่า credentials นี้ คุณจะต้องมีบัญชี [Typeform](https://typeform.com/){:target=_blank .external-link} และ:

- **Client ID**: ได้จากการลงทะเบียนแอป
- **Client Secret**: ได้จากการลงทะเบียนแอป

วิธีขอ Client ID และ Client Secret ให้ลงทะเบียนแอปใหม่ใน Typeform:

1. เข้าสู่ระบบบัญชี Typeform ของคุณ
2. มุมซ้ายบน เลือก dropdown สำหรับ organization แล้วเลือก **Developer apps**
3. เลือก **Register a new app**
4. กรอก **App Name** เช่น `n8n OAuth2 integration`
5. กรอก n8n base URL เป็น **App website** เช่น `https://n8n-sample.app.n8n.cloud/`
6. จาก n8n คัดลอก **OAuth Redirect URL** แล้วนำไปใส่ใน Typeform เป็น **Redirect URI(s)**
7. เลือก **Register app**
8. คัดลอก **Client Secret** แล้วนำไปใส่ใน n8n credential
9. ใน Typeform เลือก **Got it** เพื่อปิด modal
10. ใน **Developer apps** จะเห็นแอปใหม่ ให้คัดลอก **Client ID** แล้วนำไปใส่ใน n8n credential
10. เมื่อกรอก **Client ID** และ **Client Secret** ใน n8n แล้ว ให้เลือก **Connect my account** และทำตามขั้นตอนบนหน้าจอเพื่อ authorize แอป

ดูรายละเอียดเพิ่มเติมได้ที่ [Create applications that integrate with Typeform's APIs](https://www.typeform.com/developers/get-started/applications/#1-create-an-application-in-the-typeform-admin-panel){:target=_blank .external-link}
