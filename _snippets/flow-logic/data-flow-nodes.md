Nodes สามารถประมวลผลได้หลาย items

ตัวอย่างเช่น หากคุณตั้งค่า Trello node เป็น `Create-Card` และสร้าง expression ที่ตั้งค่า `Name` โดยใช้ property ที่ชื่อ `name-input-value` จากข้อมูลขาเข้า node จะสร้าง card สำหรับแต่ละ item โดยเลือก `name-input-value` ของ item ปัจจุบันเสมอ

ตัวอย่างเช่น input นี้จะสร้างสอง cards หนึ่งชื่อ `test1` อีกอันชื่อ `test2`:

```json
[
	{
		name-input-value: "test1"
	},
	{
		name-input-value: "test2"
	}
]
```
