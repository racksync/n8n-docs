---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Google Books node
description: เรียนรู้วิธีใช้ Google Books node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Google Books node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Google Books node

ใช้ Google Books node เพื่อทำงานอัตโนมัติใน Google Books และเชื่อมต่อ Google Books กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Google Books หลายอย่าง เช่น การดึงข้อมูล bookshelf resource ที่ระบุสำหรับผู้ใช้ที่ระบุ, การเพิ่ม volume ไปยัง bookshelf, และการดึงข้อมูล volume

ในหน้านี้จะมีรายการ operations ที่ Google Books node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Google credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Bookshelf
    * Retrieve a specific bookshelf resource for the specified user
    * Get all public bookshelf resource for the specified user
* Bookshelf Volume
    * Add a volume to a bookshelf
    * Clears all volumes from a bookshelf
    * Get all volumes in a specific bookshelf for the specified user
    * Moves a volume within a bookshelf
    * Removes a volume from a bookshelf
* Volume
    * Get a volume resource based on ID
    * Get all volumes filtered by query

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-books') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
