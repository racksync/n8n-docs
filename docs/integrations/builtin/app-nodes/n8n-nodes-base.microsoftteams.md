---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Microsoft Teams node documentation
description: Learn how to use the Microsoft Teams node in n8n. Follow technical documentation to integrate Microsoft Teams node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Microsoft Teams node

ใช้ Microsoft Teams node ในการทำงานอัตโนมัติใน Microsoft Teams และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับฟีเจอร์ต่าง ๆ เช่น การสร้างและลบ channels, messages และ tasks.

ในหน้านี้ คุณจะพบรายการ operations ที่ Microsoft Teams node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [Microsoft credentials](/integrations/builtin/credentials/microsoft.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Channel
    * Create
    * Delete
    * Get
    * Get Many
    * Update
* Channel Message
    * Create
    * Get Many
* Chat Message
	* Create
	* Get
	* Get Many
	* Send and Wait for Response
* Task
    * Create
    * Delete
    * Get
    * Get Many
    * Update

--8<-- "_snippets/integrations/builtin/send-and-wait-operation.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'microsoft-teams') ]]

## Related resources

Refer to [Microsoft Teams' API documentation](https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0){:target=_blank .external-link} for more information about the service.

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
