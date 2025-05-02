---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Text Classifier node documentation
description: Learn how to use the Text Classifier node in n8n. Follow technical documentation to integrate Text Classifier node into your workflows.
contentType: [integration, reference]
---

# Text Classifier node

ใช้ Text Classifier node เพื่อจำแนก (จัดหมวดหมู่) ข้อมูลที่เข้ามา โดยใช้ categories ที่ระบุใน parameters (ดูด้านล่าง) แต่ละ item จะถูกส่งไปยัง model เพื่อกำหนด category ของมัน

ในหน้านี้ คุณจะพบ node parameters สำหรับ Text Classifier node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

## Node parameters

*   **Input Prompt** กำหนด input ที่จะจำแนก โดยปกติจะเป็น expression ที่อ้างอิงถึง field จาก input items ตัวอย่างเช่น อาจเป็น `{{ $json.chatInput }}` หาก input เป็น chat trigger โดยค่าเริ่มต้นจะอ้างอิงถึง field `text`
*   **Categories**: เพิ่ม categories ที่คุณต้องการจำแนก input ของคุณ Categories มี name และ description ใช้ description เพื่อบอก model ว่า category นั้นหมายถึงอะไร นี่เป็นสิ่งสำคัญหากความหมายไม่ชัดเจน คุณสามารถเพิ่ม categories ได้มากเท่าที่คุณต้องการ

## Node options

*   **Allow Multiple Classes To Be True**: คุณสามารถกำหนดค่า classifier ให้ออกผลลัพธ์เป็น class เดียวต่อ item เสมอ (ปิด) หรืออนุญาตให้ model เลือกหลาย classes (เปิด)
*   **When No Clear Match**: กำหนดว่าจะเกิดอะไรขึ้นหาก model ไม่พบการจับคู่ที่ดีสำหรับ item มีสองตัวเลือก:
    *   **Discard Item** (ค่าเริ่มต้น): หาก node ไม่ตรวจพบ categories ใดๆ เลย มันจะทิ้ง item นั้นไป
    *   **Output on Extra, 'Other' Branch**: สร้าง output branch แยกต่างหากชื่อ **Other** เมื่อ node ไม่ตรวจพบ categories ใดๆ มันจะส่ง output items ใน branch นี้
*   **System Prompt Template**: ใช้ตัวเลือกนี้เพื่อเปลี่ยน system prompt ที่ใช้สำหรับการจำแนก มันใช้ placeholder `{categories}` สำหรับ categories

*   **Enable Auto-Fixing**: เมื่อเปิดใช้งาน node จะแก้ไข outputs ของ model โดยอัตโนมัติเพื่อให้แน่ใจว่าตรงกับ format ที่คาดหวัง ทำได้โดยส่ง schema parsing error ไปยัง LLM และขอให้แก้ไข

## Related resources

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
