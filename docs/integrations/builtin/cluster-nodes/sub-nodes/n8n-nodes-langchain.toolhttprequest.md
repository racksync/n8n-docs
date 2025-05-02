---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: HTTP Request Tool node documentation
description: Learn how to use the HTTP Request Tool node in n8n. Follow technical documentation to integrate HTTP Request Tool node into your workflows.
search:
  exclude: true
contentType: [integration, reference]
---

# HTTP Request Tool node

/// warning | Legacy tool version
ถ้าคุณเพิ่ม HTTP Request tool node ใหม่ใน workflow ตอนนี้จะใช้ node [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) แบบมาตรฐานเป็น tool อัตโนมัติ หน้านี้อธิบายเฉพาะเวอร์ชัน legacy ของ HTTP Request tool node

คุณสามารถดูว่า workflow ของคุณใช้ tool เวอร์ชันไหนได้โดยดูว่ามีปุ่ม **Add option** ใน node หรือไม่ ถ้ามีปุ่มนี้ แสดงว่าคุณใช้เวอร์ชันใหม่ ไม่ใช่เวอร์ชันที่อธิบายไว้ในหน้านี้
///

HTTP Request tool ทำงานเหมือนกับ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) node ปกติ แต่ถูกออกแบบมาให้ใช้กับ [AI agent](/glossary.md#ai-agent) เป็น tool เพื่อดึงข้อมูลจากเว็บไซต์หรือ API

ในหน้านี้จะมีรายการ operation ที่ HTTP Request node รองรับ และลิงก์ไปยัง resource อื่นๆ

/// note | Credentials
ดูวิธีตั้งค่า authentication ได้ที่ [HTTP Request credentials](/integrations/builtin/credentials/httprequest.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'http-request-tool') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/cluster-nodes/tools-link.md"

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
