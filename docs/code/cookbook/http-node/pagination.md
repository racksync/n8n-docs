---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: ตัวอย่าง Pagination สำหรับ HTTP Request node
contentType: howto
---

# Pagination in the HTTP Request node

HTTP Request node รองรับ pagination รวมถึงให้ตัวอย่างการกำหนดค่าบางส่วน รวมถึงการใช้ [HTTP node variables](/code/builtin/http-node-variables.md)

อ้างอิง [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ node

--8<-- "_snippets/integrations/builtin/core-nodes/http/pagination-api-differences.md"


## Enable pagination

ใน HTTP Request node เลือก **Add Option** > **Pagination**

## Use a URL from the response to get the next page using `$response`

หาก API คืนค่า URL ของหน้าถัดไปในการตอบสนอง (response):

1. ตั้งค่า **Pagination Mode** เป็น **Response Contains Next URL** n8n จะแสดงพารามิเตอร์สำหรับตัวเลือกนี้
1. ใน **Next URL** ใช้ [expression](/glossary.md#expression-n8n) เพื่อตั้งค่า URL expression ที่แน่นอนขึ้นอยู่กับข้อมูลที่ API ของคุณส่งคืน ตัวอย่างเช่น หาก API มีพารามิเตอร์ชื่อ `next-page` ใน response body:
	```javascript
	{{ $response.body["next-page"] }}
	```

## Get the next page by number using `$pageCount`

หาก API ที่คุณใช้รองรับการกำหนดเป้าหมายหน้าเฉพาะตามหมายเลข:

1. ตั้งค่า **Pagination Mode** เป็น **Update a Parameter in Each Request**
1. ตั้งค่า **Type** เป็น **Query**
1. ป้อน **Name** ของ query parameter ซึ่งขึ้นอยู่กับ API ของคุณและมักจะอธิบายไว้ในเอกสารประกอบ ตัวอย่างเช่น บาง API ใช้ query parameter ชื่อ `page` เพื่อตั้งค่าหน้า ดังนั้น **Name** จะเป็น `page`
1. วางเมาส์เหนือ **Value** และเปิดใช้งาน **Expression**
1. ป้อน `{{ $pageCount + 1 }}`

`$pageCount` คือจำนวนหน้าที่ HTTP Request node ดึงข้อมูลมาแล้ว เริ่มต้นที่ศูนย์ API pagination ส่วนใหญ่นับจากหนึ่ง (หน้าแรกคือหน้าหนึ่ง) ซึ่งหมายความว่าการเพิ่ม `+1` ให้กับ `$pageCount` จะทำให้ node ดึงข้อมูลหน้าหนึ่งในลูปแรก หน้าสองในลูปที่สอง และต่อไปเรื่อยๆ

## Navigate pagination through body parameters

หาก API ที่คุณใช้ อนุญาตให้คุณทำ pagination ผ่าน body parameters:

1. ตั้งค่า HTTP Request Method เป็น **POST**
1. ตั้งค่า **Pagination Mode** เป็น **Update a Parameter in Each Request**
1. เลือก **Body** ในพารามิเตอร์ **Type**
1. ป้อน **Name** ของ body parameter ซึ่งขึ้นอยู่กับ API ที่คุณใช้ `page` เป็นชื่อ key ทั่วไป
1. วางเมาส์เหนือ **Value** และเปิดใช้งาน **Expression**
1. ป้อน `{{ $pageCount + 1 }}`

## Set the page size in the query

หาก API ที่คุณใช้รองรับการเลือกขนาดหน้า (page size) ใน query:

1. เลือก **Send Query Parameters** ในพารามิเตอร์หลักของ node (นี่คือพารามิเตอร์ที่คุณเห็นเมื่อเปิด node ครั้งแรก ไม่ใช่การตั้งค่าภายใน options)
1. ป้อน **Name** ของ query parameter ซึ่งขึ้นอยู่กับ API ของคุณ ตัวอย่างเช่น API จำนวนมากใช้ query parameter ชื่อ `limit` เพื่อตั้งค่าขนาดหน้า ดังนั้น **Name** จะเป็น `limit`
1. ใน **Value** ป้อนขนาดหน้าที่คุณต้องการ


