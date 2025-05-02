---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Query JSON with JMESPath
description: n8n supports the JMESPath library, to simplify working with JSON formatted data.
contentType: howto
---

# Query JSON with JMESPath

[JMESPath](https://jmespath.org/){:target=_blank .external-link} เป็นภาษา query สำหรับ JSON ที่คุณสามารถใช้เพื่อดึงและแปลงองค์ประกอบจากเอกสาร JSON สำหรับรายละเอียดทั้งหมดเกี่ยวกับวิธีใช้ JMESPath โปรดดู [เอกสาร JMESPath](https://jmespath.org/tutorial.html){:target=_blank .external-link}


## The `jmespath()` method

n8n มีเมธอดที่กำหนดเองคือ `jmespath()` ใช้เมธอดนี้เพื่อทำการค้นหาบนออบเจกต์ JSON โดยใช้ภาษา query ของ JMESPath

 синтаксис พื้นฐานคือ:

=== "JavaScript"
	```js
	$jmespath(object, searchString)
	```
=== "Python"
	```python
	_jmespath(object, searchString)
	```


เพื่อช่วยให้เข้าใจว่าเมธอดทำอะไร นี่คือ JavaScript ที่ยาวกว่าซึ่งเทียบเท่ากัน:


```js
var jmespath = require('jmespath');
jmespath.search(object, searchString);
```

/// note | Expressions must be single-line
ตัวอย่างโค้ดที่ยาวกว่านี้ใช้ไม่ได้ใน Expressions เนื่องจากต้องเป็นบรรทัดเดียว
///

`object` คือออบเจกต์ JSON เช่น ผลลัพธ์จาก node ก่อนหน้า `searchString` คือ expression ที่เขียนด้วยภาษา query ของ JMESPath [JMESPath Specification](https://jmespath.org/specification.html#jmespath-specification){:target=_blank .external-link} มีรายการของ expressions ที่รองรับ ในขณะที่ [Tutorial](https://jmespath.org/tutorial.html) และ [Examples](https://jmespath.org/examples.html){:target=_blank .external-link} ของพวกเขามีตัวอย่างแบบโต้ตอบ

/// warning | Search parameter order
ตัวอย่างใน [JMESPath Specification](https://jmespath.org/specification.html#jmespath-specification){:target=_blank .external-link} เป็นไปตามรูปแบบ `search(searchString, object)` [ไลบรารี JMESPath JavaScript](https://github.com/jmespath/jmespath.js/){:target=_blank .external-link} ซึ่ง n8n ใช้ รองรับ `search(object, searchString)` แทน ซึ่งหมายความว่าเมื่อใช้ตัวอย่างจากเอกสาร JMESPath คุณอาจต้องเปลี่ยนลำดับของพารามิเตอร์ฟังก์ชัน search
///

## Common tasks

ส่วนนี้ให้ตัวอย่างสำหรับการดำเนินการทั่วไปบางอย่าง ตัวอย่างเพิ่มเติมและคำแนะนำโดยละเอียดมีอยู่ใน [เอกสารของ JMESPath เอง](https://jmespath.org/tutorial.html){:target=_blank .external-link}

เมื่อลองใช้ตัวอย่างเหล่านี้ คุณต้องตั้งค่า Code node **Mode** เป็น **Run Once for Each Item**

### Apply a JMESPath expression to a collection of elements with projections

จาก [เอกสาร JMESPath projections](https://jmespath.org/tutorial.html#projections){:target=_blank .external-link}:

> Projections เป็นหนึ่งในฟีเจอร์หลักของ JMESPath ใช้เพื่อใช้ expression กับคอลเลกชันขององค์ประกอบ JMESPath รองรับ projections ห้าประเภท:
>
> * List Projections
> * Slice Projections
> * Object Projections
> * Flatten Projections
> * Filter Projections

ตัวอย่างต่อไปนี้แสดงการใช้งานพื้นฐานของ list, slice, และ object projections โปรดดู [เอกสาร JMESPath projections](https://jmespath.org/tutorial.html#projections){:target=_blank .external-link} สำหรับคำอธิบายโดยละเอียดของแต่ละประเภท projection และตัวอย่างเพิ่มเติม

กำหนด JSON นี้จาก webhook node:


```js
[
  {
    "headers": {
      "host": "n8n.instance.address",
      ...
    },
    "params": {},
    "query": {},
    "body": {
      "people": [
        {
          "first": "James",
          "last": "Green"
        },
        {
          "first": "Jacob",
          "last": "Jones"
        },
        {
          "first": "Jayden",
          "last": "Smith"
        }
      ],
      "dogs": {
        "Fido": {
          "color": "brown",
          "age": 7
        },
        "Spot": {
          "color": "black and white",
          "age": 5
        }
      }
    }
  }
]

```


ดึง [list](https://jmespath.org/tutorial.html#list-and-slice-projections){:target=_blank .external-link} ของชื่อจริงของทุกคน:

=== "Expressions (JavaScript)"

	```js
	{{$jmespath($json.body.people, "[*].first" )}}
	// Returns ["James", "Jacob", "Jayden"]
	```

=== "Code node (JavaScript)"

	```js
	let firstNames = $jmespath($json.body.people, "[*].first" )
	return {firstNames};
	/* Returns:
	[
		{
			"firstNames": [
				"James",
				"Jacob",
				"Jayden"
			]
		}
	]
	*/
	```
=== "Code node (Python)"
	```python
	firstNames = _jmespath(_json['body']['people'], "[*].first" )
	return {"firstNames":firstNames}
	"""
	Returns:
	[
	 	{
			"firstNames": [
				"James",
				"Jacob",
				"Jayden"
			]
		}
	]
	"""
	```

รับ [slice](https://jmespath.org/tutorial.html#list-and-slice-projections){:target=_blank .external-link} ของชื่อจริง:

=== "Expressions (JavaScript)"

	```js
	{{$jmespath($json.body.people, "[:2].first")}}
	// Returns ["James", "Jacob"]
	```

=== "Code node (JavaScript)"
	```js
	let firstTwoNames = $jmespath($json.body.people, "[:2].first");
	return {firstTwoNames};
	/* Returns:
	[
		{
			"firstNames": [
				"James",
				"Jacob",
				"Jayden"
			]
		}
	]
	*/
	```
=== "Code node (Python)"
	```python
	firstTwoNames = _jmespath(_json['body']['people'], "[:2].first" )
	return {"firstTwoNames":firstTwoNames}
	"""
	Returns:
	[
  		{
			"firstTwoNames": [
			"James",
			"Jacob"
			]
		}
	]
	"""
	```

รับรายการอายุของสุนัขโดยใช้ [object projections](https://jmespath.org/tutorial.html#object-projections){:target=_blank .external-link}:

=== "Expressions (JavaScript)"

	```js
	{{$jmespath($json.body.dogs, "*.age")}}
	// Returns [7,5]
	```

=== "Code node (JavaScript)"
	```js
	let dogsAges = $jmespath($json.body.dogs, "*.age");
	return {dogsAges};
	/* Returns:
	[
		{
			"dogsAges": [
				7,
				5
			]
		}
	]
	*/
	```
=== "Code node (Python)"
	```python
	dogsAges = _jmespath(_json['body']['dogs'], "*.age")
	return {"dogsAges": dogsAges}
	"""
	Returns:
	[
		{
			"dogsAges": [
				7,
				5
			]
		}
	]
	"""
	```

### Select multiple elements and create a new list or object

ใช้ [Multiselect](https://jmespath.org/tutorial.html#multiselect){:target=_blank .external-link} เพื่อเลือกองค์ประกอบจากออบเจกต์ JSON และรวมเข้าด้วยกันเป็น list หรือ object ใหม่

กำหนด JSON นี้จาก webhook node:


```js
[
  {
    "headers": {
      "host": "n8n.instance.address",
      ...
    },
    "params": {},
    "query": {},
    "body": {
      "people": [
        {
          "first": "James",
          "last": "Green"
        },
        {
          "first": "Jacob",
          "last": "Jones"
        },
        {
          "first": "Jayden",
          "last": "Smith"
        }
      ],
      "dogs": {
        "Fido": {
          "color": "brown",
          "age": 7
        },
        "Spot": {
          "color": "black and white",
          "age": 5
        }
      }
    }
  }
]

```

<!-- vale off -->
ใช้ multiselect list เพื่อรับชื่อจริงและนามสกุล และสร้าง lists ใหม่ที่มีทั้งสองชื่อ:
<!-- vale on -->
=== "Expressions (JavaScript)"

	[[% raw %]]
	```js
	{{$jmespath($json.body.people, "[].[first, last]")}}
	// Returns [["James","Green"],["Jacob","Jones"],["Jayden","Smith"]]
	```
	[[% endraw %]]

=== "Code node (JavaScript)"

	```js
	let newList = $jmespath($json.body.people, "[].[first, last]");
	return {newList};
	/* Returns:
	[
		{
			"newList": [
				[
					"James",
					"Green"
				],
				[
					"Jacob",
					"Jones"
				],
				[
					"Jayden",
					"Smith"
				]
			]
		}
	]
	*/
	```
=== "Code node (Python)"
	```python
	newList = _jmespath(_json['body']['people'], "[].[first, last]")
	return {"newList":newList}
	"""
	Returns:
	[
		{
			"newList": [
				[
					"James",
					"Green"
				],
				[
					"Jacob",
					"Jones"
				],
				[
					"Jayden",
					"Smith"
				]
			]
		}
	]
	"""
	```

### An alternative to arrow functions in expressions

ตัวอย่างเช่น สร้างข้อมูลอินพุตบางส่วนโดยการคืนค่าโค้ดด้านล่างจาก Code node:

```js
return[
  {
    "json": {      
      "num_categories": "0",
      "num_products": "45",
      "category_id": 5529735,
      "parent_id": 1407340,
      "pos_enabled": 1,
      "pos_favorite": 0,
      "name": "HP",
      "description": "",
      "image": ""
    }
  },
  {
    "json": {
      "num_categories": "0",
      "num_products": "86",
      "category_id": 5529740,
      "parent_id": 1407340,
      "pos_enabled": 1,
      "pos_favorite": 0,
      "name": "Lenovo",
      "description": "",
      "image": ""
    }
  }  
]
```

คุณสามารถทำการค้นหาเช่น "ค้นหารายการที่มีชื่อ Lenovo และบอก category ID ของพวกเขา"

```js
{{ $jmespath($("Code").all(), "[?json.name=='Lenovo'].json.category_id") }}
```
