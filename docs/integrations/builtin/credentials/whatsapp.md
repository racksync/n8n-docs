---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: WhatsApp Business Cloud credentials
description: Documentation for WhatsApp Business Cloud credentials. Use these credentials to authenticate WhatsApp Business Cloud in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: high
---

# WhatsApp Business Cloud credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [WhatsApp Business Cloud](/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/index.md)
- [WhatsApp Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md)

## Requirements

ในการสร้าง credentials สำหรับ WhatsApp คุณต้องมี Meta assets ต่อไปนี้:

- [Meta developer](https://developers.facebook.com/docs/development/register) account: บัญชีนักพัฒนา Meta จะช่วยให้คุณสร้างและจัดการ Meta apps รวมถึงการเชื่อมต่อ WhatsApp
??? note "Set up a Meta developer account"
	1. ไปที่ [Facebook Developers site](https://developers.facebook.com)
	2. คลิก **Getting Started** ที่มุมขวาบน (ถ้าขึ้นว่า **My Apps** แสดงว่าคุณมีบัญชีนักพัฒนาแล้ว)
	3. ยอมรับข้อตกลง
	4. ใส่เบอร์โทรศัพท์เพื่อยืนยันตัวตน
	5. เลือกอาชีพหรือบทบาทของคุณ
- [business portfolio](https://www.facebook.com/business/help/1710077379203657?id=180505742745347) ของ Meta: การส่งข้อความ WhatsApp ต้องใช้ business portfolio ของ Meta (ชื่อเดิม Business Manager account) UI อาจแสดงชื่อใดชื่อหนึ่ง
??? note "Set up a Meta business portfolio"
	1. ไปที่ [Facebook Business site](https://business.facebook.com)
	2. เลือก **Create an account**
		* ถ้ามี Facebook Business account และ portfolio อยู่แล้ว แต่ต้องการสร้าง portfolio ใหม่ ให้เปิดตัวเลือก business portfolio ทางเมนูซ้ายแล้วเลือก **Create a business portfolio**
	3. กรอก **Business portfolio name**
	4. กรอก **name** ของคุณ
	5. กรอก **business email**
	6. กด **Submit** หรือ **Create**
- [business app](https://developers.facebook.com/docs/development/create-an-app/) ของ Meta ที่ตั้งค่า WhatsApp แล้ว: เมื่อมีบัญชีนักพัฒนาแล้ว ให้สร้าง business app ของ Meta
??? note "Set up a Meta business app with WhatsApp"
	1. ไปที่ [Meta for Developers Apps dashboard](https://developers.facebook.com/apps/)
	2. เลือก **Create app**
	3. ใน **Add products to your app** ให้เลือก **Set up** ที่ช่อง WhatsApp ดูรายละเอียดที่ [Add the WhatsApp Product](https://developers.facebook.com/docs/whatsapp/solution-providers/get-started-for-tech-providers#step-3--add-the-whatsapp-product)
	4. จะเข้าสู่หน้า WhatsApp **Quickstart** เลือก business portfolio ของคุณ
	5. กด **Continue**
	6. ทางเมนูซ้ายไปที่ **App settings** > **Basic**
	7. ตั้งค่า **Privacy Policy URL** และ **Terms of Service URL** ให้กับแอป
	8. เปลี่ยน **App Mode** เป็น **Live**

## Supported authentication methods

- API key: ใช้กับ [WhatsApp Business Cloud](/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/index.md) node
- OAuth2: ใช้กับ [WhatsApp Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md) node

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [WhatsApp's API documentation](https://developers.facebook.com/docs/whatsapp/#platform-apis)

Meta จะจัดกลุ่มผู้สร้าง WhatsApp business apps เป็น Tech Providers ดูรายละเอียดที่ [Get Started for Tech Providers](https://developers.facebook.com/docs/whatsapp/solution-providers/get-started-for-tech-providers)

## Using API key

คุณต้องมี WhatsApp API key credentials เพื่อใช้ [WhatsApp Business Cloud](/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/index.md) node

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Access Token** สำหรับ API
- **Business Account ID**

วิธีสร้าง access token:

1. ไปที่ [Meta for Developers Apps dashboard](https://developers.facebook.com/apps/)
2. เลือก Meta app ของคุณ
3. ทางเมนูซ้ายเลือก **WhatsApp** > **API Setup**
4. เลือก **Generate access token** และยืนยันสิทธิ์ที่ต้องการ
5. คัดลอก **Access token** แล้วนำไปใส่ใน n8n ที่ **Access Token**
6. คัดลอก **WhatsApp Business Account ID** แล้วนำไปใส่ใน n8n ที่ **Business Account ID**

ดูรายละเอียดขั้นตอนเพิ่มเติมได้ที่ [Test Business Messaging on WhatsApp](https://developers.facebook.com/docs/whatsapp/solution-providers/become-a-tech-provider-legacy-flow#step-4--test-business-messaging-on-whatsapp)

การยืนยันและเปิดใช้งานแอปจริงจะต้องตั้งค่าเพิ่มเติม ดูรายละเอียดที่ [Get Started for Tech Providers](https://developers.facebook.com/docs/whatsapp/solution-providers/become-a-tech-provider-legacy-flow#step-5--scale-your-solution) ขั้นตอน 5 ขึ้นไป และ [App Review](https://developers.facebook.com/docs/resp-plat-initiatives/app-review)

## Using OAuth2

คุณต้องมี WhatsApp OAuth2 credentials เพื่อใช้ [WhatsApp Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md) node

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Client ID**
- **Client Secret**

วิธีรับค่าเหล่านี้:

1. ไปที่ [Meta for Developers Apps dashboard](https://developers.facebook.com/apps/)
2. เลือก Meta app ของคุณ
3. ทางเมนูซ้ายเลือก **App settings** > **Basic**
4. คัดลอก **App ID** แล้วนำไปใส่ใน n8n ที่ **Client ID**
5. คัดลอก **App Secret** แล้วนำไปใส่ใน n8n ที่ **Client Secret**

การยืนยันและเปิดใช้งานแอปจริงจะต้องตั้งค่าเพิ่มเติม ดูรายละเอียดที่ [Get Started for Tech Providers](https://developers.facebook.com/docs/whatsapp/solution-providers/become-a-tech-provider-legacy-flow#step-5--scale-your-solution) ขั้นตอน 5 ขึ้นไป และ [App Review](https://developers.facebook.com/docs/resp-plat-initiatives/app-review)
