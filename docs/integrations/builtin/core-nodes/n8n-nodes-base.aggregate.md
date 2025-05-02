---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Aggregate
description: Documentation for the Aggregate node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: high
---

# Aggregate

ใช้ Aggregate node เพื่อรวม item หลายๆ อัน หรือบางส่วนของ item เข้าด้วยกันเป็น item เดียว

## Node parameters

เริ่มต้นใช้งาน node นี้ ให้เลือก **Aggregate** ที่ต้องการใช้:

* [**Individual Fields**](#individual-fields): รวม field ทีละอันแยกกัน
* [**All Item Data**](#all-item-data): รวมข้อมูลทั้งหมดของ item เข้าเป็น list เดียว

### Individual Fields

* **Input Field Name**: ใส่ชื่อ field ใน input data ที่ต้องการรวมเข้าด้วยกัน
* **Rename Field**: toggle นี้ใช้สำหรับตั้งชื่อ field ใหม่ใน output data ที่รวมแล้ว ถ้าเปิดไว้จะสามารถตั้งชื่อใหม่ได้ ถ้ารวมหลาย field ต้องตั้งชื่อใหม่ให้ครบทุกอัน ห้ามเว้นว่าง
	* **Output Field Name**: จะเห็น field นี้เมื่อเปิด **Rename Field** ใส่ชื่อ field สำหรับ output data ที่รวมแล้ว

ดู [Node options](#node-options) สำหรับตัวเลือกเพิ่มเติม

### All Item Data

* **Put Output in Field**: ใส่ชื่อ field ที่ต้องการให้ output data ไปอยู่ในนั้น
* **Include**: เลือกว่าจะรวม field ไหนใน output เลือกได้จาก:
	* **All fields**: output จะรวมข้อมูลจากทุก field โดยไม่มี parameter เพิ่มเติม
	* **Specified Fields**: ถ้าเลือกอันนี้ ให้ใส่ชื่อ field ที่ต้องการรวมใน output เป็น comma-separated ใน **Fields To Include** output จะรวมเฉพาะ field ที่อยู่ใน list นี้
	* **All Fields Except**: ถ้าเลือกอันนี้ ให้ใส่ชื่อ field ที่ไม่ต้องการรวมใน output เป็น comma-separated ใน **Fields To Exclude** output จะรวมทุก field ที่ไม่ได้อยู่ใน list นี้

ดู [Node options](#node-options) สำหรับตัวเลือกเพิ่มเติม

## Node options

สามารถตั้งค่า node เพิ่มเติมได้ใน **Options**:

* **Disable Dot Notation**: toggle นี้จะแสดงเมื่อเลือก Aggregate แบบ **Individual Fields** ใช้สำหรับปิดการอ้างถึง field ลูกด้วย `parent.child` ในชื่อ field (เปิดไว้คือปิดการอ้างถึง, ปิดไว้คือใช้ได้ตามปกติ)
* **Merge Lists**: toggle นี้จะแสดงเมื่อเลือก Aggregate แบบ **Individual Fields** เปิดไว้ถ้า field ที่จะรวมเป็น list และต้องการ output เป็น list เดียวแบบแบน ไม่ใช่ list ซ้อน list
* **Include Binaries**: toggle นี้จะแสดงสำหรับ Aggregate ทั้งสองแบบ เปิดไว้ถ้าต้องการรวม binary data จาก input ใน output ใหม่ด้วย
* **Keep Missing And Null Values**: toggle นี้จะแสดงเมื่อเลือก Aggregate แบบ **Individual Fields** เปิดไว้เพื่อให้มีค่า null (ว่าง) ใน output list ถ้า input มีค่า null หรือขาดค่า ถ้าปิดไว้ output จะข้ามค่า null หรือว่าง

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'aggregate') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md"
