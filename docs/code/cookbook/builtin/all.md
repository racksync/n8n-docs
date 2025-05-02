---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: reference
---

# `("<node-name>").all(branchIndex?: number, runIndex?: number)`

ฟังก์ชันนี้ให้สิทธิ์เข้าถึง item ทั้งหมดของ node ปัจจุบันหรือ node แม่ หากคุณไม่ระบุพารามิเตอร์ใดๆ มันจะคืนค่า item ทั้งหมดของ node ปัจจุบัน

## Getting items

=== "JavaScript"
	```js
	// Returns all the items of the given node and current run
	let allItems = $("<node-name>").all();

	// Returns all items the node "IF" outputs (index: 0 which is Output "true" of its most recent run)
	let allItems = $("IF").all();

	// Returns all items the node "IF" outputs (index: 0 which is Output "true" of the same run as current node)
	let allItems = $("IF").all(0, $runIndex);

	// Returns all items the node "IF" outputs (index: 1 which is Output "false" of run 0 which is the first run)
	let allItems = $("IF").all(1, 0);
	```
=== "Python"
	```python
	# Returns all the items of the given node and current run
	allItems = _("<node-name>").all();

	# Returns all items the node "IF" outputs (index: 0 which is Output "true" of its most recent run)
	allItems = _("IF").all();

	# Returns all items the node "IF" outputs (index: 0 which is Output "true" of the same run as current node)
	allItems = _("IF").all(0, _runIndex);

	# Returns all items the node "IF" outputs (index: 1 which is Output "false" of run 0 which is the first run)
	allItems = _("IF").all(1, 0);
	```

## Accessing item data

รับ item ทั้งหมดที่ส่งออกจาก node ก่อนหน้า และ log ข้อมูลที่อยู่ในนั้นออกมา:

=== "JavaScript"
	```typescript
	previousNodeData = $("<node-name>").all();
	for(let i=0; i<previousNodeData.length; i++) {
		console.log(previousNodeData[i].json);
	}
	```
=== "Python"
	```python
	previousNodeData = _("<node-name>").all();
	for item in previousNodeData:
		# item is of type <class 'pyodide.ffi.JsProxy'>
		# You need to convert it to a Dict
  		itemDict = item.json.to_py()
  		print(itemDict)
	```
