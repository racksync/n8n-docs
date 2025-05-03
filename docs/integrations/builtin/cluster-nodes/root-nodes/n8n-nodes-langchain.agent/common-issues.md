---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาที่พบบ่อย AI Agent node
description: รวมปัญหาและแนวทางแก้ไขสำหรับ AI Agent node ใน n8n
contentType: [integration, reference]
priority: critical
---

# AI Agent node common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปบางประการเกี่ยวกับ [AI Agent node](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) และขั้นตอนในการแก้ไขหรือแก้ไขปัญหา

## Internal error: 400 Invalid value for 'content'

ข้อความแสดงข้อผิดพลาดแบบเต็มอาจมีลักษณะดังนี้:

```
Internal error
Error: 400 Invalid value for 'content': expected a string, got null.
<stack-trace>
```

ข้อผิดพลาดนี้อาจเกิดขึ้นหาก input **Prompt** มีค่า null

คุณอาจเห็นสิ่งนี้ในหนึ่งในสองสถานการณ์:

1. เมื่อคุณตั้งค่า **Prompt** เป็น **Define below** และมี expression ใน **Text** ของคุณที่ไม่ได้สร้างค่า
    * ในการแก้ไข ตรวจสอบให้แน่ใจว่า expressions ของคุณอ้างอิงถึง fields ที่ถูกต้องและแก้ไขเป็น input ที่ถูกต้องแทนที่จะเป็น null
2. เมื่อคุณตั้งค่า **Prompt** เป็น **Connected Chat Trigger Node** และข้อมูลขาเข้ามีค่า null
    * ในการแก้ไข ให้ลบค่า null ใดๆ ออกจาก field `chatInput` ของ input node

## Error in sub-node Simple Memory

ข้อผิดพลาดนี้จะแสดงขึ้นเมื่อ n8n พบปัญหากับ [Simple Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/index.md) sub-node

ส่วนใหญ่มักเกิดขึ้นเมื่อ workflow ของคุณหรือ workflow template ที่คุณคัดลอกมาใช้ Simple memory node เวอร์ชันเก่า (เดิมชื่อ "Window Buffer Memory")

ลองลบ Simple Memory node ออกจาก workflow ของคุณแล้วเพิ่มเข้าไปใหม่ ซึ่งจะรับประกันว่าคุณกำลังใช้ node เวอร์ชันล่าสุด

## A Chat Model sub-node must be connected error

ข้อผิดพลาดนี้จะแสดงขึ้นเมื่อ n8n พยายาม execute node โดยไม่ได้เชื่อมต่อ Chat Model

ในการแก้ไขปัญหานี้ ให้คลิกปุ่ม + Chat Model ที่ด้านล่างของหน้าจอเมื่อ node เปิดอยู่ หรือคลิกตัวเชื่อมต่อ Chat Model + เมื่อ node ปิดอยู่ จากนั้น n8n จะเปิดรายการ Chat Models ที่เป็นไปได้ให้เลือก

## No prompt specified error

ข้อผิดพลาดนี้เกิดขึ้นเมื่อ agent คาดว่าจะได้รับ prompt จาก node ก่อนหน้าโดยอัตโนมัติ โดยทั่วไป สิ่งนี้จะเกิดขึ้นเมื่อคุณใช้ [Chat Trigger Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/)

ในการแก้ไขปัญหานี้ ให้ค้นหา parameter **Prompt** ของ AI Agent node และเปลี่ยนจาก **Connected Chat Trigger Node** เป็น **Define below** ซึ่งช่วยให้คุณสร้าง prompt ของคุณด้วยตนเองโดยอ้างอิงข้อมูล output จาก nodes อื่นๆ หรือโดยการเพิ่มข้อความคงที่
