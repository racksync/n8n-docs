---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Customer.io node
description: เรียนรู้วิธีใช้ Customer.io node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Customer.io node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Customer.io node

ใช้ Customer.io node เพื่อทำงานอัตโนมัติใน Customer.io และ integrate Customer.io กับแอปพลิเคชันอื่นๆ n8n มีการรองรับในตัวสำหรับฟีเจอร์ต่างๆ ของ Customer.io รวมถึงการสร้างและอัปเดต customers, การติดตาม events และการดึง campaigns

ในหน้านี้ คุณจะพบรายการ operations ที่ Customer.io node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [Customer.io credentials](/integrations/builtin/credentials/customerio.md) สำหรับคำแนะนำในการตั้งค่า authentication
///

## Operations

* Customer
    * Create/Update a customer.
    * Delete a customer.
* Event
    * Track a customer event.
    * Track an anonymous event.
* Campaign
    * Get
    * Get All
    * Get Metrics
* Segment
    * Add Customer
    * Remove Customer

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'customerio') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

