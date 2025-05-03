---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
title: เรียก API เพื่อดึงข้อมูล
description: ใช้ n8n workflow tool โหลดข้อมูลจาก API โดยใช้ HTTP Request node เข้า AI workflow ของคุณ
---

# Call an API to fetch data

ใช้ n8n เพื่อดึงข้อมูลจาก [API](/glossary.md#api) มาใช้กับ AI workflow ตัวอย่างนี้ใช้ [Chat Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md) สำหรับ chat interface และ [Call n8n Workflow Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md) เพื่อเรียก workflow ที่ไปเรียก API โดย workflow ที่สองจะใช้ AI ช่วยปรับ request ให้เหมาะกับคำถามของผู้ใช้

[[ workflowDemo("file:///advanced-ai/examples/let_your_ai_call_an_api.json") ]]

## Key features

workflow นี้ใช้:

* [Chat Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md): เริ่ม workflow และตอบโต้กับผู้ใช้ผ่าน chat interface ที่ปรับแต่งได้
* [Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md): ตัวหลักของ AI workflow ที่โต้ตอบกับ component อื่นและตัดสินใจเลือก tool
* [Call n8n Workflow Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md): เสียบ workflow ของ n8n เป็น custom tool ใน AI tool คือ interface ที่ AI ใช้โต้ตอบกับโลก (ในที่นี้คือข้อมูลจาก workflow) ทำให้ AI เข้าถึงข้อมูลนอก dataset เดิมได้
* [Basic LLM Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md) ที่มี [Auto-fixing Output Parser](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing.md) และ [Structured Output Parser](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/index.md) เพื่ออ่านคำถามผู้ใช้และตั้งค่าพารามิเตอร์ API ตาม input

## Using the example

--8<-- "_snippets/examples-color-key.md"
