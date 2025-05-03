---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Google Cloud Firestore node
description: เรียนรู้วิธีใช้ Google Cloud Firestore node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Google Cloud Firestore node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Google Cloud Firestore node

ใช้ Google Cloud Firestore node เพื่อทำงานอัตโนมัติใน Google Cloud Firestore และเชื่อมต่อ Google Cloud Firestore กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Google Cloud Firestore หลายอย่าง เช่น การสร้าง ลบ และดึงข้อมูล documents

ในหน้านี้จะมีรายการ operations ที่ Google Cloud Firestore node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Google credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Document
    * Create a document
    * Create/Update a document
    * Delete a document
    * Get a document
    * Get all documents from a collection
    * Runs a query against your documents
* Collection
    * Get all root collections

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-cloud-firestore') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
