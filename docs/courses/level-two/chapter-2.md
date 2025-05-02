---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Processing different data types

ในบทนี้ คุณจะได้เรียนรู้วิธีการประมวลผลข้อมูลประเภทต่างๆ โดยใช้ [n8n core nodes](/workflows/components/nodes.md)


## HTML and XML data

คุณน่าจะคุ้นเคยกับ HTML และ XML อยู่แล้ว

/// note | HTML vs. XML
HTML เป็น markup language ที่ใช้ในการอธิบายโครงสร้างและความหมายของหน้าเว็บ XML ดูคล้ายกับ HTML แต่ชื่อ tag จะแตกต่างกัน เนื่องจากใช้อธิบายประเภทของข้อมูลที่เก็บอยู่
///
หากคุณต้องการประมวลผลข้อมูล HTML หรือ XML ใน n8n workflows ของคุณ ให้ใช้ [**HTML node**](/integrations/builtin/core-nodes/n8n-nodes-base.html.md) หรือ [**XML node**](/integrations/builtin/core-nodes/n8n-nodes-base.xml.md)

ใช้ **HTML node** เพื่อดึงเนื้อหา HTML ของหน้าเว็บโดยอ้างอิง CSS selectors ซึ่งมีประโยชน์หากคุณต้องการรวบรวมข้อมูลที่มีโครงสร้างจากเว็บไซต์ (web-scraping)

### HTML Exercise

มาลองดึง title ของโพสต์ล่าสุดในบล็อก n8n กัน:

1. ใช้ **HTTP Request node** เพื่อส่ง GET request ไปยัง URL `https://blog.n8n.io/` (endpoint นี้ไม่ต้องใช้ authentication)
2. เชื่อมต่อ **HTML node** และกำหนดค่าให้ดึง title ของโพสต์แรกบนหน้าเว็บ
	- คำใบ้: หากคุณไม่คุ้นเคยกับ CSS selectors หรือการอ่าน HTML, CSS selector `.post .item-title  a` น่าจะช่วยได้!

??? note "Show me the solution"

	1. กำหนดค่า HTTP Request node ด้วย parameters ต่อไปนี้:
		- **Authentication**: None
		- **Request Method**: GET
		- **URL**: https://blog.n8n.io/
	ผลลัพธ์ควรมีลักษณะดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-two/exercise_html_httprequestnode.png" alt="Result of HTTP Request node" style="width:100%"><figcaption align = "center"><i>Result of HTTP Request node</i></figcaption></figure>

	2. เชื่อมต่อ **HTML node** เข้ากับ **HTTP Request node** และกำหนดค่า parameters ของ HTML node ดังนี้:
		- **Operation**: Extract HTML Content
		- **Source Data**: JSON
		- **JSON Property**: data
		- **Extraction Values**:
			- **Key**: title
			- **CSS Selector**: `.post .item-title  a`
			- **Return Value**: HTML

	คุณสามารถเพิ่ม values เพิ่มเติมเพื่อดึงข้อมูลอื่นๆ ได้

	ผลลัพธ์ควรมีลักษณะดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-two/exercise_html_htmlextractnode.png" alt="Result of HTML Extract node" style="width:100%"><figcaption align = "center"><i>Result of HTML Extract node</i></figcaption></figure>


ใช้ **XML node** เพื่อแปลง XML เป็น JSON และ JSON เป็น XML การดำเนินการนี้มีประโยชน์หากคุณทำงานกับ web services ต่างๆ ที่ใช้ XML หรือ JSON และต้องการรับและส่งข้อมูลระหว่างกันในสองรูปแบบนี้

### XML Exercise

ใน [final exercise of Chapter 1](/courses/level-two/chapter-1.md#exercise_2) คุณได้ใช้ **HTTP Request node** เพื่อส่ง request ไปยัง PokéAPI ในแบบฝึกหัดนี้ เราจะกลับไปที่ API เดิม แต่เราจะแปลง output เป็น XML:

1. เพิ่ม **HTTP Request node** ที่ส่ง request เดิมไปยัง PokéAPI ที่ `https://pokeapi.co/api/v2/pokemon`
2. ใช้ XML node เพื่อแปลง JSON output เป็น XML

??? note "Show me the solution"

	1. หากต้องการรับ pokemon จาก PokéAPI ให้ execute **HTTP Request node** ด้วย parameters ต่อไปนี้:
		- **Authentication**: None
		- **Request Method**: GET
		- **URL**: https://pokeapi.co/api/v2/pokemon
	2. เชื่อมต่อ **XML node** เข้ากับมันด้วย parameters ต่อไปนี้:
		- **Mode**: JSON to XML
		- **Property name**: data

	ผลลัพธ์ควรมีลักษณะดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-two/exercise_html_xmlnode_table.png" alt="Table view of XML Node (JSON to XML)" style="width:100%"><figcaption align = "center"><i>XML node (JSON to XML) – Table View</i></figcaption></figure>

	หากต้องการแปลงข้อมูลในทิศทางตรงกันข้าม ให้เลือก mode **XML to JSON**


## Date, time, and interval data

ประเภทข้อมูล Date และ time รวมถึง `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, และ `YEAR` วันที่และเวลาสามารถส่งผ่านในรูปแบบต่างๆ ได้ ตัวอย่างเช่น:
<!-- vale off -->
- `DATE`: March 29 2022, 29-03-2022, 2022/03/29
- `TIME`: 08:30:00, 8:30, 20:30
- `DATETIME`: 2022/03/29 08:30:00
- `TIMESTAMP`: 1616108400 (Unix timestamp), 1616108400000 (Unix ms timestamp)
- `YEAR`: 2022, 22
<!-- vale on -->
มีสองสามวิธีที่คุณสามารถทำงานกับวันที่และเวลาได้:

- ใช้ [**Date & Time node**](/integrations/builtin/core-nodes/n8n-nodes-base.datetime.md) เพื่อแปลงข้อมูลวันที่และเวลาเป็นรูปแบบต่างๆ และคำนวณวันที่
- ใช้ [**Schedule Trigger node**](/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/index.md) เพื่อกำหนดเวลาให้ workflows ทำงานในเวลา, ช่วงเวลา, หรือระยะเวลาที่ระบุ

บางครั้ง คุณอาจต้องหยุดการ execute workflow ชั่วคราว ซึ่งอาจจำเป็นหากคุณรู้ว่า service ไม่ได้ประมวลผลข้อมูลทันที หรือใช้เวลานานในการคืนผลลัพธ์ทั้งหมด ในกรณีเหล่านี้ คุณไม่ต้องการให้ n8n ส่งข้อมูลที่ไม่สมบูรณ์ไปยัง node ถัดไป

หากคุณเจอกับสถานการณ์เช่นนี้ ให้ใช้ [**Wait node**](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md) หลังจาก node ที่คุณต้องการหน่วงเวลา **Wait node** จะหยุดการ execute workflow ชั่วคราวและจะกลับมาทำงานต่อ:

- ณ เวลาที่ระบุ
- หลังจากช่วงเวลาที่ระบุ
- เมื่อมีการเรียก webhook



### Date Exercise

สร้าง workflow ที่เพิ่มห้าวันให้กับ input date จาก Customer Datastore node ที่คุณเคยใช้ก่อนหน้านี้ จากนั้น หากวันที่ที่คำนวณได้เกิดขึ้นหลังปี 1959 workflow จะรอ 1 นาทีก่อนที่จะ [setting](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) วันที่ที่คำนวณได้เป็น value workflow ควรถูก trigger ทุกๆ 30 นาที


ในการเริ่มต้น:
<!-- To do: need to figure out what the actual desired output is here since Date & Time options have changed and I'm unclear what the Set node should be doing-->
1. เพิ่ม **Customer Datastore (n8n training) node** โดยเลือก action **Get All People** Return All
2. เพิ่ม **Date & Time node** เพื่อ Round Up วันที่ created จาก datastore เป็น End of Month ส่ง output นี้ไปยัง field new-date รวม input fields ทั้งหมด
3. เพิ่ม **If node** เพื่อตรวจสอบว่าวันที่ที่ปัดเศษใหม่นั้นอยู่หลัง `1960-01-01 00:00:00` หรือไม่
4. เพิ่ม **Wait node** ไปยัง True output ของ node นั้นและตั้งค่าให้รอหนึ่งนาที
5. เพิ่ม **Edit Fields (Set) node** เพื่อตั้งค่า field ใหม่ชื่อ outputValue เป็น String ที่มี new-date รวม input fields ทั้งหมด
6. เพิ่ม **Schedule Trigger node** ที่จุดเริ่มต้นของ workflow เพื่อ trigger ทุกๆ 30 นาที (คุณสามารถเก็บ [Manual Trigger node](/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md) ไว้สำหรับการทดสอบได้!)

??? note "Show me the solution"

	1. เพิ่ม **Customer Datastore (n8n training) node** โดยเลือก action **Get All People**
		- เลือก option **Return All**
	2. เพิ่ม **Date & Time node** ที่เชื่อมต่อกับ Customer Datastore node เลือก option **Round a Date**
		- เพิ่ม `created` date เป็น **Date** ที่จะปัดเศษ
		- เลือก `Round Up` เป็น **Mode** และ `End of Month` เป็น **To**
		- ตั้งค่า **Output Field Name** เป็น `new-date`
		- ใน **Options** เลือก **Add Option** และใช้ control เพื่อ **Include Input Fields**
	3. เพิ่ม **If node** ที่เชื่อมต่อกับ **Date & Time node**
		- เพิ่ม field new-date เป็นส่วนแรกของ condition
		- ตั้งค่า comparison เป็น **Date &Time > is after**
		- เพิ่ม `1960-01-01 00:00:00` เป็นส่วนที่สองของ expression (ควรจะได้ 3 items ใน True Branch และ 2 items ใน False Branch)
	4. เพิ่ม **Wait node** ไปยัง True output ของ **If node**
		- ตั้งค่า **Resume** เป็น `After Time interval`
		- ตั้งค่า **Wait Amount** เป็น `1.00`
		- ตั้งค่า **Wait Unit** เป็น `Minutes`
	5. เพิ่ม **Edit Fields (Set) node** ไปยัง **Wait node**
		- ใช้ **Mode** เป็น JSON หรือ Manual Mapping อย่างใดอย่างหนึ่ง
		- ตั้งค่า field ใหม่ชื่อ `outputValue` ให้เป็น value ของ field new-date
		- เลือก option **Include Other Input Fields** และ include **All** fields
	6. เพิ่ม **Schedule Trigger node** ที่จุดเริ่มต้นของ workflow
		- ตั้งค่า **Trigger Interval** ให้ใช้ `Minutes`
		- ตั้งค่า **Minutes Between Triggers** เป็น 30
		- หากต้องการทดสอบ schedule ของคุณ อย่าลืม activate workflow
		- อย่าลืมเชื่อมต่อ node นี้กับ **Customer Datastore (n8n training) node** ที่คุณเริ่มต้นด้วย!

	workflow ควรมีลักษณะดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-two/exercise_datetime.png" alt="Workflow for transforming dates" style="width:100%"><figcaption align = "center"><i>Workflow for transforming dates</i></figcaption></figure>

	หากต้องการตรวจสอบการกำหนดค่าของแต่ละ node คุณสามารถคัดลอกโค้ด JSON ของ workflow นี้และวางลงใน Editor UI หรือบันทึกเป็นไฟล์และ import จากไฟล์ลงใน workflow ใหม่ ดู [Export and import workflows](/workflows/export-import.md) สำหรับข้อมูลเพิ่มเติม

	```json
	{
	"name": "Course 2, Ch 2, Date exercise",
	"nodes": [
		{
		"parameters": {},
		"id": "6bf64d5c-4b00-43cf-8439-3cbf5e5f203b",
		"name": "When clicking \"Test workflow\"",
		"type": "n8n-nodes-base.manualTrigger",
		"typeVersion": 1,
		"position": [
			620,
			280
		]
		},
		{
		"parameters": {
			"operation": "getAllPeople",
			"returnAll": true
		},
		"id": "a08a8157-99ee-4d50-8fe4-b6d7e16e858e",
		"name": "Customer Datastore (n8n training)",
		"type": "n8n-nodes-base.n8nTrainingCustomerDatastore",
		"typeVersion": 1,
		"position": [
			840,
			360
		]
		},
		{
		"parameters": {
			"operation": "roundDate",
			"date": "={{ $json.created }}",
			"mode": "roundUp",
			"outputFieldName": "new-date",
			"options": {
			"includeInputFields": true
			}
		},
		"id": "f66a4356-2584-44b6-a4e9-1e3b5de53e71",
		"name": "Date & Time",
		"type": "n8n-nodes-base.dateTime",
		"typeVersion": 2,
		"position": [
			1080,
			360
		]
		},
		{
		"parameters": {
			"conditions": {
			"options": {
				"caseSensitive": true,
				"leftValue": "",
				"typeValidation": "strict"
			},
			"conditions": [
				{
				"id": "7c82823a-e603-4166-8866-493f643ba354",
				"leftValue": "={{ $json['new-date'] }}",
				"rightValue": "1960-01-01T00:00:00",
				"operator": {
					"type": "dateTime",
					"operation": "after"
				}
				}
			],
			"combinator": "and"
			},
			"options": {}
		},
		"id": "cea39877-6183-4ea0-9400-e80523636912",
		"name": "If",
		"type": "n8n-nodes-base.if",
		"typeVersion": 2,
		"position": [
			1280,
			360
		]
		},
		{
		"parameters": {
			"amount": 1,
			"unit": "minutes"
		},
		"id": "5aa860b7-c73c-4df0-ad63-215850166f13",
		"name": "Wait",
		"type": "n8n-nodes-base.wait",
		"typeVersion": 1.1,
		"position": [
			1480,
			260
		],
		"webhookId": "be78732e-787d-463e-9210-2c7e8239761e"
		},
		{
		"parameters": {
			"assignments": {
			"assignments": [
				{
				"id": "e058832a-2461-4c6d-b584-043ecc036427",
				"name": "outputValue",
				"value": "={{ $json['new-date'] }}",
				"type": "string"
				}
			]
			},
			"includeOtherFields": true,
			"options": {}
		},
		"id": "be034e9e-3cf1-4264-9d15-b6760ce28f91",
		"name": "Edit Fields",
		"type": "n8n-nodes-base.set",
		"typeVersion": 3.3,
		"position": [
			1700,
			260
		]
		},
		{
		"parameters": {
			"rule": {
			"interval": [
				{
				"field": "minutes",
				"minutesInterval": 30
				}
			]
			}
		},
		"id": "6e8e4308-d0e0-4d0d-bc29-5131b57cf061",
		"name": "Schedule Trigger",
		"type": "n8n-nodes-base.scheduleTrigger",
		"typeVersion": 1.1,
		"position": [
			620,
			480
		]
		}
	],
	"pinData": {},
	"connections": {
		"When clicking \"Test workflow\"": {
		"main": [
			[
			{
				"node": "Customer Datastore (n8n training)",
				"type": "main",
				"index": 0
			}
			]
		]
		},
		"Customer Datastore (n8n training)": {
		"main": [
			[
			{
				"node": "Date & Time",
				"type": "main",
				"index": 0
			}
			]
		]
		},
		"Date & Time": {
		"main": [
			[
			{
				"node": "If",
				"type": "main",
				"index": 0
			}
			]
		]
		},
		"If": {
		"main": [
			[
			{
				"node": "Wait",
				"type": "main",
				"index": 0
			}
			]
		]
		},
		"Wait": {
		"main": [
			[
			{
				"node": "Edit Fields",
				"type": "main",
				"index": 0
			}
			]
		]
		},
		"Schedule Trigger": {
		"main": [
			[
			{
				"node": "Customer Datastore (n8n training)",
				"type": "main",
				"index": 0
			}
			]
		]
		}
	}
	}
	```


## Binary data

จนถึงตอนนี้ คุณได้ทำงานกับข้อมูล text เป็นหลัก แต่ถ้าคุณต้องการประมวลผลข้อมูลที่ไม่ใช่ text เช่น รูปภาพหรือไฟล์ PDF ล่ะ? ไฟล์ประเภทนี้จะถูกแสดงในระบบเลขฐานสอง ดังนั้นจึงถือว่าเป็น binary data ในรูปแบบนี้ binary data ไม่ได้ให้ข้อมูลที่เป็นประโยชน์แก่คุณ ดังนั้นคุณจะต้องแปลงให้อยู่ในรูปแบบที่อ่านได้

ใน n8n คุณสามารถประมวลผล binary data ด้วย nodes ต่อไปนี้:

- [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) เพื่อ request และส่งไฟล์จาก/ไปยัง web resources และ APIs
- [Read/Write Files from Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) เพื่ออ่านและเขียนไฟล์จาก/ไปยังเครื่องที่ n8n กำลังทำงานอยู่
- [Convert to File](/integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md) เพื่อรับ input data และส่ง output เป็นไฟล์
- [Extract From File](/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md) เพื่อรับข้อมูลจากรูปแบบ binary และแปลงเป็น JSON

/// note | Reading and writing files is only available on self-hosted n8n
การอ่านและเขียนไฟล์ไปยัง disk ไม่สามารถใช้งานได้บน n8n Cloud คุณจะอ่านและเขียนไปยังเครื่องที่คุณติดตั้ง n8n หากคุณรัน n8n ใน Docker คำสั่งของคุณจะทำงานใน n8n container ไม่ใช่ Docker host Read/Write Files From Disk node จะมองหาไฟล์ที่สัมพันธ์กับ n8n install path n8n แนะนำให้ใช้ absolute file paths เพื่อป้องกันข้อผิดพลาดใดๆ
///

ในการอ่านหรือเขียน binary file คุณต้องเขียน path (ตำแหน่ง) ของไฟล์ใน parameter `File(s) Selector` ของ node (สำหรับการดำเนินการ Read) หรือใน parameter `File Path and Name` ของ node (สำหรับการดำเนินการ Write)

/// warning | Naming the right path
file path จะดูแตกต่างกันเล็กน้อยขึ้นอยู่กับว่าคุณกำลังรัน n8n อย่างไร:

- npm: `~/my_file.json`
- n8n cloud / Docker: `/tmp/my_file.json`
///



### Binary Exercise 1

สำหรับแบบฝึกหัด binary แรกของเรา มาแปลงไฟล์ PDF เป็น JSON กัน:

1. ส่ง HTTP request เพื่อรับไฟล์ PDF นี้: `https://media.kaspersky.com/pdf/Kaspersky_Lab_Whitepaper_Anti_blocker.pdf.`
2. ใช้ **Extract From File node** เพื่อแปลงไฟล์จาก binary เป็น JSON

??? note "Show me the solution"

	ใน **HTTP Request node** คุณควรเห็นไฟล์ PDF ดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-two/exercise_binarydata_httprequest_file.png" alt="HTTP Request node to get PDF" style="width:100%"><figcaption align = "center"><i>HTTP Request node to get PDF</i></figcaption></figure>

	เมื่อคุณแปลง PDF จาก binary เป็น JSON โดยใช้ **Extract From File node** ผลลัพธ์ควรมีลักษณะดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-two/exercise_binarydata_movedata_btoj.png" alt="Extract From File node" style="width:100%"><figcaption align = "center"><i>Extract From File node</i></figcaption></figure>

	หากต้องการตรวจสอบการกำหนดค่าของ nodes คุณสามารถคัดลอกโค้ด JSON workflow ด้านล่างและวางลงใน Editor UI ของคุณ:

	```json
	{
		"name": "Binary to JSON",
		"nodes": [
			{
			"parameters": {},
			"id": "78639a25-b69a-4b9c-84e0-69e045bed1a3",
			"name": "When clicking \"Execute Workflow\"",
			"type": "n8n-nodes-base.manualTrigger",
			"typeVersion": 1,
			"position": [
				480,
				520
			]
			},
			{
			"parameters": {
				"url": "https://media.kaspersky.com/pdf/Kaspersky_Lab_Whitepaper_Anti_blocker.pdf",
				"options": {}
			},
			"id": "a11310df-1287-4e9a-b993-baa6bd4265a6",
			"name": "HTTP Request",
			"type": "n8n-nodes-base.httpRequest",
			"typeVersion": 4.1,
			"position": [
				700,
				520
			]
			},
			{
			"parameters": {
				"operation": "pdf",
				"options": {}
			},
			"id": "88697b6b-fb02-4c3d-a715-750d60413e9f",
			"name": "Extract From File",
			"type": "n8n-nodes-base.extractFromFile",
			"typeVersion": 1,
			"position": [
				920,
				520
			]
			}
		],
		"pinData": {},
		"connections": {
			"When clicking \"Execute Workflow\"": {
			"main": [
				[
				{
					"node": "HTTP Request",
					"type": "main",
					"index": 0
				}
				]
			]
			},
			"HTTP Request": {
			"main": [
				[
				{
					"node": "Extract From File",
					"type": "main",
					"index": 0
				}
				]
			]
			}
		}
	}
	```



### Binary Exercise 2

สำหรับแบบฝึกหัด binary ที่สองของเรา มาแปลงข้อมูล JSON บางส่วนเป็น binary กัน:

1. ส่ง HTTP request ไปยัง Poetry DB API `https://poetrydb.org/random/1`
2. แปลงข้อมูลที่ส่งคืนจาก JSON เป็น binary โดยใช้ **Convert to File node**
3. เขียนข้อมูล binary file ใหม่ไปยังเครื่องที่ n8n กำลังทำงานอยู่โดยใช้ **Read/Write Files From Disk node**
4. หากต้องการตรวจสอบว่าทำงานได้หรือไม่ ให้ใช้ **Read/Write Files From Disk node** เพื่ออ่าน binary file ที่สร้างขึ้น

??? note "Show me the solution"

	workflow สำหรับแบบฝึกหัดนี้มีลักษณะดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-two/exercise_binarydata.png" alt="Workflow for moving JSON to binary data" style="width:100%"><figcaption align = "center"><i>Workflow for moving JSON to binary data</i></figcaption></figure>

	หากต้องการตรวจสอบการกำหนดค่าของ nodes คุณสามารถคัดลอกโค้ด JSON workflow ด้านล่างและวางลงใน Editor UI ของคุณ:

	```json
	{
		"name": "JSON to file and Read-Write",
		"nodes": [
			{
			"parameters": {},
			"id": "78639a25-b69a-4b9c-84e0-69e045bed1a3",
			"name": "When clicking \"Execute Workflow\"",
			"type": "n8n-nodes-base.manualTrigger",
			"typeVersion": 1,
			"position": [
				480,
				520
			]
			},
			{
			"parameters": {
				"url": "https://poetrydb.org/random/1",
				"options": {}
			},
			"id": "a11310df-1287-4e9a-b993-baa6bd4265a6",
			"name": "HTTP Request",
			"type": "n8n-nodes-base.httpRequest",
			"typeVersion": 4.1,
			"position": [
				680,
				520
			]
			},
			{
			"parameters": {
				"operation": "toJson",
				"options": {}
			},
			"id": "06be18f6-f193-48e2-a8d9-35f4779d8324",
			"name": "Convert to File",
			"type": "n8n-nodes-base.convertToFile",
			"typeVersion": 1,
			"position": [
				880,
				520
			]
			},
			{
			"parameters": {
				"operation": "write",
				"fileName": "/tmp/poetrydb.json",
				"options": {}
			},
			"id": "f2048e5d-fa8f-4708-b15a-d07de359f2e5",
			"name": "Read/Write Files from Disk",
			"type": "n8n-nodes-base.readWriteFile",
			"typeVersion": 1,
			"position": [
				1080,
				520
			]
			},
			{
			"parameters": {
				"fileSelector": "={{ $json.fileName }}",
				"options": {}
			},
			"id": "d630906c-09d4-49f4-ba14-416c0f4de1c8",
			"name": "Read/Write Files from Disk1",
			"type": "n8n-nodes-base.readWriteFile",
			"typeVersion": 1,
			"position": [
				1280,
				520
			]
			}
		],
		"pinData": {},
		"connections": {
			"When clicking \"Execute Workflow\"": {
			"main": [
				[
				{
					"node": "HTTP Request",
					"type": "main",
					"index": 0
				}
				]
			]
			},
			"HTTP Request": {
			"main": [
				[
				{
					"node": "Convert to File",
					"type": "main",
					"index": 0
				}
				]
			]
			},
			"Convert to File": {
			"main": [
				[
				{
					"node": "Read/Write Files from Disk",
					"type": "main",
					"index": 0
				}
				]
			]
			},
			"Read/Write Files from Disk": {
			"main": [
				[
				{
					"node": "Read/Write Files from Disk1",
					"type": "main",
					"index": 0
				}
				]
			]
			}
		}
	}
	```
