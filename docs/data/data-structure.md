---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
---

# Data structure

ใน n8n ข้อมูลทั้งหมดที่ส่งผ่านระหว่าง nodes เป็น array ของ objects มีโครงสร้างดังนี้:

```json
[
	{
		// For most data:
		// Wrap each item in another object, with the key 'json'
		"json": {
			// Example data
			"apple": "beets",
			"carrot": {
				"dill": 1
			}
		},
		// For binary data:
		// Wrap each item in another object, with the key 'binary'
		"binary": {
			// Example data
			"apple-picture": {
				"data": "....", // Base64 encoded binary data (required)
				"mimeType": "image/png", // Best practice to set if possible (optional)
				"fileExtension": "png", // Best practice to set if possible (optional)
				"fileName": "example.png", // Best practice to set if possible (optional)
			}
		}
	},
]
```

/// note | Skipping the `json` key and array syntax
ตั้งแต่เวอร์ชัน 0.166.0 เป็นต้นไป เมื่อใช้ Function node หรือ Code node, n8n จะเพิ่ม `json` key โดยอัตโนมัติหากไม่มีอยู่ นอกจากนี้ยังจะห่อ items ของคุณใน array (`[]`) โดยอัตโนมัติหากจำเป็น สิ่งนี้ใช้ได้เฉพาะเมื่อใช้ Function หรือ Code nodes เท่านั้น เมื่อสร้าง nodes ของคุณเอง คุณยังคงต้องตรวจสอบให้แน่ใจว่า node ส่งคืนข้อมูลพร้อมกับ `json` key
///
## Data item processing

--8<-- "_snippets/flow-logic/data-flow-nodes.md"


