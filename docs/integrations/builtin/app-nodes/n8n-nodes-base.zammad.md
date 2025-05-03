---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Zammad node
description: เรียนรู้วิธีใช้ Zammad node ใน n8n และเชื่อมต่อ Zammad node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Zammad node

ใช้ Zammad node ในการทำงานอัตโนมัติใน Zammad และเชื่อมต่อ Zammad กับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนฟีเจอร์ของ Zammad ที่หลากหลาย เช่น การสร้าง, การดึงข้อมูล และการลบ groups และ organizations.

ในหน้านี้ คุณจะพบรายการของ operations ที่ Zammad node รองรับและลิงก์ไปยัง resource เพิ่มเติม.

/// note | Credentials
ดู [Zammad credentials](/integrations/builtin/credentials/zammad.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

## Operations

* Group
    * Create
    * Delete
    * Get
    * Get many
    * Update
* Organization
    * Create
    * Delete
    * Get
    * Get many
    * Update
* Ticket
    * Create
    * Delete
    * Get
    * Get many
* User
    * Create
    * Delete
    * Get
    * Get many
	* Get self
    * Update

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'zammad') ]]
