---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Invoice Ninja node documentation
description: Learn how to use the Invoice Ninja node in n8n. Follow technical documentation to integrate Invoice Ninja node into your workflows.
contentType: [integration, reference]
---

# Invoice Ninja node

ใช้ Invoice Ninja node เพื่อทำงานอัตโนมัติใน Invoice Ninja และเชื่อมต่อ Invoice Ninja กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Invoice Ninja หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล clients, expense, invoice, payments และ quotes

ในหน้านี้จะมีรายการ operations ที่ Invoice Ninja node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Invoice Ninja credentials](/integrations/builtin/credentials/invoiceninja.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Client
    * Create a new client
    * Delete a client
    * Get data of a client
    * Get data of all clients
* Expense
    * Create a new expense
    * Delete an expense
    * Get data of an expense
    * Get data of all expenses
* Invoice
    * Create a new invoice
    * Delete a invoice
    * Email an invoice
    * Get data of a invoice
    * Get data of all invoices
* Payment
    * Create a new payment
    * Delete a payment
    * Get data of a payment
    * Get data of all payments
* Quote
    * Create a new quote
    * Delete a quote
    * Email an quote
    * Get data of a quote
    * Get data of all quotes
* Task
    * Create a new task
    * Delete a task
    * Get data of a task
    * Get data of all tasks

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'invoice-ninja') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
