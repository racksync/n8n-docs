---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: TheHive 5 node documentation
description: Learn how to use the TheHive 5 node in n8n. Follow technical documentation to integrate TheHive 5 node into your workflows.
contentType: [integration, reference]
---

# TheHive 5 node

ใช้ TheHive 5 node เพื่อช่วยงานอัตโนมัติใน TheHive และเชื่อมต่อ TheHive กับแอปพลิเคชันอื่น ๆ โดย n8n มีการสนับสนุนฟีเจอร์ต่าง ๆ เช่น การสร้าง alert, การนับ log ของ task, case และ observables

/// note | TheHive and TheHive 5
n8n มี node สำหรับ TheHive อยู่ 2 ตัว ใช้ node นี้ (TheHive 5) หากต้องการใช้ API ของ TheHive เวอร์ชัน 5 หากต้องการใช้เวอร์ชัน 3 หรือ 4 ให้ใช้ [TheHive](/integrations/builtin/app-nodes/n8n-nodes-base.thehive.md).

/// note | Credentials
ดู [TheHive credentials](/integrations/builtin/credentials/thehive5.md) สำหรับคำแนะนำในการตั้งค่า authentication.

## Operations

* Alert
	* Create
	* Delete
	* Execute Responder
	* Get
	* Merge Into Case
	* Promote to Case
	* Search
	* Update
	* Update Status
* Case
	* Add Attachment
	* Create
	* Delete Attachment
	* Delete Case
	* Execute Responder
	* Get
	* Get Attachment
	* Get Timeline
	* Search
	* Update
* Comment
	* Create
	* Delete
	* Search
	* Update
* Observable
	* Create
	* Delete
	* Execute Analyzer
	* Execute Responder
	* Get
	* Search
	* Update
* Page
	* Create
	* Delete
	* Search
	* Update
* Query
	* Execute Query
* Task
	* Create
	* Delete
	* Execute Responder
	* Get
	* Search
	* Update
* Task Log
	* Add Attachment
	* Create
	* Delete
	* Delete Attachment
	* Execute Responder
	* Get
	* Search

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'thehive-5') ]]

## Related resources

n8n provides a trigger node for TheHive. You can find the trigger node docs [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger.md).

ดู [documentation](https://docs.strangebee.com/){:target=_blank .external-link} ของ TheHive สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้.
