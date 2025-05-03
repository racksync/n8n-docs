---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการใช้งาน Motorhead node
description: วิธีใช้ Motorhead node ใน n8n สำหรับเชื่อมต่อและจัดการ memory ด้วย Motorhead
contentType: [integration, reference]
priority: medium
---

# Motorhead node

ใช้ Motorhead node เพื่อใช้ Motorhead เป็น [memory](/glossary.md#ai-memory) server

ในหน้านี้จะมีรายการ operations ที่ Motorhead node รองรับ พร้อมลิงก์ไปยัง resource อื่นๆ ที่เกี่ยวข้อง

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ที่ [ที่นี่](/integrations/builtin/credentials/motorhead.md)
///

## Node parameters

* **Session ID**: ใส่ ID ที่จะใช้เก็บ memory ใน workflow data

## Node reference

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Templates and examples

[[ templatesWidget(page.title, 'motorhead') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's Motorhead documentation](https://js.langchain.com/docs/integrations/memory/motorhead_memory){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Single memory instance

[[% include "_includes/integrations/cluster-nodes/memory-shared.html" %]]

--8<-- "_glossary/ai-glossary.md"
