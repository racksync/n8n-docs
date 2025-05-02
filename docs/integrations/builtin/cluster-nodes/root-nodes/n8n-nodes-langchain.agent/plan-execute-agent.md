---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Plan and Execute AI Agent node documentation
description: Learn how to use the Plan and Execute Agent of the AI Agent node in n8n. Follow technical documentation to integrate the Plan and Execute Agent into your workflows.
contentType: [integration, reference]
priority: critical
---

# Plan and Execute Agent node

Plan and Execute Agent คล้ายกับ [ReAct agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent.md) แต่เน้นที่การวางแผน มันจะสร้างแผนระดับสูงเพื่อแก้ปัญหางานที่กำหนดก่อน แล้วจึงดำเนินการตามแผนทีละขั้นตอน Agent นี้มีประโยชน์ที่สุดสำหรับงานที่ต้องการแนวทางที่มีโครงสร้างและการวางแผนอย่างรอบคอบ

อ้างอิง [AI Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ AI Agent node เอง

## Node parameters

กำหนดค่า Plan and Execute Agent โดยใช้ parameters ต่อไปนี้

### Prompt

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md"

### Require Specific Output Format

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/output-format.md"

## Node options

ปรับแต่งพฤติกรรมของ Plan and Execute Agent node โดยใช้ options เหล่านี้:

### Human Message Template

ป้อนข้อความที่ n8n จะส่งไปยัง agent ในระหว่างการดำเนินการแต่ละขั้นตอน

LangChain expressions ที่มีอยู่:

* `{previous_steps}`: มีข้อมูลเกี่ยวกับขั้นตอนก่อนหน้าที่ agent ได้ทำเสร็จแล้ว
* `{current_step}`: มีข้อมูลเกี่ยวกับขั้นตอนปัจจุบัน
* `{agent_scratchpad}`: ข้อมูลที่ต้องจำสำหรับการวนซ้ำครั้งต่อไป

## Templates and examples

อ้างอิงส่วน [Templates and examples](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md#templates-and-examples) ของ AI Agent node หลัก

## Common issues

สำหรับคำถามหรือปัญหาทั่วไปและแนวทางแก้ไขที่แนะนำ โปรดดูที่ [Common issues](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md)

--8<-- "_glossary/ai-glossary.md"
