---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: เพิ่มข้อมูลแบบกำหนดเอง (custom data) ให้กับ workflow executions ของคุณโดยใช้ Code node จากนั้นคุณสามารถกรอง executions ตามข้อมูลนี้ได้
contentType: howto
---

# Custom executions data

คุณสามารถตั้งค่าข้อมูลแบบกำหนดเอง (custom data) ใน workflow ของคุณโดยใช้ Code node หรือ [Execution Data node](/integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md) n8n จะบันทึกข้อมูลนี้พร้อมกับแต่ละ execution จากนั้นคุณสามารถใช้ข้อมูลนี้เมื่อกรองรายการ executions หรือดึงข้อมูลนี้ใน workflows ของคุณโดยใช้ Code node

--8<-- "_snippets/workflows/executions/custom-execution-data-availability.md"

## Set and access custom data using the Code node

ส่วนนี้อธิบายวิธีการตั้งค่าและเข้าถึงข้อมูลโดยใช้ Code node โปรดดู [Execution Data node](/integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md) สำหรับข้อมูลเกี่ยวกับการใช้ Execution Data node เพื่อตั้งค่าข้อมูล คุณไม่สามารถดึงข้อมูลแบบกำหนดเองโดยใช้ Execution Data node ได้

### Set custom executions data

ตั้งค่าข้อมูลพิเศษชิ้นเดียว:

=== "JavaScript"
	```js
	$execution.customData.set("key", "value");
	```
=== "Python"
	```python
	_execution.customData.set("key", "value");
	```

ตั้งค่าข้อมูลพิเศษทั้งหมด การดำเนินการนี้จะเขียนทับ object ข้อมูลแบบกำหนดเองทั้งหมดสำหรับ execution นี้:

=== "JavaScript"
	```js
	$execution.customData.setAll({"key1": "value1", "key2": "value2"})
	```
=== "Python"
	```python
	_execution.customData.setAll({"key1": "value1", "key2": "value2"})
	```

มีข้อจำกัดดังนี้:

* ต้องเป็น strings
* `key` มีความยาวสูงสุด 50 ตัวอักษร
* `value` มีความยาวสูงสุด 255 ตัวอักษร
* n8n รองรับข้อมูลแบบกำหนดเองสูงสุด 10 รายการ

### Access the custom data object during execution

คุณสามารถดึง object ข้อมูลแบบกำหนดเอง หรือค่าเฉพาะในนั้น ในระหว่าง execution:

<!-- vale off -->
=== "JavaScript"
	```js
	// เข้าถึงสถานะปัจจุบันของ object ในระหว่างการ execution
	const customData = $execution.customData.getAll();

	// เข้าถึงค่าเฉพาะที่ตั้งค่าไว้ในระหว่าง execution นี้
	const customData = $execution.customData.get("key");
	```
=== "Python"
	```python
	# เข้าถึงสถานะปัจจุบันของ object ในระหว่างการ execution
	customData = _execution.customData.getAll();

	# เข้าถึงค่าเฉพาะที่ตั้งค่าไว้ในระหว่าง execution นี้
	customData = _execution.customData.get("key");
	```
<!-- vale on -->
