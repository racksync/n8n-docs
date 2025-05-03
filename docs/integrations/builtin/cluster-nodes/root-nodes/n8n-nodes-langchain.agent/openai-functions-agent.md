---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ OpenAI Functions Agent node
description: วิธีใช้งาน OpenAI Functions Agent ของ AI Agent node ใน n8n สำหรับเรียกใช้ฟังก์ชันผ่าน OpenAI
contentType: [integration, reference]
priority: critical
---

# OpenAI Functions Agent node

ใช้ OpenAI Functions Agent node เพื่อใช้ [OpenAI functions model](https://platform.openai.com/docs/guides/function-calling){:target=_blank .external-link} เหล่านี้คือ models ที่ตรวจจับว่าเมื่อใดควรเรียกใช้ function และตอบสนองด้วย inputs ที่ควรส่งผ่านไปยัง function นั้น

อ้างอิง [AI Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ AI Agent node เอง

--8<-- "_snippets/integrations/builtin/cluster-nodes/use-with-chat-trigger.md"

/// note | OpenAI Chat Model required
คุณต้องใช้ [OpenAI Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/index.md) กับ agent นี้
///

## Node parameters

กำหนดค่า OpenAI Functions Agent โดยใช้ parameters ต่อไปนี้

### Prompt

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md"

### Require Specific Output Format

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/output-format.md"

## Node options

ปรับแต่งพฤติกรรมของ OpenAI Functions Agent node โดยใช้ options เหล่านี้:

### System Message

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/system-message.md"

### Max Iterations

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/max-iterations.md"

### Return Intermediate Steps

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/return-intermediate-steps.md"

## Templates and examples

อ้างอิงส่วน [Templates and examples](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md#templates-and-examples) ของ AI Agent node หลัก

## Common issues

สำหรับคำถามหรือปัญหาทั่วไปและแนวทางแก้ไขที่แนะนำ โปรดดูที่ [Common issues](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md)

--8<-- "_glossary/ai-glossary.md"
