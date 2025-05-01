---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Facebook Graph API credentials
description: Documentation for Facebook Graph API credentials. Use these credentials to authenticate Facebook Graph API in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Facebook Graph API credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Facebook Graph API](/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi.md)

/// note | Facebook Trigger credentials
หากคุณต้องการสร้าง credentials สำหรับ node [Facebook Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/index.md) ให้ทำตามคำแนะนำที่กล่าวถึงในเอกสาร [Facebook App credentials](/integrations/builtin/credentials/facebookapp.md)
///

## Supported authentication methods

- App access token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Meta's Graph API documentation](https://developers.facebook.com/docs/graph-api/overview){:target=_blank .external-link}

## Using app access token

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [Meta for Developers](https://developers.facebook.com/){:target=_blank .external-link} และ:

- **Access Token** ของแอป

มีสองขั้นตอนในการตั้งค่า credential ของคุณ:

1. [สร้าง Meta app](#create-a-meta-app) พร้อมผลิตภัณฑ์ที่คุณต้องการเข้าถึง
2. [สร้าง App Access Token](#generate-an-app-access-token) สำหรับแอปนั้น

ดูคำแนะนำโดยละเอียดด้านล่างสำหรับแต่ละขั้นตอน

### Create a Meta app

วิธีสร้าง Meta app:

1. ไปที่ [App Dashboard](https://developers.facebook.com/apps){:target=_blank .external-link} ของ Meta Developer แล้วเลือก **Create App**
2. หากคุณมี business portfolio และพร้อมที่จะเชื่อมต่อแอปเข้ากับมัน ให้เลือก business portfolio หากคุณไม่มี business portfolio หรือยังไม่พร้อมที่จะเชื่อมต่อแอปเข้ากับ portfolio ให้เลือก **I don’t want to connect a business portfolio yet** แล้วเลือก **Next** หน้า **Use cases** จะเปิดขึ้น
3. เลือก **Use case** ที่สอดคล้องกับวิธีที่คุณต้องการใช้ Facebook Graph API ตัวอย่างเช่น สำหรับผลิตภัณฑ์ในชุด **Business** ของ Meta (เช่น Messenger, Instagram, WhatsApp, Marketing API, App Events, Audience Network, Commerce API, Fundraisers, Jobs, Threat Exchange และ Webhooks) ให้เลือก **Other** จากนั้นเลือก **Next**
4. เลือก **Business** และ **Next**
5. กรอกข้อมูลที่จำเป็น:
    * เพิ่ม **App name**
    * เพิ่ม **App contact email**
    * ที่นี่คุณสามารถเชื่อมต่อกับ business portfolio หรือข้ามไปได้อีกครั้ง
1. เลือก **Create app**
1. หน้า **Add products to your app** จะเปิดขึ้น
1. เลือก **App settings > Basic** จากเมนูด้านซ้าย
1. ป้อน **Privacy Policy URL** (จำเป็นต้องใช้เพื่อทำให้แอป "Live")
1. เลือก **Save changes**
1. ที่ด้านบนของหน้า สลับ **App Mode** จาก **Development** เป็น **Live**
1. ในเมนูด้านซ้าย เลือก **Add Product**
6. หน้า **Add products to your app** จะปรากฏขึ้น เลือกผลิตภัณฑ์ที่เหมาะสมกับแอปของคุณและกำหนดค่า

ดูข้อมูลเพิ่มเติมเกี่ยวกับการสร้างแอป ฟิลด์ที่จำเป็น เช่น Privacy Policy URL และการเพิ่มผลิตภัณฑ์ได้ที่เอกสาร [Create an app](https://developers.facebook.com/docs/development/create-an-app){:target=_blank .external-link} ของ Meta

สำหรับข้อมูลเพิ่มเติมเกี่ยวกับโหมดแอปและการเปลี่ยนเป็นโหมด **Live** โปรดดูที่ [App Modes](https://developers.facebook.com/docs/development/build-and-test/app-modes){:target=_blank .external-link} และ [Publish | App Types](https://developers.facebook.com/docs/development/release#app-types){:target=_blank .external-link}

### Generate an App Access Token

ถัดไป สร้าง app access token เพื่อใช้กับ n8n credential ของคุณและผลิตภัณฑ์ที่คุณเลือก:

1. ในแท็บหรือหน้าต่างแยกต่างหาก เปิด [Graph API explorer](https://developers.facebook.com/tools/explorer/){:target=_blank .external-link}
2. เลือก **Meta App** ที่คุณเพิ่งสร้างในส่วน **Access Token**
3. ใน **User or Page** เลือก **Get App Token**
4. เลือก **Generate Access Token**
5. หน้าเว็บจะแจ้งให้คุณเข้าสู่ระบบและให้สิทธิ์การเข้าถึง ทำตามคำแนะนำบนหน้าจอ

    /// warning | App unavailable
    คุณอาจได้รับคำเตือนว่าแอปไม่พร้อมใช้งาน เมื่อคุณทำให้แอปใช้งานได้จริง อาจมีความล่าช้าเล็กน้อยก่อนที่คุณจะสามารถสร้าง access token ได้
    ///

5. คัดลอก token และป้อนลงใน n8n credential ของคุณเป็น **Access Token**

ดูข้อมูลเพิ่มเติมเกี่ยวกับการสร้าง token ได้ที่คำแนะนำของ Meta สำหรับ [Your First Request](https://developers.facebook.com/docs/graph-api/get-started#get-started){:target=_blank .external-link}
