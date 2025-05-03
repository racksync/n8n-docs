---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาทั่วไปเกี่ยวกับ Expressions
description: เอกสารเกี่ยวกับปัญหาและคำถามทั่วไปเกี่ยวกับ expressions ใน n8n พร้อมรายละเอียดและวิธีแก้ปัญหา
contentType: howto
---

# Expressions common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปบางประการที่เกี่ยวข้องกับ [expressions](/code/expressions.md) และขั้นตอนในการแก้ไขหรือแก้ไขปัญหา

## The 'JSON Output' in item 0 contains invalid JSON

ข้อผิดพลาดนี้เกิดขึ้นเมื่อคุณใช้โหมด JSON แต่ไม่ได้ให้ JSON object ที่ถูกต้อง ขึ้นอยู่กับปัญหาของ JSON object บางครั้งข้อผิดพลาดอาจแสดงเป็น `The 'JSON Output' in item 0 does not contain a valid JSON object`

ในการแก้ไขปัญหานี้ ตรวจสอบให้แน่ใจว่าโค้ดที่คุณให้มาเป็น JSON ที่ถูกต้อง:

- ตรวจสอบ JSON ด้วย [JSON validator](https://jsonlint.com/)
- ตรวจสอบว่า JSON object ของคุณไม่ได้อ้างอิงถึงข้อมูล input ที่ไม่ได้กำหนดค่า (undefined) สิ่งนี้อาจเกิดขึ้นหากข้อมูลขาเข้าไม่ได้มี fields เดียวกันเสมอไป

## Can't get data for expression

ข้อผิดพลาดนี้เกิดขึ้นเมื่อ n8n ไม่สามารถดึงข้อมูลที่อ้างอิงโดย expression ได้ บ่อยครั้ง สิ่งนี้เกิดขึ้นเมื่อ node ก่อนหน้ายังไม่ได้รัน

รูปแบบอื่นของปัญหานี้อาจปรากฏเป็น `Referenced node is unexecuted` ในกรณีนั้น ข้อความเต็มของข้อผิดพลาดนี้จะบอกคุณถึง node ที่แน่นอนที่ไม่ได้ execute ในรูปแบบนี้:

> An expression references the node '&lt;node-name&gt;', but it hasn’t been executed yet. Either change the expression, or re-wire your workflow to make sure that node executes first.
>

ในการเริ่มแก้ไขปัญหา ให้ทดสอบ workflow จนถึง node ที่ระบุชื่อไว้

สำหรับ node ที่ใช้ JavaScript หรือโค้ดที่กำหนดเองอื่นๆ คุณสามารถตรวจสอบว่า node ก่อนหน้าได้ execute แล้วหรือยัง ก่อนที่จะพยายามใช้ค่าของมัน โดยตรวจสอบสิ่งต่อไปนี้:

```javascript
$("<node-name>").isExecuted
```

ตัวอย่างเช่น JSON นี้อ้างอิงถึง parameters ของข้อมูล input ข้อผิดพลาดนี้จะแสดงขึ้นหากคุณทดสอบขั้นตอนนี้โดยไม่ได้เชื่อมต่อกับ node อื่น:

```javascript
{
  "my_field_1": {{ $input.params }}
}
```

## Invalid syntax

ข้อผิดพลาดนี้เกิดขึ้นเมื่อคุณใช้ expression ที่มีข้อผิดพลาดทางไวยากรณ์ (syntax error)

ตัวอย่างเช่น expression ใน JSON นี้มีเครื่องหมายจุดต่อท้าย ซึ่งส่งผลให้เกิดข้อผิดพลาด invalid syntax:

```jsx
{
  "my_field_1": "value",
  "my_field_2": {{ $('If').item.json. }}
}

```

ในการแก้ไขข้อผิดพลาดนี้ ให้ตรวจสอบ [expression syntax](/code/expressions/) ของคุณเพื่อให้แน่ใจว่าเป็นไปตามรูปแบบที่คาดไว้
