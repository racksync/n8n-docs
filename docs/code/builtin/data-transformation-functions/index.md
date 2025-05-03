---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ฟังก์ชันแปลงข้อมูล
description: แนะนำฟังก์ชันแปลงข้อมูลสำหรับ expressions
contentType: overview
---

# Data transformation functions

Data transformation functions คือ helper functions ที่ช่วยให้การแปลงข้อมูลง่ายขึ้นใน [expressions](/glossary.md#expression-n8n)

/// note | JavaScript in expressions
คุณสามารถใช้ JavaScript ใดๆ ใน expressions ได้ โปรดดู [Expressions](/code/expressions.md) สำหรับข้อมูลเพิ่มเติม
///
สำหรับรายการฟังก์ชันที่มีอยู่ โปรดดูหน้าสำหรับประเภทข้อมูลของคุณ:

* [Arrays](/code/builtin/data-transformation-functions/arrays.md)
* [Dates](/code/builtin/data-transformation-functions/dates.md)
* [Numbers](/code/builtin/data-transformation-functions/numbers.md)
* [Objects](/code/builtin/data-transformation-functions/objects.md)
* [Strings](/code/builtin/data-transformation-functions/strings.md)

## Usage

Data transformation functions มีให้ใช้งานใน expressions editor

Syntax คือ:

```js
{{ dataItem.function() }}
```

ตัวอย่างเช่น เพื่อตรวจสอบว่า string เป็น email หรือไม่:

```js
{{ "example@example.com".isEmail() }}

// คืนค่า true
```
