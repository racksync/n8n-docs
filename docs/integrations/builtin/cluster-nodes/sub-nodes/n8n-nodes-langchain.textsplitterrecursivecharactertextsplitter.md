---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Recursive Character Text Splitter node documentation
description: Learn how to use the Recursive Character Text Splitter node in n8n. Follow technical documentation to integrate Recursive Character Text Splitter node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Recursive Character Text Splitter node

Recursive Character Text Splitter node จะช่วยแยกข้อมูลเอกสารแบบ recursive โดยพยายามคง paragraph, sentence และ word ไว้ด้วยกันให้นานที่สุด

ในหน้านี้จะมี parameter ของ node Recursive Character Text Splitter และลิงก์ resource อื่นๆ ที่เกี่ยวข้อง

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Chunk Size**: ใส่จำนวนตัวอักษรในแต่ละ chunk
* **Chunk Overlap**: ใส่จำนวนตัวอักษรที่ chunk จะซ้อนทับกัน

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'recursive-character-text-splitter') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's text splitter documentation](https://js.langchain.com/docs/concepts/text_splitters){:target=_blank .external-link} และ [LangChain's recursively split by character documentation](https://v03.api.js.langchain.com/classes/langchain.text_splitter.RecursiveCharacterTextSplitter.html){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
