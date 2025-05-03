---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสาร Notion node
description: เรียนรู้วิธีใช้ Notion node ใน n8n ดูเอกสารทางเทคนิคเพื่อเชื่อม Notion node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
priority: high
---

# Notion node

ใช้ Notion node เพื่อทำงานอัตโนมัติใน Notion และเชื่อมต่อ Notion กับแอปพลิเคชันอื่นๆ n8n มี built-in support สำหรับฟีเจอร์ต่างๆ ของ Notion เช่น การดึง (get) และค้นหา (search) databases, การสร้าง pages และการดึงข้อมูล users

ในหน้านี้ คุณจะพบรายการ operations ที่ Notion node รองรับ พร้อมลิงก์ไปยัง resources เพิ่มเติม

/// note | Credentials
อ้างอิงถึง [Notion credentials](/integrations/builtin/credentials/notion.md) เพื่อดูวิธีตั้งค่า authentication 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Block
	* Append After
	* Get Child Blocks
* Database
	* Get
	* Get Many
	* Search
* Database Page
	* Create
	* Get
	* Get Many
	* Update
* Page
	* Archive
	* Create
	* Search
* User
	* Get
	* Get Many

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'notion') ]]

## Related resources

n8n มี app node สำหรับ Notion คุณสามารถดู docs ของ trigger node ได้ที่ [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.notiontrigger.md)

อ้างอิงถึง [Notion's documentation](https://developers.notion.com/){:target=_blank .external-link} เพื่อดูรายละเอียดของ API

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

## Common issues

For common errors or issues and suggested resolution steps, refer to [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues.md).
