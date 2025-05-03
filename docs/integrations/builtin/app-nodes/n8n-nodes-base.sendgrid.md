---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือโหนด SendGrid
description: เรียนรู้วิธีใช้โหนด SendGrid ใน n8n ดูเอกสารทางเทคนิคเพื่อผสานโหนด SendGrid เข้ากับ workflow ของคุณ
contentType: [integration, reference]
priority: medium
---

# SendGrid node

ใช้ SendGrid node เพื่อให้การทำงานใน SendGrid เป็นไปโดยอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ ได้อย่างมีประสิทธิภาพ. n8n รองรับฟีเจอร์ของ SendGrid หลากหลาย เช่น การสร้าง, อัปเดต, ลบ, และดึงข้อมูล contacts และ lists รวมถึงการส่ง emails.

/// note | Credentials
ดู [SendGrid credentials](/integrations/builtin/credentials/sendgrid.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Contact
    * Create/update a contact
    * Delete a contact
    * Get a contact by ID
    * Get all contacts
* List
    * Create a list
    * Delete a list
    * Get a list
    * Get all lists
    * Update a list
* Mail
    * Send an email.

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'sendgrid') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
