---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือโหนด Todoist
description: เรียนรู้วิธีใช้โหนด Todoist ใน n8n ดูเอกสารทางเทคนิคเพื่อผสานโหนด Todoist เข้ากับ workflow ของคุณ
contentType: [integration, reference]
priority: medium
---

# Todoist node

ใช้ Todoist node เพื่อช่วยงานอัตโนมัติใน Todoist และเชื่อมต่อ Todoist กับแอปพลิเคชันอื่น ๆ โดย n8n มีการสนับสนุนคุณสมบัติต่าง ๆ เช่น การสร้าง, อัปเดต, ลบ และดึงข้อมูล task

/// note | Credentials
ดู [Todoist credentials](/integrations/builtin/credentials/todoist.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

// เนื้อหานี้ยกเว้นการแปลเพราะอยู่ในภาษาไทยแล้ว

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Task
    * Create a new task
    * Close a task
    * Delete a task
    * Get a task
    * Get all tasks
    * Reopen a task
    * Update a task

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'todoist') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
