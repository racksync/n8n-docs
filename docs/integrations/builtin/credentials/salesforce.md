---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Salesforce credentials
description: Documentation for Salesforce credentials. Use these credentials to authenticate Salesforce in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Salesforce credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Salesforce](/integrations/builtin/app-nodes/n8n-nodes-base.salesforce.md)
- [Salesforce trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.salesforcetrigger.md)

## Supported authentication methods

- JWT
- OAuth2

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ Salesforce ได้ที่ [Salesforce's developer documentation](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_intro.htm){:target=_blank .external-link}

## Using JWT

ในการตั้งค่า credentials นี้ คุณต้องมี [Salesforce](https://www.salesforce.com/){:target=_blank .external-link} account และ:

- **Environment Type** (Production หรือ Sandbox)
- **Client ID**: ได้จากการสร้าง connected app
- **Username** ของ Salesforce
- **Private Key** สำหรับ self-signed digital certificate

ขั้นตอนการตั้งค่า:

1. ใน n8n ให้เลือก **Environment Type** ที่ตรงกับ environment ของคุณ (Production หรือ Sandbox)
2. กรอก **Username** ของ Salesforce
3. ล็อกอินเข้า Salesforce ของคุณ
4. คุณต้องมี private key และ certificate ที่ออกโดย certification authority จะใช้ key/cert ของคุณเอง หรือใช้ OpenSSL สร้าง key และ self-signed digital certificate ก็ได้ ดูวิธีที่ [Create a Private Key and Self-Signed Digital Certificate documentation](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm){:target=_blank .external-link}
5. ที่ Salesforce ไปที่ **Setup** แล้วค้นหา `App Manager` จากนั้นเลือก **App Manager**
6. ในหน้า App Manager ให้เลือก **New Connected App**
7. กรอก **Basic Info** ที่จำเป็น เช่น **Name** และ **Contact Email address** ดูรายละเอียดที่ [Configure Basic Connected App Settings](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_basics.htm&type=5){:target=_blank .external-link}
8. ติ๊กถูกที่ **Enable OAuth Settings**
9. สำหรับ **Callback URL** ให้ใส่ `http://localhost:1717/OauthRedirect`
10. ติ๊กถูกที่ **Use digital signatures**
11. เลือก **Choose File** แล้วอัปโหลดไฟล์ certificate เช่น `server.crt`
12. เพิ่ม **OAuth scopes** ดังนี้:
	- **Full access (full)**
	- **Perform requests at any time (refresh_token, offline_access)**
13. กด **Save** แล้ว **Continue** จะเข้าสู่หน้า **Manage Connected Apps** ของแอปที่เพิ่งสร้าง
14. ในส่วน **API (Enable OAuth Settings)** ให้เลือก **Manage Consumer Details**
15. คัดลอก **Consumer Key** ไปใส่ใน n8n ที่ **Client ID**
16. ใส่เนื้อหาในไฟล์ private key ลงใน n8n ที่ **Private Key**
	- ใช้ multi-line editor ใน n8n
	- ใส่ private key ในรูปแบบ PEM key มาตรฐาน:
        ```
        -----BEGIN PRIVATE KEY-----
        KEY DATA GOES HERE
        -----END PRIVATE KEY-----
        ```

ขั้นตอนข้างต้นคือสิ่งที่ต้องทำในฝั่ง n8n Salesforce แนะนำให้ตั้งค่า refresh token policies, session policies, และ OAuth policies เพิ่มเติม:

17. ที่ Salesforce เลือก **Back to Manage Connected Apps**
18. เลือก **Manage**
19. เลือก **Edit Policies**
20. ตรวจสอบ **Refresh Token Policy** Salesforce แนะนำให้ใช้ expire refresh token after 90 days
21. ในส่วน **Session Policies** Salesforce แนะนำให้ตั้ง **Timeout Value** เป็น 15 นาที
22. ในส่วน **OAuth Policies** เลือก **Admin approved users are pre-authorized for permitted users** ที่ **Permitted Users** แล้วกด **OK**
23. กด **Save**
24. เลือก **Manage Profiles** แล้วเลือก profile ที่ pre-authorized ให้ใช้ connected app นี้ แล้วกด **Save**
25. เลือก **Manage Permission Sets** เพื่อเลือก permission sets (สร้าง permission sets ถ้าจำเป็น)

ดูรายละเอียดเพิ่มเติมที่ [Create a Connected App in Your Org](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm){:target=_blank .external-link}

## Using OAuth2

ในการตั้งค่า credentials นี้ คุณต้องมี [Salesforce](https://www.salesforce.com/){:target=_blank .external-link} account

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

สำหรับผู้ใช้ Cloud และ hosted ให้เลือก **Environment Type** ระหว่าง **Production** และ **Sandbox**

ถ้าคุณ [self-hosting](/hosting/index.md) n8n คุณต้องตั้งค่า OAuth2 เองโดยสร้าง connected app:

1. ใน n8n ให้เลือก **Environment Type** ที่ตรงกับ environment ของคุณ (Production หรือ Sandbox)
2. กรอก **Username** ของ Salesforce
3. ล็อกอินเข้า Salesforce ของคุณ
4. ที่ Salesforce ไปที่ **Setup** แล้วค้นหา `App Manager` จากนั้นเลือก **App Manager**
5. ในหน้า App Manager ให้เลือก **New Connected App**
6. กรอก **Basic Info** ที่จำเป็น เช่น **Name** และ **Contact Email address** ดูรายละเอียดที่ [Configure Basic Connected App Settings](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_basics.htm&type=5){:target=_blank .external-link}
7. ติ๊กถูกที่ **Enable OAuth Settings**
8. สำหรับ **Callback URL** ให้ใส่ `http://localhost:1717/OauthRedirect`
9. เพิ่ม **OAuth scopes** ดังนี้:
	- **Full access (full)**
	- **Perform requests at any time (refresh_token, offline_access)**
10. ตรวจสอบให้แน่ใจว่าไม่ได้ติ๊กถูกที่:
	- **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows**
	- **Require Secret for Web Server Flow**
	- **Require Secret for Refresh Token Flow**
11. กด **Save** แล้ว **Continue** จะเข้าสู่หน้า **Manage Connected Apps** ของแอปที่เพิ่งสร้าง
12. ในส่วน **API (Enable OAuth Settings)** ให้เลือก **Manage Consumer Details**
13. คัดลอก **Consumer Key** ไปใส่ใน n8n ที่ **Client ID**
14. คัดลอก **Consumer Secret** ไปใส่ใน n8n ที่ **Client Secret**

ขั้นตอนข้างต้นคือสิ่งที่ต้องทำในฝั่ง n8n Salesforce แนะนำให้ตั้งค่า refresh token policies และ session policies เพิ่มเติม:

15. ที่ Salesforce เลือก **Back to Manage Connected Apps**
16. เลือก **Manage**
17. เลือก **Edit Policies**
18. ตรวจสอบ **Refresh Token Policy** Salesforce แนะนำให้ใช้ expire refresh token after 90 days
19. ในส่วน **Session Policies** Salesforce แนะนำให้ตั้ง **Timeout Value** เป็น 15 นาที

ดูรายละเอียดเพิ่มเติมที่ [Create a Connected App in Your Org](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm){:target=_blank .external-link}
