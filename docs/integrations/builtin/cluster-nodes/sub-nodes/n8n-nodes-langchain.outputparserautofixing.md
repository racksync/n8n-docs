---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Auto-fixing Output Parser node documentation
description: เรียนรู้วิธีการใช้ Auto-fixing Output Parser node ใน n8n ทำตามเอกสารทางเทคนิคเพื่อรวม Auto-fixing Output Parser node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Auto-fixing Output Parser node

Auto-fixing Output Parser node จะ wrap output parser ตัวอื่น ถ้าตัวแรก error จะเรียก LLM ตัวอื่นมาช่วยแก้ไขผลลัพธ์ให้

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'auto-fixing-output-parser') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's output parser documentation](https://js.langchain.com/docs/concepts/output_parsers/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
