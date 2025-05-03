---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการใช้งาน Airtable Trigger node
description: วิธีใช้ Airtable Trigger node กับ n8n เพื่อเชื่อมต่อและเริ่ม workflow อัตโนมัติ
contentType: [integration, reference]
priority: medium
---

# Airtable Trigger node

[Airtable](https://airtable.com/){:target=_blank .external-link} เป็น hybrid ระหว่าง spreadsheet กับ database ที่ใช้งานง่ายมาก ฟีเจอร์เหมือน database แต่ใช้งานเหมือน spreadsheet เช่น field ใน table จะเหมือน cell ใน spreadsheet แต่เลือก type ได้ เช่น 'checkbox', 'phone number', 'drop-down list' หรือแนบไฟล์รูปภาพก็ได้

ในหน้านี้จะมีรายการ event ที่ Airtable Trigger node สามารถตอบสนองได้ พร้อมลิงก์ไปยัง resource อื่น ๆ

/// note | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/airtable.md)
///

## Events

* **New Airtable event**

## Related resources

n8n มี app node สำหรับ Airtable ด้วย ดูเอกสาร node ได้ [ที่นี่](/integrations/builtin/app-nodes/n8n-nodes-base.airtable/index.md)

ดู [example workflows และเนื้อหาที่เกี่ยวข้อง](https://n8n.io/integrations/airtable-trigger/) ได้ที่เว็บไซต์ n8n

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ API ได้ที่ [Airtable's documentation](https://airtable.com/developers/web/api/introduction)

## Node parameters

ใช้ parameter เหล่านี้เพื่อ config node ของคุณ

### Poll Times

Airtable node ของ n8n ใช้ polling เพื่อตรวจสอบการอัปเดตบน resource ที่ตั้งค่าไว้ **Poll Times** จะกำหนดความถี่ในการ query:

* Every Minute
* Every Hour
* Every Day
* Every Week
* Every Month
* Every X: ตรวจสอบการอัปเดตทุก ๆ X นาทีหรือชั่วโมง
* Custom: ปรับแต่ง interval polling โดยใส่ [cron expression](https://en.wikipedia.org/wiki/Cron)

กด **Add Poll Time** เพื่อเพิ่มช่วงเวลา polling ได้

### Base

ใส่ [Airtable base](https://support.airtable.com/docs/airtable-bases-overview) ที่ต้องการตรวจสอบการอัปเดต จะใส่ URL หรือ [base ID](https://support.airtable.com/docs/finding-airtable-ids#finding-base-table-and-view-ids-from-urls) ก็ได้

### Table

เลือก [Airtable table](https://support.airtable.com/docs/tables-overview) ใน base ที่ต้องการตรวจสอบการอัปเดต ใส่ URL หรือ [table ID](https://support.airtable.com/docs/finding-airtable-ids#finding-base-table-and-view-ids-from-urls) ก็ได้

### Trigger Field

เลือก field ที่สร้างหรือแก้ไขล่าสุดใน table node จะใช้ field นี้เพื่อตรวจสอบว่ามีการอัปเดตอะไรตั้งแต่ครั้งล่าสุด

### Download Attachments

เลือกว่าจะดาวน์โหลดไฟล์แนบจาก table หรือไม่ ถ้าเปิดใช้งาน จะต้องกำหนด **Download Fields** ด้วย

### Download Fields

เมื่อเปิด **Download Attachments** ให้ใส่ชื่อ field ที่ต้องการดาวน์โหลดไฟล์แนบ (case sensitive) ถ้ามีหลาย field ให้คั่นด้วย comma

### Additional Fields

กด **Add Field** เพื่อเพิ่ม parameter ต่อไปนี้:

* **Fields**: รายชื่อ field ที่ต้องการให้อยู่ใน output (คั่นด้วย comma) ถ้าไม่ใส่อะไรเลย output จะมีแค่ **Trigger Field**
* **Formula**: ใส่ [Airtable formula](https://support.airtable.com/docs/formula-field-reference) เพื่อ filter ผลลัพธ์เพิ่มเติม ใช้สำหรับ production polling เท่านั้น (manual execution ไม่สนใจ formula)
* **View ID**: ใส่ชื่อหรือ ID ของ table view ถ้ากำหนดไว้ จะคืนค่าข้อมูลเฉพาะที่อยู่ใน view นั้น
