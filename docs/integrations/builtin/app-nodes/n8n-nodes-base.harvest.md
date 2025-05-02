า---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Harvest node documentation
description: Learn how to use the Harvest node in n8n. Follow technical documentation to integrate Harvest node into your workflows.
contentType: [integration, reference]
---

# Harvest node

ใช้ Harvest node เพื่อทำงานอัตโนมัติใน Harvest และเชื่อมต่อ Harvest กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Harvest หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล clients, contacts, invoices, tasks, expenses, users, และ projects

ในหน้านี้จะมีรายการ operations ที่ Harvest node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Harvest credentials](/integrations/builtin/credentials/harvest.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Client
    * Create a client
    * Delete a client
    * Get data of a client
    * Get data of all clients
    * Update a client
* Company
    * Retrieves the company for the currently authenticated user
* Contact
    * Create a contact
    * Delete a contact
    * Get data of a contact
    * Get data of all contacts
    * Update a contact
* Estimate
    * Create an estimate
    * Delete an estimate
    * Get data of an estimate
    * Get data of all estimates
    * Update an estimate
* Expense
    * Get data of an expense
    * Get data of all expenses
    * Create an expense
    * Update an expense
    * Delete an expense
* Invoice
    * Get data of an invoice
    * Get data of all invoices
    * Create an invoice
    * Update an invoice
    * Delete an invoice
* Project
    * Create a project
    * Delete a project
    * Get data of a project
    * Get data of all projects
    * Update a project
* Task
    * Create a task
    * Delete a task
    * Get data of a task
    * Get data of all tasks
    * Update a task
* Time Entries
    * Create a time entry using duration
    * Create a time entry using start and end time
    * Delete a time entry
    * Delete a time entry's external reference.
    * Get data of a time entry
    * Get data of all time entries
    * Restart a time entry
    * Stop a time entry
    * Update a time entry
* User
    * Create a user
    * Delete a user
    * Get data of a user
    * Get data of all users
    * Get data of authenticated user
    * Update a user

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'harvest') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
