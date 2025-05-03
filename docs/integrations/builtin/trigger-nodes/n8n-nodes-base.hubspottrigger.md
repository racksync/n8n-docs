---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ HubSpot Trigger node
description: วิธีใช้ HubSpot Trigger node ใน n8n พร้อมตัวอย่าง workflow
contentType: [integration, reference]
priority: medium
---

# HubSpot Trigger node

[HubSpot](https://www.hubspot.com/){:target=_blank .external-link} ให้บริการเครื่องมือสำหรับ social media marketing, content management, web analytics, landing pages, customer support และ search engine optimization

/// warning | Webhooks
ถ้าคุณเปิดใช้งาน trigger ตัวที่สอง ตัวก่อนหน้าจะหยุดทำงานทันที เพราะ trigger จะลงทะเบียน webhook ใหม่กับ HubSpot ทุกครั้งที่เปิดใช้งาน และ HubSpot อนุญาตให้มี webhook ได้แค่หนึ่งอันในแต่ละครั้ง
///

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/hubspot.md)
///

/// note | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่จะช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [HubSpot Trigger integrations](https://n8n.io/integrations/hubspot-trigger/){:target=_blank .external-link} ของ n8n
///

## Events

* Company
	* Created
	* Deleted
	* Property changed
* Contact
	* Created
	* Deleted
	* Privacy deleted
	* Property changed
* Conversation
	* Created
	* Deleted
	* New message
	* Privacy deletion
	* Property changed
* Deal
	* Created
	* Deleted
	* Property changed
* Ticket
	* Created
	* Deleted
	* Property changed 

## Related resources

n8n มี app node สำหรับ HubSpot ด้วย คุณสามารถดูเอกสาร node ได้ [ที่นี่](/integrations/builtin/app-nodes/n8n-nodes-base.hubspot.md)

ดู [example workflows และเนื้อหาอื่น ๆ ที่เกี่ยวข้อง](https://n8n.io/integrations/hubspot-trigger/){:target=_blank .external-link} ได้ที่เว็บไซต์ n8n

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ API ได้ที่ [HubSpot's documentation](https://developers.hubspot.com/docs/api/overview){:target=_blank .external-link}

