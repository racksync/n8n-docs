---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Brevo node
description: เรียนรู้วิธีใช้ Brevo node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Brevo node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Brevo node

ใช้ Brevo node เพื่อทำงานอัตโนมัติใน Brevo และ integrate Brevo กับแอปพลิเคชันอื่นๆ n8n มีการรองรับในตัวสำหรับฟีเจอร์ต่างๆ ของ Brevo รวมถึงการสร้าง, อัปเดต, ลบ, และดึง contacts, attributes, รวมถึงการส่ง emails

ในหน้านี้ คุณจะพบรายการ operations ที่ Brevo node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [Brevo credentials](/integrations/builtin/credentials/brevo.md) สำหรับคำแนะนำในการตั้งค่า authentication
///

## Operations

* Contact
    * Create
    * Create or Update
    * Delete
    * Get
    * Get All
    * Update
* Contact Attribute
    * Create
    * Delete
    * Get All
    * Update
* Email
    * Send
    * Send Template
* Sender
    * Create
    * Delete
    * Get All

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'brevo') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

