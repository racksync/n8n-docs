---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: SyncroMSP node documentation
description: Learn how to use the SyncroMSP node in n8n. Follow technical documentation to integrate SyncroMSP node into your workflows.
contentType: [integration, reference]
---

# SyncroMSP node

ใช้ SyncroMSP node เพื่อทำให้งานใน SyncroMSP เป็นไปโดยอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ ได้อย่างลงตัว. n8n มีการรองรับฟีเจอร์ของ SyncroMSP ที่หลากหลาย เช่น การสร้างและลบลูกค้า, tickets, และ contacts.

/// note | Credentials
ดู [SyncroMSP credentials](/integrations/builtin/credentials/syncromsp.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Contact
    * Create new contact
    * Delete contact
    * Retrieve contact
    * Retrieve all contacts
    * Update contact
* Customer
    * Create new customer
    * Delete customer
    * Retrieve customer
    * Retrieve all customers
    * Update customer
* RMM
    * Create new RMM Alert
    * Delete RMM Alert
    * Retrieve RMM Alert
    * Retrieve all RMM Alerts
    * Mute RMM Alert
* Ticket
    * Create new ticket
    * Delete ticket
    * Retrieve ticket
    * Retrieve all tickets
    * Update ticket

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'syncromsp') ]]
