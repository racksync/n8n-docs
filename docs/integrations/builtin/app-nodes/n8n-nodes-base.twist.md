---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือโหนด Twist
description: เรียนรู้วิธีใช้โหนด Twist ใน n8n ดูเอกสารทางเทคนิคเพื่อผสานโหนด Twist เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Twist node

ใช้ Twist node เพื่อช่วยให้งานใน Twist เป็นอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันต่างๆ โดย n8n รองรับฟีเจอร์ของ Twist หลากหลาย เช่น การสร้าง conversation ใน channel และการสร้างรวมถึงการลบ comment ใน thread

/// note | Credentials
ดู [Twist credentials](/integrations/builtin/credentials/twist.md) สำหรับคำแนะนำในการตั้งค่า authentication
///

## Operations

* Channel
    * Archive a channel
    * Initiates a public or private channel-based conversation
    * Delete a channel
    * Get information about a channel
    * Get all channels
    * Unarchive a channel
    * Update a channel
* Comment
    * Create a new comment to a thread
    * Delete a comment
    * Get information about a comment
    * Get all comments
    * Update a comment
* Message Conversation
    * Create a message in a conversation
    * Delete a message in a conversation
    * Get a message in a conversation
    * Get all messages in a conversation
    * Update a message in a conversation
* Thread
    * Create a new thread in a channel
    * Delete a thread
    * Get information about a thread
    * Get all threads
    * Update a thread

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'twist') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

## Get the User ID

สำหรับการดึง User ID ของผู้ใช้:

1. เปิดแท็บ **Team**
2. เลือก avatar ของผู้ใช้
3. คัดลอกชุดตัวอักษรที่อยู่หลัง `/u/` ใน Twist URL ของคุณ ซึ่งชุดตัวอักษรนี้คือ User ID
4. ตัวอย่างเช่น ถ้า URL เป็น `https://twist.com/a/4qw45/people/u/475370` User ID จะเป็น `475370`

