---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาที่พบบ่อย Question and Answer Chain node
description: รวมปัญหาและแนวทางแก้ไขสำหรับ Question and Answer Chain node ใน n8n
contentType: [integration, reference]
priority: high
---

# Question and Answer Chain node common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปบางประการเกี่ยวกับ [Question and Answer Chain node](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md) และขั้นตอนในการแก้ไขหรือแก้ไขปัญหา

## No prompt specified error

ข้อผิดพลาดนี้จะแสดงขึ้นเมื่อ **Prompt** ว่างเปล่าหรือไม่ถูกต้อง

คุณอาจเห็นสิ่งนี้ในหนึ่งในสองสถานการณ์:

1.  เมื่อคุณตั้งค่า **Prompt** เป็น **Define below** และมี expression ใน **Text** ของคุณที่ไม่ได้สร้างค่า
    *   ในการแก้ไข ให้ป้อน prompt ที่ถูกต้องในช่อง **Text**
    *   ตรวจสอบให้แน่ใจว่า expression ใดๆ อ้างอิงถึงฟิลด์ที่ถูกต้อง และ resolve เป็น input ที่ถูกต้องแทนที่จะเป็น null
2.  เมื่อคุณตั้งค่า **Prompt** เป็น **Connected Chat Trigger Node** และข้อมูลขาเข้ามีค่า null
    *   ในการแก้ไข ตรวจสอบให้แน่ใจว่า input ของคุณมีฟิลด์ `chatInput` เพิ่มโหนด [Edit Fields (Set)](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) เพื่อแก้ไขชื่อฟิลด์ขาเข้าเป็น `chatInput`
    *   ลบค่า null ใดๆ ออกจากฟิลด์ `chatInput` ของโหนด input

<!-- vale from-write-good.Passive = NO -->
## A Retriever sub-node must be connected error
<!-- vale from-write-good.Passive = YES -->

ข้อผิดพลาดนี้จะแสดงขึ้นเมื่อ n8n พยายาม execute โหนดโดยไม่มี Retriever เชื่อมต่ออยู่

ในการแก้ไขปัญหานี้ ให้คลิกปุ่ม + Retriever ที่ด้านล่างของหน้าจอเมื่อโหนดเปิดอยู่ หรือคลิกตัวเชื่อมต่อ Retriever + เมื่อโหนดไม่ได้เปิดอยู่ จากนั้น n8n จะเปิดรายการ Retrievers ที่เป็นไปได้ให้เลือก

## Can't produce longer responses

หากคุณต้องการสร้างการตอบสนองที่ยาวกว่าที่ Question and Answer Chain node สร้างขึ้นโดยค่าเริ่มต้น คุณสามารถลองใช้เทคนิคต่อไปนี้อย่างน้อยหนึ่งอย่าง:

*   **Connect a more verbose model**: AI model บางตัวให้ผลลัพธ์ที่กระชับกว่าตัวอื่นๆ การเปลี่ยน model ของคุณเป็น model ที่มี context window ใหญ่ขึ้นและให้ output ที่ละเอียดมากขึ้นสามารถเพิ่มความยาวของคำตอบของคุณได้
*   **Increase the maximum number of tokens**: โหนด model หลายตัว (เช่น [OpenAI Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/index.md#maximum-number-of-tokens)) มีตัวเลือก **Maximum Number of Tokens** คุณสามารถตั้งค่านี้เพื่อเพิ่มจำนวน tokens สูงสุดที่ model สามารถใช้เพื่อสร้างการตอบสนองได้
*   **Build larger responses in stages**: สำหรับคำตอบที่มีรายละเอียดมากขึ้น คุณอาจต้องการสร้างการตอบกลับเป็นขั้นตอนโดยใช้โหนด AI ที่หลากหลาย คุณสามารถใช้ AI แบ่งคำถามเดียวออกเป็นหลาย prompts และสร้างการตอบสนองสำหรับแต่ละ prompt จากนั้นคุณสามารถเขียนคำตอบสุดท้ายโดยการรวมการตอบสนองเข้าด้วยกันอีกครั้ง แม้ว่ารายละเอียดจะแตกต่างกัน คุณสามารถหาตัวอย่างที่ดีของแนวคิดทั่วไปได้ใน [template สำหรับการเขียนโพสต์ WordPress ด้วย AI](https://n8n.io/workflows/2187-write-a-wordpress-post-with-ai-starting-from-a-few-keywords/) นี้
