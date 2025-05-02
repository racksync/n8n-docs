---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Data transformation functions for dates
description: A reference document listing built-in convenience functions to support data transformation in expressions for dates.
contentType: reference
---

# Dates

เอกสารอ้างอิงที่แสดงรายการ convenience functions ที่สร้างไว้ให้เพื่อรองรับการแปลงข้อมูลใน [expressions](/glossary.md#expression-n8n) สำหรับ dates

/// note | JavaScript in expressions
คุณสามารถใช้ JavaScript ใดๆ ใน expressions ได้ โปรดดู [Expressions](/code/expressions.md) สำหรับข้อมูลเพิ่มเติม
///
[[% import "_macros/data-functions.html" as dataFunctions %]]

[[% for func in df_date %]]
[[ dataFunctions.dataFunctions("date", func.funcName, func.returns, func.description, func.args, func.examples ) ]]
[[% endfor %]]
