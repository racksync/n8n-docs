---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Adalo
description: เอกสารข้อมูลรับรอง Adalo ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Adalo ใน n8n
contentType: [integration, reference]
priority: medium
---

# Adalo credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Adalo](/integrations/builtin/app-nodes/n8n-nodes-base.adalo.md)

/// note | API access
คุณต้องมีแผน Team หรือ Business เพื่อใช้ Adalo APIs
///

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับบริการได้ที่ [Adalo's API collections documentation](https://help.adalo.com/integrations/the-adalo-api/collections){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [Adalo](https://www.adalo.com/){:target=_blank .external-link} และ:

- **API Key**
- **App ID**

หากต้องการรับสิ่งเหล่านี้ ให้สร้าง Adalo app:

1. จาก dropdown ของ app ในแถบนำทางด้านบน เลือก **CREATE NEW APP**
1. เลือกประเภท App Layout ที่เหมาะสมกับคุณแล้วเลือก **Next**
    - หากคุณเพิ่งเริ่มใช้ผลิตภัณฑ์ Adalo แนะนำให้ใช้ **Mobile Only**
1. เลือก template เพื่อเริ่มต้น หรือเลือก **Blank** แล้วเลือก **Next**
1. ป้อน **App Name** เช่น `n8n integration`
1. หากมี ให้เลือก **Team** สำหรับ app
1. เลือกสี branding
1. เลือก **Create** ตัวแก้ไข app จะเปิดขึ้น
1. ในเมนูด้านซ้าย เลือก **Settings** (ไอคอนรูปเฟือง)
1. เลือก **App Access**
1. ในส่วน **API Key** เลือก **Generate Key**
    - หากคุณไม่มีระดับแผนที่ถูกต้อง คุณจะเห็นข้อความแจ้งให้อัปเกรดแทน
1. คัดลอก key และป้อนเป็น **API Key** ใน n8n credential ของคุณ
1. URL จะรวม **App ID** ไว้หลัง `https://app.adalo.com/apps/` ตัวอย่างเช่น หาก URL สำหรับ app ของคุณคือ `https://app.adalo.com/apps/b78bdfcf-48dc-4550-a474-dd52c19fc371/app-settings` `b78bdfcf-48dc-4550-a474-dd52c19fc371` คือ App ID คัดลอกค่านี้และป้อนลงใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมเกี่ยวกับการสร้าง apps ใน Adalo ได้ที่ [Creating an app](https://help.adalo.com/design/designing-your-app/creating-an-app){:target=_blank .external-link} ดูข้อมูลเพิ่มเติมเกี่ยวกับการสร้าง API keys ได้ที่ [The Adalo API](https://help.adalo.com/integrations/the-adalo-api){:target=_blank .external-link}
