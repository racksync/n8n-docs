---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ ActiveCampaign node
description: เรียนรู้วิธีใช้ ActiveCampaign node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ ActiveCampaign node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# ActiveCampaign node

ใช้ ActiveCampaign node เพื่อทำงานอัตโนมัติใน ActiveCampaign และผสานรวม ActiveCampaign กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ ActiveCampaign ในตัว รวมถึงการสร้าง, การดึงข้อมูล, การอัปเดต, และการลบ accounts, contact, orders, e-commerce customers, connections, lists, tags, และ deals

ในหน้านี้ คุณจะพบรายการ operations ที่ ActiveCampaign node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [ActiveCampaign credentials](/integrations/builtin/credentials/activecampaign.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Account
    * Create an account
    * Delete an account
    * Get data of an account
    * Get data of all accounts
    * Update an account
* Account Contact
    * Create an association
    * Delete an association
    * Update an association
* Contact
    * Create a contact
    * Delete a contact
    * Get data of a contact
    * Get data of all contact
    * Update a contact
* Contact List
    * Add contact to a list
    * Remove contact from a list
* Contact Tag
    * Add a tag to a contact
    * Remove a tag from a contact
* Connection
    * Create a connection
    * Delete a connection
    * Get data of a connection
    * Get data of all connections
    * Update a connection
* Deal
    * Create a deal
    * Delete a deal
    * Get data of a deal
    * Get data of all deals
    * Update a deal
    * Create a deal note
    * Update a deal note
* E-commerce Order
    * Create a order
    * Delete a order
    * Get data of a order
    * Get data of all orders
    * Update a order
* E-Commerce Customer
    * Create a E-commerce Customer
    * Delete a E-commerce Customer
    * Get data of a E-commerce Customer
    * Get data of all E-commerce Customer
    * Update a E-commerce Customer
* E-commerce Order Products
    * Get data of all order products
    * Get data of a ordered product
    * Get data of an order's products
* List
    * Get all lists
* Tag
    * Create a tag
    * Delete a tag
    * Get data of a tag
    * Get data of all tags
    * Update a tag

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'activecampaign') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

