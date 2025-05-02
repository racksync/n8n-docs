---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: A method for working with the JMESPath library in n8n.
contentType: reference
hide:
  - toc
---

# JMESPath method

นี่คือ method ที่ n8n เตรียมไว้ให้สำหรับการทำงานกับ library [JMESPath](/code/cookbook/jmespath.md)

/// note | Python support
คุณสามารถใช้ Python ใน Code node ได้ แต่ไม่สามารถใช้ใน expressions ได้
///
=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `$jmespath()` | ทำการค้นหาบน JSON object โดยใช้ JMESPath | :white_check_mark: |
=== "Python"
	| Method | Description | 
	| ------ | ----------- | 
	| `_jmespath()` | ทำการค้นหาบน JSON object โดยใช้ JMESPath |
