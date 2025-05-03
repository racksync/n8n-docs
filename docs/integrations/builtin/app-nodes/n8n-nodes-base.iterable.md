---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Iterable node
description: เรียนรู้วิธีใช้ Iterable node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Iterable node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Iterable node

ใช้ Iterable node เพื่อทำงานอัตโนมัติใน Iterable และเชื่อมต่อ Iterable กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Iterable หลายอย่าง เช่น การสร้าง users, บันทึก actions ที่ users ทำ และเพิ่มหรือลบ users จาก list

ในหน้านี้จะมีรายการ operations ที่ Iterable node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Iterable credentials](/integrations/builtin/credentials/iterable.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Event
    * Record the actions a user perform
* User
    * Create/Update a user
    * Delete a user
    * Get a user
* User List
    * Add user to list
    * Remove a user from a list

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'iterable') ]]
