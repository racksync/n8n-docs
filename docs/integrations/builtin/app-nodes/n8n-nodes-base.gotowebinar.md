---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: GoToWebinar node documentation
description: Learn how to use the GoToWebinar node in n8n. Follow technical documentation to integrate GoToWebinar node into your workflows.
contentType: [integration, reference]
---

# GoToWebinar node

ใช้ GoToWebinar node เพื่อทำงานอัตโนมัติใน GoToWebinar และเชื่อมต่อ GoToWebinar กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ GoToWebinar หลายอย่าง เช่น การสร้าง ดึงข้อมูล และลบ attendees, organizers, และ registrants

ในหน้านี้จะมีรายการ operations ที่ GoToWebinar node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [GoToWebinar credentials](/integrations/builtin/credentials/gotowebinar.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Attendee
    * Get
    * Get All
    * Get Details
* Co-Organizer
    * Create
    * Delete
    * Get All
    * Re-invite
* Panelist
    * Create
    * Delete
    * Get All
    * Re-invite
* Registrant
    * Create
    * Delete
    * Get
    * Get All
* Session
    * Get
    * Get All
    * Get Details
* Webinar
    * Create
    * Get
    * Get All
    * Update

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'gotowebinar') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
