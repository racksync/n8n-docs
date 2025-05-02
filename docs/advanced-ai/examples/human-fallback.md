---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
title: Set a human fallback for AI workflows
description: Have a workflow that triggers a human answer when the AI can't help.
---

# Have a human fallback for AI workflows

workflow นี้จะพยายามตอบคำถามผู้ใช้ด้วย GPT-4 ถ้าตอบไม่ได้จะส่งข้อความไป Slack เพื่อขอให้คนช่วย และจะขอให้ผู้ใช้กรอกอีเมลด้วย

workflow นี้ใช้ [Chat Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md) สำหรับ chat interface และ [Call n8n Workflow Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md) เพื่อเรียก workflow ที่สองสำหรับเช็คอีเมลและส่งข้อความ Slack

[[ workflowDemo("file:///advanced-ai/examples/ask_a_human.json") ]]

## Key features

workflow นี้ใช้:

* [Chat Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md): เริ่ม workflow และตอบโต้กับผู้ใช้ผ่าน chat interface ที่ปรับแต่งได้
* [Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md): ตัวหลักของ AI workflow ที่โต้ตอบกับ component อื่นและตัดสินใจเลือก tool
* [Call n8n Workflow Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md): เสียบ workflow ของ n8n เป็น custom tool ใน AI tool คือ interface ที่ AI ใช้โต้ตอบกับโลก (ในที่นี้คือข้อมูลจาก workflow) ทำให้ AI เข้าถึงข้อมูลนอก dataset เดิมได้

## Using the example

--8<-- "_snippets/examples-color-key.md"
