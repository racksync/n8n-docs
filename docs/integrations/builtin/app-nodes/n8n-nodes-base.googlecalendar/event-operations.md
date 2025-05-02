---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Calendar Event operations
description: Documentation for the Event operations in Google Calendar node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
contentType: [integration, reference]
priority: high
---

# Google Calendar Event operations

ใช้ operations เหล่านี้เพื่อสร้าง, ลบ, ดึงข้อมูล และอัปเดต event ใน Google Calendar โปรดดู [Google Calendar](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ Google Calendar node

## Create

ใช้ operation นี้เพื่อเพิ่ม event ลงใน Google Calendar

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Calendar credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Event**
- **Operation**: เลือก **Create**
- **Calendar**: เลือกปฏิทินที่คุณต้องการเพิ่ม event เลือก **From list** เพื่อเลือกชื่อจากรายการดรอปดาวน์ หรือ **By ID** เพื่อป้อน calendar ID
- **Start Time**: เวลาเริ่มต้นของ event โดยค่าเริ่มต้นจะใช้นิพจน์ที่ประเมินเป็นเวลาปัจจุบัน (`{{ $now }}`)
- **End Time**: เวลาสิ้นสุดของ event โดยค่าเริ่มต้นจะใช้นิพจน์ที่ประเมินเป็นหนึ่งชั่วโมงนับจากนี้ (`{{ $now.plus(1, 'hour') }}`)
- **Use Default Reminders**: กำหนดว่าจะเปิดใช้งานการแจ้งเตือนเริ่มต้นสำหรับ event ตามการกำหนดค่าของปฏิทินหรือไม่

### Options

- **All Day**: กำหนดว่า event นี้เป็นแบบทั้งวันหรือไม่
- **Attendees**: ผู้เข้าร่วมที่จะเชิญเข้าร่วม event
- **Color Name or ID**: สีของ event เลือกจากรายการหรือระบุ ID โดยใช้นิพจน์
- **Conference Data**: สร้างลิงก์การประชุม (Hangouts, Meet ฯลฯ) และแนบไปกับ event
- **Description**: คำอธิบายสำหรับ event
- **Guests Can Invite Others**: กำหนดว่าผู้เข้าร่วมนอกเหนือจากผู้จัดสามารถเชิญผู้อื่นเข้าร่วม event ได้หรือไม่
<!-- vale from-write-good.TooWordy = NO -->
- **Guests Can Modify**: กำหนดว่าผู้เข้าร่วมนอกเหนือจากผู้จัดสามารถแก้ไข event ได้หรือไม่
<!-- vale from-write-good.TooWordy = YES -->
- **Guests Can See Other Guests**: กำหนดว่าผู้เข้าร่วมนอกเหนือจากผู้จัดสามารถดูรายชื่อผู้เข้าร่วม event ได้หรือไม่
- **ID**: ตัวระบุที่ไม่ซ้ำกันของ event
- **Location**: ตำแหน่งทางภูมิศาสตร์ของ event ในรูปแบบข้อความอิสระ
- **Max Attendees**: จำนวนผู้เข้าร่วมสูงสุดที่จะรวมไว้ในการตอบกลับ หากมีผู้เข้าร่วมมากกว่าจำนวนที่ระบุ จะส่งคืนเฉพาะผู้เข้าร่วมเท่านั้น
- **Repeat Frequency**: ช่วงเวลาการเกิดซ้ำสำหรับ event ที่เกิดซ้ำ
- **Repeat How Many Times?**: จำนวนครั้งที่จะสร้างสำหรับ event ที่เกิดซ้ำ
- **Repeat Until**: วันที่ที่ event ที่เกิดซ้ำควรหยุด
<!-- vale from-write-good.Weasel = NO -->
- **RRULE**: กฎการเกิดซ้ำ (Recurrence rule) เมื่อตั้งค่าแล้ว จะไม่สนใจ parameters Repeat Frequency, Repeat How Many Times และ Repeat Until
<!-- vale from-write-good.Weasel = YES -->
- **Send Updates**: กำหนดว่าจะส่งการแจ้งเตือนเกี่ยวกับการสร้าง event ใหม่หรือไม่
- **Show Me As**: กำหนดว่า event นี้จะบล็อกเวลาในปฏิทินหรือไม่
- **Summary**: ชื่อของ event

โปรดดูเอกสาร [Events: insert | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/insert){:target=_blank .external-link} API สำหรับข้อมูลเพิ่มเติม

## Delete

ใช้ operation นี้เพื่อลบ event ออกจาก Google Calendar

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Calendar credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Event**
- **Operation**: เลือก **Delete**
- **Calendar**: เลือกปฏิทินที่คุณต้องการลบ event ออก เลือก **From list** เพื่อเลือกชื่อจากรายการดรอปดาวน์ หรือ **By ID** เพื่อป้อน calendar ID
- **Event ID**: ID ของ event ที่ต้องการลบ

### Options

- **Send Updates**: กำหนดว่าจะส่งการแจ้งเตือนเกี่ยวกับการลบ event หรือไม่

โปรดดูเอกสาร [Events: delete | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/delete){:target=_blank .external-link} API สำหรับข้อมูลเพิ่มเติม

## Get

ใช้ operation นี้เพื่อดึงข้อมูล event จาก Google Calendar

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Calendar credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Event**
- **Operation**: เลือก **Get**
- **Calendar**: เลือกปฏิทินที่คุณต้องการดึงข้อมูล event เลือก **From list** เพื่อเลือกชื่อจากรายการดรอปดาวน์ หรือ **By ID** เพื่อป้อน calendar ID
- **Event ID**: ID ของ event ที่ต้องการดึงข้อมูล

### Options

- **Max Attendees**: จำนวนผู้เข้าร่วมสูงสุดที่จะรวมไว้ในการตอบกลับ หากมีผู้เข้าร่วมมากกว่าจำนวนที่ระบุ จะส่งคืนเฉพาะผู้เข้าร่วมเท่านั้น
- **Return Next Instance of Recurrent Event**: กำหนดว่าจะส่งคืน instance ถัดไปของ event ที่เกิดซ้ำแทน event เองหรือไม่
- **Timezone**: ไทม์โซนที่ใช้ในการตอบกลับ โดยค่าเริ่มต้นจะใช้ไทม์โซนของ n8n

โปรดดูเอกสาร [Events: get | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/get){:target=_blank .external-link} API สำหรับข้อมูลเพิ่มเติม

<!-- vale from-write-good.Weasel = NO -->
## Get Many
<!-- vale from-write-good.Weasel = YES -->

ใช้ operation นี้เพื่อดึงข้อมูล event มากกว่าหนึ่งรายการจาก Google Calendar

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Calendar credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Event**
- **Operation**: เลือก **Get Many**
- **Calendar**: เลือกปฏิทินที่คุณต้องการดึงข้อมูล event เลือก **From list** เพื่อเลือกชื่อจากรายการดรอปดาวน์ หรือ **By ID** เพื่อป้อน calendar ID
- **Return All**: กำหนดว่าจะส่งคืนผลลัพธ์ทั้งหมดหรือจำกัดจำนวนตามที่กำหนด
- **Limit**: (เมื่อไม่ได้เลือก "Return All") จำนวนผลลัพธ์สูงสุดที่จะส่งคืน
- **After**: ดึงข้อมูล event ที่เกิดขึ้นหลังเวลานี้ อย่างน้อยส่วนหนึ่งของ event ต้องอยู่หลังเวลานี้ โดยค่าเริ่มต้นจะใช้นิพจน์ที่ประเมินเป็นเวลาปัจจุบัน (`{{ $now }}`) สลับฟิลด์เป็น "fixed" เพื่อเลือกวันที่จากวิดเจ็ตวันที่
- **Before**: ดึงข้อมูล event ที่เกิดขึ้นก่อนเวลานี้ อย่างน้อยส่วนหนึ่งของ event ต้องอยู่ก่อนเวลานี้ โดยค่าเริ่มต้นจะใช้นิพจน์ที่ประเมินเป็นเวลาปัจจุบันบวกหนึ่งสัปดาห์ (`{{ $now.plus({ week: 1 }) }}`) สลับฟิลด์เป็น "fixed" เพื่อเลือกวันที่จากวิดเจ็ตวันที่

### Options

- **Fields**: ระบุฟิลด์ที่จะส่งคืน โดยค่าเริ่มต้นจะส่งคืนชุดฟิลด์ที่ใช้กันทั่วไปซึ่งกำหนดไว้ล่วงหน้าโดย Google ใช้ "*" เพื่อส่งคืนทุกฟิลด์ คุณสามารถดูข้อมูลเพิ่มเติมได้ใน [เอกสารของ Google Calendar เกี่ยวกับการทำงานกับ partial resources](https://developers.google.com/calendar/api/guides/performance#partial)
<!-- vale Vale.Spelling = NO -->
- **iCalUID**: ระบุ event ID (ในรูปแบบ iCalendar) ที่จะรวมไว้ในการตอบกลับ
<!-- vale Vale.Spelling = YES -->
- **Max Attendees**: จำนวนผู้เข้าร่วมสูงสุดที่จะรวมไว้ในการตอบกลับ หากมีผู้เข้าร่วมมากกว่าจำนวนที่ระบุ จะส่งคืนเฉพาะผู้เข้าร่วมเท่านั้น
- **Order By**: ลำดับที่จะใช้สำหรับ event ในการตอบกลับ
- **Query**: คำค้นหาข้อความอิสระเพื่อค้นหา event ที่ตรงกัน การค้นหานี้จะค้นหาทุกฟิลด์ยกเว้น extended properties
- **Recurring Event Handling**: สิ่งที่จะทำสำหรับ event ที่เกิดซ้ำ:
	- **All Occurrences**: ส่งคืนทุก instance ของ event ที่เกิดซ้ำสำหรับช่วงเวลาที่ระบุ
	- **First Occurrence**: ส่งคืน event แรกของ event ที่เกิดซ้ำภายในช่วงเวลาที่ระบุ
	- **Next Occurrence**: ส่งคืน instance ถัดไปของ event ที่เกิดซ้ำภายในช่วงเวลาที่ระบุ
- **Show Deleted**: กำหนดว่าจะรวม event ที่ถูกลบ (ที่มีสถานะเท่ากับ "cancelled") ในผลลัพธ์หรือไม่
- **Show Hidden Invitations**: กำหนดว่าจะรวมคำเชิญที่ซ่อนอยู่ในผลลัพธ์หรือไม่
- **Timezone**: ไทม์โซนที่ใช้ในการตอบกลับ โดยค่าเริ่มต้นจะใช้ไทม์โซนของ n8n
- **Updated Min**: ขอบเขตล่างสำหรับเวลาแก้ไขล่าสุดของ event (ในรูปแบบ [RFC 3339 timestamp](https://datatracker.ietf.org/doc/html/rfc3339))

โปรดดูเอกสาร [Events: list | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/list){:target=_blank .external-link} API สำหรับข้อมูลเพิ่มเติม

## Update

ใช้ operation นี้เพื่ออัปเดต event ใน Google Calendar

ป้อน parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Calendar credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Event**
- **Operation**: เลือก **Update**
- **Calendar**: เลือกปฏิทินที่คุณต้องการเพิ่ม event เลือก **From list** เพื่อเลือกชื่อจากรายการดรอปดาวน์ หรือ **By ID** เพื่อป้อน calendar ID
- **Event ID**: ID ของ event ที่ต้องการอัปเดต
<!-- vale from-write-good.TooWordy = NO -->
- **Modify**: สำหรับ event ที่เกิดซ้ำ เลือกว่าจะอัปเดต event ที่เกิดซ้ำหรือ instance เฉพาะของ event ที่เกิดซ้ำ
<!-- vale from-write-good.TooWordy = YES -->
- **Use Default Reminders**: กำหนดว่าจะเปิดใช้งานการแจ้งเตือนเริ่มต้นสำหรับ event ตามการกำหนดค่าของปฏิทินหรือไม่
- **Update Fields**: ฟิลด์ของ event ที่ต้องการอัปเดต:
	- **All Day**: กำหนดว่า event นี้เป็นแบบทั้งวันหรือไม่
	- **Attendees**: ผู้เข้าร่วมที่จะเชิญเข้าร่วม event คุณสามารถเลือกที่จะเพิ่มผู้เข้าร่วมหรือแทนที่รายชื่อผู้เข้าร่วมที่มีอยู่
	- **Color Name or ID**: สีของ event เลือกจากรายการหรือระบุ ID โดยใช้นิพจน์
	- **Description**: คำอธิบายสำหรับ event
	- **End**: เวลาสิ้นสุดของ event
	- **Guests Can Invite Others**: กำหนดว่าผู้เข้าร่วมนอกเหนือจากผู้จัดสามารถเชิญผู้อื่นเข้าร่วม event ได้หรือไม่
	<!-- vale from-write-good.TooWordy = NO -->
	- **Guests Can Modify**: กำหนดว่าผู้เข้าร่วมนอกเหนือจากผู้จัดสามารถทำการเปลี่ยนแปลง event ได้หรือไม่
	<!-- vale from-write-good.TooWordy = YES -->
	- **Guests Can See Other Guests**: กำหนดว่าผู้เข้าร่วมนอกเหนือจากผู้จัดสามารถดูรายชื่อผู้เข้าร่วม event ได้หรือไม่
	- **ID**: ตัวระบุที่ไม่ซ้ำกันของ event
	- **Location**: ตำแหน่งทางภูมิศาสตร์ของ event ในรูปแบบข้อความอิสระ
	- **Max Attendees**: จำนวนผู้เข้าร่วมสูงสุดที่จะรวมไว้ในการตอบกลับ หากมีผู้เข้าร่วมมากกว่าจำนวนที่ระบุ จะส่งคืนเฉพาะผู้เข้าร่วมเท่านั้น
	- **Repeat Frequency**: ช่วงเวลาการเกิดซ้ำสำหรับ event ที่เกิดซ้ำ
	- **Repeat How Many Times?**: จำนวนครั้งที่จะสร้างสำหรับ event ที่เกิดซ้ำ
	- **Repeat Until**: วันที่ที่ event ที่เกิดซ้ำควรหยุด
	<!-- vale from-write-good.Weasel = NO -->
	- **RRULE**: กฎการเกิดซ้ำ (Recurrence rule) เมื่อตั้งค่าแล้ว จะไม่สนใจ parameters Repeat Frequency, Repeat How Many Times และ Repeat Until
	<!-- vale from-write-good.Weasel = YES -->
	- **Send Updates**: กำหนดว่าจะส่งการแจ้งเตือนเกี่ยวกับการสร้าง event ใหม่หรือไม่
	- **Show Me As**: กำหนดว่า event นี้จะบล็อกเวลาในปฏิทินหรือไม่
	- **Start**: เวลาเริ่มต้นของ event
	- **Summary**: ชื่อของ event
	- **Visibility**: การมองเห็นของ event:
		<!-- vale from-write-good.Passive = NO -->
		- **Confidential**: event เป็นส่วนตัว ค่านี้มีไว้เพื่อความเข้ากันได้
		<!-- vale from-write-good.Passive = YES -->
		- **Default**: ใช้การมองเห็นเริ่มต้นสำหรับ event ในปฏิทิน
		- **Public**: event เป็นสาธารณะและรายละเอียด event สามารถมองเห็นได้โดยผู้อ่านปฏิทินทุกคน
		- **Private**: event เป็นส่วนตัวและมีเพียงผู้เข้าร่วม event เท่านั้นที่สามารถดูรายละเอียด event ได้

โปรดดูเอกสาร [Events: update | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/update){:target=_blank .external-link} API สำหรับข้อมูลเพิ่มเติม
