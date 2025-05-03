---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Asana node
description: เรียนรู้วิธีใช้ Asana node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Asana node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Asana node

ใช้ Asana node เพื่อทำงานอัตโนมัติใน Asana และผสานรวม Asana กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ Asana ในตัว รวมถึงการสร้าง, การอัปเดต, การลบ, และการดึงข้อมูล users, tasks, projects, และ subtasks

ในหน้านี้ คุณจะพบรายการ operations ที่ Asana node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [Asana credentials](/integrations/builtin/credentials/asana.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

/// note | Update to 1.22.2 or above
เนื่องจากการเปลี่ยนแปลงใน API ของ Asana บาง operations ใน node นี้หยุดทำงานเมื่อวันที่ 17 มกราคม 2023 โปรดอัปเกรดเป็น n8n 1.22.2 หรือสูงกว่า
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Project
    * Create a new project
    * Delete a project
    * Get a project
    * Get all projects
    * Update a project
* Subtask
    * Create a subtask
    * Get all subtasks
* Task
    * Create a task
    * Delete a task
    * Get a task
    * Get all tasks
    * Move a task
    * Search for tasks
    * Update a task
* Task Comment
    * Add a comment to a task
    * Remove a comment from a task
* Task Tag
    * Add a tag to a task
    * Remove a tag from a task
* Task Project
    * Add a task to a project
    * Remove a task from a project
* User
    * Get a user
    * Get all users

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'asana') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
