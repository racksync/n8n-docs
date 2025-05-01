---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Set up SAML
description: Generic setup instructions for using SAML SSO with n8n.
contentType: howto
---

# Set up SAML

/// info | Feature availability
* มีให้ใช้งานบน Enterprise plans
* คุณต้องมีสิทธิ์เข้าถึง n8n instance owner account เพื่อเปิดใช้งานและกำหนดค่า SAML

มีให้ใช้งานตั้งแต่เวอร์ชัน 0.225.0
///

หน้านี้จะบอกวิธีเปิดใช้งาน SAML SSO (single sign-on) ใน n8n โดยสมมติว่าคุณคุ้นเคยกับ SAML อยู่แล้ว หากไม่คุ้นเคย [SAML Explained in Plain English](https://www.onelogin.com/learn/saml){:target=_blank .external-link} สามารถช่วยให้คุณเข้าใจวิธีการทำงานของ SAML และประโยชน์ของมันได้

## Enable SAML

1. ใน n8n ไปที่ **Settings** > **SSO**
2. จดบันทึก n8n **Redirect URL** และ **Entity ID**
    1. **Optional**: หาก IdP ของคุณอนุญาตให้ตั้งค่า SAML จาก metadata ที่ import เข้ามา ให้ไปที่ URL ของ **Entity ID** และบันทึกไฟล์ XML นั้น
    2. **Optional**: หากคุณใช้งาน n8n หลัง load balancer ตรวจสอบให้แน่ใจว่าคุณได้กำหนดค่า `N8N_EDITOR_BASE_URL` แล้ว
3. ตั้งค่า SAML กับ IdP (identity provider) ของคุณ คุณจะต้องใช้ redirect URL และ entity ID นอกจากนี้คุณอาจต้องใช้ email address และชื่อสำหรับผู้ใช้ IdP
4. หลังจากตั้งค่าใน IdP ของคุณเสร็จแล้ว ให้โหลด metadata XML เข้าสู่ n8n คุณสามารถใช้ metadata URL หรือ raw XML ได้:
    1. **Metadata URL**: คัดลอก metadata URL จาก IdP ของคุณไปวางในช่อง **Identity Provider Settings** ใน n8n
    2. **Raw XML**: ดาวน์โหลด metadata XML จาก IdP ของคุณ สลับ **Identity Provider Settings** เป็น **XML** จากนั้นคัดลอก raw XML ไปวางใน **Identity Provider Settings**
5. เลือก **Save settings**
6. เลือก **Test settings** เพื่อตรวจสอบว่าการตั้งค่า SAML ของคุณทำงานได้ถูกต้อง
7. ตั้งค่า SAML 2.0 เป็น **Activated**

## Generic IdP setup

ขั้นตอนในการกำหนดค่า IdP จะแตกต่างกันไปขึ้นอยู่กับ IdP ที่คุณเลือก นี่คืองานตั้งค่าทั่วไปบางส่วน:

* สร้าง app สำหรับ n8n ใน IdP ของคุณ
* Map n8n attributes กับ IdP attributes:

    | Name | Name format | Value (IdP side) |
    | ---- | ----------- | ---------------- |
    | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress | URI Reference | User email       |
    | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstname    | URI Reference | User First Name  |
    | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastname     | URI Reference | User Last Name   |
    | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn          | URI Reference | User Email       |

## Setup resources for common IdPs

ลิงก์เอกสารสำหรับ IdPs ทั่วไป

| IdP | Documentation |
| --- | ------------- |
| Auth0 | [Configure Auth0 as SAML Identity Provider: Manually configure SSO integrations](https://auth0.com/docs/authenticate/protocols/saml/saml-sso-integrations/configure-auth0-saml-identity-provider#manually-configure-sso-integrations){:target=_blank .external-link} |
| Authentik | [Applications](https://goauthentik.io/docs/applications){:target=_blank .external-link} and the [SAML Provider](https://goauthentik.io/docs/providers/saml/){:target=_blank .external-link} |
| Azure AD | [SAML authentication with Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/auth-saml){:target=_blank .external-link} |
| Keycloak | Choose a [Getting Started](https://www.keycloak.org/guides#getting-started){:target=_blank .external-link} guide depending on your hosting. |
| Okta | n8n provides a [Workforce Identity setup guide](/user-management/saml/okta.md) |
| PingIdentity | [PingOne SSO](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_p1sso_start.html){:target=_blank .external-link} |

