---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: จัดการ API rate limit
description: วิธีจัดการ API rate limit เมื่อใช้งาน integration ของ n8n
---

# Handling API rate limits

[API](/glossary.md#api) rate limits คือข้อจำกัดในการส่ง request ไปยัง API ในช่วงเวลาหนึ่ง เช่น บาง API อาจจำกัดจำนวน request ที่ส่งได้ต่อ 1 นาที หรือ 1 วัน

API บางตัวอาจจำกัดปริมาณข้อมูลที่ส่งได้ในแต่ละ request หรือจำกัดข้อมูลที่ API ส่งกลับมาในแต่ละ response ด้วย

## Identify rate limit issues

เมื่อ node ของ n8n เจอ rate limit จะเกิด error ขึ้น โดย n8n จะแสดงข้อความ error ใน output panel ของ node นั้น ซึ่งจะมีข้อความ error ที่ได้จาก service ด้วย

ถ้า n8n ได้รับ error 429 (too many requests) จาก service ข้อความ error จะเป็น **The service is receiving too many requests from you**

ถ้าอยากรู้ว่า service ที่ใช้อยู่มี rate limit เท่าไหร่ ให้ดูที่เอกสาร API ของ service นั้น

## Handle rate limits for integrations

มี 2 วิธีในการจัดการ rate limits ใน integration ของ n8n: ใช้ Retry On Fail หรือใช้ [Loop Over Items](/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md) ร่วมกับ [Wait](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md) node

* Retry On Fail จะเพิ่มการหน่วงเวลา (pause) ระหว่างการลองส่ง request ใหม่
* การใช้ Loop Over Items กับ Wait จะช่วยแบ่งข้อมูลที่ต้องส่งออกเป็นชุดเล็ก ๆ และหยุดรอระหว่างแต่ละ request

### Enable Retry On Fail

ถ้าเปิด Retry On Fail node จะลองส่ง request ใหม่ให้อัตโนมัติถ้าครั้งแรกไม่สำเร็จ

1. เปิด node ที่ต้องการ
1. เลือก **Settings**
1. เปิด toggle **Retry On Fail**
1. ตั้งค่าการ retry: ถ้าใช้เพื่อจัดการ rate limit ให้ตั้ง **Wait Between Tries (ms)** มากกว่าค่าที่ API กำหนด เช่น ถ้า API อนุญาต 1 request ต่อวินาที ให้ตั้ง **Wait Between Tries (ms)** เป็น `1000` เพื่อรอ 1 วินาที

### Use Loop Over Items and Wait

ใช้ Loop Over Items node เพื่อแบ่งข้อมูล input ออกเป็น batch และใช้ Wait node เพื่อหยุดรอระหว่างแต่ละ request

1. เพิ่ม Loop Over Items node ไว้ก่อน node ที่จะเรียก API ดูวิธีตั้งค่าที่ [Loop Over Items](/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md)
1. เพิ่ม Wait node หลัง node ที่เรียก API แล้วเชื่อมกลับไปที่ Loop Over Items node ดูวิธีตั้งค่าที่ [Wait](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md)

ตัวอย่างการจัดการ rate limit กับ OpenAI:

!["Screenshot of a workflow using the Loop Over Items node and Wait node to handle API rate limits for the OpenAI APIs"](/_images/integrations/builtin/rate-limits/loop-wait.png)

## Handle rate limits in the HTTP Request node

HTTP Request node มี option สำหรับจัดการ rate limit และข้อมูลจำนวนมากในตัว

### Batch requests

ใช้ option Batching เพื่อส่ง request หลายครั้ง ลดขนาด request และเพิ่มการหน่วงระหว่างแต่ละ request ซึ่งเหมือนกับการใช้ Loop Over Items กับ Wait

1. ใน HTTP Request node เลือก **Add Option** > **Batching**
1. ตั้งค่า **Items per Batch** คือจำนวน input ที่จะรวมในแต่ละ request
1. ตั้งค่า **Batch Interval (ms)** เพื่อหน่วงระหว่างแต่ละ request เช่น ถ้า API อนุญาต 1 request ต่อวินาที ให้ตั้ง **Wait Between Tries (ms)** เป็น `1000` เพื่อรอ 1 วินาที

### Paginate results

API หลายตัวจะ paginate ข้อมูลถ้าต้องส่งข้อมูลเยอะเกินกว่าที่จะส่งใน response เดียว ดูข้อมูลเพิ่มเติมเกี่ยวกับ pagination ใน HTTP Request node ได้ที่ [HTTP Request node | Pagination](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md#pagination)
