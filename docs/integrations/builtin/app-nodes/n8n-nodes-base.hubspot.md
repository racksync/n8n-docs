---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ HubSpot node
description: เรียนรู้วิธีใช้ HubSpot node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ HubSpot node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# HubSpot node

ใช้ HubSpot node เพื่อทำงานอัตโนมัติใน HubSpot และเชื่อมต่อ HubSpot กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ HubSpot หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล contacts, deals, lists, engagements และ companies

ในหน้านี้จะมีรายการ operations ที่ HubSpot node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [HubSpot credentials](/integrations/builtin/credentials/hubspot.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Contact
    * Create/Update a contact
    * Delete a contact
    * Get a contact
    * Get all contacts
    * Get recently created/updated contacts
    * Search contacts
* Contact List
    * Add contact to a list
    * Remove a contact from a list
* Company
    * Create a company
    * Delete a company
    * Get a company
    * Get all companies
    * Get recently created companies
    * Get recently modified companies
    * Search companies by domain
    * Update a company
* Deal
    * Create a deal
    * Delete a deal
    * Get a deal
    * Get all deals
    * Get recently created deals
    * Get recently modified deals
    * Search deals
    * Update a deal
* Engagement
    * Create an engagement
    * Delete an engagement
    * Get an engagement
    * Get all engagements
* Form
    * Get all fields from a form
    * Submit data to a form
* Ticket
    * Create a ticket
    * Delete a ticket
    * Get a ticket
    * Get all tickets
    * Update a ticket

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'hubspot') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
