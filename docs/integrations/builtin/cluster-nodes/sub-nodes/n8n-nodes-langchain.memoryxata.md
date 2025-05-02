---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Xata node documentation
description: Learn how to use the Xata node in n8n. Follow technical documentation to integrate Xata node into your workflows.
contentType: [integration, reference]
---

# Xata node

ใช้ Xata node เพื่อใช้ Xata เป็น [memory](/glossary.md#ai-memory) server
ในหน้านี้จะมีรายการ operations ที่ Xata node รองรับ พร้อมลิงก์ไปยัง resource อื่นๆ ที่เกี่ยวข้อง

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ที่ [ที่นี่](/integrations/builtin/credentials/xata.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

-   **Session ID**: ใส่ ID ที่จะใช้เก็บ memory ใน workflow data
-   **Context Window Length**: ใส่จำนวน interactions ก่อนหน้าที่จะนำมาใช้เป็น context

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'xata') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's Xata documentation](https://js.langchain.com/docs/integrations/memory/xata){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Single memory instance

[[% include "_includes/integrations/cluster-nodes/memory-shared.html" %]]

--8<-- "_glossary/ai-glossary.md"
