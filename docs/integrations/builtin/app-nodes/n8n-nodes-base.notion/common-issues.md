---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาที่พบบ่อยใน Notion node
description: เอกสารปัญหาและคำถามที่พบบ่อยใน Notion node ของ n8n พร้อมรายละเอียดและวิธีแก้ปัญหา
contentType: [integration, reference]
priority: high
---

# Notion node common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปที่พบบ่อยกับ [Notion node](/integrations/builtin/app-nodes/n8n-nodes-base.notion/index.md) พร้อมขั้นตอนการแก้ไขหรือการตรวจสอบ

## Relation property not displaying

Notion node จะแสดงข้อมูล relation property ได้เฉพาะกับ [two-way relations](https://www.notion.com/help/relations-and-rollups) เท่านั้น เมื่อคุณเชื่อมสองฐานข้อมูลใน Notion ด้วยความสัมพันธ์แบบ two-way คุณจะสามารถเลือกหรือกรองตาม relation property ได้เมื่อตั้งค่า Notion node ใน resource **Database Page**

ในการเปิดใช้งาน two-way relations ให้แก้ property ใน Notion และเปิดใช้งานตัวเลือก **Show on [name of related database]** เพื่อสร้าง reverse relation แล้วตั้งชื่อสำหรับ relation ใหม่นั้น Relation ก็จะพร้อมใช้งานใน n8n เมื่อต้องการกรองหรือเลือกข้อมูล

ถ้าคุณจำเป็นต้องใช้งานกับความสัมพันธ์แบบ one-way คุณสามารถใช้ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) ร่วมกับ Notion credentials เดิมของคุณ เช่น เพื่ออัปเดต one-way relationship ให้ส่ง `PATCH` request ไปที่:

```
https://api.notion.com/v1/pages/<page_id>
```

เปิด **Send Body** ตั้ง **Body Content Type** เป็น **JSON** แล้วเลือก **Specify Body** เป็น **Using JSON** จากนั้นใส่วัตถุ JSON แบบนี้ในช่อง **JSON**:

```json
{
	"properties": {
		"Account": {
			"relation": [
				{
					"id": "<your_relation_ID>"
				}
			]
		}
	}
}
```

## Create toggle heading

Notion node อนุญาตให้สร้าง headings และ toggles เมื่อเพิ่ม blocks ใน resource **Page**, **Database Page**, หรือ **Block** แต่การสร้าง toggleable headings ยังไม่รองรับใน Notion node โดยตรง

คุณสามารถแก้ปัญหาได้โดยสร้าง heading ปกติแล้วแก้ไขเพื่อเปิดใช้งาน [`is_toggleable` property](https://developers.notion.com/reference/block#headings) ตามขั้นตอน:

1. เพิ่ม heading ด้วย Notion node  
2. เลือก resource ที่ต้องการใส่ heading:  
   * สำหรับการสร้าง page ใหม่พร้อม heading ให้ใช้ **Page** หรือ **Database Page** กับ operation **Create**  
   * สำหรับการเพิ่ม heading บนหน้าเดิม ให้ใช้ **Block** กับ operation **Append After**  
3. เลือก **Add Block** แล้วตั้ง **Type Name or ID** เป็น **Heading 1**, **Heading 2**, หรือ **Heading 3** ตามต้องการ  
4. เพิ่ม [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) ที่ต่อกับ Notion node แล้วเลือก method `GET`  
5. ตั้ง **URL** เป็น `https://api.notion.com/v1/blocks/<block_ID>` เช่น ถ้าเพิ่ม heading ให้กับ page เดิม อาจตั้งค่าเป็น `https://api.notion.com/v1/blocks/{{ $json.results[0].id }}` ถ้าเป็น page ใหม่ อาจต้องดึง block ID ก่อน  
6. เลือก **Predefined Credential Type** และต่อกับ Notion credentials  
7. เพิ่ม [Edit Fields (Set)](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) หลัง HTTP Request  
8. ใส่ `heading_1.is_toggleable` เป็นฟิลด์ใหม่แบบ **Boolean** ตั้งค่าเป็น `true` (ถ้าใช้ heading 2 หรือ 3 ให้แทนด้วย `heading_2` หรือ `heading_3`)  
9. เพิ่ม HTTP Request อีกตัวหลัง Edit Fields (Set)  
10. ตั้ง **Method** เป็น `PATCH` และ **URL** เป็น `https://api.notion.com/v1/blocks/{{ $json.id }}`  
11. เลือก **Predefined Credential Type** แล้วต่อกับ Notion credentials เดิม  
12. เปิด **Send Body** แล้วตั้ง parameter  
13. ตั้ง **Name** เป็น `heading_1` (แทนด้วยเลขหัวข้อที่ใช้)  
14. ตั้ง **Value** เป็น `{{ $json.heading_1 }}` (แทนด้วยเลขหัวข้อที่ใช้)

วิธีนี้จะสร้าง heading ปกติ ดึงข้อมูล heading ที่สร้าง แล้วแก้ไขเพื่อเปิดใช้งาน `is_toggleable` ก่อนอัปเดต heading block

## Handle null and empty values

อาจพบข้อผิดพลาด validation เมื่อใช้ Notion node ถ้าส่งฟิลด์ที่ว่างหรือมีค่า null ซึ่งเกิดได้เมื่อกรอกฟิลด์จาก node ก่อนหน้าแต่ไม่มีข้อมูล

เพื่อแก้ไข ให้ตรวจสอบว่ามีข้อมูลก่อนส่งไปยัง Notion หรือกำหนดค่า default

- ใช้ [If](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) ตรวจสอบว่าฟิลด์ไม่ได้กำหนดค่า เพื่อให้ [Edit Fields (Set)](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) ลบฟิลด์นั้นเมื่อไม่มีข้อมูล  
- อีกทางเลือกคือกำหนด [default value](/code/cookbook/expressions/check-incoming-data.md) ถ้ามีค่า incoming data ไม่ครบ
