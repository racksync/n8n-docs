---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Zep node documentation
description: Learn how to use the Zep node in n8n. Follow technical documentation to integrate Zep node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Zep node

ใช้ Zep node เพื่อใช้งาน Zep เป็น [memory](/glossary.md#ai-memory) server

ในหน้านี้จะมีรายการ operations ที่ Zep node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/zep.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Session ID**: กรอก ID ที่จะใช้เก็บ memory ใน workflow data

## Templates and examples

[[ templatesWidget(page.title, 'zep') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's Zep documentation](https://js.langchain.com/docs/integrations/memory/zep_memory){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Single memory instance

[[% include "_includes/integrations/cluster-nodes/memory-shared.html" %]]

--8<-- "_glossary/ai-glossary.md"
