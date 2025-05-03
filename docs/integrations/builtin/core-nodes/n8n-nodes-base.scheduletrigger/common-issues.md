---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาที่พบบ่อยใน Schedule Trigger node
description: รวมปัญหาและคำถามที่พบบ่อยเกี่ยวกับ Schedule Trigger node ใน n8n พร้อมแนวทางแก้ไข
contentType: [integration, reference]
priority: critical
---

# Schedule Trigger node common issues

รวมปัญหาที่เจอบ่อยกับ [Schedule Trigger node](/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/index.md) พร้อมวิธีแก้ไขหรือแนวทางตรวจสอบ

## Invalid cron expression

ปัญหานี้เกิดขึ้นเมื่อคุณตั้ง **Trigger Interval** เป็น **Custom (Cron)** แล้ว n8n ไม่เข้าใจ cron expression ที่ใส่ไว้ อาจจะเพราะ syntax ผิด หรือใช้รูปแบบที่ไม่รองรับ

วิธีตรวจสอบ ให้เช็คตามนี้:

* ตรวจสอบว่า cron expression ที่ใช้ตรงกับ syntax ใน [cron examples](/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/index.md#custom-cron-interval)
* ลองเอา cron expression (หลังจากลบ [seconds column](/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/index.md#why-there-are-six-asterisks-in-the-cron-expression)) ไปเช็คใน [crontab guru](https://crontab.guru/)

## Scheduled workflows run at the wrong time

ถ้า Schedule Trigger node ทำงานไม่ตรงเวลาที่ตั้งไว้ อาจจะต้องตั้งค่า timezone ของ n8n ให้ตรงกับเวลาท้องถิ่นของคุณ

### Adjust the timezone globally

ถ้าใช้ [n8n Cloud](/manage-cloud/overview.md) ให้ดูวิธีตั้ง timezone ได้ที่ [set the Cloud instance timezone](/manage-cloud/set-cloud-timezone.md) เพื่อให้ n8n ทำงานตรงกับเวลาท้องถิ่น

ถ้า [self hosting](/hosting/index.md) ให้ตั้งค่า timezone ทั่วระบบด้วย [`GENERIC_TIMEZONE` environment variable](/hosting/configuration/environment-variables/timezone-localization.md)

### Adjust the timezone for an individual workflow

ถ้าต้องการตั้ง timezone แยกเฉพาะ workflow:

1. เปิด workflow ที่ต้องการใน canvas
1. กด <span class="inline-image">![three dots menu](/_images/common-icons/three-dots-horizontal.png)</span> **Three dots icon** มุมขวาบน
1. เลือก **Settings**
1. เปลี่ยนค่า **Timezone**
1. กด **Save**

### Variables not working as expected

ถึงจะใช้ตัวแปรใน scheduled trigger ได้ แต่ค่าของตัวแปรจะถูกประเมินแค่ตอนที่ workflow ถูก activate เท่านั้น ถ้าเปลี่ยนค่าตัวแปรใน settings หลังจาก activate แล้ว schedule จะไม่เปลี่ยนตาม ต้อง stop แล้ว activate workflow ใหม่เพื่อให้ค่าตัวแปรใหม่ถูกนำไปใช้

### Changing the trigger interval

สามารถเปลี่ยน scheduled trigger interval ได้ตลอดเวลา แต่จะมีผลเฉพาะตอนที่ workflow ถูก activate ใหม่ ถ้าเปลี่ยน interval หลังจาก workflow active อยู่แล้ว การเปลี่ยนแปลงจะยังไม่เกิดขึ้นจนกว่าจะ stop แล้ว activate ใหม่

นอกจากนี้ schedule จะเริ่มนับจากเวลาที่ activate workflow ตัวอย่างเช่น ถ้าเดิมตั้งไว้ทุก 1 ชั่วโมง และควรจะรันตอน 12:00 แต่เปลี่ยนเป็นทุก 2 ชั่วโมงแล้ว activate ใหม่ตอน 11:30 ครั้งถัดไปจะรันตอน 13:30 คือ 2 ชั่วโมงหลัง activate
