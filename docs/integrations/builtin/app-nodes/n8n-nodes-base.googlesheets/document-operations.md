---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การดำเนินการ Document ใน Google Sheets
description: เอกสารการดำเนินการ Document ใน Google Sheets node ของ n8n พร้อมรายละเอียด การตั้งค่า และลิงก์ตัวอย่าง
contentType: [integration, reference]
priority: critical
---

# Google Sheets Document operations

ใช้ operation นี้เพื่อสร้างหรือลบ Google spreadsheet จาก Google Sheets อ้างอิงถึง [Google Sheets](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ Google Sheets node

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Create a spreadsheet

ใช้ operation นี้เพื่อสร้าง spreadsheet ใหม่

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Document**
- **Operation**: เลือก **Create**
- **Title**: ป้อนชื่อของ spreadsheet ใหม่ที่คุณต้องการสร้าง
- **Sheets**: เพิ่ม **Title(s)** ของ sheet ที่คุณต้องการสร้างภายใน spreadsheet
<!-- vale off -->

### Options

- **Locale**: ป้อน locale ของ spreadsheet ซึ่งมีผลต่อรายละเอียดการจัดรูปแบบ เช่น ฟังก์ชัน วันที่ และสกุลเงิน ใช้รูปแบบใดรูปแบบหนึ่งต่อไปนี้:
    - `en` (639-1)
    - `fil` (639-2 หากไม่มีรูปแบบ 639-1)
    - `en_US` (การรวมกันของภาษา ISO และประเทศ)
    - อ้างอิงถึง [List of ISO 639 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes){:target=_blank .external link} และ [List of ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes){:target=_blank .external link} สำหรับรหัสภาษาและประเทศ โปรดทราบว่า Google ไม่รองรับทุก locales/ภาษา
- **Recalculation Interval**: ป้อนช่วงเวลาการคำนวณซ้ำที่ต้องการสำหรับฟังก์ชันของ spreadsheet ซึ่งมีผลต่อความถี่ในการอัปเดต `NOW`, `TODAY`, `RAND`, และ `RANDBETWEEN` เลือก **On Change** สำหรับการคำนวณซ้ำทุกครั้งที่มีการเปลี่ยนแปลงใน spreadsheet, **Minute** สำหรับการคำนวณซ้ำทุกนาที, หรือ **Hour** สำหรับการคำนวณซ้ำทุกชั่วโมง อ้างอิงถึง [Set a spreadsheet’s location & calculation settings](https://support.google.com/docs/answer/58515){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับตัวเลือกเหล่านี้

อ้างอิงถึงเอกสาร API [Method: spreadsheets.create | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/create){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Delete a spreadsheet

ใช้ operation นี้เพื่อลบ spreadsheet ที่มีอยู่

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Document**
- **Operation**: เลือก **Delete**
- **Document**: เลือก spreadsheet ที่คุณต้องการลบ
    - เลือก **From list** เพื่อเลือกชื่อจากรายการดรอปดาวน์, **By URL** เพื่อป้อน URL ของ spreadsheet, หรือ **By ID** เพื่อป้อน `spreadsheetId`
    - คุณสามารถหา `spreadsheetId` ได้ใน URL ของ Google Sheets: `https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`

อ้างอิงถึงเอกสาร API [Method: files.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/delete){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม