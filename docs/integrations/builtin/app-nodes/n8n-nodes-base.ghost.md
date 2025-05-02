---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Ghost node documentation
description: เรียนรู้วิธีการใช้ Ghost node ใน n8n ติดตามเอกสารทางเทคนิคเพื่อรวม Ghost node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Ghost node

ใช้ Ghost node เพื่อทำงานอัตโนมัติใน Ghost และเชื่อมต่อ Ghost กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Ghost หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล posts สำหรับ Admin และ content API

ในหน้านี้จะมีรายการ operations ที่ Ghost node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Ghost credentials](/integrations/builtin/credentials/ghost.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

### Admin API

* **Post**
    * Create a post
    * Delete a post
    * Get a post
    * Get all posts
    * Update a post


### Content API

* **Post**
    * Get a post
    * Get all posts

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'ghost') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

