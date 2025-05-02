---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Elastic Security node documentation
description: Learn how to use the Elastic Security node in n8n. Follow technical documentation to integrate Elastic Security node into your workflows.
contentType: [integration, reference]
---

# Elastic Security node

ใช้ Elastic Security node เพื่อทำงานอัตโนมัติใน Elastic Security และเชื่อมต่อ Elastic Security กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Elastic Security หลายอย่าง เช่น การสร้าง อัปเดต ลบ ดึงข้อมูล และรับ cases

ในหน้านี้จะมีรายการ operations ที่ Elastic Security node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Elastic Security credentials](/integrations/builtin/credentials/elasticsecurity.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Case
    * Create a case
    * Delete a case
    * Get a case
    * Retrieve all cases
    * Retrieve a summary of all case activity
    * Update a case
* Case Comment
    * Add a comment to a case
    * Get a case comment
    * Retrieve all case comments
    * Remove a comment from a case
    * Update a comment in a case
* Case Tag
    * Add a tag to a case
    * Remove a tag from a case
* Connector
    * Create a connector

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'elastic-security') ]]
