---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ฟังก์ชันแปลงข้อมูลสำหรับ booleans
description: รายการ convenience functions สำหรับแปลงข้อมูล booleans ใน expressions
contentType: reference
---

# Booleans

เอกสารอ้างอิงที่แสดงรายการ convenience functions ที่สร้างไว้ให้เพื่อรองรับการแปลงข้อมูลใน [expressions](/glossary.md#expression-n8n) สำหรับ booleans

/// note | JavaScript in expressions
คุณสามารถใช้ JavaScript ใดๆ ใน expressions ได้ โปรดดู [Expressions](/code/expressions.md) สำหรับข้อมูลเพิ่มเติม
///
[[% import "_macros/data-functions.html" as dataFunctions %]]

[[% for func in df_boolean %]]
[[ dataFunctions.dataFunctions("boolean", func.funcName, func.returns, func.description, func.args, func.examples ) ]]
[[% endfor %]]
