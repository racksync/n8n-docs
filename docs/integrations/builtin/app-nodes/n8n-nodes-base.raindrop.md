---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Raindrop node
description: เรียนรู้วิธีใช้ Raindrop node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Raindrop node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Raindrop node

ใช้ Raindrop node ในการอัตโนมัติงานใน Raindrop และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนฟีเจอร์ของ Raindrop มากมาย เช่น การดึงข้อมูลผู้ใช้, การลบ tags, รวมถึงการสร้าง, อัปเดต, ลบ และดึงข้อมูล collections และ bookmarks.

ในหน้านี้ คุณจะพบรายการ operations ที่ Raindrop node รองรับ และลิงก์ไปยัง resources เพิ่มเติม.

/// note | Credentials
ดู [Raindrop credentials](/integrations/builtin/credentials/raindrop.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Bookmark
    * Create
    * Delete
    * Get
    * Get All
    * Update
* Collection
    * Create
    * Delete
    * Get
    * Get All
    * Update
* Tag
    * Delete
    * Get All
* User
    * Get

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'raindrop') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
