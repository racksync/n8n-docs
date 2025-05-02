---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: How to use `("<node-name>").itemMatching(currentNodeinputIndex)`
contentType: howto
---

# Retrieve linked items from earlier in the workflow

ทุก item ในข้อมูล input ของ node จะเชื่อมโยงกลับไปยัง item ที่ใช้ใน node ก่อนหน้าเพื่อสร้างมันขึ้นมา สิ่งนี้มีประโยชน์หากคุณต้องการดึง item ที่เชื่อมโยงจาก node ที่อยู่ก่อนหน้ามากกว่า node ที่อยู่ติดกันทันที

ในการเข้าถึง item ที่เชื่อมโยงจาก node ก่อนหน้าใน workflow ให้ใช้ `("<node-name>").itemMatching(currentNodeinputIndex)`


ตัวอย่างเช่น พิจารณา workflow ที่ทำสิ่งต่อไปนี้:

1. The Customer Datastore node generates example data:
	```json
	[
		{
			"id": "23423532",
			"name": "Jay Gatsby",
			"email": "gatsby@west-egg.com",
			"notes": "Keeps asking about a green light??",
			"country": "US",
			"created": "1925-04-10"
		},
		{
			"id": "23423533",
			"name": "José Arcadio Buendía",
			"email": "jab@macondo.co",
			"notes": "Lots of people named after him. Very confusing",
			"country": "CO",
			"created": "1967-05-05"
		},
		...
    ]
	```
2. The Edit Fields node simplifies this data:
	```json
	[
		{
			"name": "Jay Gatsby"
		},
		{
			"name": "José Arcadio Buendía"
		},
        ...
	]
	```
3. The Code node restore the email address to the correct person:
	```json
	[
		{
			"name": "Jay Gatsby",
			"restoreEmail": "gatsby@west-egg.com"
		},
		{
			"name": "José Arcadio Buendía",
			"restoreEmail": "jab@macondo.co"
		},
		...
	]
	```

Code node ทำสิ่งนี้โดยใช้โค้ดต่อไปนี้:

=== "JavaScript"
	```js
	for(let i=0; i<$input.all().length; i++) {
  		$input.all()[i].json.restoreEmail = $('Customer Datastore (n8n training)').itemMatching(i).json.email;
	}
	return $input.all();
	```
=== "Python"
	```python
	for i,item in enumerate(_input.all()):
  		_input.all()[i].json.restoreEmail = _('Customer Datastore (n8n training)').itemMatching(i).json.email

	return _input.all();
	```

คุณสามารถดูและดาวน์โหลด workflow ตัวอย่างได้จาก [n8n website | itemMatchin usage example ](https://n8n.io/workflows/1966-itemmatching-usage-example/){:target=_blank .external-link}.
