---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Google Slides node
description: เรียนรู้วิธีใช้ Google Slides node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Google Slides node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Google Slides node

ใช้ Google Slides node เพื่อทำงานอัตโนมัติใน Google Slides และเชื่อมต่อ Google Slides กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Google Slides หลายอย่าง เช่น การสร้าง presentations และดึงข้อมูล pages

ในหน้านี้จะมีรายการ operations ที่ Google Slides node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Google credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Page
    * Get a page
    * Get a thumbnail
* Presentation
    * Create a presentation
    * Get a presentation
    * Get presentation slides
    * Replace text in a presentation

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-slides') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
