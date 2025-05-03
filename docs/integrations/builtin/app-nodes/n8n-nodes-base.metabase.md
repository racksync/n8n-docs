---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Metabase node
description: เรียนรู้วิธีใช้ Metabase node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Metabase node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Metabase node

ใช้ Metabase node ในการทำงานอัตโนมัติใน Metabase และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับฟีเจอร์ต่าง ๆ เช่น การจัดการ alerts, databases, metrics และ questions.

ในหน้านี้ คุณจะพบรายการ operations ที่ Metabase node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [Metabase credentials](/integrations/builtin/credentials/metabase.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Alert
    * Get
    * Get All
* Database
    * Add
    * Get All
    * Get Fields
* Metric
    * Get
    * Get All
* Question
    * Get
    * Get All
    * Result Data

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'metabase') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
