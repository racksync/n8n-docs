---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Token Splitter node documentation
description: Learn how to use the Token Splitter node in n8n. Follow technical documentation to integrate Token Splitter node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Token Splitter node

Token Splitter node จะช่วยแยก string ข้อความดิบ โดยจะแปลงข้อความเป็น BPE token ก่อน แล้วค่อยแบ่ง token เป็น chunk จากนั้นแปลง token ในแต่ละ chunk กลับเป็นข้อความ

ในหน้านี้จะมี parameter ของ node Token Splitter และลิงก์ resource อื่นๆ ที่เกี่ยวข้อง

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Chunk Size**: ใส่จำนวนตัวอักษรในแต่ละ chunk
* **Chunk Overlap**: ใส่จำนวนตัวอักษรที่ chunk จะซ้อนทับกัน

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'token-splitter') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's token documentation](https://js.langchain.com/docs/concepts/tokens/){:target=_blank .external-link} และ [LangChain's text splitter documentation](https://js.langchain.com/docs/concepts/text_splitters/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
