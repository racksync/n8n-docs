---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Discourse node
description: เรียนรู้วิธีใช้ Discourse node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Discourse node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Discourse node

ใช้ Discourse node เพื่อทำงานอัตโนมัติใน Discourse และเชื่อมต่อ Discourse กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Discourse หลายอย่าง เช่น การสร้าง ดึงข้อมูล อัปเดต และลบ categories, groups, posts, และ users

ในหน้านี้จะมีรายการ operations ที่ Discourse node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Discourse credentials](/integrations/builtin/credentials/discourse.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Category
    * Create a category
    * Get all categories
    * Update a category
* Group
    * Create a group
    * Get a group
    * Get all groups
    * Update a group
* Post
    * Create a post
    * Get a post
    * Get all posts
    * Update a post
* User
    * Create a user
    * Get a user
    * Get all users
* User Group
    * Create a user to group
    * Remove user from group

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'discourse') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

