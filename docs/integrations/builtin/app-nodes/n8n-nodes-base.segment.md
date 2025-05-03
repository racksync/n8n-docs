---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือโหนด Segment
description: เรียนรู้วิธีใช้โหนด Segment ใน n8n ดูเอกสารทางเทคนิคเพื่อผสานโหนด Segment เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Segment node

ใช้ Segment node เพื่อให้การทำงานใน Segment เป็นไปโดยอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ ได้อย่างลงตัว. n8n รองรับฟีเจอร์ของ Segment หลากหลาย เช่น การเพิ่มผู้ใช้เข้ากลุ่ม, การสร้าง identities, และการติดตาม activities.

/// note | Credentials
ดู [Segment credentials](/integrations/builtin/credentials/segment.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Group
    * Add a user to a group
* Identify
    * Create an identity
* Track
    * Record the actions your users perform. Every action triggers an event, which can also have associated properties.
    * Record page views on your website, along with optional extra information about the page being viewed.

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'segment') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
