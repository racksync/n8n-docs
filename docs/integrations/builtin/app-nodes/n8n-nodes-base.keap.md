---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Keap node
description: เรียนรู้วิธีใช้ Keap node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Keap node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Keap node

ใช้ Keap node เพื่อทำงานอัตโนมัติใน Keap และเชื่อมต่อ Keap กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Keap หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล companies, products, ecommerce orders, emails, และ files

ในหน้านี้จะมีรายการ operations ที่ Keap node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Keap credentials](/integrations/builtin/credentials/keap.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Company
    * Create a company
    * Retrieve all companies
* Contact
    * Create/update a contact
    * Delete an contact
    * Retrieve an contact
    * Retrieve all contacts
* Contact Note
    * Create a note
    * Delete a note
    * Get a notes
    * Retrieve all notes
    * Update a note
* Contact Tag
    * Add a list of tags to a contact
    * Delete a contact's tag
    * Retrieve all contact's tags
* Ecommerce Order
    * Create an ecommerce order
    * Get an ecommerce order
    * Delete an ecommerce order
    * Retrieve all ecommerce orders
* Ecommerce Product
    * Create an ecommerce product
    * Delete an ecommerce product
    * Get an ecommerce product
    * Retrieve all ecommerce product
* Email
    * Create a record of an email sent to a contact
    * Retrieve all sent emails
    * Send Email
* File
    * Delete a file
    * Retrieve all files
    * Upload a file

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'keap') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
