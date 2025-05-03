---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Help Scout node
description: เรียนรู้วิธีใช้ Help Scout node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Help Scout node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Help Scout node

ใช้ Help Scout node เพื่อทำงานอัตโนมัติใน Help Scout และเชื่อมต่อ Help Scout กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Help Scout หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล conversations และ customers

ในหน้านี้จะมีรายการ operations ที่ Help Scout node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Help Scout credentials](/integrations/builtin/credentials/helpscout.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Conversation
    * Create a new conversation
    * Delete a conversation
    * Get a conversation
    * Get all conversations
* Customer
    * Create a new customer
    * Get a customer
    * Get all customers
    * Get customer property definitions
    * Update a customer
* Mailbox
    * Get data of a mailbox
    * Get all mailboxes
* Thread
    * Create a new chat thread
    * Get all chat threads

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'helpscout') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
