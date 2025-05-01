---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Facebook App credentials
description: Documentation for Facebook App credentials. Use these credentials to authenticate Facebook App in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Facebook App credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Facebook Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/index.md)

/// note | Facebook Graph API credentials
หากคุณต้องการสร้าง credentials สำหรับ node [Facebook Graph API](/integrations/builtin/app-nodes/n8n-nodes-base.facebookgraphapi.md) ให้ทำตามคำแนะนำในเอกสาร [Facebook Graph API credentials](/integrations/builtin/credentials/facebookgraph.md)
///

## Supported authentication methods

- App access token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Meta's Graph API documentation](https://developers.facebook.com/docs/graph-api/overview){:target=_blank .external-link}

## Using app access token

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [Meta for Developers](https://developers.facebook.com/){:target=_blank .external-link} และ:

- **Access Token** ของแอป
- **App Secret** (ทางเลือก): ใช้เพื่อตรวจสอบความสมบูรณ์และที่มาของ payload

มีห้าขั้นตอนในการตั้งค่า credential ของคุณ:

1. [สร้าง Meta app](#create-a-meta-app) พร้อมผลิตภัณฑ์ Webhooks
2. [สร้าง App Access Token](#generate-an-app-access-token) สำหรับแอปนั้น
3. [กำหนดค่า Facebook trigger](#configure-the-facebook-trigger)
4. ทางเลือก: [เพิ่ม app secret](#optional-add-an-app-secret)
5. [App Review](#app-review): จำเป็นเฉพาะเมื่อผู้ใช้แอปของคุณไม่มีบทบาทในแอปเอง หากคุณกำลังสร้างแอปเพื่อวัตถุประสงค์ภายในของคุณเอง สิ่งนี้ไม่จำเป็น

ดูคำแนะนำโดยละเอียดด้านล่างสำหรับแต่ละขั้นตอน

### Create a Meta app

วิธีสร้าง Meta app:

1. ไปที่ [App Dashboard](https://developers.facebook.com/apps){:target=_blank .external-link} ของ Meta Developer แล้วเลือก **Create App**
2. หากคุณมี business portfolio และพร้อมที่จะเชื่อมต่อแอปเข้ากับมัน ให้เลือก business portfolio หากคุณไม่มี business portfolio หรือยังไม่พร้อมที่จะเชื่อมต่อแอปเข้ากับ portfolio ให้เลือก **I don’t want to connect a business portfolio yet** แล้วเลือก **Next** หน้า **Use cases** จะเปิดขึ้น
3. เลือก **Other** จากนั้นเลือก **Next**
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
6. หน้า **Add products to your app** จะปรากฏขึ้น เลือก **Webhooks**
7. ผลิตภัณฑ์ **Webhooks** จะเปิดขึ้น

ดูข้อมูลเพิ่มเติมเกี่ยวกับการสร้างแอป ฟิลด์ที่จำเป็น เช่น Privacy Policy URL และการเพิ่มผลิตภัณฑ์ได้ที่เอกสาร [Create an app](https://developers.facebook.com/docs/development/create-an-app){:target=_blank .external-link} ของ Meta

สำหรับข้อมูลเพิ่มเติมเกี่ยวกับโหมดแอปและการเปลี่ยนเป็นโหมด **Live** โปรดดูที่ [App Modes](https://developers.facebook.com/docs/development/build-and-test/app-modes){:target=_blank .external-link} และ [Publish | App Types](https://developers.facebook.com/docs/development/release#app-types){:target=_blank .external-link}

### Generate an App Access Token

ถัดไป สร้าง app access token เพื่อใช้กับ n8n credential ของคุณและผลิตภัณฑ์ Webhooks:

1. ในแท็บหรือหน้าต่างแยกต่างหาก เปิด [Graph API explorer](https://developers.facebook.com/tools/explorer/){:target=_blank .external-link}
2. เลือก **Meta App** ที่คุณเพิ่งสร้างในส่วน **Access Token**
3. ใน **User or Page** เลือก **Get App Token**
4. เลือก **Generate Access Token**
5. หน้าเว็บจะแจ้งให้คุณเข้าสู่ระบบและให้สิทธิ์การเข้าถึง ทำตามคำแนะนำบนหน้าจอ

    /// warning | App unavailable
    คุณอาจได้รับคำเตือนว่าแอปไม่พร้อมใช้งาน เมื่อคุณทำให้แอปใช้งานได้จริง อาจมีความล่าช้าเล็กน้อยก่อนที่คุณจะสามารถสร้าง access token ได้
    ///

5. คัดลอก token และป้อนลงใน n8n credential ของคุณเป็น **Access Token** บันทึก token นี้ไว้ที่อื่นด้วย เนื่องจากคุณจะต้องใช้สำหรับการกำหนดค่า Webhooks
6. บันทึก n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมเกี่ยวกับการสร้าง token ได้ที่คำแนะนำของ Meta สำหรับ [Your First Request](https://developers.facebook.com/docs/graph-api/get-started#get-started){:target=_blank .external-link}

### Configure the Facebook Trigger

ตอนนี้คุณมี token แล้ว คุณสามารถกำหนดค่า node Facebook Trigger ได้:

1. ในแอป Meta ของคุณ คัดลอก **App ID** จากแถบนำทางด้านบน
1. ใน n8n เปิด node Facebook Trigger ของคุณ
2. วาง **App ID** ลงในฟิลด์ **APP ID**
3. เลือก **Test step** เพื่อเปลี่ยน trigger เข้าสู่โหมด listening
6. กลับไปที่แท็บหรือหน้าต่างที่การกำหนดค่าผลิตภัณฑ์ **Webhooks** ของแอป Meta ของคุณเปิดอยู่
7. **Subscribe** กับ objects ที่คุณต้องการรับการแจ้งเตือน Facebook Trigger สำหรับการสมัครสมาชิกแต่ละครั้ง:
    1. คัดลอก **Webhook URL** จาก n8n และป้อนเป็น **Callback URL** ในแอป Meta ของคุณ
    1. ป้อน **Access Token** ที่คุณคัดลอกไว้ด้านบนเป็น **Verify token**
    1. เลือก **Verify and save** (ขั้นตอนนี้จะล้มเหลวหากคุณไม่ได้ให้ n8n trigger ของคุณอยู่ในโหมด listening)
    1. การสมัครสมาชิก webhook บางอย่าง เช่น **User** จะแจ้งให้คุณสมัครสมาชิกเหตุการณ์แต่ละรายการ สมัครสมาชิกเหตุการณ์ที่คุณสนใจ
    1. คุณสามารถส่งเหตุการณ์ **Test** บางส่วนจาก Meta เพื่อยืนยันว่าทุกอย่างทำงานได้ หากคุณส่งเหตุการณ์ทดสอบ ให้ตรวจสอบการรับใน n8n

ดูข้อมูลเพิ่มเติมได้ที่เอกสาร [Facebook Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/index.md)

### Optional: Add an App Secret

เพื่อความปลอดภัยที่เพิ่มขึ้น Meta แนะนำให้เพิ่ม **App Secret** สิ่งนี้จะลงนามการเรียก API ทั้งหมดด้วยพารามิเตอร์ `appsecret_proof` app secret proof คือ sha256 hash ของ access token ของคุณ โดยใช้ app secret ของคุณเป็น key

วิธีสร้าง App Secret:

1. ใน Meta ขณะดูแอปของคุณ เลือก **App settings > Basic** จากเมนูด้านซ้าย
1. เลือก **Show** ถัดจากฟิลด์ **App secret**
1. หน้าเว็บจะแจ้งให้คุณป้อนข้อมูลประจำตัวบัญชี Facebook ของคุณอีกครั้ง เมื่อคุณทำเช่นนั้น Meta จะแสดง App Secret
1. ไฮไลต์เพื่อเลือก คัดลอก และวางสิ่งนี้ลงใน n8n credential ของคุณเป็น **App Secret**
1. **Save** n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมได้ที่ [App Secret documentation](https://developers.facebook.com/docs/facebook-login/security#appsecret){:target=_blank .external-link}

### App review

App Review ต้องการ Business Verification

แอปของคุณต้องผ่าน App Review หากจะถูกใช้โดยบุคคลที่:

- ไม่มีบทบาทในแอปเอง
- ไม่มีบทบาทใน Business ที่ได้อ้างสิทธิ์ในแอป

หากผู้ใช้แอปของคุณเพียงคนเดียวคือผู้ใช้ที่มีบทบาทในแอปเอง App Review ก็ไม่จำเป็น

ในฐานะส่วนหนึ่งของกระบวนการ App Review คุณอาจต้องขอ advanced access สำหรับการสมัครสมาชิก webhook ของคุณ

ดูข้อมูลเพิ่มเติมได้ที่เอกสาร [App Review](https://developers.facebook.com/docs/resp-plat-initiatives/app-review){:target=_blank .external-link} และ [Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels#advanced-access){:target=_blank .external-link} ของ Meta

## Common issues

### Unverified apps limit

Facebook อนุญาตให้คุณมีบทบาท developer หรือ administrator ได้สูงสุด 15 แอปเท่านั้นที่ยังไม่ได้เชื่อมโยงกับ Meta Verified Business Account

โปรดดูที่ [Limitations | Create an app](https://developers.facebook.com/docs/development/create-an-app#limitations){:target=_blank .external-link} หากคุณเกินขีดจำกัดนั้น
