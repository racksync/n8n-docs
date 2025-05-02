---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
title: Agents vs chains
description: A workflow example that demonstrates key differences between agents and chains.
---

# Demonstration of key differences between agents and chains

workflow ตัวอย่างนี้ให้คุณเลือกได้ว่าจะส่งคำถามไปที่ [agent](/glossary.md#ai-agent) หรือ [chain](/glossary.md#ai-chain) เพื่อโชว์ความแตกต่างที่สำคัญระหว่าง agent กับ chain

[[ workflowDemo("file:///advanced-ai/examples/agents_vs_chains.json") ]]

## Key features

workflow นี้ใช้:

* [Chat Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md): เริ่ม workflow และตอบโต้กับผู้ใช้ผ่าน chat interface ที่ปรับแต่งได้
* [Switch node](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md): ส่งคำถามไปที่ agent หรือ chain ตามที่ผู้ใช้ระบุในข้อความ ถ้าพิมพ์ว่า "agent" จะส่งไป agent ถ้าพิมพ์ว่า "chain" จะส่งไป chain
* [Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md): node นี้จะโต้ตอบกับ component อื่นใน workflow และตัดสินใจเลือก [tools](/glossary.md#ai-tool) ที่จะใช้
* [Basic LLM Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md): node นี้ใช้คุยกับ LLM โดยตรง แต่ไม่รองรับ [memory](/glossary.md#ai-memory) หรือ tools

## Using the example

--8<-- "_snippets/examples-color-key.md"
