---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Sheets Trigger node common issues
description: Documentation for common issues and questions in the Google Sheets Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: high
---

# Google Sheets Trigger node common issues

รวม error และปัญหาที่พบบ่อยกับ [Google Sheets Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/index.md) พร้อมวิธีแก้ไขหรือแนวทางตรวจสอบ

## Stuck waiting for trigger event

เวลาทดสอบ Google Sheets Trigger node ด้วยปุ่ม **Test step** หรือ **Test workflow** อาจเจอ workflow ค้างและหยุดฟัง event ไม่ได้ ถ้าเกิดแบบนี้ให้ลองออกจาก workflow แล้วเข้าใหม่เพื่อ reset canvas

ปัญหานี้มักเกิดจาก network configuration ภายนอก n8n โดยเฉพาะถ้าคุณ run n8n หลัง reverse proxy ที่ไม่ได้ตั้งค่า websocket proxying

วิธีแก้ไข ให้เช็ค config reverse proxy (Nginx, Caddy, Apache HTTP Server, Traefik ฯลฯ) ให้รองรับ websocket

## Date and time columns are rendering as numbers

Google Sheets อาจแสดงวันที่และเวลาได้หลายแบบ

[**serial number** format](https://developers.google.com/sheets/api/reference/rest/v4/DateTimeRenderOption) (ที่ Lotus 1-2-3 ทำให้ฮิตและ spreadsheet อื่นๆ ก็ใช้) จะเก็บวันที่เป็นเลขทศนิยม ส่วนที่เป็นจำนวนเต็ม (ซ้ายจุดทศนิยม) คือจำนวนวันนับจาก 30 ธันวาคม 1899 ส่วนที่เป็นทศนิยม (ขวาจุด) คือเวลาใน 24 ชั่วโมง (เช่น `.5` คือเที่ยงตรง)

ถ้าอยากได้ format อื่นสำหรับวันที่และเวลา ให้เปลี่ยน format ใน Google Sheet Trigger node โดยตั้งค่า **Trigger On** เป็น **Row Added**:

1. เปิด Google Sheet Trigger node บน canvas
2. เลือก **Add option**
3. เลือก **DateTime Render**
4. เปลี่ยน **DateTime Render** เป็น **Formatted String**

Google Sheets Trigger node จะส่งค่าประเภท date, time, datetime, duration เป็น string ตาม number format

number format จะขึ้นกับ locale ของ spreadsheet สามารถเปลี่ยน locale ได้ที่ **File > Settings** ใน Google Sheets แล้วเลือก **Locale** ที่ต้องการ กด **Save settings** เพื่อเปลี่ยนค่า
