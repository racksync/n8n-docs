---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Access your environment's custom variables.
contentType: reference
---

# `vars`

/// info | Feature availability
* มีให้ใช้งานบนแผน Self-hosted Enterprise และ Pro และ Enterprise Cloud
* คุณต้องมีสิทธิ์เข้าถึงบัญชีเจ้าของ instance n8n เพื่อสร้างตัวแปร
///	

`vars` ประกอบด้วย [Variables](/code/variables.md) ทั้งหมดสำหรับ environment ที่ใช้งานอยู่ เป็นแบบอ่านอย่างเดียว (read-only): คุณสามารถเข้าถึงตัวแปรโดยใช้ `vars` แต่ต้องตั้งค่าผ่าน UI เท่านั้น

=== "JavaScript"
	```js
	// Access a variable
	$vars.<variable-name>
	```
=== "Python"
	```python
	# Access a variable
	_vars.<variable-name>
	```

/// note | `vars` and `env`
`vars` ให้สิทธิ์เข้าถึงตัวแปรที่ผู้ใช้สร้างขึ้น เป็นส่วนหนึ่งของคุณสมบัติ [Environments](/source-control-environments/index.md) ส่วน `env` ให้สิทธิ์เข้าถึง [configuration environment variables](/hosting/configuration/environment-variables/index.md) สำหรับ instance n8n ของคุณ
///
