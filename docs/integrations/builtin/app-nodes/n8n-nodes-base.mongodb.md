---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ MongoDB node
description: เรียนรู้วิธีใช้ MongoDB node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ MongoDB node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# MongoDB node

ใช้ MongoDB node ในการทำงานอัตโนมัติใน MongoDB และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับฟีเจอร์หลากหลาย เช่น aggregation, update, find, delete และการดึงเอกสาร.

ในหน้านี้ คุณจะพบรายการ operations ที่ MongoDB node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [MongoDB credentials](/integrations/builtin/credentials/mongodb.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Aggregate documents
* Delete documents
* Find documents
* Find and replace documents
* Find and update documents
* Insert documents
* Update documents

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'mongodb') ]]
