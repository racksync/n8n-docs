---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Dropbox node
description: เรียนรู้วิธีใช้ Dropbox node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Dropbox node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Dropbox node

ใช้ Dropbox node เพื่อทำงานอัตโนมัติใน Dropbox และเชื่อมต่อ Dropbox กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Dropbox หลายอย่าง เช่น การสร้าง ดาวน์โหลด ย้าย และคัดลอก files และ folders

ในหน้านี้จะมีรายการ operations ที่ Dropbox node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Dropbox credentials](/integrations/builtin/credentials/dropbox.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* File
    * Copy a file
    * Delete a file
    * Download a file
    * Move a file
    * Upload a file
* Folder
    * Copy a folder
    * Create a folder
    * Delete a folder
    * Return the files and folders in a given folder
    * Move a folder
* Search
    * Query

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'dropbox') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

