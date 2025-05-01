---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Facebook Lead Ads credentials
description: Documentation for the Facebook Lead Ads credentials. Use these credentials to authenticate Facebook Lead Ads in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Facebook Lead Ads credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

* [Facebook Lead Ads trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md)

## Supported authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Facebook Lead Ads' documentation](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/){:target=_blank .external-link}

ดู [example workflows and related content](https://n8n.io/integrations/facebook-lead-ads-trigger/){:target=_blank .external-link} บนเว็บไซต์ของ n8n

## Using OAuth2

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [Meta for Developers](https://developers.facebook.com/){:target=_blank .external-link} และ:

- **Client ID**
- **Client Secret**

หากต้องการรับทั้งสองอย่าง ให้ [create a Meta app](https://developers.facebook.com/docs/development/create-an-app){:target=_blank .external-link} ด้วยผลิตภัณฑ์ Facebook Login หรือ Facebook Login for Business

วิธีสร้างแอปของคุณและตั้งค่า credential ด้วย **Facebook Login for Business**:

1. ไปที่ [App Dashboard](https://developers.facebook.com/apps){:target=_blank .external-link} ของ Meta Developer แล้วเลือก **Create App**
2. หากคุณมี business portfolio และพร้อมที่จะเชื่อมต่อแอปเข้ากับมัน ให้เลือก business portfolio หากคุณไม่มี business portfolio หรือยังไม่พร้อมที่จะเชื่อมต่อแอปเข้ากับ portfolio ให้เลือก **I don’t want to connect a business portfolio yet** แล้วเลือก **Next** หน้า **Use cases** จะเปิดขึ้น
3. เลือก **Other** จากนั้นเลือก **Next**
4. เลือก **Business** และ **Next**
5. กรอกข้อมูลที่จำเป็น:
    * เพิ่ม **App name**
    * เพิ่ม **App contact email**
    * ที่นี่คุณสามารถเชื่อมต่อกับ business portfolio หรือข้ามไปได้อีกครั้ง
1. เลือก **Create app** หน้า **Add products to your app** จะเปิดขึ้น
1. เลือก **Facebook Login for Business** หน้า **Settings** สำหรับผลิตภัณฑ์นี้จะเปิดขึ้น
1. คัดลอก **OAuth Redirect URL** จาก n8n credential ของคุณ
1. ในการตั้งค่าแอป Meta ของคุณใน **Client OAuth settings** ให้วาง URL นั้นเป็น **Valid OAuth Redirect URIs**
1. เลือก **App settings > Basic** จากเมนูด้านซ้าย
1. คัดลอก **App ID** และป้อนเป็น **Client ID** ภายใน n8n credential ของคุณ
1. คัดลอก **App Secret** และป้อนเป็น **Client Secret** ภายใน n8n credential ของคุณ

ตอนนี้ credential ของคุณควรเชื่อมต่อได้สำเร็จ แต่คุณจะต้องทำตามขั้นตอนเพื่อทำให้แอป Meta ของคุณใช้งานได้จริง (live) ก่อนจึงจะสามารถใช้กับ [Facebook Lead Ads trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md) ได้ นี่คือสรุปสิ่งที่คุณต้องทำ:

1. ในแอป Meta ของคุณ เลือก **App settings > Basic** จากเมนูด้านซ้าย
1. ป้อน **Privacy Policy URL** (จำเป็นต้องใช้เพื่อทำให้แอป "Live")
1. เลือก **Save changes**
1. ที่ด้านบนของหน้า สลับ **App Mode** จาก **Development** เป็น **Live**
1. Facebook Login for Business ต้องการ Advanced Access สำหรับ `public_profile` หากต้องการเพิ่ม ให้ไปที่ **App Review > Permissions and Features**
1. ค้นหา `public_profile` และเลือก **Request advanced access**
1. ทำตามขั้นตอนสำหรับ [business verification](https://www.facebook.com/business/tools/meta-verified-for-business/){:target=_blank .external-link}
1. ใช้ [Lead Ads Testing Tool](https://developers.facebook.com/tools/lead-ads-testing){:target=_blank .external-link} เพื่อทริกเกอร์การส่งฟอร์มตัวอย่างและทดสอบ workflow ของคุณ

ดูข้อมูลเพิ่มเติมเกี่ยวกับการสร้างแอป ฟิลด์ที่จำเป็น เช่น Privacy Policy URL และการเพิ่มผลิตภัณฑ์ได้ที่เอกสาร [Create an app](https://developers.facebook.com/docs/development/create-an-app){:target=_blank .external-link} ของ Meta

สำหรับข้อมูลเพิ่มเติมเกี่ยวกับโหมดแอปและการเปลี่ยนเป็นโหมด **Live** โปรดดูที่ [App Modes](https://developers.facebook.com/docs/development/build-and-test/app-modes){:target=_blank .external-link} และ [Publish | App Types](https://developers.facebook.com/docs/development/release#app-types){:target=_blank .external-link}
