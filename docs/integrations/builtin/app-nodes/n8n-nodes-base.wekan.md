---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Wekan node documentation
description: Learn how to use the Wekan node in n8n. Follow technical documentation to integrate Wekan node into your workflows.
contentType: [integration, reference]
---

# Wekan node

ใช้ Wekan node ในการทำงานอัตโนมัติใน Wekan และเชื่อมต่อ Wekan กับแอปพลิเคชันอื่น ๆ. n8n รองรับฟีเจอร์ของ Wekan หลากหลาย เช่น การสร้าง, การอัปเดต, การลบ และการดึงข้อมูล boards และ cards.

ในหน้านี้ คุณจะพบรายการของ operations ที่ Wekan node รองรับและลิงก์ไปยัง resource เพิ่มเติม.

/// note | Credentials
ดู [Wekan credentials](/integrations/builtin/credentials/wekan.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

## Operations

* Board
    * Create a new board
    * Delete a board
    * Get the data of a board
    * Get all user boards
* Card
    * Create a new card
    * Delete a card
    * Get a card
    * Get all cards
    * Update a card
* Card Comment
    * Create a comment on a card
    * Delete a comment from a card
    * Get a card comment
    * Get all card comments
* Checklist
    * Create a new checklist
    * Delete a checklist
    * Get the data of a checklist
    * Returns all checklists for the card
* Checklist Item
    * Delete a checklist item
    * Get a checklist item
    * Update a checklist item
* List
    * Create a new list
    * Delete a list
    * Get the data of a list
    * Get all board lists

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'wekan') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

## Load all the parameters for the node

ในการโหลด parameters ทั้งหมด เช่น Author ID คุณต้องให้สิทธิ์ admin กับผู้ใช้. ดู [Wekan documentation](https://github.com/wekan/wekan/wiki/Features#members-click-member-initials-or-avatar--permissions-adminnormalcomment-only){:target=_blank .external-link} เพื่อดูวิธีการเปลี่ยนแปลง permissions.

