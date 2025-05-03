---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Google Calendar Trigger node
description: วิธีใช้ Google Calendar Trigger node ใน n8n พร้อมตัวอย่าง workflow
contentType: [integration, reference]
priority: medium
---

# Google Calendar Trigger node

[Google Calendar](https://www.google.com/calendar/){:target=_blank .external-link} เป็นบริการปฏิทินสำหรับจัดการเวลาและนัดหมายที่พัฒนาโดย Google

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/google/index.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template เพื่อช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [Google Calendar Trigger integrations ของ n8n](https://n8n.io/integrations/google-calendar-trigger/){:target=_blank .external-link}
///

## Events

- **Event Cancelled**: แจ้งเตือนเมื่อมีการยกเลิก event
- **Event Created**: แจ้งเตือนเมื่อมีการสร้าง event ใหม่
- **Event Ended**: แจ้งเตือนเมื่อ event สิ้นสุด
- **Event Started**: แจ้งเตือนเมื่อ event เริ่มต้น
- **Event Updated**: แจ้งเตือนเมื่อมีการแก้ไข event

[[ templatesWidget(page.title, 'google-calendar-trigger') ]]

## Related resources

n8n มี app node สำหรับ Google Calendar ดูเอกสาร node ได้ [ที่นี่](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/index.md)

ดู [ตัวอย่าง workflow และเนื้อหาที่เกี่ยวข้อง](https://n8n.io/integrations/google-calendar-trigger/){:target=_blank .external-link} บนเว็บไซต์ n8n

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ API ได้ที่ [Google Calendar's documentation](https://developers.google.com/calendar/api/v3/reference){:target=_blank .external-link}
