---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ NocoDB node
description: เรียนรู้วิธีใช้ NocoDB node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ NocoDB node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# NocoDB node

ใช้ NocoDB node เพื่อทำงานอัตโนมัติใน NocoDB และเชื่อมต่อกับแอปอื่น ๆ. n8n รองรับฟีเจอร์ของ NocoDB เช่น การสร้าง, การอัปเดต, การลบ และการดึงข้อมูล rows

ในหน้านี้ คุณจะพบรายการ operations ที่ NocoDB node รองรับ พร้อมลิงก์สำหรับข้อมูลเพิ่มเติม

/// note | Credentials
ดู [NocoDB credentials](/integrations/builtin/credentials/nocodb.md) เพื่อดูวิธีการตั้งค่า authentication
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Row
    * Create
    * Delete
    * Get
    * Get Many
    * Update a row

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'nocodb') ]]

## Relates resources

ดู [NocoDB's documentation](https://docs.nocodb.com/){:target=_blank .external-link} เพื่อข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
