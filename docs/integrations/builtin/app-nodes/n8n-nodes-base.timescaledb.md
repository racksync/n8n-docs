---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: TimescaleDB node documentation
description: Learn how to use the TimescaleDB node in n8n. Follow technical documentation to integrate TimescaleDB node into your workflows.
contentType: [integration, reference]
---

# TimescaleDB node

ใช้ TimescaleDB node เพื่อช่วยงานอัตโนมัติใน TimescaleDB และเชื่อมต่อ TimescaleDB กับแอปพลิเคชันอื่น ๆ โดย n8n มีการสนับสนุนฟีเจอร์ต่าง ๆ เช่น การรัน SQL query และการเพิ่ม/อัปเดตแถวในฐานข้อมูล

/// note | Credentials
ดู [TimescaleDB credentials](/integrations/builtin/credentials/timescaledb.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Execute an SQL query
* Insert rows in database
* Update rows in database

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'timescaledb') ]]

## Specify a column's data type

ในการระบุประเภทข้อมูลของ column ให้ต่อท้ายชื่อ column ด้วย `:type` โดยที่ `type` คือประเภทข้อมูลที่คุณต้องการ สำหรับตัวอย่าง หากต้องการให้ column **id** เป็นประเภท `int` และ column **name** เป็นประเภท `text` คุณสามารถใช้ snippet ต่อไปนี้ในฟิลด์ **Columns**: `id:int,name:text`

