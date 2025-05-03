---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ QuickBooks Online node
description: เรียนรู้วิธีใช้ QuickBooks Online node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ QuickBooks Online node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# QuickBooks Online node

ใช้ QuickBooks node ในการอัตโนมัติงานใน QuickBooks และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนฟีเจอร์หลากหลายของ QuickBooks เช่น การสร้าง, อัปเดต, ลบ และดึงข้อมูล bills, customers, employees, estimates และ invoices.

ในหน้านี้ คุณจะพบรายการ operations ที่ QuickBooks node รองรับ พร้อมทั้งลิงก์ไปยัง resources เพิ่มเติม.

/// note | Credentials
ดู [QuickBooks credentials](/integrations/builtin/credentials/quickbooks.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Bill
    * Create
    * Delete
    * Get
    * Get All
    * Update
* Customer
    * Create
    * Get
    * Get All
    * Update
* Employee
    * Create
    * Get
    * Get All
    * Update
* Estimate
    * Create
    * Delete
    * Get
    * Get All
    * Send
    * Update
* Invoice
    * Create
    * Delete
    * Get
    * Get All
    * Send
    * Update
    * Void
* Item
    * Get
    * Get All
* Payment
    * Create
    * Delete
    * Get
    * Get All
    * Send
    * Update
    * Void
* Purchase
    * Get
    * Get All
* Transaction
    * Get Report
* Vendor
    * Create
    * Get
    * Get All
    * Update

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'quickbooks-online') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
