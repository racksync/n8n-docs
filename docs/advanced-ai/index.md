---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารและคู่มือ n8n Advanced AI
description: ใช้ n8n LangChain integrations สร้างฟังก์ชัน AI ใน workflows ของคุณ เชื่อมต่อ LangChain กับ data sources และ services อื่นๆ
contentType: overview
---

# Advanced AI

สร้างฟังก์ชัน AI ด้วย n8n: ตั้งแต่การสร้าง chat bot ของคุณเอง ไปจนถึงการใช้ AI เพื่อประมวลผลเอกสารและข้อมูลจากแหล่งอื่น

/// info | Feature availability
ฟีเจอร์นี้มีให้ใช้ทั้งบน Cloud และ self-hosted n8n เวอร์ชัน 1.19.4 ขึ้นไป
///

<div class="grid cards" markdown>

-   __Get started__

    ทำตามบทแนะนำสั้นๆ เพื่อเรียนรู้พื้นฐานการสร้าง AI workflows ใน n8n

    [:octicons-arrow-right-24: Tutorial](/advanced-ai/intro-tutorial.md)

-   __Use a Starter Kit__

    ลองใช้ Self-hosted AI Starter Kit ของ n8n เพื่อเริ่มต้นสร้าง AI workflows ได้อย่างรวดเร็ว

    [:octicons-arrow-right-24: Self-hosted AI Starter Kit](/hosting/starter-kits/ai-starter-kit.md)

-   __Explore examples and concepts__

	เรียกดูตัวอย่างและ workflow templates เพื่อช่วยคุณสร้าง พร้อมคำอธิบาย AI concepts ที่สำคัญ

    [:octicons-arrow-right-24: Examples](/advanced-ai/examples/introduction.md)

-   __How n8n uses LangChain__

    เรียนรู้เพิ่มเติมเกี่ยวกับวิธีที่ n8n สร้างขึ้นบน LangChain

    [:octicons-arrow-right-24: LangChain in n8n](/advanced-ai/langchain/overview.md)

-   __Browse AI templates__

    สำรวจ AI workflow templates หลากหลายบนเว็บไซต์ n8n

    [:octicons-arrow-right-24: AI workflows on n8n.io](https://n8n.io/workflows/?categories=25){:target=_blank .external-link}

</div>

## Related resources

เอกสารและเครื่องมือที่เกี่ยวข้อง

### Node types

ฟีเจอร์นี้ใช้ [Cluster nodes](/integrations/builtin/cluster-nodes/index.md): กลุ่มของ [root](/integrations/builtin/cluster-nodes/root-nodes/index.md) และ [sub](/integrations/builtin/cluster-nodes/sub-nodes/index.md) nodes ที่ทำงานร่วมกัน

--8<-- "_snippets/integrations/builtin/cluster-nodes/cluster-nodes-summary.md"

### Workflow templates

คุณสามารถเรียกดู [workflow templates](/glossary.md#template-n8n) ในแอปหรือบนหน้า [Workflows](https://n8n.io/workflows/?categories=25,26){:target=_blank .external-link} ของเว็บไซต์ n8n

ดู [Templates](/workflows/templates.md) สำหรับข้อมูลเกี่ยวกับการเข้าถึง templates ในแอป

### Chat trigger

ใช้ [n8n Chat Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md) เพื่อ trigger workflow ตามการโต้ตอบใน chat

### Chatbot widget

n8n มี chatbot widget ที่คุณสามารถใช้เป็น frontend สำหรับ AI-powered chat workflows ดูที่หน้า [@n8n/chat npm](https://www.npmjs.com/package/@n8n/chat){:target=_blank .external-link} สำหรับวิธีใช้งาน
