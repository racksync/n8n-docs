---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาที่พบบ่อย OpenAI Chat Model node
description: รวมปัญหาและวิธีแก้ OpenAI Chat Model node ใน n8n สำหรับ workflow automation
contentType: [integration, reference]
priority: high
---

# OpenAI Chat Model node common issues

นี่คือข้อผิดพลาดและปัญหาที่พบบ่อยบางประการเกี่ยวกับ [OpenAI Chat Model node](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/index.md) และขั้นตอนในการแก้ไขหรือแก้ไขปัญหาเหล่านั้น

## Processing parameters

OpenAI Chat Model node เป็น [sub-node](/glossary.md#sub-node-n8n) Sub-node มีพฤติกรรมแตกต่างจาก node อื่นๆ เมื่อประมวลผลหลายรายการโดยใช้ expressions

Node ส่วนใหญ่ รวมถึง [root nodes](/glossary.md#root-node-n8n) จะรับรายการจำนวนเท่าใดก็ได้เป็น input ประมวลผลรายการเหล่านี้ และส่งออกผลลัพธ์ คุณสามารถใช้ expressions เพื่ออ้างอิงถึงรายการ input และ node จะประมวลผล expression สำหรับแต่ละรายการตามลำดับ ตัวอย่างเช่น หากมี input เป็นค่าชื่อห้าค่า expression `{{ $json.name }}` จะประมวลผลเป็นแต่ละชื่อตามลำดับ

ใน sub-node expression จะประมวลผลเป็นรายการแรกเสมอ ตัวอย่างเช่น หากมี input เป็นค่าชื่อห้าค่า expression `{{ $json.name }}` จะประมวลผลเป็นชื่อแรกเสมอ

--8<-- "_snippets/integrations/openai-api-issues.md"
