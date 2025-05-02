---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Data transformation functions for objects
description: A reference document listing built-in convenience functions to support data transformation in expressions for objects.
contentType: reference
---

# Objects

เอกสารอ้างอิงที่แสดงรายการ convenience functions ที่สร้างไว้ให้เพื่อรองรับการแปลงข้อมูลใน expressions สำหรับ objects

/// note | JavaScript in expressions
คุณสามารถใช้ JavaScript ใดๆ ใน expressions ได้ โปรดดู [Expressions](/code/expressions.md) สำหรับข้อมูลเพิ่มเติม
///
[[% import "_macros/data-functions.html" as dataFunctions %]]

[[% for func in df_object %]]
[[ dataFunctions.dataFunctions("object", func.funcName, func.returns, func.description, func.args, func.examples ) ]]
[[% endfor %]]
