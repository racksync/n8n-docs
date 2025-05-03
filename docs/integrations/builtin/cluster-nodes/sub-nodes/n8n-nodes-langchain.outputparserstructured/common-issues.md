---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาที่พบบ่อย Structured Output Parser node
description: รวมปัญหาและวิธีแก้ Structured Output Parser node ใน n8n สำหรับ workflow automation
contentType: [integration, reference]
priority: high
---

# Structured Output Parser node common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปบางประการเกี่ยวกับ [Structured Output Parser node](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/index.md) และขั้นตอนในการแก้ไขหรือแก้ไขปัญหา

## Processing parameters

Structured Output Parser node เป็น [sub-node](/glossary.md#sub-node-n8n) Sub-nodes มีพฤติกรรมแตกต่างจากโหนดอื่น ๆ เมื่อประมวลผลหลายรายการโดยใช้ expressions

โหนดส่วนใหญ่ รวมถึง [root nodes](/glossary.md#root-node-n8n) รับ input กี่รายการก็ได้ ประมวลผลรายการเหล่านี้ และส่ง output ผลลัพธ์ คุณสามารถใช้ expressions เพื่ออ้างอิงถึง input items และโหนดจะประมวลผล expression สำหรับแต่ละ item ตามลำดับ ตัวอย่างเช่น หากมี input เป็นค่าชื่อห้าค่า expression `{{ $json.name }}` จะประมวลผลเป็นแต่ละชื่อตามลำดับ

ใน sub-nodes, expression จะประมวลผลเป็น item แรกเสมอ ตัวอย่างเช่น หากมี input เป็นค่าชื่อห้าค่า expression `{{ $json.name }}` จะประมวลผลเป็นชื่อแรกเสมอ

## Adding the structured output parser node to AI nodes

คุณสามารถแนบ output parser nodes เข้ากับ [AI root nodes](/integrations/builtin/cluster-nodes/root-nodes/index.md) ที่เลือกได้

หากต้องการเพิ่ม Structured Output Parser ไปยังโหนด ให้เปิดใช้งานตัวเลือก **Require Specific Output Format** ใน AI root node ที่คุณต้องการจัดรูปแบบ เมื่อเปิดใช้งานตัวเลือกแล้ว จุดแนบ **output parser** ใหม่จะปรากฏขึ้น คลิกที่จุดแนบ **output parser** เพื่อเพิ่ม Structured Output Parser node ไปยังโหนด

## Using the structured output parser to format intermediary steps

Structured Output Parser node จัดโครงสร้าง output สุดท้ายจาก AI agents ไม่ได้มีไว้สำหรับจัดโครงสร้าง output ขั้นกลางเพื่อส่งต่อไปยัง AI tools หรือ stages อื่นๆ

หากต้องการร้องขอรูปแบบเฉพาะสำหรับ output ขั้นกลาง ให้รวมโครงสร้างการตอบกลับไว้ใน **System Message** สำหรับ **AI Agent** ข้อความสามารถรวม schema หรือตัวอย่างการตอบกลับเพื่อให้ agent ใช้เป็น template สำหรับผลลัพธ์

## Structuring output from agents

การแยกวิเคราะห์ output แบบมีโครงสร้างมักไม่น่าเชื่อถือเมื่อทำงานกับ [agents](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md)

หาก workflow ของคุณใช้ agents, n8n แนะนำให้ใช้ [LLM-chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md) แยกต่างหากเพื่อรับข้อมูลจาก agent และแยกวิเคราะห์ข้อมูลนั้น ซึ่งจะนำไปสู่ผลลัพธ์ที่ดีขึ้นและสอดคล้องกันมากกว่าการแยกวิเคราะห์โดยตรงใน agent workflow
