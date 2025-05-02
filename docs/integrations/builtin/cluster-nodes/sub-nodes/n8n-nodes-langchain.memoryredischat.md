---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Redis Chat Memory node documentation
description: Learn how to use the Redis Chat Memory node in n8n. Follow technical documentation to integrate Redis Chat Memory node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Redis Chat Memory node

ใช้ Redis Chat Memory node เพื่อใช้ Redis เป็น [memory](/glossary.md#ai-memory) server

ในหน้านี้จะมีรายการ operations ที่ Redis Chat Memory node รองรับ พร้อมลิงก์ไปยัง resource อื่นๆ ที่เกี่ยวข้อง

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ที่ [ที่นี่](/integrations/builtin/credentials/redis.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Session Key**: ใส่ key ที่จะใช้เก็บ memory ใน workflow data
* **Session Time To Live**: ใช้ parameter นี้เพื่อกำหนดให้ session หมดอายุหลังจากเวลาที่กำหนด (วินาที)
* **Context Window Length**: ใส่จำนวน interactions ก่อนหน้าที่จะนำมาใช้เป็น context

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'redis-chat-memory') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's Redis Chat Memory documentation](https://js.langchain.com/docs/integrations/memory/redis){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Single memory instance

[[% include "_includes/integrations/cluster-nodes/memory-shared.html" %]]

--8<-- "_glossary/ai-glossary.md"
