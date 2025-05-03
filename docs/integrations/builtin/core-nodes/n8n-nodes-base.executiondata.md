---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Execution Data
description: เอกสารสำหรับ Execution Data node ใน n8n แพลตฟอร์ม workflow automation พร้อมคำแนะนำการใช้งานและตัวอย่าง
contentType: [integration, reference]
priority: high
---

# Execution Data

ใช้ node นี้เพื่อบันทึก metadata ของ workflow execution สามารถค้นหาข้อมูลนี้ได้ใน **Executions** list

สามารถดึง custom execution data ระหว่าง workflow execution ได้โดยใช้ Code node ดูรายละเอียดที่ [Custom executions data](/workflows/executions/custom-executions-data.md)

/// info | Feature availability
ใช้งานได้บน Pro และ Enterprise plans เท่านั้น
///

## Operations

* Save Execution Data for Search

## Data to Save

เพิ่ม **Saved Field** สำหรับแต่ละ key/value ของ metadata ที่ต้องการบันทึก

## Limitations

Execution Data node มีข้อจำกัดดังนี้:

* `key`: จำกัด 50 ตัวอักษร
* `value`: จำกัด 512 ตัวอักษร

ถ้า `key` หรือ `value` เกินขนาด n8n จะตัดให้เหลือขนาดสูงสุดและบันทึก log

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'execution-data') ]]
