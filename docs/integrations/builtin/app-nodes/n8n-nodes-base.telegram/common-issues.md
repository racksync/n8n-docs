---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Telegram node common issues
description: Documentation for common issues and questions in the Telegram node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: critical
---

# Telegram node common issues

ต่อไปนี้คือข้อผิดพลาดและปัญหาที่พบบ่อยกับ [Telegram node](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/index.md) พร้อมวิธีแก้ไขหรือวินิจฉัย

## Add a bot to a Telegram channel

เพื่อให้ bot ส่งข้อความไปยัง channel ได้ ต้องเพิ่ม bot ลงใน channel ก่อน  
หากยังไม่เพิ่ม คุณจะเห็น error ประมาณ:  
`Error: Forbidden: bot is not a participant of the channel`.

วิธีเพิ่ม bot:

1. เปิด channel ใน Telegram app แล้วแตะชื่อ channel  
2. ตรวจสอบว่า channel ตั้งเป็น **public channel**  
3. เลือก **Administrators** > **Add Admin**  
4. ค้นหา username ของ bot แล้วเลือก  
5. แตะ ✔️ มุมขวาบนเพื่อยืนยัน

## Get the Chat ID

คุณสามารถใช้ `@channelusername` กับ public channel เท่านั้น หากเป็น group จะต้องใช้ Chat ID จริง  

มี 3 วิธีรับ Chat ID:

1. จาก [Telegram Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md) node ใน workflow  
2. จากเว็บเบราว์เซอร์: เปิด Telegram เว็บ, เข้ากลุ่ม แล้วดูเลขหลัง “g.” จากนั้นเติม `-` ข้างหน้าเมื่อนำไปใส่ใน n8n  
3. เชิญ [@RawDataBot](https://t.me/RawDataBot){:target=_blank .external-link} เข้า group แล้วมันจะส่ง JSON ที่มี `chat.id` คือ Chat ID ของกลุ่ม จากนั้นลบ bot ออก

## Send more than 30 messages per second

Telegram API จำกัดการส่ง 30 ข้อความต่อวินาที ให้ทำตามนี้:

1. ใช้ [Loop Over Items](/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md) node ดึง Chat IDs ไม่เกิน 30  
2. ต่อเข้ากับ Telegram node และใช้ Expression Editor เลือก Chat IDs จาก Loop Over Items  
3. ใช้ [Code](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md) node รอสักครู่ก่อนดึง batch ถัดไป

หรือดู [workflow ตัวอย่าง](https://n8n.io/workflows/772){:target=_blank .external-link}

## Remove the n8n attribution from sent messages

ถ้าใช้ node ในการ [send Telegram messages](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-message) ข้อความจะมี attribution ต่อท้าย:

> This message was sent automatically with n8n

วิธีลบ attribution:

1. ใน node’s **Additional Fields** เลือก **Add Field**  
2. เลือก **Append n8n Attribution**  
3. ปิด toggle  

ดู [Send Message additional fields](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-message-additional-fields) สำหรับรายละเอียดเพิ่มเติม
