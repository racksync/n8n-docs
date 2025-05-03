---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Baserow node
description: เรียนรู้วิธีใช้ Baserow node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Baserow node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: high
---

# Baserow node

ใช้ Baserow node เพื่อทำงานอัตโนมัติใน Baserow และ integrate Baserow กับแอปพลิเคชันอื่นๆ n8n มีการรองรับในตัวสำหรับฟีเจอร์ต่างๆ ของ Baserow รวมถึงการสร้าง, ดึง, เรียกดู, และอัปเดต rows

ในหน้านี้ คุณจะพบรายการ operations ที่ Baserow node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [Baserow credentials](/integrations/builtin/credentials/baserow.md) สำหรับคำแนะนำในการตั้งค่า authentication
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Row
    * Create a row
    * Delete a row
    * Retrieve a row
    * Retrieve all rows
    * Update a row

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'baserow') ]]
