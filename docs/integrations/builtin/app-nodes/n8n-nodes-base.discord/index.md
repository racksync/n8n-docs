---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสาร Discord node
description: เรียนรู้วิธีใช้ Discord node ใน n8n ทำตามเอกสารทางเทคนิคเพื่อผสาน Discord node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: high
---

# Discord node

ใช้ Discord node เพื่อทำงานอัตโนมัติใน Discord และผสาน Discord เข้ากับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์ต่างๆ ของ Discord ในตัวมากมาย รวมถึงการส่งข้อความในช่อง Discord และการจัดการช่องต่างๆ

ในหน้านี้ คุณจะพบรายการ operations ที่ Discord node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
โปรดดู [Discord credentials](/integrations/builtin/credentials/discord.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations
<!-- vale off -->
<!-- "Many" triggers warnings -->

- Channel
	- Create
	- Delete
	- Get
	- Get Many
	- Update
- Message
	- Delete
	- Get
	- Get Many
	- React with Emoji
	- Send
	* Send and Wait for Response
- Member
	- Get Many
	- Role Add
	- Role Remove

--8<-- "_snippets/integrations/builtin/send-and-wait-operation.md"

<!-- vale on -->

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'discord') ]]

## Related resources

โปรดดู [Discord's documentation](https://discord.com/developers/docs/intro){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

## Common issues

สำหรับข้อผิดพลาดหรือปัญหาทั่วไปและขั้นตอนการแก้ไขที่แนะนำ โปรดดูที่ [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues.md)
