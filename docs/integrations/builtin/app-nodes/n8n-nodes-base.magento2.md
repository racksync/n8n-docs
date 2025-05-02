---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Magento 2 node documentation
description: Learn how to use the Magento 2 node in n8n. Follow technical documentation to integrate Magento 2 node into your workflows.
contentType: [integration, reference]
---

# Magento 2 node

ใช้ Magento 2 node ในการทำงานอัตโนมัติใน Magento 2 และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ ได้อย่างง่ายดาย โดย n8n รองรับฟีเจอร์หลัก เช่น การสร้าง, อัปเดต, ลบ และดึงข้อมูลลูกค้า, invoices, orders และ products.

ในหน้านี้ คุณจะพบรายการ operations ที่ Magento 2 node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม

/// note | Credentials
ดู [Magento 2 credentials] สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Customer
    * Create a new customer
    * Delete a customer
    * Get a customer
    * Get all customers
    * Update a customer
* Invoice
    * Create an invoice
* Order
    * Cancel an order
    * Get an order
    * Get all orders
    * Ship an order
* Product
    * Create a product
    * Delete a product
    * Get a product
    * Get all products
    * Update a product

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'magento-2') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
