---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Grist node
description: เรียนรู้วิธีใช้ Grist node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Grist node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Grist node

ใช้ Grist node เพื่อทำงานอัตโนมัติใน Grist และเชื่อมต่อ Grist กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Grist หลายอย่าง เช่น การสร้าง อัปเดต ลบ และอ่าน rows ใน table

ในหน้านี้จะมีรายการ operations ที่ Grist node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Grist credentials](/integrations/builtin/credentials/grist.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Create rows in a table
* Delete rows from a table
* Read rows from a table
* Update rows in a table

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'grist') ]]

## Get the Row ID

ถ้าต้องการอัปเดตหรือลบ record ใดๆ ต้องใช้ Row ID โดยมี 2 วิธีในการหา Row ID:

**สร้างคอลัมน์ Row ID ใน Grist**

สร้างคอลัมน์ใหม่ในตาราง Grist ของคุณ แล้วใส่สูตร `$id`

**ใช้ Operation Get All**

Operation **Get All** จะคืนค่า Row ID ของแต่ละ record พร้อม fields

สามารถดึง Row ID ได้ด้วย expression `{{$node["GristNodeName"].json["id"]}}`

## Filter records when using the Get All operation

- เลือก **Add Option** แล้วเลือก **Filter** จาก dropdown
- สามารถเพิ่ม filter ได้หลายคอลัมน์ ผลลัพธ์จะรวมเฉพาะ records ที่ตรงกับทุกคอลัมน์
- สำหรับแต่ละคอลัมน์ สามารถใส่ค่าหลายค่าโดยคั่นด้วย comma ผลลัพธ์จะรวม records ที่ตรงกับค่าใดค่าหนึ่งในคอลัมน์นั้น

