---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Agent ใน AI คืออะไร
description: ทำความเข้าใจ agents ในบริบท AI เรียนรู้วิธีที่ n8n ให้บริการ agents
contentType: explanation
---

# What's an agent in AI?

อีกวิธีหนึ่งในการเข้าใจ [agent](/glossary.md#ai-agent) คือมันเหมือนกับ [chain](/advanced-ai/examples/understand-chains.md) ที่สามารถตัดสินใจเองได้ ในขณะที่ chain จะทำงานตามลำดับที่กำหนดไว้ล่วงหน้า agent จะใช้ language model ในการเลือกว่าจะทำอะไรต่อ

Agent คือส่วนที่ทำหน้าที่ตัดสินใจใน AI สามารถโต้ตอบกับ agent อื่นหรือ [tools](/glossary.md#ai-tool) ได้ เมื่อคุณส่งคำถามไปที่ agent มันจะพยายามเลือก tool ที่เหมาะสมที่สุดเพื่อหาคำตอบ Agent จะปรับตัวตามคำถามของคุณและ prompt ที่ใช้ตั้งค่าพฤติกรรมของมัน

## Agents in n8n

n8n มี Agent node ตัวเดียว ซึ่งสามารถตั้งค่าให้ทำงานเป็น agent หลายประเภทได้ ขึ้นอยู่กับการตั้งค่าที่เลือก ดูรายละเอียด agent type ได้ที่ [Agent node documentation](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md)

เมื่อรัน workflow ที่มี agent ตัว agent จะทำงานหลายรอบ เช่น อาจจะมีรอบ setup, รอบที่เรียก tool, แล้วก็รอบที่ประเมินผลลัพธ์จาก tool และตอบกลับผู้ใช้
