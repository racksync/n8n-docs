---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: MongoDB Chat Memory node documentation
description: Learn how to use the MongoDB Chat Memory node in n8n. Follow technical documentation to integrate MongoDB Chat Memory node into your workflows.
contentType: [integration, reference]
---

# MongoDB Chat Memory node

ใช้ MongoDB Chat Memory node เพื่อใช้ MongoDB เป็น [memory](/glossary.md#ai-memory) server สำหรับเก็บประวัติแชท

ในหน้านี้จะมีรายการ operations ที่ MongoDB Chat Memory node รองรับ พร้อมลิงก์ไปยัง resource อื่นๆ ที่เกี่ยวข้อง

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ที่ [ที่นี่](/integrations/builtin/credentials/mongodb.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Session Key**: ใส่ key ที่จะใช้เก็บ memory ใน workflow data
* **Collection Name**: ใส่ชื่อ collection ที่จะใช้เก็บประวัติแชท ถ้า collection ยังไม่มี ระบบจะสร้างให้
* **Database Name**: ใส่ชื่อ database ที่จะใช้เก็บประวัติแชท ถ้าไม่ใส่จะใช้ database จาก credentials
* **Context Window Length**: ใส่จำนวน interactions ก่อนหน้าที่จะนำมาใช้เป็น context

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's MongoDB Chat Message History documentation](https://js.langchain.com/docs/integrations/memory/mongodb){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Single memory instance

[[% include "_includes/integrations/cluster-nodes/memory-shared.html" %]]

--8<-- "_glossary/ai-glossary.md"
