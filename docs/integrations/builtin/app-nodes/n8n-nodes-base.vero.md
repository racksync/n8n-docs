---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Vero node
description: เรียนรู้วิธีใช้ Vero node ใน n8n และเชื่อมต่อ Vero node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Vero node

ใช้ Vero node ในการทำงานอัตโนมัติใน Vero และเชื่อมต่อ Vero กับแอปพลิเคชันอื่น ๆ. n8n รองรับฟีเจอร์ของ Vero หลากหลาย เช่น การสร้างและลบ users.

ในหน้านี้ คุณจะพบรายการของ operations ที่ Vero node รองรับและลิงก์ไปยัง resource เพิ่มเติม.

/// note | Credentials
ดู [Vero credentials](/integrations/builtin/credentials/vero.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

## Operations

* User
    * Create or update a user profile
    * Change a users identifier
    * Unsubscribe a user.
    * Resubscribe a user.
    * Delete a user.
    * Adds a tag to a users profile.
    * Removes a tag from a users profile.
* Event
    * Track an event for a specific customer

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'vero') ]]
