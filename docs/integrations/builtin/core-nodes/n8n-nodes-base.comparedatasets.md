---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Compare Datasets
description: Documentation for the Compare Datasets node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: high
---

# Compare Datasets

Compare Datasets node ช่วยให้คุณเปรียบเทียบข้อมูลจาก input สองชุดได้ง่ายๆ

## Node parameters

1. เลือกว่าจะเปรียบเทียบ field ไหน ใน **Input A Field** ให้ใส่ชื่อ field ที่ต้องการใช้จาก input stream A ส่วน **Input B Field** ให้ใส่ชื่อ field ที่ต้องการใช้จาก input stream B 
2. **Optional**: ถ้าอยากเปรียบเทียบหลาย field ก็เลือก **Add Fields to Match** เพื่อเพิ่ม field ที่จะเปรียบเทียบได้เลย
3. เลือกว่าจะจัดการกับความแตกต่างของ dataset ยังไง ใน **When There Are Differences** เลือกได้ดังนี้:
	* **Use Input A Version** จะถือว่า input stream A คือข้อมูลหลัก
	* **Use Input B Version** จะถือว่า input stream B คือข้อมูลหลัก
	* **Use a Mix of Versions** จะเลือกใช้ input แต่ละอันสำหรับแต่ละ field ได้
		* ใช้ **Prefer** เพื่อเลือกว่าจะให้ **Input A Version** หรือ **Input B Version** เป็นหลัก
		* ใส่ชื่อ field ที่เป็นข้อยกเว้นใน **For Everything Except** เพื่อดึงข้อมูลจาก input อีกฝั่ง (ใส่หลาย field ได้โดยคั่นด้วย comma)
	* **Include Both Versions** จะรวมข้อมูลจากทั้งสอง input ใน output ซึ่งอาจทำให้โครงสร้างซับซ้อนขึ้น
4. เลือกว่าจะใช้ **Fuzzy Compare** ไหม ถ้าเปิดไว้ การเปรียบเทียบจะยืดหยุ่นเรื่อง type มากขึ้น เช่น 3 กับ "3" จะถือว่าเหมือนกัน แต่ถ้าปิดไว้จะถือว่าไม่เหมือนกัน

## Understand item comparison

การเปรียบเทียบ item จะมี 2 ขั้นตอน:

1. n8n จะเช็คค่าของ field ที่เลือกเปรียบเทียบว่าตรงกันไหมระหว่าง input ทั้งสอง
2. ถ้า field ที่เปรียบเทียบตรงกัน n8n จะเปรียบเทียบ field ทั้งหมดใน item นั้นๆ เพื่อดูว่าข้อมูลเหมือนกันหรือไม่

## Node options

ใช้ **Options** ของ node เพื่อปรับแต่งการเปรียบเทียบหรือเปลี่ยนพฤติกรรมการเปรียบเทียบ

### Fields to Skip Comparing

ใส่ชื่อ field ที่ไม่อยากให้เอามาเปรียบเทียบ

ตัวอย่าง ถ้าเปรียบเทียบ dataset ด้านล่างโดยใช้ `person.language` เป็น **Fields to Match** n8n จะบอกว่าข้อมูลต่างกัน แต่ถ้าเพิ่ม `person.name` ใน **Fields to Skip Comparing** n8n จะถือว่าข้อมูลเหมือนกัน

```json
	// Input 1
	[
		{
			"person":
			{
				"name":	"Stefan",
				"language":	"de"
			}
		},
		{
			"person":
			{
				"name":	"Jim",
				"language":	"en"
			}
		},
		{
			"person":
			{
				"name":	"Hans",
				"language":	"de"
			}
		}
	]
	// Input 2
		[
		{
			"person":
			{
				"name":	"Sara",
				"language":	"de"
			}
		},
		{
			"person":
			{
				"name":	"Jane",
				"language":	"en"
			}
		},
		{
			"person":
			{
				"name":	"Harriet",
				"language":	"de"
			}
		}
	]
```

### Disable Dot Notation

เลือกว่าจะปิดการอ้างถึง field ลูกด้วย `parent.child` ในชื่อ field หรือไม่ (เปิดไว้คือปิดการอ้างถึง, ปิดไว้คือใช้ได้ตามปกติ)

### Multiple Matches

เลือกว่าจะจัดการกับข้อมูลซ้ำยังไง ค่า default คือ **Include All Matches** หรือจะเลือก **Include First Match Only** ก็ได้

ตัวอย่าง ถ้ามี dataset แบบนี้:
```json
	// Input 1
	[
		{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "banana",
				"color": "yellow"
			}
		}
	]
	// Input 2
	[
		{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "banana",
				"color": "yellow"
			}
		}
	]
```

n8n จะคืนค่า 3 item ใน **Same Branch** tab ข้อมูลเหมือนกันทั้งสอง branch

ถ้าเลือก **Include First Match Only** n8n จะคืนค่า 2 item ใน **Same Branch** tab ข้อมูลเหมือนกันแต่จะเอาเฉพาะอันแรกของที่ซ้ำ

## Understand the output

output จะมี 4 แบบ:

* **In A only Branch**: ข้อมูลที่มีเฉพาะใน input แรก
* **Same Branch**: ข้อมูลที่เหมือนกันทั้งสอง input
* **Different Branch**: ข้อมูลที่ต่างกันระหว่าง input
* **In B only Branch**: ข้อมูลที่มีเฉพาะใน input ที่สอง

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'compare-datasets') ]]

