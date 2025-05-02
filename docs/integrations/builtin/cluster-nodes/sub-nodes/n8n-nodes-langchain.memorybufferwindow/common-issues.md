---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Simple Memory node common issues
description: Documentation for common issues and questions in the Simple Memory node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: high
---

# Simple Memory node common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปบางประการเกี่ยวกับ [Simple Memory node](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/index.md) และขั้นตอนในการแก้ไขหรือ troubleshoot

## Single memory instance

หากคุณเพิ่ม Simple Memory node มากกว่าหนึ่ง node ใน workflow ของคุณ โดยค่าเริ่มต้นแล้ว ทุก node จะเข้าถึง memory instance เดียวกัน โปรดระมัดระวังเมื่อดำเนินการ destructive actions ที่เขียนทับเนื้อหา memory ที่มีอยู่ เช่น operation override all messages ใน [Chat Memory Manager](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager.md) node หากคุณต้องการ memory instance มากกว่าหนึ่ง instance ใน workflow ของคุณ ให้ตั้งค่า session IDs ที่แตกต่างกันใน memory nodes ที่ต่างกัน

## Managing the Session ID

ในกรณีส่วนใหญ่ `sessionId` จะถูกดึงมาจาก trigger **On Chat Message** โดยอัตโนมัติ แต่คุณอาจพบข้อผิดพลาดพร้อมข้อความ `No sessionId`

หากคุณพบข้อผิดพลาดนี้ ให้ตรวจสอบ output ของ Chat trigger ของคุณก่อนเพื่อให้แน่ใจว่ามี `sessionId` รวมอยู่ด้วย

หากคุณไม่ได้ใช้ trigger **On Chat Message** คุณจะต้องจัดการ sessions ด้วยตนเอง

เพื่อวัตถุประสงค์ในการทดสอบ คุณสามารถใช้ static key เช่น `my_test_session` หากคุณใช้วิธีนี้ อย่าลืมตั้งค่าการจัดการ session ที่เหมาะสมก่อนที่จะ activate workflow เพื่อหลีกเลี่ยงปัญหาที่อาจเกิดขึ้นในสภาพแวดล้อมจริง (live environment)
