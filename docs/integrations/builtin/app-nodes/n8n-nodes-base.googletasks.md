---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Google Tasks node
description: เรียนรู้วิธีใช้ Google Tasks node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Google Tasks node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Google Tasks node

ใช้ Google Tasks node เพื่อทำงานอัตโนมัติใน Google Tasks และเชื่อมต่อ Google Tasks กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Google Tasks หลายอย่าง เช่น การเพิ่ม อัปเดต และดึงข้อมูล contacts

ในหน้านี้จะมีรายการ operations ที่ Google Tasks node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Google Tasks credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Task
    * Add a task to task list
    * Delete a task
    * Retrieve a task
    * Retrieve all tasks from a task list
    * Update a task

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-tasks') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
