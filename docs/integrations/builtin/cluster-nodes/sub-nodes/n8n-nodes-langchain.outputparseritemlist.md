---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Item List Output Parser node documentation
description: Learn how to use the Item List Output Parser node in n8n. Follow technical documentation to integrate Item List Output Parser node into your workflows.
contentType: [integration, reference]
priority: high
---

# Item List Output Parser node

ใช้ Item List Output Parser node เพื่อคืนค่ารายการ item ตามจำนวนและ separator ที่กำหนด

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node options

* **Number of Items**: ใส่จำนวนสูงสุดของ item ที่จะคืนค่า ถ้าใส่ `-1` จะไม่จำกัดจำนวน
* **Separator**: เลือก separator ที่จะใช้แยกผลลัพธ์เป็นแต่ละ item (ค่าเริ่มต้นคือขึ้นบรรทัดใหม่)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'item-list-output-parser') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's output parser documentation](https://js.langchain.com/docs/concepts/output_parsers){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
