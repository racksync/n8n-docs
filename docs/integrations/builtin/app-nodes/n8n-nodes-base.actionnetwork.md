---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Action Network node
description: เรียนรู้วิธีใช้ Action Network node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Action Network node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Action Network node

ใช้ Action Network node เพื่อทำงานอัตโนมัติใน Action Network และผสานรวม Action Network กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ Action Network ในตัว รวมถึงการสร้าง, การอัปเดต, และการลบ events, people, tags, และ signatures

ในหน้านี้ คุณจะพบรายการ operations ที่ Action Network node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [Action Network credentials](/integrations/builtin/credentials/actionnetwork.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Attendance
    * Create
    * Get
    * Get All
* Event
    * Create
    * Get
    * Get All
* Person
    * Create
    * Get
    * Get All
    * Update
* Person Tag
    * Add
    * Remove
* Petition
    * Create
    * Get
    * Get All
    * Update
* Signature
    * Create
    * Get
    * Get All
    * Update
* Tag
    * Create
    * Get
    * Get All

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'action-network') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

