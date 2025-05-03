---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Methods ที่ช่วยให้ทำงานทั่วไปใน expressions ได้ง่ายขึ้น
contentType: reference
hide:
  - toc
---

# Convenience methods

n8n มี methods เหล่านี้เพื่อให้ง่ายต่อการทำงานทั่วไปใน [expressions](/glossary.md#expression-n8n)

/// note | Python support
คุณสามารถใช้ Python ใน Code node ได้ แต่ไม่สามารถใช้ใน expressions ได้
///

=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :---------------------: |
	| `$evaluateExpression(expression: string, itemIndex?: number)` | ประเมินผล string เป็น expression หากคุณไม่ได้ระบุ `itemIndex` n8n จะใช้ข้อมูลจาก item 0 ใน Code node | :white_check_mark: |
	| `$ifEmpty(value, defaultValue)` | ฟังก์ชัน `$ifEmpty()` รับสอง parameters ทดสอบ parameter แรกเพื่อตรวจสอบว่าว่างเปล่าหรือไม่ จากนั้นคืนค่า parameter แรก (หากไม่ว่างเปล่า) หรือ parameter ที่สอง (หาก parameter แรกว่างเปล่า) parameter แรกจะถือว่าว่างเปล่าหากเป็น:<ul><li>`undefined`</li><li>`null`</li><li>สตริงว่าง `''`</li><li>Array ที่ `value.length` คืนค่า `false`</li><li>Object ที่ `Object.keys(value).length` คืนค่า `false`</li></ul> | :white_check_mark: |
	| `$if()` | ฟังก์ชัน `$if()` รับสาม parameters: เงื่อนไข, ค่าที่จะคืนหากเป็น true, และค่าที่จะคืนหากเป็น false | :x: | 
	| `$max()` | คืนค่าตัวเลขที่สูงที่สุดจากตัวเลขที่ให้มา | :x: |
	| `$min()` | คืนค่าตัวเลขที่ต่ำที่สุดจากตัวเลขที่ให้มา | :x: |
=== "Python"
	| Method | Description |
	| ------ | ----------- | 
	| `_evaluateExpression(expression: string, itemIndex?: number)` | ประเมินผล string เป็น expression หากคุณไม่ได้ระบุ `itemIndex` n8n จะใช้ข้อมูลจาก item 0 ใน Code node |
	| `_ifEmpty(value, defaultValue)` | ฟังก์ชัน `_ifEmpty()` รับสอง parameters ทดสอบ parameter แรกเพื่อตรวจสอบว่าว่างเปล่าหรือไม่ จากนั้นคืนค่า parameter แรก (หากไม่ว่างเปล่า) หรือ parameter ที่สอง (หาก parameter แรกว่างเปล่า) parameter แรกจะถือว่าว่างเปล่าหากเป็น:<ul><li>`undefined`</li><li>`null`</li><li>สตริงว่าง `''`</li><li>Array ที่ `value.length` คืนค่า `false`</li><li>Object ที่ `Object.keys(value).length` คืนค่า `false`</li></ul> | :white_check_mark: |
