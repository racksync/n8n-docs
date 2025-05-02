---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Mautic node documentation
description: Learn how to use the Mautic node in n8n. Follow technical documentation to integrate Mautic node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Mautic node

ใช้ Mautic node ในการทำงานอัตโนมัติใน Mautic และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับฟีเจอร์ต่าง ๆ เช่น การสร้าง, อัปเดต, ลบ และดึงข้อมูล companies และ contacts รวมถึงการจัดการ campaign contacts.

ในหน้านี้ คุณจะพบรายการ operations ที่ Mautic node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [Mautic credentials] สำหรับคำแนะนำในการตั้งค่า authentication.
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Campaign Contact
    * Add contact to a campaign
    * Remove contact from a campaign
* Company
    * Create a new company
    * Delete a company
    * Get data of a company
    * Get data of all companies
    * Update a company
* Company Contact
    * Add contact to a company
    * Remove a contact from a company
* Contact
    * Create a new contact
    * Delete a contact
    * Edit contact's points
    * Add/remove contacts from/to the don't contact list
    * Get data of a contact
    * Get data of all contacts
    * Send email to contact
    * Update a contact
* Contact Segment
    * Add contact to a segment
    * Remove contact from a segment
* Segment Email
    * Send

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'mautic') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
