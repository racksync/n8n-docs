---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Conversational AI Agent node documentation
description: Learn how to use the Conversational Agent of the AI Agent node in n8n. Follow technical documentation to integrate the Conversational Agent into your workflows.
contentType: [integration, reference]
priority: critical
---

# Conversational AI Agent node

Conversational Agent มีการสนทนาที่เหมือนมนุษย์ มันสามารถรักษาบริบท เข้าใจเจตนาของผู้ใช้ และให้คำตอบที่เกี่ยวข้อง Agent นี้มักใช้สำหรับการสร้าง chatbots, virtual assistants และระบบสนับสนุนลูกค้า

Conversational Agent อธิบาย [tools](/glossary.md#ai-tool) ใน system prompt และแยกวิเคราะห์ JSON responses สำหรับการเรียก tool หาก AI model ที่คุณต้องการไม่รองรับการเรียก tool หรือคุณกำลังจัดการกับการโต้ตอบที่ง่ายกว่า agent นี้เป็นตัวเลือกทั่วไปที่ดี มันมีความยืดหยุ่นมากกว่า แต่อาจมีความแม่นยำน้อยกว่า [Tools Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md)

อ้างอิง [AI Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ AI Agent node เอง

--8<-- "_snippets/integrations/builtin/cluster-nodes/use-with-chat-trigger.md"

## Node parameters

กำหนดค่า Conversational Agent โดยใช้ parameters ต่อไปนี้

### Prompt

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md"

### Require Specific Output Format

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/output-format.md"

## Node options

ปรับแต่งพฤติกรรมของ Conversational Agent node โดยใช้ options เหล่านี้:

### Human Message

บอก agent เกี่ยวกับ tools ที่สามารถใช้และเพิ่มบริบทให้กับ input ของผู้ใช้

คุณต้องรวม expressions และ variable เหล่านี้:

* `{tools}`: LangChain expression ที่ให้สตริงของ tools ที่คุณเชื่อมต่อกับ Agent ให้บริบทหรือคำอธิบายเกี่ยวกับว่าใครควรใช้ tools และควรใช้อย่างไร
* `{format_instructions}`: LangChain expression ที่ให้ schema หรือ format จาก output parser node ที่คุณเชื่อมต่อ เนื่องจาก instructions เองเป็นบริบท คุณไม่จำเป็นต้องให้บริบทสำหรับ expression นี้
* `{{input}}`: LangChain variable ที่มี prompt ของผู้ใช้ variable นี้จะเติมค่าด้วยค่าของ parameter **Prompt** ให้บริบทว่านี่คือ input ของผู้ใช้

นี่คือตัวอย่างวิธีที่คุณอาจใช้สตริงเหล่านี้:

Example:

```
TOOLS
------
Assistant can ask the user to use tools to look up information that may be helpful in answering the user's original question. The tools the human can use are:

{tools}

{format_instructions}

USER'S INPUT
--------------------
Here is the user's input (remember to respond with a markdown code snippet of a JSON blob with a single action, and NOTHING else):

{{input}}
```

### System Message

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/system-message.md"

### Max Iterations

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/max-iterations.md"

### Return Intermediate Steps

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/return-intermediate-steps.md"

## Templates and examples

อ้างอิงส่วน [Templates and examples](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md#templates-and-examples) ของ AI Agent node หลัก

## Common issues

สำหรับคำถามหรือปัญหาทั่วไปและแนวทางแก้ไขที่แนะนำ โปรดดูที่ [Common issues](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md)

--8<-- "_glossary/ai-glossary.md"
