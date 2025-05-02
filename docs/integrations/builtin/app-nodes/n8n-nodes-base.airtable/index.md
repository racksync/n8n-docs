---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Airtable node documentation
description: Learn how to use the Airtable node in n8n. Follow technical documentation to integrate Airtable node into your workflows.
contentType: [integration, reference]
priority: high
---

# Airtable node

ใช้ Airtable node เพื่อทำงานอัตโนมัติใน Airtable และเชื่อมต่อ Airtable กับแอปพลิเคชันอื่นๆ n8n มีฟีเจอร์ของ Airtable ให้ใช้งานหลากหลาย เช่น การสร้าง อ่าน แสดงรายการ อัปเดต และลบตาราง

ในหน้านี้คุณจะเจอรายการ operations ที่ Airtable node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
ดู [Airtable credentials](/integrations/builtin/credentials/airtable.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Append the data to a table
* Delete data from a table
* List data from a table
* Read data from a table
* Update data in a table

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'airtable') ]]

## Related resources

n8n มี trigger node สำหรับ Airtable คุณสามารถดูเอกสาร trigger node ได้ [ที่นี่](/integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger.md)

ดู [Airtable's documentation](https://airtable.com/developers/web/api/introduction){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"


## Node reference

### Get the Record ID

ถ้าคุณต้องการดึงข้อมูลของ record ใด record หนึ่ง คุณต้องใช้ Record ID ซึ่งมี 2 วิธีในการหา Record ID

### Create a Record ID column in Airtable

ถ้าต้องการสร้างคอลัมน์ `Record ID` ในตารางของคุณ ให้ดู [บทความนี้](https://support.airtable.com/docs/finding-airtable-ids){:target=_blank .external-link} แล้วนำ Record ID นี้ไปใช้กับ Airtable node ได้เลย

### Use the List operation

ถ้าต้องการหา Record ID ของ record คุณ สามารถใช้ **List** operation ของ Airtable node ได้เลย โดย operation นี้จะคืนค่า Record ID พร้อม fields ต่างๆ จากนั้นนำ Record ID ไปใช้กับ Airtable node ได้

### Filter records when using the List operation

ถ้าต้องการกรอง records จาก Airtable base ของคุณ ให้ใช้ตัวเลือก **Filter By Formula** เช่น ถ้าอยากได้ผู้ใช้ทั้งหมดที่อยู่ใน organization `n8n` ให้ทำตามขั้นตอนนี้:

1. เลือก 'List' จาก **Operation** dropdown
2. กรอก base ID และ table name ใน **Base ID** และ **Table**
3. คลิก **Add Option** แล้วเลือก 'Filter By Formula'
4. ใส่สูตรนี้ใน **Filter By Formula**: `{Organization}='n8n'`

ถ้าอยากได้ผู้ใช้ที่ไม่ได้อยู่ใน organization `n8n` ให้ใช้สูตรนี้: `NOT({Organization}='n8n')`

ดู [documentation](https://support.airtable.com/hc/en-us/articles/203255215-Formula-Field-Reference){:target=_balnk .external-link} ของ Airtable เพื่อเรียนรู้เพิ่มเติมเกี่ยวกับสูตร

## Common issues

สำหรับข้อผิดพลาดหรือปัญหาทั่วไปและวิธีแก้ไข ดูที่ [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues.md)
