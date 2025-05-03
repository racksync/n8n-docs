---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือโหนด Trello
description: เรียนรู้วิธีใช้โหนด Trello ใน n8n ดูเอกสารทางเทคนิคเพื่อผสานโหนด Trello เข้ากับ workflow ของคุณ
contentType: [integration, reference]
priority: medium
---

# Trello node

ใช้ Trello node เพื่อช่วยงานอัตโนมัติใน Trello และเชื่อมต่อ Trello กับแอปพลิเคชันอื่น ๆ 

/// note | Credentials
ดู [Trello credentials](/integrations/builtin/credentials/trello.md) สำหรับคำแนะนำในการตั้งค่า authentication.

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Attachment
    * Create a new attachment for a card
    * Delete an attachment
    * Get the data of an attachment
    * Returns all attachments for the card
* Board
    * Create a new board
    * Delete a board
    * Get the data of a board
    * Update a board
* Board Member
    * Add
    * Get All
    * Invite
    * Remove
* Card
    * Create a new card
    * Delete a card
    * Get the data of a card
    * Update a card
* Card Comment
    * Create a comment on a card
    * Delete a comment from a card
    * Update a comment on a card
* Checklist
    * Create a checklist item
    * Create a new checklist
    * Delete a checklist
    * Delete a checklist item
    * Get the data of a checklist
    * Returns all checklists for the card
    * Get a specific checklist on a card
    * Get the completed checklist items on a card
    * Update an item in a checklist on a card
* Label
    * Add a label to a card.
    * Create a new label
    * Delete a label
    * Get the data of a label
    * Returns all labels for the board
    * Remove a label from a card.
    * Update a label.
* List
    * Archive/Unarchive a list
    * Create a new list
    * Get the data of a list
    * Get all the lists
    * Get all the cards in a list
    * Update a list

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'trello') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

## Find the List ID

1. เปิดบอร์ด Trello ที่มี list นั้น
2. หาก list ไม่มีการ์ดใด ๆ ให้เพิ่มการ์ดลงใน list
3. เปิดการ์ดแล้วเพิ่ม `.json` ต่อท้าย URL จากนั้นกด enter
4. ในไฟล์ JSON คุณจะเห็นฟิลด์ที่ชื่อ `idList`
5. คัดลอกข้อมูลจากฟิลด์ `idList` แล้ววางลงในฟิลด์ ***List ID** ใน n8n






