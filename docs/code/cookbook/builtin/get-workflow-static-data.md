---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
tags:
  - "static data"
  - "global variables"
hide:
  - tags
contentType: reference
---

# `getWorkflowStaticData(type)`

ฟังก์ชันนี้ให้สิทธิ์เข้าถึงข้อมูล static ของ workflow

/// note | Experimental feature
- ข้อมูล Static จะไม่สามารถใช้งานได้เมื่อทดสอบ workflows ต้องให้ workflow ทำงาน (active) และถูกเรียกโดย [trigger](/glossary.md#trigger-node-n8n) หรือ webhook เพื่อบันทึกข้อมูล static
- คุณสมบัตินี้อาจทำงานไม่น่าเชื่อถือภายใต้การ execute workflow ที่มีความถี่สูง
///
คุณสามารถบันทึกข้อมูลได้โดยตรงใน workflow ข้อมูลนี้ควรมีขนาดเล็ก

ตัวอย่างเช่น: คุณสามารถบันทึก timestamp ของ item ล่าสุดที่ประมวลผลจาก
RSS feed หรือ database ฟังก์ชันนี้จะคืนค่าเป็น object เสมอ จากนั้นสามารถอ่าน, ลบ หรือ
ตั้งค่า properties บน object นั้นได้ เมื่อการ execute workflow สำเร็จ n8n จะตรวจสอบโดยอัตโนมัติว่าข้อมูลมีการเปลี่ยนแปลงหรือไม่ และบันทึกข้อมูลหากจำเป็น

ข้อมูล static มีสองประเภทคือ global และ node ข้อมูล static แบบ Global จะเหมือนกัน
ทั้ง workflow ทุก node ใน workflow สามารถเข้าถึงได้ ส่วนข้อมูล static แบบ Node จะเป็นเอกลักษณ์เฉพาะของ node นั้นๆ เฉพาะ node ที่ตั้งค่าเท่านั้นที่จะสามารถดึงข้อมูลกลับมาได้อีกครั้ง

ตัวอย่างกับข้อมูล global:

=== "JavaScript"
	```javascript
	// Get the global workflow static data
	const workflowStaticData = $getWorkflowStaticData('global');

	// Access its data
	const lastExecution = workflowStaticData.lastExecution;

	// Update its data
	workflowStaticData.lastExecution = new Date().getTime();

	// Delete data
	delete workflowStaticData.lastExecution;
	```
=== "Python"
	```python
	# Get the global workflow static data
	workflowStaticData = _getWorkflowStaticData('global')

	# Access its data
	lastExecution = workflowStaticData.lastExecution

	# Update its data
	workflowStaticData.lastExecution = new Date().getTime()

	# Delete data
	delete workflowStaticData.lastExecution
	```

ตัวอย่างกับข้อมูล node:

=== "JavaScript"
	```js
	// Get the static data of the node
	const nodeStaticData = $getWorkflowStaticData('node');

	// Access its data
	const lastExecution = nodeStaticData.lastExecution;

	// Update its data
	nodeStaticData.lastExecution = new Date().getTime();

	// Delete data
	delete nodeStaticData.lastExecution;
	```
=== "Python"
	```python
	# Get the static data of the node
	nodeStaticData = _getWorkflowStaticData('node')

	# Access its data
	lastExecution = nodeStaticData.lastExecution

	# Update its data
	nodeStaticData.lastExecution = new Date().getTime()

	# Delete data
	delete nodeStaticData.lastExecution
	```

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ workflowDemo("https://api.n8n.io/workflows/templates/2538") ]]
