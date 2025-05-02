---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: WhatsApp Business Cloud node documentation
description: Learn how to use the WhatsApp Business Cloud node in n8n. Follow technical documentation to integrate WhatsApp Business Cloud node into your workflows.
contentType: [integration, reference]
priority: high
---

# WhatsApp Business Cloud node

ใช้ WhatsApp Business Cloud node เพื่ออัตโนมัติการทำงานใน WhatsApp Business และเชื่อมต่อ WhatsApp Business เข้ากับแอปพลิเคชันอื่นๆ n8n รองรับฟีเจอร์หลากหลายของ WhatsApp Business ไม่ว่าจะเป็นการส่งข้อความ รวมถึงการอัปโหลด, ดาวน์โหลด และลบสื่อ

ในหน้านี้ คุณจะพบรายการของ operations ที่ WhatsApp Business Cloud node รองรับและลิงก์ไปยังเอกสารเพิ่มเติม

/// note | Credentials
ดูวิธีการตั้งค่า authentication ได้ที่ [WhatsApp Business Cloud credentials](/integrations/builtin/credentials/whatsapp.md)
///

## Operations

* Message
	* Send
	* Send and Wait for Response
	* Send Template
* Media
	* Upload
	* Download
	* Delete

--8<-- "_snippets/integrations/builtin/send-and-wait-operation.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'whatsapp-business-cloud') ]]

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ operations ได้ที่ [WhatsApp Business Platform's Cloud API documentation](https://developers.facebook.com/docs/whatsapp/cloud-api){:target=_blank}

## Common issues

สำหรับข้อผิดพลาดและปัญหาที่พบได้บ่อยรวมถึงขั้นตอนแนะนำการแก้ไข ให้ดูที่ [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues.md)

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
