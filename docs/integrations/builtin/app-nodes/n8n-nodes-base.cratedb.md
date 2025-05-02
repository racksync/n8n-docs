---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: CrateDB node documentation
description: Learn how to use the CrateDB node in n8n. Follow technical documentation to integrate CrateDB node into your workflows.
contentType: [integration, reference]
---

# CrateDB node

ใช้ CrateDB node เพื่อทำงานอัตโนมัติใน CrateDB และ integrate CrateDB กับแอปพลิเคชันอื่นๆ n8n มีการรองรับในตัวสำหรับฟีเจอร์ต่างๆ ของ CrateDB รวมถึงการ execute, insert, และ update rows ใน database

ในหน้านี้ คุณจะพบรายการ operations ที่ CrateDB node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [CrateDB credentials](/integrations/builtin/credentials/cratedb.md) สำหรับคำแนะนำในการตั้งค่า authentication
///

## Operations

* Execute an SQL query
* Insert rows in database
* Update rows in database

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'cratedb') ]]

## Node reference

### Specify a column's data type

เพื่อระบุ data type ของ column ให้ต่อท้ายชื่อ column ด้วย `:type` โดยที่ `type` คือ data type ที่คุณต้องการสำหรับ column นั้น ตัวอย่างเช่น หากคุณต้องการระบุ type `int` สำหรับ column **id** และ type `text` สำหรับ column **name** คุณสามารถใช้ snippet ต่อไปนี้ใน field **Columns**: `id:int,name:text`





