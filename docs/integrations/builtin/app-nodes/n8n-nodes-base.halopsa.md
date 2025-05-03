---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ HaloPSA node
description: เรียนรู้วิธีใช้ HaloPSA node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ HaloPSA node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# HaloPSA node

ใช้ HaloPSA node เพื่อทำงานอัตโนมัติใน HaloPSA และเชื่อมต่อ HaloPSA กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ HaloPSA หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล clients, sites และ tickets

ในหน้านี้จะมีรายการ operations ที่ HaloPSA node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [HaloPSA credentials](/integrations/builtin/credentials/halopsa.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Client
    * Create a client
    * Delete a client
    * Get a client
    * Get all clients
    * Update a client
* Site
    * Create a site
    * Delete a site
    * Get a site
    * Get all sites
    * Update a site
* Ticket
    * Create a ticket
    * Delete a ticket
    * Get a ticket
    * Get all tickets
    * Update a ticket
* User
    * Create a user
    * Delete a user
    * Get a user
    * Get all users
    * Update a user

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'halopsa') ]]
