---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: HighLevel node documentation
description: เรียนรู้วิธีการใช้ HighLevel node ใน n8n ทำตามเอกสารทางเทคนิคเพื่อรวม HighLevel node เข้ากับเวิร์กโฟลว์ของคุณ
contentType: [integration, reference]
---

# HighLevel node

ใช้ HighLevel node เพื่อทำงานอัตโนมัติใน HighLevel และเชื่อมต่อ HighLevel กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ HighLevel หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล contacts, opportunities, tasks รวมถึงการจองนัดหมายและดูเวลาว่างใน calendar

ในหน้านี้จะมีรายการ operations ที่ HighLevel node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [HighLevel credentials](/integrations/builtin/credentials/highlevel.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Contact
	* Create or update
	* Delete
	* Get
	* Get many
	* Update
* Opportunity
	* Create
	* Delete
	* Get
	* Get many
	* Update
* Task
	* Create
	* Delete
	* Get
	* Get many
	* Update
* Calendar
	* Book an appointment
	* Get free slots

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'highlevel') ]]

## Related resources

โปรดดู [HighLevel's API documentation and support forums](https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
