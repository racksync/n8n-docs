---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Google Contacts node
description: เรียนรู้วิธีใช้ Google Contacts node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Google Contacts node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Google Contacts node

ใช้ Google Contacts node เพื่อทำงานอัตโนมัติใน Google Contacts และเชื่อมต่อ Google Contacts กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Google Contacts หลายอย่าง เช่น การสร้าง อัปเดต ดึงข้อมูล ลบ และรับ contacts

ในหน้านี้จะมีรายการ operations ที่ Google Contacts node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Google Contacts credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Contact
    * Create a contact
    * Delete a contact
    * Get a contact
    * Retrieve all contacts
    * Update a contact

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-contacts') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
