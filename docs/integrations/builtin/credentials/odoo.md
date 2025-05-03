---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Odoo
description: เอกสารสำหรับข้อมูลยืนยันตัวตน Odoo ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Odoo ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: medium
---

# Odoo credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Odoo](/integrations/builtin/app-nodes/n8n-nodes-base.odoo.md)

## Supported authentication methods

- API key (แนะนำ)
- Password

## Related resources

อ้างอิง [Odoo's External API documentation](https://www.odoo.com/documentation/17.0/developer/reference/external_api.html){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

อ้างอิง Odoo [Getting Started tutorial](https://www.odoo.com/slides/getting-started-15){:target=_blank .external-link} หากคุณยังใหม่กับ Odoo

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชีผู้ใช้บนฐานข้อมูล [Odoo](https://www.odoo.com/){:target=_blank .external-link} และ:

- **Site URL** ของคุณ
- **Username** ของคุณ
- **API key**
- **Database name** ของคุณ

วิธีตั้งค่า credential ด้วย API key:

1. ป้อน URL เซิร์ฟเวอร์หรือไซต์ Odoo ของคุณเป็น **Site URL**
2. ป้อน **Username** ของคุณตามที่แสดงบนหน้าจอ **Change password** ใน Odoo
4. หากต้องการใช้ API key ให้ไปที่ **Your Profile > Preferences > Account Security > Developer API Keys**
    - หากคุณไม่มีตัวเลือกนี้ คุณอาจต้องอัปเกรดแผน Odoo ของคุณ อ้างอิง [Required plan type](#required-plan-type) สำหรับข้อมูลเพิ่มเติม
5. เลือก **New API Key**
6. ป้อน **Description** สำหรับ key เช่น `n8n integration`
7. เลือก **Generate Key**
8. คัดลอก key และป้อนเป็น **Password or API key** ใน credential ของ n8n
9. ป้อน **Database name** ของ Odoo หรือที่เรียกว่า instance name

อ้างอิง [Odoo API Keys](https://www.odoo.com/documentation/15.0/developer/reference/external_api.html?#api-keys){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Using password

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชีผู้ใช้บนฐานข้อมูล [Odoo](https://www.odoo.com/){:target=_blank .external-link} และ:

- **Site URL** ของคุณ
- **Username** ของคุณ
- **Password** ของคุณ
- **Database name** ของคุณ

วิธีตั้งค่า credential ด้วย password:

1. ป้อน URL เซิร์ฟเวอร์หรือไซต์ Odoo ของคุณเป็น **Site URL**
2. ป้อน **Username** ของคุณตามที่แสดงบนหน้าจอ **Change password** ใน Odoo
3. หากต้องการใช้ password ให้ป้อนรหัสผ่านผู้ใช้ของคุณในฟิลด์ **Password or API key**
4. ป้อน **Database name** ของ Odoo หรือที่เรียกว่า instance name

/// note | Password compatibility
หากคุณลองใช้ credential แบบ password แล้วใช้งานไม่ได้สำหรับฟังก์ชัน node เฉพาะ ให้ลองเปลี่ยนไปใช้ API key Odoo ต้องการ API key สำหรับโมดูลบางอย่างหรือขึ้นอยู่กับการตั้งค่าบางอย่าง
///

## Required plan type

/// note | Required plan type
การเข้าถึง external API มีให้ใช้งานเฉพาะในแผน Odoo แบบ **Custom** เท่านั้น (แผน One App Free หรือ Standard จะไม่ให้คุณเข้าถึง)

อ้างอิง [Odoo Pricing Plans](https://www.odoo.com/pricing-plan){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
///
