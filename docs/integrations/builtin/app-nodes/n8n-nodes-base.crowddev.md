---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ crowd.dev node
description: เรียนรู้วิธีใช้ crowd.dev node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ crowd.dev node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# crowd.dev node

ใช้ crowd.dev node เพื่อทำงานอัตโนมัติใน crowd.dev และ integrate crowd.dev กับแอปพลิเคชันอื่นๆ n8n มีการรองรับในตัวสำหรับฟีเจอร์ต่างๆ ของ crowd.dev ซึ่งรวมถึงการสร้าง, อัปเดต, และลบ members, notes, organizations, และ tasks

ในหน้านี้ คุณจะพบรายการ operations ที่ crowd.dev node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูล authentication สำหรับ node นี้ได้ [here](/integrations/builtin/credentials/crowddev.md)
///

## Operations

* Activity
	* Create or Update with a Member
	* Create
* Automation
	* Create
	* Destroy
	* Find
	* List
	* Update
* Member
	* Create or Update
	* Delete
	* Find
	* Update
* Note
	* Create
	* Delete
	* Find
	* Update
* Organization
	* Create
	* Delete
	* Find
	* Update
* Task
	* Create
	* Delete
	* Find
	* Update

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'crowddev') ]]

## Related resources

n8n มี trigger node สำหรับ crowd.dev คุณสามารถดูเอกสาร trigger node ได้ [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.crowddevtrigger.md)

อ้างอิง [crowd.dev's documentation](https://docs.crowd.dev/reference/getting-started-with-crowd-dev-api){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ service นี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

