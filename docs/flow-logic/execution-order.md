---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Execution order in multi-branch workflows
description: How n8n decides the node execution order in multi-branch workflows.
contentType: explanation
---

# Execution order in multi-branch workflows

ลำดับการ execute node ใน n8n ขึ้นอยู่กับ version ที่คุณใช้:

* ถ้า workflow ถูกสร้างก่อน version 1.0: n8n จะ execute node แรกของแต่ละ branch ก่อน แล้วค่อย execute node ที่สองของแต่ละ branch ต่อไปเรื่อยๆ
* ถ้า workflow ถูกสร้างใน version 1.0 ขึ้นไป: จะ execute ทีละ branch ให้จบ branch นั้นก่อน แล้วค่อยไป branch ถัดไป โดยเรียง branch จากบนลงล่างบน [canvas](/glossary.md#canvas-n8n) ถ้าสูงเท่ากัน branch ที่อยู่ซ้ายสุดจะ execute ก่อน

คุณสามารถเปลี่ยนลำดับ execution ได้ใน [workflow settings](/workflows/settings.md)

