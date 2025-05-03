---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ QuestDB node
description: เรียนรู้วิธีใช้ QuestDB node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ QuestDB node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# QuestDB node

ใช้ QuestDB node ในการอัตโนมัติงานใน QuestDB และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n รองรับการรัน SQL query และการแทรก rows ลงในฐานข้อมูลของ QuestDB.

ในหน้านี้ คุณจะพบรายการ operations ที่ QuestDB node รองรับ พร้อมกับลิงก์ไปยัง resources เพิ่มเติม.

/// note | Credentials
ดู [QuestDB credentials](/integrations/builtin/credentials/questdb.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Executes a SQL query.
* Insert rows in database.

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'questdb') ]]

## Node reference

### Specify a column's data type

ในการระบุ data type ของ column ให้นำชื่อ column ต่อด้วย `:type` โดยที่ `type` คือชนิดข้อมูลที่ต้องการสำหรับ column นั้น. ตัวอย่างเช่น หากคุณต้องการระบุชนิด `int` สำหรับ column **id** และชนิด `text` สำหรับ column **name** คุณสามารถใช้ snippet ต่อไปนี้ในช่อง **Columns**: `id:int,name:text`.





