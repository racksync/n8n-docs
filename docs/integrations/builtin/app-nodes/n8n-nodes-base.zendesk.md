---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Zendesk node documentation
description: Learn how to use the Zendesk node in n8n. Follow technical documentation to integrate Zendesk node into your workflows.
contentType: [integration, reference]
---

# Zendesk node

ใช้ Zendesk node ในการทำงานอัตโนมัติใน Zendesk และเชื่อมต่อ Zendesk กับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนฟีเจอร์ของ Zendesk หลากหลาย เช่น การสร้างและการลบ tickets, users และ organizations.

ในหน้านี้ คุณจะพบรายการของ operations ที่ Zendesk node รองรับและลิงก์ไปยัง resource เพิ่มเติม.

/// note | Credentials
ดู [Zendesk credentials](/integrations/builtin/credentials/zendesk.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Ticket
    * Create a ticket
    * Delete a ticket
    * Get a ticket
    * Get all tickets
    * Recover a suspended ticket
    * Update a ticket
* Ticket Field
    * Get a ticket field
    * Get all system and custom ticket fields
* User
    * Create a user
    * Delete a user
    * Get a user
    * Get all users
    * Get a user's organizations
    * Get data related to the user
    * Search users
    * Update a user
* Organization
    * Create an organization
    * Delete an organization
    * Count organizations
    * Get an organization
    * Get all organizations
    * Get data related to the organization
    * Update a organization

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'zendesk') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
