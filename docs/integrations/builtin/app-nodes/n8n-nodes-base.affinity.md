---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Affinity node
description: เรียนรู้วิธีใช้ Affinity node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Affinity node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Affinity node

ใช้ Affinity node เพื่อทำงานอัตโนมัติใน Affinity และผสานรวม Affinity กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ Affinity ในตัว รวมถึงการสร้าง, การดึงข้อมูล, การอัปเดต และการลบ lists, entries, organization, และ persons

ในหน้านี้ คุณจะพบรายการ operations ที่ Affinity node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [Affinity credentials](/integrations/builtin/credentials/affinity.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///	

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* List
    * Get a list
    * Get all lists
* List Entry
    * Create a list entry
    * Delete a list entry
    * Get a list entry
    * Get all list entries
* Organization
    * Create an organization
    * Delete an organization
    * Get an organization
    * Get all organizations
    * Update an organization
* Person
    * Create a person
    * Delete a person
    * Get a person
    * Get all persons
    * Update a person

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'affinity') ]]
