---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Google Chat node
description: เรียนรู้วิธีใช้ Google Chat node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Google Chat node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Google Chat node

ใช้ Google Chat node เพื่อทำงานอัตโนมัติใน Google Chat และเชื่อมต่อ Google Chat กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Google Chat หลายอย่าง เช่น การดึงข้อมูล membership และ spaces รวมถึงการสร้างและลบ messages

ในหน้านี้จะมีรายการ operations ที่ Google Chat node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Google credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Member
    * Get a membership
    * Get all memberships in a space
* Message
    * Create a message
    * Delete a message
    * Get a message
	* Send and Wait for Response
    * Update a message
* Space
    * Get a space
    * Get all spaces the caller is a member of

--8<-- "_snippets/integrations/builtin/send-and-wait-operation.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-chat') ]]
