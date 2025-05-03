---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Agile CRM node
description: เรียนรู้วิธีใช้ Agile CRM node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Agile CRM node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Agile CRM node

ใช้ Agile CRM node เพื่อทำงานอัตโนมัติใน Agile CRM และผสานรวม Agile CRM กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ Agile CRM ในตัว รวมถึงการสร้าง, การดึงข้อมูล, การอัปเดต และการลบ companies, contracts, และ deals

ในหน้านี้ คุณจะพบรายการ operations ที่ Agile CRM node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [Agile CRM credentials](/integrations/builtin/credentials/agilecrm.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Company
    * Create a new company
    * Delete a company
    * Get a company
    * Get all companies
    * Update company properties
* Contact
    * Create a new contact
    * Delete a contact
    * Get a contact
    * Get all contacts
    * Update contact properties
* Deal
    * Create a new deal
    * Delete a deal
    * Get a deal
    * Get all deals
    * Update deal properties

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'agile-crm') ]]
