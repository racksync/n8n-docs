---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: MISP node documentation
description: Learn how to use the MISP node in n8n. Follow technical documentation to integrate MISP node into your workflows.
contentType: [integration, reference]
---

# MISP node

ใช้ MISP node ในการทำงานอัตโนมัติใน MISP และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับฟีเจอร์หลากหลาย เช่น การสร้าง, อัปเดต, ลบ และดึงข้อมูล events, feeds และ organizations.

ในหน้านี้ คุณจะพบรายการ operations ที่ MISP node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [MISP credentials](/integrations/builtin/credentials/misp.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Attribute
    * Create
    * Delete
    * Get
    * Get All
	* Search
    * Update
* Event
    * Create
    * Delete
    * Get
    * Get All
    * Publish
	* Search
    * Unpublish
    * Update
* Event Tag
    * Add
    * Remove
* Feed
    * Create
    * Disable
    * Enable
    * Get
    * Get All
    * Update
* Galaxy
    * Delete
    * Get
    * Get All
* Noticelist
    * Get
    * Get All
* Object
	* Search
* Organisation
    * Create
    * Delete
    * Get
    * Get All
    * Update
* Tag
    * Create
    * Delete
    * Get All
    * Update
* User
    * Create
    * Delete
    * Get
    * Get All
    * Update
* Warninglist
    * Get
    * Get All

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'misp') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
