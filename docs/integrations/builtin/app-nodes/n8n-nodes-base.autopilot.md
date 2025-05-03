---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Autopilot node
description: เรียนรู้วิธีใช้ Autopilot node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Autopilot node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Autopilot node

ใช้ Autopilot node เพื่อทำงานอัตโนมัติใน Autopilot และผสานรวม Autopilot กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ Autopilot ในตัว รวมถึงการสร้าง, การลบ, และการอัปเดต contacts, รวมถึงการเพิ่ม contacts ไปยัง list

ในหน้านี้ คุณจะพบรายการ operations ที่ Autopilot node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// warning | Autopilot branding change
Autopilot ได้เปลี่ยนเป็น Ortto แล้ว Credentials และ nodes ของ Autopilot สามารถใช้งานได้กับ Autopilot เท่านั้น ไม่สามารถใช้งานร่วมกับ Ortto API ใหม่ได้
///
/// note | Credentials
อ้างอิง [Autopilot credentials](/integrations/builtin/credentials/autopilot.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

## Operations

* Contact
    * Create/Update a contact
    * Delete a contact
    * Get a contact
    * Get all contacts
* Contact Journey
    * Add contact to list
* Contact List
    * Add contact to list
    * Check if contact is on list
    * Get all contacts on list
    * Remove a contact from a list
* List
    * Create a list
    * Get all lists

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'autopilot') ]]

