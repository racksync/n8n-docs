---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Google Workspace Admin node
description: เรียนรู้วิธีใช้ Google Workspace Admin node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Google Workspace Admin node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Google Workspace Admin node

ใช้ Google Workspace Admin node เพื่อทำงานอัตโนมัติใน Google Workspace Admin และเชื่อมต่อ Google Workspace Admin กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Google Workspace Admin หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล users กับ groups

ในหน้านี้จะมีรายการ operations ที่ Google Workspace Admin node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Google credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Group
    * Create a group
    * Delete a group
    * Get a group
    * Get all groups
    * Update a group
* User
    * Create a user
    * Delete a user
    * Get a user
    * Get all users
    * Update a user

## Templates and examples

[[ templatesWidget(page.title, 'google-workspace-admin') ]]

## How to project a user's information

มี 3 วิธีในการ project ข้อมูลของ user:

- **Basic**: ไม่รวม custom fields ใดๆ
- **Custom**: รวม custom fields จาก schemas ใน `customField`
- **Full**: รวม fields ทั้งหมดที่เกี่ยวข้องกับ user

ถ้าอยากรวม custom fields ให้ทำตามนี้:

1. เลือก **Custom** จาก dropdown **Projection**
2. กด **Add Options** แล้วเลือก **Custom Schemas** จาก dropdown
3. เลือกชื่อ schema ที่ต้องการรวมจาก dropdown **Custom Schemas**

