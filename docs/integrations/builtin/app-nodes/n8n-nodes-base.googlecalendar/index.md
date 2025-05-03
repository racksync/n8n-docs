---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสาร Google Calendar node
description: เรียนรู้วิธีใช้ Google Calendar node ใน n8n ทำตามเอกสารทางเทคนิคเพื่อผสาน Google Calendar node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: high
---

# Google Calendar node

ใช้ Google Calendar node เพื่อทำงานอัตโนมัติใน Google Calendar และเชื่อมต่อ Google Calendar กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์ต่างๆ ของ Google Calendar ในตัวมากมาย รวมถึงการเพิ่ม, ดึงข้อมูล, ลบ และอัปเดต event ในปฏิทิน

ในหน้านี้ คุณจะพบรายการ operations ที่ Google Calendar node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
โปรดดู [Google Calendar credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* **Calendar**
    * [**Availability**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations.md#availability): ตรวจสอบว่าช่วงเวลานั้นว่างในปฏิทินหรือไม่
* **Event**
    * [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md#create): เพิ่ม event ลงในปฏิทิน
    * [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md#delete): ลบ event
    * [**Get**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md#get): ดึงข้อมูล event
    * [**Get Many**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md#get-many): ดึงข้อมูล event ทั้งหมดจากปฏิทิน
    * [**Update**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md#update): อัปเดต event

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-calendar') ]]

## Related resources

n8n มี trigger node สำหรับ Google Calendar คุณสามารถดูเอกสาร trigger node ได้ [ที่นี่](/integrations/builtin/trigger-nodes/n8n-nodes-base.googlecalendartrigger.md)

โปรดดู [เอกสารของ Google Calendar](https://developers.google.com/calendar/api/v3/reference){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

ดู [ตัวอย่าง workflows และเนื้อหาที่เกี่ยวข้อง](https://n8n.io/integrations/google-calendar/){:target=_blank .external-link} บนเว็บไซต์ของ n8n
