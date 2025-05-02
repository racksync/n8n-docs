---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Limit
description: Documentation for the Limit node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: high
---

# Limit

ใช้ Limit node เพื่อตัดข้อมูลที่เกินจำนวนสูงสุดที่กำหนดไว้ คุณสามารถเลือกได้ว่า n8n จะเก็บข้อมูลจากต้นหรือท้ายของข้อมูล input

## Node parameters

ตั้งค่า node นี้โดยใช้ parameter ต่อไปนี้

### Max Items

ใส่จำนวนสูงสุดของรายการที่ n8n ควรเก็บไว้ ถ้าข้อมูล input มีมากกว่าค่านี้ n8n จะตัดรายการที่เกินออก

### Keep

ถ้า node ต้องตัดข้อมูลออก ให้เลือกว่าจะเก็บข้อมูลจากตรงไหน:

* **First Items**: เก็บข้อมูลตามจำนวน **Max Items** จากต้นของข้อมูล input
* **Last Items**: เก็บข้อมูลตามจำนวน **Max Items** จากท้ายของข้อมูล input

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'limit') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md"
