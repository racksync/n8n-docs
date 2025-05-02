---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Merging and splitting data

ในบทนี้ คุณจะได้เรียนรู้วิธีการรวม (merge) และแบ่ง (split) ข้อมูล และในกรณีใดบ้างที่อาจเป็นประโยชน์ในการดำเนินการเหล่านี้


## Merging data

ในบางกรณี คุณอาจต้องรวม (combine) และประมวลผลข้อมูลจากแหล่งต่างๆ

การรวมข้อมูลอาจเกี่ยวข้องกับ:

- การสร้าง data set หนึ่งชุดจากหลายแหล่ง
- การซิงโครไนซ์ข้อมูลระหว่างหลายระบบ ซึ่งอาจรวมถึงการลบข้อมูลที่ซ้ำซ้อน หรือการอัปเดตข้อมูลในระบบหนึ่งเมื่อมีการเปลี่ยนแปลงในอีกระบบหนึ่ง

/// note | One-way vs. two-way sync
ในการซิงค์แบบ one-way ข้อมูลจะถูกซิงโครไนซ์ในทิศทางเดียว ระบบหนึ่งทำหน้าที่เป็น single source of truth เมื่อข้อมูลในระบบหลักนั้นเปลี่ยนแปลง มันจะเปลี่ยนแปลงในระบบรองโดยอัตโนมัติ แต่ถ้าข้อมูลในระบบรองเปลี่ยนแปลง การเปลี่ยนแปลงนั้นจะไม่สะท้อนในระบบหลัก

ในการซิงค์แบบ two-way ข้อมูลจะถูกซิงโครไนซ์ทั้งสองทิศทาง (ระหว่างทั้งสองระบบ) เมื่อข้อมูลในระบบใดระบบหนึ่งเปลี่ยนแปลง มันจะเปลี่ยนแปลงในอีกระบบหนึ่งโดยอัตโนมัติเช่นกัน

[This blog tutorial](https://blog.n8n.io/how-to-sync-data-between-two-systems/) อธิบายวิธีการซิงค์ข้อมูลแบบ one-way และ two-way ระหว่าง CRM สองระบบ
///


ใน n8n คุณสามารถรวมข้อมูลจากสอง nodes ที่แตกต่างกันโดยใช้ [Merge node](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md){:target="_blank"} ซึ่งมีตัวเลือกการรวมหลายแบบ:

- [Append](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md#append){:target="_blank"}
- [Combine](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md#combine){:target="_blank"}
	- [Merge by Fields](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md#combine-by-matching-fields){:target="_blank"}: ต้องการ input fields ที่จะใช้จับคู่
	- [Merge by Position](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md#combine-by-position){:target="_blank"}
	- [Combine all possible combinations](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md#combine-by-all-possible-combinations){:target="_blank"}
- [Choose Branch](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md#choose-branch){:target="_blank"}

สังเกตว่า Combine > Merge by Fields ต้องการให้คุณป้อน input fields เพื่อใช้จับคู่ fields เหล่านี้ควรมีค่าที่เหมือนกันระหว่าง data sources เพื่อให้ n8n สามารถจับคู่ข้อมูลได้อย่างถูกต้อง ใน **Merge node** จะเรียกว่า `Input 1 Field` และ `Input 2 Field`

<figure><img src="/_images/courses/level-two/chapter-three/explanation_mergepropertyinput.png" alt="Property Input fields in the Merge node" style="width:100%"><figcaption align = "center"><i>Property Input fields in the Merge node</i></figcaption></figure>

/// warning | Property Input in dot notation
หากคุณต้องการอ้างอิงค่าที่ซ้อนกัน (nested values) ใน parameters `Input 1 Field` และ `Input 2 Field` ของ **Merge node** คุณต้องป้อน property key ในรูปแบบ dot-notation (เป็น text ไม่ใช่ expression)
///

/// note
คุณยังสามารถค้นหา **Merge node** ได้ภายใต้ชื่อ alias ว่า Join ซึ่งอาจจะเข้าใจง่ายกว่าหากคุณคุ้นเคยกับ SQL joins
///

### Merge Exercise

สร้าง workflow ที่รวมข้อมูลจาก Customer Datastore node และ Code node

1. เพิ่ม **Merge node** ที่รับ `Input 1` จาก **Customer Datastore node** และ `Input 2` จาก **Code node**
2. ใน **Customer Datastore node** ให้รัน operation **Get All People**
3. ใน **Code node** ให้สร้าง array ของสอง objects ที่มีสาม properties: `name`, `language`, และ `country` โดยที่ property `country` มีสอง sub-properties คือ `code` และ `name`
	- กรอกค่าของ properties เหล่านี้ด้วยข้อมูลของตัวละครสองตัวจาก Customer Database
	- ตัวอย่างเช่น ภาษาของ Jay Gatsby คือ English และชื่อประเทศคือ United States
4. ใน **Merge node** ให้ลองใช้ merge options ต่างๆ

??? note "Show me the solution"

	workflow สำหรับแบบฝึกหัดนี้มีลักษณะดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-three/exercise_merge.png" alt="Workflow exercise for merging data" style="width:100%"><figcaption align = "center"><i>Workflow exercise for merging data</i></figcaption></figure>

	หากคุณรวมข้อมูลด้วย option **Keep Matches** โดยใช้ name เป็น input fields เพื่อจับคู่ ผลลัพธ์ควรมีลักษณะดังนี้ (โปรดทราบว่าตัวอย่างนี้มีเพียง Jay Gatsby; ของคุณอาจดูแตกต่างกันไปขึ้นอยู่กับตัวละครที่คุณเลือก):

	<figure><img src="/_images/courses/level-two/chapter-three/exercise_merge_kkm.png" alt="Output of Merge node with option to keep matches" style="width:100%"><figcaption align = "center"><i>Output of Merge node with option to keep matches</i></figcaption></figure>

	หากต้องการตรวจสอบการกำหนดค่าของ nodes คุณสามารถคัดลอกโค้ด JSON workflow ด้านล่างและวางลงใน Editor UI ของคุณ:

	```json
	{
	"meta": {
		"templateCredsSetupCompleted": true,
		"instanceId": "cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7"
	},
	"nodes": [
		{
		"parameters": {
			"mode": "combine",
			"mergeByFields": {
			"values": [
				{
				"field1": "name",
				"field2": "name"
				}
			]
			},
			"options": {}
		},
		"id": "578365f3-26dd-4fa6-9858-f0a5fdfc413b",
		"name": "Merge",
		"type": "n8n-nodes-base.merge",
		"typeVersion": 2.1,
		"position": [
			720,
			580
		]
		},
		{
		"parameters": {},
		"id": "71aa5aad-afdf-4f8a-bca0-34450eee8acc",
		"name": "When clicking \"Test workflow\"",
		"type": "n8n-nodes-base.manualTrigger",
		"typeVersion": 1,
		"position": [
			260,
			560
		]
		},
		{
		"parameters": {
			"operation": "getAllPeople"
		},
		"id": "497174fe-3cab-4160-8103-78b44efd038d",
		"name": "Customer Datastore (n8n training)",
		"type": "n8n-nodes-base.n8nTrainingCustomerDatastore",
		"typeVersion": 1,
		"position": [
			500,
			460
		]
		},
		{
		"parameters": {
			"jsCode": "return [\n  {\n    'name': 'Jay Gatsby',\n    'language': 'English',\n    'country': {\n      'code': 'US',\n      'name': 'United States'\n    }\n    \n  }\n  \n];"
		},
		"id": "387e8a1e-e796-4f05-8e75-7ce25c786c5f",
		"name": "Code",
		"type": "n8n-nodes-base.code",
		"typeVersion": 2,
		"position": [
			500,
			720
		]
		}
	],
	"connections": {
		"When clicking \"Test workflow\"": {
		"main": [
			[
			{
				"node": "Customer Datastore (n8n training)",
				"type": "main",
				"index": 0
			},
			{
				"node": "Code",
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
				"node": "Merge",
				"type": "main",
				"index": 0
			}
			]
		]
		},
		"Code": {
		"main": [
			[
			{
				"node": "Merge",
				"type": "main",
				"index": 1
			}
			]
		]
		}
	},
	"pinData": {}
	}
	```


## Looping

ในบางกรณี คุณอาจต้องดำเนินการเดียวกันกับแต่ละ element ของ array หรือแต่ละ data item (เช่น การส่งข้อความไปยังทุก contact ใน address book ของคุณ) ในทางเทคนิค คุณต้อง iterate ผ่านข้อมูล (ด้วย loops)

โดยทั่วไป n8n จะจัดการกับการประมวลผลซ้ำๆ นี้โดยอัตโนมัติ เนื่องจาก nodes จะทำงานหนึ่งครั้งสำหรับแต่ละ item ดังนั้นคุณไม่จำเป็นต้องสร้าง loops ใน workflows ของคุณ

อย่างไรก็ตาม มี [exceptions ของ nodes และ operations](/flow-logic/looping.md#node-exceptions){:target="_blank"} บางอย่างที่จะต้องให้คุณสร้าง loop ใน workflow ของคุณ

ในการ [create a loop in an n8n workflow](/flow-logic/looping.md#using-loops-in-n8n){:target="_blank"} คุณต้องเชื่อมต่อ output ของ node หนึ่งไปยัง input ของ node ก่อนหน้า และเพิ่ม **If node** เพื่อตรวจสอบว่าจะหยุด loop เมื่อใด

## Splitting data in batches

หากคุณต้องการประมวลผลข้อมูลขาเข้าจำนวนมาก, execute **Code node** หลายครั้ง, หรือหลีกเลี่ยง API rate limits วิธีที่ดีที่สุดคือการแบ่งข้อมูลออกเป็น batches (กลุ่ม) และประมวลผล batches เหล่านี้

สำหรับกระบวนการเหล่านี้ ให้ใช้ [**Loop Over Items node**](/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md){:target="_blank"} node นี้จะแบ่งข้อมูล input ออกเป็น batch size ที่ระบุ และในแต่ละ iteration จะคืนค่าข้อมูลตามจำนวนที่กำหนดไว้ล่วงหน้า

/// warning | Execution of Loop Over Items node
**Loop Over Items node** จะหยุด executing หลังจากที่ items ขาเข้าทั้งหมดถูกแบ่งออกเป็น batches และส่งต่อไปยัง node ถัดไปใน workflow ดังนั้นจึงไม่จำเป็นต้องเพิ่ม **If node** เพื่อหยุด loop
///

### Loop/Batch Exercise

สร้าง workflow ที่อ่าน RSS feed จาก Medium และ dev.to workflow ควรประกอบด้วยสาม nodes:

1. **Code node** ที่คืนค่า URLs ของ RSS feeds ของ Medium (`https://medium.com/feed/n8n-io`) และ dev.to (`https://dev.to/feed/n8n`)
2. **Loop Over Items node** ที่มี `Batch Size: 1` ซึ่งรับ inputs จาก **Code node** และ **RSS Read node** และ iterates เหนือ items
3. **RSS Read node** ที่รับ URL ของ Medium RSS feed ซึ่งส่งผ่านเป็น expression: `{{ $json.url }}`
	- **RSS Read node** เป็นหนึ่งใน [exception nodes](/flow-logic/looping.md#node-exceptions){:target="_blank"} ซึ่งประมวลผลเฉพาะ item แรกที่ได้รับ ดังนั้น **Loop Over Items node** จึงจำเป็นสำหรับการ iterating เหนือ multiple items

??? note "Show me the solution"

	1. เพิ่ม **Code Node** คุณสามารถจัดรูปแบบโค้ดได้หลายวิธี วิธีหนึ่งคือ:
		- ตั้งค่า **Mode** เป็น `Run Once for All Items`
		- ตั้งค่า **Language** เป็น `JavaScript`
		- คัดลอกโค้ดด้านล่างและวางลงใน JavaScript Code editor:
			```javascript
			let urls = [
				{
					json: {
					url: 'https://medium.com/feed/n8n-io'
					}
				},
				{
				json: {
					url: 'https://dev.to/feed/n8n'
					} 
				}
			]
			return urls;
			```
	2. เพิ่ม **Loop Over Items node** ที่เชื่อมต่อกับ **Code node**
		- ตั้งค่า **Batch Size** เป็น `1`
	3. **Loop Over Items node** จะเพิ่ม node ที่ชื่อ "Replace Me" โดยอัตโนมัติ ให้แทนที่ node นั้นด้วย **RSS Read node**
		- ตั้งค่า **URL** ให้ใช้ url จาก Code Node: `{{ $json.url }}`
	
	workflow สำหรับแบบฝึกหัดนี้มีลักษณะดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-three/exercise_splitinbatches.png" alt="Workflow for getting RSS feeds from two blogs" style="width:100%"><figcaption align = "center"><i>Workflow for getting RSS feeds from two blogs</i></figcaption></figure>

	หากต้องการตรวจสอบการกำหนดค่าของ nodes คุณสามารถคัดลอกโค้ด JSON workflow ด้านล่างและวางลงใน Editor UI ของคุณ:

	```json
	{
	"meta": {
		"templateCredsSetupCompleted": true,
		"instanceId": "cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7"
	},
	"nodes": [
		{
		"parameters": {},
		"id": "ed8dc090-ae8c-4db6-a93b-0fa873015c25",
		"name": "When clicking \"Test workflow\"",
		"type": "n8n-nodes-base.manualTrigger",
		"typeVersion": 1,
		"position": [
			460,
			460
		]
		},
		{
		"parameters": {
			"jsCode": "let urls = [\n  {\n    json: {\n      url: 'https://medium.com/feed/n8n-io'\n    }\n  },\n  {\n   json: {\n     url: 'https://dev.to/feed/n8n'\n   } \n  }\n]\n\nreturn urls;"
		},
		"id": "1df2a9bf-f970-4e04-b906-92dbbc9e8d3a",
		"name": "Code",
		"type": "n8n-nodes-base.code",
		"typeVersion": 2,
		"position": [
			680,
			460
		]
		},
		{
		"parameters": {
			"options": {}
		},
		"id": "3cce249a-0eab-42e2-90e3-dbdf3684e012",
		"name": "Loop Over Items",
		"type": "n8n-nodes-base.splitInBatches",
		"typeVersion": 3,
		"position": [
			900,
			460
		]
		},
		{
		"parameters": {
			"url": "={{ $json.url }}",
			"options": {}
		},
		"id": "50e1c1dc-9a5d-42d3-b7c0-accc31636aa6",
		"name": "RSS Read",
		"type": "n8n-nodes-base.rssFeedRead",
		"typeVersion": 1,
		"position": [
			1120,
			460
		]
		}
	],
	"connections": {
		"When clicking \"Test workflow\"": {
		"main": [
			[
			{
				"node": "Code",
				"type": "main",
				"index": 0
			}
			]
		]
		},
		"Code": {
		"main": [
			[
			{
				"node": "Loop Over Items",
				"type": "main",
				"index": 0
			}
			]
		]
		},
		"Loop Over Items": {
		"main": [
			null,
			[
			{
				"node": "RSS Read",
				"type": "main",
				"index": 0
			}
			]
		]
		},
		"RSS Read": {
		"main": [
			[
			{
				"node": "Loop Over Items",
				"type": "main",
				"index": 0
			}
			]
		]
		}
	},
	"pinData": {}
	}
	```
