---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: MultiQuery Retriever node documentation
description: Learn how to use the MultiQuery Retriever node in n8n. Follow technical documentation to integrate MultiQuery Retriever node into your workflows.
contentType: [integration, reference]
priority: medium
---

# MultiQuery Retriever node

MultiQuery Retriever node จะช่วย automate การปรับ prompt โดยใช้ LLM สร้าง query หลายแบบจากมุมมองต่างๆ สำหรับ input query ที่ผู้ใช้กรอกเข้ามา

ในหน้านี้จะมี parameter ของ node MultiQuery Retriever และลิงก์ resource อื่นๆ ที่เกี่ยวข้อง

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node options

* **Query Count**: ใส่จำนวน query ที่ต้องการให้สร้าง (แต่ละอันจะต่างมุมมองกัน)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'multiquery-retriever') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's retriever conceptual documentation](https://js.langchain.com/docs/concepts/retrievers){:target=_blank .external-link} และ [LangChain's multiquery retriever API documentation](https://v03.api.js.langchain.com/classes/langchain.retrievers_multi_query.MultiQueryRetriever.html){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
