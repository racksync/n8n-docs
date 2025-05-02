---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Elasticsearch node documentation
description: เรียนรู้วิธีการใช้ Elasticsearch node ใน n8n ทำตามเอกสารทางเทคนิคเพื่อรวม Elasticsearch node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Elasticsearch node

ใช้ Elasticsearch node เพื่อทำงานอัตโนมัติใน Elasticsearch และเชื่อมต่อ Elasticsearch กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Elasticsearch หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล documents และ indexes

ในหน้านี้จะมีรายการ operations ที่ Elasticsearch node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Elasticsearch credentials](/integrations/builtin/credentials/elasticsearch.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Document
    * Create a document
    * Delete a document
    * Get a document
    * Get all documents
    * Update a document
* Index
    * Create
    * Delete
    * Get
    * Get All

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'elasticsearch') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

