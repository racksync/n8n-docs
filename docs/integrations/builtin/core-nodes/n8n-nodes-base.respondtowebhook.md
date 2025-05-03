---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Respond to Webhook
description: เอกสารสำหรับ Respond to Webhook node ใน n8n แพลตฟอร์ม workflow automation พร้อมคำแนะนำการใช้งานและตัวอย่าง
contentType: [integration, reference]
priority: critical
---

# Respond to Webhook

ใช้ Respond to Webhook node เพื่อควบคุมการตอบกลับ (response) ไปยัง webhook ที่เข้ามา Node นี้จะทำงานร่วมกับ [Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md) node

/// note | Runs once for the first data item
Respond to Webhook node จะทำงานแค่ครั้งเดียว โดยใช้ข้อมูล item แรกที่เข้ามา ดูรายละเอียดเพิ่มเติมที่ [Return more than one data item](#return-more-than-one-data-item-deprecated)
///

## How to use Respond to Webhook

วิธีใช้งาน Respond to Webhook node:

1. เพิ่ม [Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md) node เป็น trigger node ของ workflow
1. ใน Webhook node ให้ตั้งค่า **Respond** เป็น **Using 'Respond to Webhook' node**
1. เพิ่ม Respond to Webhook node ไว้ที่ตำแหน่งใดก็ได้ใน workflow ถ้าต้องการให้ return ข้อมูลจาก node อื่น ให้ต่อหลัง node เหล่านั้น

## Node parameters

ตั้งค่าการทำงานของ node นี้ด้วย parameter เหล่านี้

### Respond With

เลือกข้อมูลที่จะส่งกลับไปใน webhook response

- **All Incoming Items**: ตอบกลับด้วย JSON ของทุก item ที่เข้ามา
- **Binary**: ตอบกลับด้วยไฟล์ binary ตามที่กำหนดใน **Response Data Source**
- **First Incoming Item**: ตอบกลับด้วย JSON ของ item แรกที่เข้ามา
- **JSON**: ตอบกลับด้วย JSON object ที่กำหนดใน **Response Body**
- **No Data**: ไม่ส่งข้อมูลกลับ
- **Redirect**: redirect ไปยัง URL ที่ตั้งไว้ใน **Redirect URL**
- **Text**: ตอบกลับด้วยข้อความที่ตั้งไว้ใน **Response Body**

## Node options

เลือก **Add Option** เพื่อดูและตั้งค่า option เพิ่มเติม

- **Response Code**: ตั้งค่า [response code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status){:target=_blank .external-link} ที่ต้องการใช้
- **Response Headers**: กำหนด response headers ที่ต้องการส่งกลับ
- **Put Response in Field**: ใช้ได้เมื่อเลือกตอบกลับแบบ **All Incoming Items** หรือ **First Incoming Item** ตั้งชื่อ field ที่จะเก็บ response data

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'respond-to-webhook') ]]

## Workflow behavior

เมื่อใช้ Respond to Webhook node, workflow จะมีพฤติกรรมดังนี้:

- ถ้า workflow จบโดยไม่ได้ execute Respond to Webhook node: จะส่งข้อความมาตรฐานพร้อม status 200
- ถ้า workflow error ก่อน execute Respond to Webhook node ตัวแรก: จะส่ง error message พร้อม status 500
- ถ้ามี Respond to Webhook node ตัวที่สอง execute หลังตัวแรก: จะถูกละเลย
- ถ้า Respond to Webhook node execute แต่ไม่มี webhook: จะถูกละเลย

## Return more than one data item (deprecated)

/// note | Deprecated in 1.22.0
ตั้งแต่ n8n 1.22.0 สามารถ return ข้อมูลทุก item ได้โดยเลือก **All Incoming Items** แนะนำให้อัปเกรด n8n แทนการใช้วิธี workaround ในหัวข้อนี้
///

Respond to Webhook node จะทำงานแค่ครั้งเดียว โดยใช้ข้อมูล item แรกที่เข้ามา รวมถึงกรณีที่ใช้ [expressions](/code/expressions.md) ไม่สามารถบังคับให้วน loop ด้วย Loop node ได้ (workflow จะรัน แต่ response จะมีแค่ผลลัพธ์แรกเท่านั้น)

ถ้าต้องการ return ข้อมูลมากกว่าหนึ่ง item ให้เลือกวิธีใดวิธีหนึ่งดังนี้:

- แทนที่จะใช้ Respond to Webhook node ให้ใช้ **When Last Node Finishes** ใน **Respond** ของ Webhook node วิธีนี้จะ return ข้อมูลสุดท้ายที่ workflow ส่งออก
- ใช้ [Aggregate](/integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md) node เพื่อรวมหลาย item เป็น item เดียวก่อนส่งต่อให้ Respond to Webhook node โดยตั้งค่า **Aggregate** เป็น **All Item Data (Into a Single List)**
