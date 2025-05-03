---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือโหนด Travis CI
description: เรียนรู้วิธีใช้โหนด Travis CI ใน n8n ดูเอกสารทางเทคนิคเพื่อผสานโหนด Travis CI เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Travis CI node

ใช้ Travis CI node เพื่อช่วยงานอัตโนมัติใน Travis CI และเชื่อมต่อ Travis CI กับแอปพลิเคชันอื่น ๆ โดย n8n มีการสนับสนุนคุณสมบัติหลากหลาย เช่น การยกเลิก build และการดึงข้อมูล build

/// note | Credentials
ดู [Travis CI credentials](/integrations/builtin/credentials/travisci.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Build
    * Cancel a build
    * Get a build
    * Get all builds
    * Restart a build
    * Trigger a build

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'travisci') ]]
