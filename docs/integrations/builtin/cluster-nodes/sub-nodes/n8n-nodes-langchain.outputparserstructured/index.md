---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Structured Output Parser node documentation
description: Learn how to use the Structured Output Parser node in n8n. Follow technical documentation to integrate Structured Output Parser node into your workflows.
contentType: [integration, reference]
priority: high
---

# Structured Output Parser node

ใช้ Structured Output Parser node เพื่อคืนค่า fields ตาม JSON Schema

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนดสำหรับ Structured Output Parser node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Schema Type**: กำหนดโครงสร้าง output และการตรวจสอบความถูกต้อง คุณมีสองตัวเลือกในการระบุ schema:

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-sub-nodes/schema-type-structuring.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'structured-output-parser') ]]

## Related resources

อ้างอิง [LangChain's output parser documentation](https://js.langchain.com/docs/concepts/output_parsers){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Common issues

สำหรับคำถามหรือปัญหาทั่วไปและแนวทางแก้ไขที่แนะนำ โปรดดูที่ [Common issues](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues.md)

--8<-- "_glossary/ai-glossary.md"
