---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ทริกเกอร์ข้อผิดพลาด (Error Trigger)
description: คู่มือ Error Trigger node สำหรับจัดการ error workflow ใน n8n
contentType: [integration, reference]
priority: medium
---

# Error Trigger node

ใช้ Error Trigger node เพื่อสร้าง error workflow เมื่อ workflow อื่นที่เชื่อมโยงกันเกิด error node นี้จะรับข้อมูล workflow ที่ error และ error details แล้วรัน error workflow

## Usage

--8<-- "_snippets/flow-logic/create-set-error-workflow.md"

หมายเหตุ:

* ถ้า workflow ใช้ Error Trigger node ไม่ต้อง activate workflow
* ถ้า workflow มี Error Trigger node โดย default workflow จะใช้ตัวเองเป็น error workflow
* ไม่สามารถทดสอบ error workflow ได้ตอนรัน workflow แบบ manual Error Trigger จะทำงานเฉพาะตอน workflow อัตโนมัติ error

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'error-trigger') ]]

## Related resources

สามารถใช้ [Stop And Error](/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md) node เพื่อส่ง custom message ไปยัง Error Trigger ได้

อ่านเพิ่มเติมเกี่ยวกับ [Error workflows](/flow-logic/error-handling.md) ใน workflow ของ n8n

## Error data

--8<-- "_snippets/integrations/builtin/core-nodes/error-trigger/error-data.md"

