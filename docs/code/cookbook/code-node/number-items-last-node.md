---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Get number of items returned by the previous node

ในการรับจำนวน item ที่ส่งคืนโดย node ก่อนหน้า:

=== "JavaScript"

	```js
	if (Object.keys(items[0].json).length === 0) {
	return [
		{
			json: {
				results: 0,
			}
		}
	]
	}
	return [
		{
			json: {
				results: items.length,
			}
		}
	];
	```

	ผลลัพธ์จะคล้ายกับตัวอย่างต่อไปนี้

	```json
	[
		{
			"results": 8
		}
	]
	```
=== "Python"
	```python
	if len(items[0].json) == 0:
		return [
			{
				"json": {
					"results": 0,
				}
			}
		]
	else:
		return [
			{
				"json": {
					"results": items.length,
				}
			}
		]
	```
	ผลลัพธ์จะคล้ายกับตัวอย่างต่อไปนี้

	```json
	[
		{
			"results": 8
		}
	]
	```
