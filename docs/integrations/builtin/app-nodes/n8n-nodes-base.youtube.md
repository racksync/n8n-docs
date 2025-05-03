---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ YouTube node
description: เรียนรู้วิธีใช้ YouTube node ใน n8n และเชื่อมต่อ YouTube node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
priority: medium
---

# YouTube node

ใช้ YouTube node ในการทำงานอัตโนมัติใน YouTube และเชื่อมต่อ YouTube กับแอปพลิเคชันอื่น ๆ. n8n รองรับฟีเจอร์ของ YouTube หลากหลาย เช่น การดึงข้อมูลและปรับปรุง channels รวมถึงการสร้างและลบ playlists.

ในหน้านี้ คุณจะพบรายการของ operations ที่ YouTube node รองรับและลิงก์ไปยัง resource เพิ่มเติม.

/// note | Credentials
ดู [YouTube credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Channel
    * Retrieve a channel
    * Retrieve all channels
    * Update a channel
    * Upload a channel banner
* Playlist
    * Create a playlist
    * Delete a playlist
    * Get a playlist
    * Retrieve all playlists
    * Update a playlist
* Playlist Item
    * Add an item to a playlist
    * Delete a item from a playlist
    * Get a playlist's item
    * Retrieve all playlist items
* Video
    * Delete a video
    * Get a video
    * Retrieve all videos
    * Rate a video
    * Update a video
    * Upload a video
* Video Category
    * Retrieve all video categories

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'youtube') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
