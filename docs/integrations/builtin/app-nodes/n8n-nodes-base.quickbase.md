---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Quick Base node
description: เรียนรู้วิธีใช้ Quick Base node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Quick Base node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Quick Base node

ใช้ Quick Base node ในการอัตโนมัติงานใน Quick Base และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนฟีเจอร์หลากหลายของ Quick Base เช่น การสร้าง, อัปเดต, ลบ และดึง records รวมถึงการดึง fields และดาวน์โหลด files.

ในหน้านี้ คุณจะพบรายการ operations ที่ Quick Base node รองรับ พร้อมทั้งลิงก์ไปยัง resources เพิ่มเติม.

/// note | Credentials
ดู [Quick Base credentials](/integrations/builtin/credentials/quickbase.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Field
    * Get all fields
* File
    * Delete a file
    * Download a file
* Record
    * Create a record
    * Delete a record
    * Get all records
    * Update a record
    * Upsert a record
* Report
    * Get a report
    * Run a report

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'quick-base') ]]
