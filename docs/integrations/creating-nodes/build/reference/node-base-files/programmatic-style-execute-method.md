---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Programmatic-style execute() method
description: A reference document for the programmatic-style execute() method of the node base file.
contentType: reference
---

# Programmatic-style execute() method

ความแตกต่างหลักระหว่าง declarative กับ programmatic style คือวิธีจัดการข้อมูลที่เข้ามาและการสร้าง API request แบบ programmatic จะต้องมี method `execute()` ซึ่งจะอ่านข้อมูลและ parameters ที่เข้ามา แล้วสร้าง request ขึ้นมา ส่วน declarative จะใช้ key `routing` ใน object ของ operations แทน

method `execute()` จะสร้างและ return instance ของ `INodeExecutionData`

/// warning | Paired items
คุณต้องใส่ข้อมูลการจับคู่ input และ output item ในข้อมูลที่ return ด้วย ดูรายละเอียดเพิ่มเติมที่ [Paired items](/integrations/creating-nodes/build/reference/paired-items.md)
///