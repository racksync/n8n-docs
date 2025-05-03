---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Matrix node
description: เรียนรู้วิธีใช้ Matrix node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Matrix node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Matrix node

ใช้ Matrix node ในการทำงานอัตโนมัติใน Matrix และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับฟีเจอร์ต่าง ๆ เช่น การดึงข้อมูลบัญชีผู้ใช้, ส่ง media และ messages ไปยังห้องแชท รวมถึงดึงรายชื่อสมาชิกและข้อความในห้อง.

ในหน้านี้ คุณจะพบรายการ operations ที่ Matrix node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [Matrix credentials] สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Account
    * Get current user's account information
* Event
    * Get single event by ID
* Media
    * Send media to a chat room
* Message
    * Send a message to a room
    * Gets all messages from a room
* Room
    * New chat room with defined settings
    * Invite a user to a room
    * Join a new room
    * Kick a user from a room
    * Leave a room
* Room Member
    * Get all members

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'matrix') ]]

