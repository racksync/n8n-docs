---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: reference
---

# `execution`

## `execution.id`

ประกอบด้วย ID ที่ไม่ซ้ำกันของการ execute workflow ปัจจุบัน

=== "JavaScript"
	```js
	let executionId = $execution.id;
	```
=== "Python"
	```python
	executionId = _execution.id
	```

## `execution.resumeUrl`

Webhook URL ที่จะเรียกเพื่อดำเนินการต่อ (resume) workflow ที่กำลัง [waiting](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md) อยู่

ดูเอกสาร [Wait > On webhook call](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md#on-webhook-call) เพื่อเรียนรู้เพิ่มเติม

## `execution.customData`

มีให้ใช้งานเฉพาะใน Code node เท่านั้น

=== "JavaScript"
	```js
	// Set a single piece of custom execution data
	$execution.customData.set("key", "value");

	// Set the custom execution data object
	$execution.customData.setAll({"key1": "value1", "key2": "value2"})

	// Access the current state of the object during the execution
	var customData = $execution.customData.getAll()

	// Access a specific value set during this execution
	var customData = $execution.customData.get("key")
	```
=== "Python"
	```python
	# Set a single piece of custom execution data
	_execution.customData.set("key", "value");

	# Set the custom execution data object
	_execution.customData.setAll({"key1": "value1", "key2": "value2"})

	# Access the current state of the object during the execution
	customData = _execution.customData.getAll()

	# Access a specific value set during this execution
	customData = _execution.customData.get("key")
	```

อ้างอิง [Custom executions data](/workflows/executions/custom-executions-data.md) สำหรับข้อมูลเพิ่มเติม
