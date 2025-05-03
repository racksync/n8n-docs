---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ ReAct AI Agent node
description: วิธีใช้งาน ReAct Agent ของ AI Agent node ใน n8n สำหรับวางแผนและดำเนินการแบบ reasoning-action
contentType: [integration, reference]
priority: critical
---

# ReAct AI Agent node

ReAct Agent node ใช้ตรรกะ [ReAct](https://react-lm.github.io/){:target=_blank .external-link} ReAct (reasoning and acting) รวบรวมพลังการให้เหตุผลของ chain-of-thought prompting และการสร้างแผนปฏิบัติการเข้าด้วยกัน

ReAct Agent ให้เหตุผลเกี่ยวกับงานที่กำหนด กำหนดการดำเนินการที่จำเป็น แล้วจึงดำเนินการตามนั้น มันทำตามวงจรของการให้เหตุผลและการดำเนินการจนกว่าจะทำงานเสร็จ ReAct agent สามารถแบ่งงานที่ซับซ้อนออกเป็นงานย่อยๆ จัดลำดับความสำคัญ และดำเนินการทีละอย่าง

อ้างอิง [AI Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ AI Agent node เอง

/// note | No memory
ReAct agent ไม่รองรับ memory sub-nodes ซึ่งหมายความว่ามันไม่สามารถจำ prompts ก่อนหน้าหรือจำลองการสนทนาที่ต่อเนื่องได้
///

## Node parameters

กำหนดค่า ReAct Agent โดยใช้ parameters ต่อไปนี้

### Prompt

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md"

### Require Specific Output Format

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/output-format.md"

## Node options

ใช้ options เพื่อสร้างข้อความที่จะส่งไปยัง agent ในตอนเริ่มต้นการสนทนา ประเภทข้อความขึ้นอยู่กับ model ที่คุณใช้:

* **Chat models**: models เหล่านี้มีแนวคิดของสามองค์ประกอบที่โต้ตอบกัน (AI, system และ human) พวกเขาสามารถรับ system messages และ human messages (prompts)
* **Instruct models**: models เหล่านี้ไม่มีแนวคิดขององค์ประกอบ AI, system และ human ที่แยกจากกัน พวกเขาได้รับข้อความเนื้อหาเดียวคือ instruct message

### Human Message Template

ใช้ option นี้เพื่อขยาย user prompt นี่เป็นวิธีที่ agent จะส่งข้อมูลจากการวนซ้ำหนึ่งไปยังอีกครั้งหนึ่ง

LangChain expressions ที่มีอยู่:

* `{input}`: มี user prompt
* `{agent_scratchpad}`: ข้อมูลที่ต้องจำสำหรับการวนซ้ำครั้งต่อไป

### Prefix Message

ป้อนข้อความเพื่อนำหน้า list ของ tools ในตอนเริ่มต้นการสนทนา คุณไม่จำเป็นต้องเพิ่ม list ของ tools LangChain จะเพิ่ม list ของ tools โดยอัตโนมัติ

### Suffix Message for Chat Model

เพิ่มข้อความเพื่อต่อท้าย list ของ tools ในตอนเริ่มต้นการสนทนาเมื่อ agent ใช้ chat model คุณไม่จำเป็นต้องเพิ่ม list ของ tools LangChain จะเพิ่ม list ของ tools โดยอัตโนมัติ

### Suffix Message for Regular Model

เพิ่มข้อความเพื่อต่อท้าย list ของ tools ในตอนเริ่มต้นการสนทนาเมื่อ agent ใช้ regular/instruct model คุณไม่จำเป็นต้องเพิ่ม list ของ tools LangChain จะเพิ่ม list ของ tools โดยอัตโนมัติ

### Return Intermediate Steps

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/return-intermediate-steps.md"

## Related resources

อ้างอิงเอกสาร [ReAct Agents](https://js.langchain.com/docs/concepts/agents/){:target=_blank .external-link} ของ LangChain สำหรับข้อมูลเพิ่มเติม

## Templates and examples

อ้างอิงส่วน [Templates and examples](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md#templates-and-examples) ของ AI Agent node หลัก

## Common issues

สำหรับคำถามหรือปัญหาทั่วไปและแนวทางแก้ไขที่แนะนำ โปรดดูที่ [Common issues](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md)

--8<-- "_glossary/ai-glossary.md"
