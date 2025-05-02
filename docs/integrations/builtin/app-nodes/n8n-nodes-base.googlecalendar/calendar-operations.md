---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Calendar Calendar operations
description: Documentation for the Calendar operations in Google Calendar node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
contentType: [integration, reference]
priority: high
---

<!-- vale Vale.Repetition = NO -->
<!-- vale from-write-good.Illusions = NO -->
# Google Calendar Calendar operations
<!-- vale from-write-good.Illusions = YES -->
<!-- vale Vale.Repetition = YES -->

ใช้ operation นี้เพื่อตรวจสอบความพร้อมใช้งานในปฏิทินใน Google Calendar โปรดดู [Google Calendar](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ Google Calendar node

## Availability

ใช้ operation นี้เพื่อตรวจสอบว่าช่วงเวลาที่ระบุว่างในปฏิทินหรือไม่

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Calendar credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Calendar**
- **Operation**: เลือก **Availability**
- **Calendar**: เลือกปฏิทินที่คุณต้องการตรวจสอบ เลือก **From list** เพื่อเลือกชื่อจากรายการดรอปดาวน์ หรือ **By ID** เพื่อป้อน calendar ID
- **Start Time**: เวลาเริ่มต้นสำหรับช่วงเวลาที่คุณต้องการตรวจสอบ โดยค่าเริ่มต้นจะใช้นิพจน์ที่ประเมินเป็นเวลาปัจจุบัน (`{{ $now }}`)
- **End Time**: เวลาสิ้นสุดสำหรับช่วงเวลาที่คุณต้องการตรวจสอบ โดยค่าเริ่มต้นจะใช้นิพจน์ที่ประเมินเป็นหนึ่งชั่วโมงนับจากนี้ (`{{ $now.plus(1, 'hour') }}`)

### Options

- **Output Format**: เลือกรูปแบบสำหรับข้อมูลความพร้อมใช้งาน:
	- **Availability**: ส่งคืนว่ามี event ที่ทับซ้อนกับช่วงเวลาที่กำหนดอยู่แล้วหรือไม่
	- **Booked Slots**: ส่งคืนช่วงเวลาที่ถูกจองแล้ว
	- **RAW**: ส่งคืนข้อมูลดิบ (RAW data) จาก API
- **Timezone**: ไทม์โซนที่ใช้ในการตอบกลับ โดยค่าเริ่มต้นจะใช้ไทม์โซนของ n8n

โปรดดูเอกสาร [Freebusy: query | Google Calendar](https://developers.google.com/calendar/api/v3/reference/freebusy/query){:target=_blank .external-link} API สำหรับข้อมูลเพิ่มเติม
