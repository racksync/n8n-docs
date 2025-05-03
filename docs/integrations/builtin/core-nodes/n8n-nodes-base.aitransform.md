---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: AI Transform
description: เอกสารสำหรับ AI Transform node ใน n8n แพลตฟอร์ม workflow automation พร้อมคำแนะนำการใช้งานและตัวอย่าง
contentType: [integration, reference]
---

# AI Transform

ใช้ AI Transform node เพื่อ generate code snippet ตาม prompt ที่ใส่ AI จะเข้าใจ context ของ workflow และ data type ของ node ต่างๆ

/// info | Feature availability
ใช้งานได้เฉพาะบน [Cloud plans](/manage-cloud/overview.md) เท่านั้น
///

## Node parameters

### Instructions

ใส่ prompt ที่อยากให้ AI ช่วย generate code แล้วกด **Generate code** เพื่อให้ AI เติม **Transformation Code** ให้อัตโนมัติ เช่น บอกว่าอยาก process หรือจัดหมวดหมู่ข้อมูลยังไง ดูตัวอย่างการเขียน prompt ได้ที่ [Writing good prompts](/code/ai-code.md#writing-good-prompts)

prompt ควรเป็นภาษาอังกฤษธรรมดา และไม่เกิน 500 ตัวอักษร

### Transformation Code

code snippet ที่ node generate ให้จะเป็นแบบ read-only ถ้าอยากแก้ไข code ให้ปรับ prompt ใน **Instructions** หรือ copy ไป paste ใน [Code](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md) node

## Templates and examples

[[ templatesWidget(page.title, 'ai-transform') ]]

