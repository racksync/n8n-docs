---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Understanding the data structure

ในบทนี้ คุณจะได้เรียนรู้เกี่ยวกับโครงสร้างข้อมูล (data structure) ของ n8n และวิธีใช้ [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md){:target="_blank"} เพื่อแปลงข้อมูลและจำลอง output ของ node


## Data structure of n8n

โดยพื้นฐานแล้ว n8n nodes ทำหน้าที่เป็นเครื่องมือ Extract, Transform, Load (ETL) nodes ช่วยให้คุณเข้าถึง (extract) ข้อมูลจากแหล่งต่างๆ ที่หลากหลาย, แก้ไข (transform) ข้อมูลนั้นในลักษณะเฉพาะ, และส่งต่อ (load) ไปยังที่ที่ต้องการ

ข้อมูลที่เคลื่อนที่จาก node หนึ่งไปยังอีก node หนึ่งใน workflow ของคุณจะต้องอยู่ในรูปแบบ (โครงสร้าง) ที่แต่ละ node สามารถรับรู้และตีความได้ ใน n8n โครงสร้างที่ต้องการนี้คือ array of objects

/// note | About array of objects
Array คือรายการของค่าต่างๆ array อาจว่างเปล่าหรือมีหลาย elements ก็ได้ แต่ละ element จะถูกเก็บไว้ที่ตำแหน่ง (index) ในรายการ โดยเริ่มจาก 0 และสามารถอ้างอิงได้ด้วยหมายเลข index ตัวอย่างเช่น ใน array `["Leonardo", "Michelangelo", "Donatello", "Raphael"];` element `Donatello` ถูกเก็บไว้ที่ index 2

Object เก็บ key-value pairs แทนที่จะเป็นค่าที่ index ที่มีหมายเลขเหมือนใน arrays ลำดับของ pairs ไม่สำคัญ เนื่องจากสามารถเข้าถึงค่าได้โดยการอ้างอิงชื่อ key ตัวอย่างเช่น object ด้านล่างมีสอง properties (`name` และ `color`):

```json
{
	name: 'Michelangelo',
	color: 'blue',
}
```

Array of objects คือ array ที่มี object หนึ่งหรือหลาย object ตัวอย่างเช่น array `turtles` ด้านล่างมีสี่ objects:

```javascript
var turtles = [
	{
		name: 'Michelangelo',
		color: 'orange',
	},
	{
		name: 'Donatello',
		color: 'purple',
	},
	{
		name: 'Raphael',
		color: 'red',
	},
	{
		name: 'Leonardo',
		color: 'blue',
	}
];
```

คุณสามารถเข้าถึง properties ของ object โดยใช้ dot notation ด้วย syntax `object.property` ตัวอย่างเช่น `turtles[1].color` จะได้สีของเต่าตัวที่สอง
///


ข้อมูลที่ส่งจาก node หนึ่งไปยังอีก node หนึ่งจะถูกส่งเป็น array of JSON objects elements ใน collection นี้เรียกว่า items

<figure><img src="/_images/courses/level-two/chapter-one/explanation_items.png" alt="" style="width:100%"><figcaption align = "center"><i>Items</i></figcaption></figure>

n8n node จะดำเนินการกับแต่ละ item ของข้อมูลขาเข้า

<figure><img src="/_images/flow-logic/looping/customer_datastore_node.png"><figcaption align = "center"><i>Items in the Customer Datastore node</i></figcaption></figure>


## Creating data sets with the Code node

ตอนนี้คุณคุ้นเคยกับโครงสร้างข้อมูล n8n แล้ว คุณสามารถใช้มันเพื่อสร้าง data sets ของคุณเองหรือจำลอง node outputs ได้ ในการทำเช่นนี้ ให้ใช้ [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md){:target="_blank"} เพื่อเขียน JavaScript code กำหนด array of objects ของคุณด้วยโครงสร้างต่อไปนี้:

```javascript
return [
	{
		json: {
			apple: 'beets',
		}
	}
];
```

ตัวอย่างเช่น array of objects ที่แสดงถึง Ninja turtles จะมีลักษณะดังนี้ใน Code node:

<figure><img src="/_images/courses/level-two/chapter-one/exercise_function_notnested.png" alt="" style="width:100%"><figcaption align = "center"><i>Array of objects in the Code node</i></figcaption></figure>

/// warning | JSON objects
สังเกตว่า array of objects นี้มี key เพิ่มเติม: `json` n8n คาดหวังให้คุณห่อหุ้มแต่ละ object ใน array ด้วย object อีกอัน โดยมี key เป็น `json`

<figure><img src="/_images/courses/level-two/chapter-one/explanation_datastructure.png" alt="" style="width:100%"><figcaption align = "center"><i>Illustration of data structure in n8n</i></figcaption></figure>

เป็นแนวปฏิบัติที่ดีที่จะส่งข้อมูลในโครงสร้างที่ถูกต้องที่ n8n ใช้ แต่ไม่ต้องกังวลหากคุณลืมเพิ่ม `json` key ให้กับ item, n8n (เวอร์ชัน 0.166.0 ขึ้นไป) จะเพิ่มให้โดยอัตโนมัติ
///

คุณยังสามารถมี nested pairs ได้ ตัวอย่างเช่น หากคุณต้องการกำหนดสีหลักและสีรอง ในกรณีนี้ คุณต้องห่อหุ้ม key-value pairs เพิ่มเติมด้วยวงเล็บปีกกา `{}`

/// note | n8n data structure video
[This talk](https://www.youtube.com/watch?v=mQHT3Unn4tY) นำเสนอคำอธิบายโดยละเอียดเพิ่มเติมเกี่ยวกับโครงสร้างข้อมูลใน n8n

<iframe width="560" height="315" src="https://www.youtube.com/embed/mQHT3Unn4tY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
///


### Exercise

ใน Code node ให้สร้าง array of objects ชื่อ `myContacts` ที่มี properties `name` และ `email` และ property `email` ถูกแบ่งย่อยออกเป็น `personal` และ `work`

??? note "Show me the solution"

	ใน **Code node** ในช่อง JavaScript Code คุณต้องเขียนโค้ดต่อไปนี้:

	```javascript
	var myContacts = [
		{
			json: {
				name: 'Alice',
				email: {
					personal: 'alice@home.com',
					work: 'alice@wonderland.org'
				},
			}
		},
		{
			json: {
				name: 'Bob',
				email: {
					personal: 'bob@mail.com',
					work: 'contact@thebuilder.com'
					},
			}
		},
	];

	return myContacts;
	```

	เมื่อคุณ execute **Code node** ผลลัพธ์ควรมีลักษณะดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-one/exercise_function.png" alt="" style="width:100%"><figcaption align = "center"><i>Result of Code node</i></figcaption></figure>



## Referencing node data with the Code node

เช่นเดียวกับที่คุณสามารถใช้ [expressions](/code/expressions.md) เพื่ออ้างอิงข้อมูลจาก nodes อื่นๆ คุณยังสามารถใช้ [methods and variables](/code/builtin/overview.md) บางอย่างใน **Code node** ได้

โปรดตรวจสอบให้แน่ใจว่าคุณได้อ่านหน้าเหล่านี้ก่อนที่จะทำแบบฝึกหัดถัดไป

### Exercise

มาต่อยอดจากแบบฝึกหัดก่อนหน้านี้ ซึ่งคุณใช้ Code node เพื่อสร้าง data set ของสอง contacts พร้อมชื่อและอีเมลของพวกเขา ตอนนี้ เชื่อมต่อ Code node ที่สองเข้ากับ node แรก ใน node ใหม่ ให้เขียนโค้ดเพื่อสร้าง column ใหม่ชื่อ `workEmail` ที่อ้างอิงถึง work email ของ contact แรก

??? note "Show me the solution"
	ใน **Code node** ในช่อง JavaScript Code คุณต้องเขียนโค้ดต่อไปนี้:

	```javascript
	let items = $input.all();
	items[0].json.workEmail = items[0].json.email['work'];
	return items;
	```

	เมื่อคุณ execute **Code node** ผลลัพธ์ควรมีลักษณะดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-one/exercise_function_reference.png" alt="" style="width:100%"><figcaption align = "center"><i>Code node reference</i></figcaption></figure>


## Transforming data

ข้อมูลขาเข้าจากบาง nodes อาจมีโครงสร้างข้อมูลที่แตกต่างจากที่ใช้ใน n8n ในกรณีนี้ คุณต้อง [transform the data](/data/transforming-data.md){:target="_blank" .external} เพื่อให้แต่ละ item สามารถประมวลผลแยกกันได้

การดำเนินการที่พบบ่อยที่สุดสองอย่างสำหรับการแปลงข้อมูลคือ:

- การสร้าง multiple items จาก one item
- การสร้าง a single item จาก multiple items

มีหลายวิธีในการแปลงข้อมูลเพื่อวัตถุประสงค์ที่กล่าวถึงข้างต้น:

- ใช้ [data transformation nodes](/data/index.md#data-transformation-nodes) ของ n8n ใช้ nodes เหล่านี้เพื่อแก้ไขโครงสร้างของข้อมูลขาเข้าที่มี lists (arrays) โดยไม่จำเป็นต้องใช้ JavaScript code ใน **Code node**:
	- ใช้ [**Split Out node**](/integrations/builtin/core-nodes/n8n-nodes-base.splitout.md) เพื่อแยก data item เดียวที่มี list ออกเป็น multiple items
	- ใช้ [**Aggregate node**](/integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md) เพื่อนำ items แยกกัน หรือบางส่วนของมัน มารวมกลุ่มกันเป็น individual items
- ใช้ **Code node** เพื่อเขียน JavaScript functions เพื่อแก้ไขโครงสร้างข้อมูลของข้อมูลขาเข้าโดยใช้โหมด **Run Once for All Items**:
    - หากต้องการสร้าง multiple items จาก single item คุณสามารถใช้ JavaScript code เช่นนี้ ตัวอย่างนี้สมมติว่า item มี key ชื่อ `data` ที่ตั้งค่าเป็น array of items ในรูปแบบ: `[{ "data": [{<item_1>}, {<item_2>}, ...] }]`:
	```javascript
	return $input.first().json.data.map(item => {
        return {
            json: item
        }
    });
	```
	- หากต้องการสร้าง single item จาก multiple items คุณสามารถใช้ JavaScript code นี้:
	```javascript
    return [
    	{
        	json: {
        		data_object: $input.all().map(item => item.json)
        	}
        }
      ];
	```

ตัวอย่าง JavaScript เหล่านี้สมมติว่า input ทั้งหมดของคุณคือสิ่งที่คุณต้องการแปลง เช่นเดียวกับในแบบฝึกหัดข้างต้น คุณยังสามารถ execute การดำเนินการอย่างใดอย่างหนึ่งบน field เฉพาะได้โดยระบุสิ่งนั้นใน items list ตัวอย่างเช่น หากตัวอย่าง workEmail ของเรามีหลายอีเมลใน field เดียว เราสามารถรันโค้ดเช่นนี้ได้:
```javascript
let items = $input.all();
return items[0].json.workEmail.map(item => {
	return {
		json: item
	}
});
```

### Exercise

1. ใช้ **HTTP Request node** เพื่อส่ง GET request ไปยัง PokéAPI `https://pokeapi.co/api/v2/pokemon` (API นี้ไม่ต้องใช้ authentication)
2. แปลงข้อมูลใน `results` field ด้วย **Split Out node**
3. แปลงข้อมูลใน `results` field ด้วย **Code node**


??? note "Show me the solution"

	1. หากต้องการรับ pokemon จาก PokéAPI ให้ execute **HTTP Request node** ด้วย parameters ต่อไปนี้:
		- **Authentication**: None
		- **Request Method**: GET
		- **URL**: https://pokeapi.co/api/v2/pokemon
	2. หากต้องการแปลงข้อมูลด้วย **Split Out node** ให้เชื่อมต่อ node นี้กับ **HTTP Request node** และตั้งค่า parameters ต่อไปนี้:
		- **Field To Split Out**: results
		- **Include**: No Other Fields
	3. หากต้องการแปลงข้อมูลด้วย **Code node** ให้เชื่อมต่อ node นี้กับ **HTTP Request node** และเขียนโค้ดต่อไปนี้ในช่อง JavaScript Code:
		```javascript
		let items = $input.all();
		return items[0].json.results.map(item => {
			return {
				json: item
			}
		});
		```
