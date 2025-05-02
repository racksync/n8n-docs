---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: XML
description: Documentation for the XML node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: medium
---

# XML

ใช้ XML node เพื่อแปลงข้อมูลจากและเป็น XML

/// note | Binary files
ถ้า XML ของคุณอยู่ใน binary file ให้ใช้ [Extract from File](/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md) node เพื่อแปลงเป็น text ก่อน
///

## Node parameters

- **Mode**: รูปแบบที่ต้องการแปลงข้อมูลจากและเป็น
	- **JSON to XML**: แปลงข้อมูลจาก JSON เป็น XML
    - **XML to JSON**: แปลงข้อมูลจาก XML เป็น JSON
- **Property Name**: ใส่ชื่อ property ที่เก็บข้อมูลที่ต้องการแปลง

## Node options

options เหล่านี้จะมีให้เลือกไม่ว่าจะเลือก **Mode** อะไร:

- **Attribute Key**: ใส่ prefix ที่ใช้เข้าถึง attributes ค่า default คือ `$`
- **Character Key**: ใส่ prefix ที่ใช้เข้าถึง character content ค่า default คือ `_`

options อื่นๆ จะขึ้นอยู่กับ **Mode** ที่เลือก

### JSON to XML options

options เหล่านี้จะมีให้เลือกเฉพาะถ้าเลือก **JSON to XML** เป็น **Mode**:

- **Allow Surrogate Chars**: ตั้งค่าว่าจะอนุญาตให้ใช้ตัวอักษรจาก Unicode surrogate blocks หรือไม่ (เปิด/ปิด)
- **Cdata**: ตั้งค่าว่าจะ wrap text node ใน `<![CDATA[ ... ]]>` แทนการ escape เมื่อจำเป็น (เปิด/ปิด)
    * ถ้าเปิด option นี้ จะไม่เพิ่ม `<![CDATA[ ... ]]>` ถ้าไม่จำเป็น
- **Headless**: ตั้งค่าว่าจะตัด XML header ออก (เปิด) หรือใส่ header (ปิด)
- **Root Name**: ใส่ชื่อ root element ที่ต้องการใช้

### XML to JSON options

options เหล่านี้จะมีให้เลือกเฉพาะถ้าเลือก **XML to JSON** เป็น **Mode**:

- **Explicit Array**: ตั้งค่าว่าจะใส่ child node ใน array เสมอ (เปิด) หรือสร้าง array เฉพาะถ้ามี child node มากกว่า 1 ตัว (ปิด)
- **Explicit Root**: ตั้งค่าว่าจะให้ root node อยู่ใน object ที่ได้ (เปิด) หรือไม่ (ปิด)
- **Ignore Attributes**: ตั้งค่าว่าจะ ignore attribute ทั้งหมดและสร้างเฉพาะ text node (เปิด) หรือไม่ (ปิด)
- **Merge Attributes**: ตั้งค่าว่าจะรวม attribute และ child element เป็น property ของ parent (เปิด) หรือแยก attribute ออกเป็น object (ปิด) option นี้จะถูก ignore ถ้า **Ignore Attribute** เปิดอยู่
- **Normalize**: ตั้งค่าว่าจะ trim whitespace ใน text node (เปิด) หรือไม่ (ปิด)
- **Normalize Tags**: ตั้งค่าว่าจะเปลี่ยนชื่อ tag ทั้งหมดเป็นตัวพิมพ์เล็ก (เปิด) หรือคงชื่อ tag เดิม (ปิด)
- **Trim**: ตั้งค่าว่าจะ trim whitespace ต้นและท้ายของ text node (เปิด) หรือไม่ (ปิด)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'xml') ]]
