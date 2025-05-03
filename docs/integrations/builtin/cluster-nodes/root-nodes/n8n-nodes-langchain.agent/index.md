---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ AI Agent node
description: วิธีใช้งาน AI Agent node ใน n8n สำหรับสร้าง agent ที่ใช้ tools และ API ภายนอก
contentType: [integration, reference]
priority: critical
---

# AI Agent node

[AI agent](/glossary.md#ai-agent) คือระบบอัตโนมัติที่รับข้อมูล ตัดสินใจอย่างมีเหตุผล และดำเนินการภายในสภาพแวดล้อมเพื่อบรรลุเป้าหมายที่เฉพาะเจาะจง สภาพแวดล้อมของ AI agent คือทุกสิ่งที่ agent สามารถเข้าถึงได้ซึ่งไม่ใช่ตัว agent เอง Agent นี้ใช้ [tools](/glossary.md#ai-tool) และ APIs ภายนอกเพื่อดำเนินการและดึงข้อมูล มันสามารถเข้าใจความสามารถของ tools ต่างๆ และตัดสินใจว่าจะใช้ tool ใดขึ้นอยู่กับงาน

/// note | Connect a tool
คุณต้องเชื่อมต่อ tool [sub-node](/integrations/builtin/cluster-nodes/sub-nodes/index.md) อย่างน้อยหนึ่งตัวเข้ากับ AI Agent node
///

/// note | Agent type
ก่อนเวอร์ชัน 1.82.0 AI Agent มีการตั้งค่าสำหรับการทำงานเป็น agent types ต่างๆ สิ่งนี้ได้ถูกลบออกไปแล้ว และ AI Agent nodes ทั้งหมดทำงานเป็น `Tools Agent` ซึ่งเป็นค่าที่แนะนำและใช้บ่อยที่สุด หากคุณกำลังทำงานกับ AI Agent เวอร์ชันเก่าใน workflows หรือ templates ตราบใดที่ตั้งค่าเป็น 'Tools Agent' พวกมันควรจะยังคงทำงานตามที่ตั้งใจไว้กับ node ที่อัปเดตแล้ว
///


## Templates and examples
<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'agent') ]]

## Related resources

อ้างอิง [LangChain's documentation on agents](https://js.langchain.com/docs/concepts/agents/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ

ใหม่สำหรับ AI Agents? อ่าน [n8n blog introduction to AI agents](https://blog.n8n.io/ai-agents/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Common issues

สำหรับข้อผิดพลาดหรือปัญหาทั่วไปและขั้นตอนการแก้ไขที่แนะนำ โปรดดูที่ [Common Issues](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md)

--8<-- "_glossary/ai-glossary.md"
