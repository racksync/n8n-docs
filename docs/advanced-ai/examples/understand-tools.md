---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Tool ใน AI คืออะไร
description: ทำความเข้าใจ tools ในบริบท AI เรียนรู้ความพิเศษของ tools ใน n8n
contentType: explanation
---

# What's a tool in AI?

ใน AI คำว่า 'tools' มีความหมายเฉพาะ Tools ทำหน้าที่เหมือน addon ที่ช่วยให้ AI เข้าถึง context หรือ resource เพิ่มเติมได้

ลองดูคำอธิบายแบบอื่นๆ:

> Tools คือ interface ที่ agent ใช้ในการโต้ตอบกับโลก ([source](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/){:target=_blank .external-link})

<!--  -->

> เราสามารถมอง tools ว่าเหมือนกับ function ที่ AI model สามารถเรียกใช้ได้ ([source](https://www.udemy.com/course/chatgpt-and-langchain-the-complete-developers-masterclass/){:target=_blank .external-link})

## AI tools in n8n

n8n มี tool [sub-nodes](/glossary.md#sub-node-n8n) ที่เชื่อมต่อกับ [AI agent](/glossary.md#ai-agent) ได้ นอกจาก tool ยอดนิยมอย่าง [Wikipedia](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia.md) และ [SerpAPI](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md) แล้ว n8n ยังมี tool ที่ทรงพลังอีก 3 ตัว:

* [Call n8n Workflow Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md): ใช้โหลด workflow ใดๆ ของ n8n มาเป็น tool
* [Custom Code Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode.md): เขียนโค้ดให้ agent รันได้เอง
* [HTTP Request Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolhttprequest.md): เรียกข้อมูลจากเว็บไซต์หรือ API

ตัวอย่างข้างล่างนี้จะเน้น Call n8n Workflow Tool:

- [Chat with Google Sheets](/advanced-ai/examples/data-google-sheets.md)
- [Call an API to fetch data](/advanced-ai/examples/api-workflow-tool.md)
- [Set up a human fallback](/advanced-ai/examples/human-fallback.md)

คุณยังสามารถเรียนรู้วิธี [ให้ AI กำหนด parameter ของ tool แบบ dynamic ด้วย `$fromAI()` function](/advanced-ai/examples/using-the-fromai-function.md) ได้ด้วย
