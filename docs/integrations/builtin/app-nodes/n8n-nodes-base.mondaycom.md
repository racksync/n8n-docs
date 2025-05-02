---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: monday.com node documentation
description: Learn how to use the monday.com node in n8n. Follow technical documentation to integrate monday.com node into your workflows.
contentType: [integration, reference]
priority: medium
---

# monday.com node

ใช้ monday.com node ในการทำงานอัตโนมัติใน monday.com และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับการสร้างบอร์ดใหม่และการจัดการ items บนบอร์ด.

ในหน้านี้ คุณจะพบรายการ operations ที่ monday.com node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// warning | Minimum required version
This node requires n8n version 1.22.6 or above.
///

/// note | Credentials
ดู [monday.com credentials](/integrations/builtin/credentials/mondaycom.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Board
    * Archive a board
    * Create a new board
    * Get a board
    * Get all boards
* Board Column
    * Create a new column
    * Get all columns
* Board Group
    * Delete a group in a board
    * Create a group in a board
    * Get list of groups in a board
* Board Item
    * Add an update to an item.
    * Change a column value for a board item
    * Change multiple column values for a board item
    * Create an item in a board's group
    * Delete an item
    * Get an item
    * Get all items
    * Get items by column value
    * Move item to group

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'mondaycom') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
