ใช้ item linking ของ n8n เพื่อเข้าถึงข้อมูลจาก items ที่อยู่ก่อนหน้า item ปัจจุบัน นอกจากนี้ยังมีผลกระทบเมื่อใช้ Code node nodes ส่วนใหญ่จะเชื่อมโยงทุก output item กับ input item สิ่งนี้สร้างห่วงโซ่ของ items ที่คุณสามารถย้อนกลับไปเพื่อเข้าถึง items ก่อนหน้าได้ สำหรับภาพรวมแนวคิดที่ลึกซึ้งยิ่งขึ้นของหัวข้อนี้ โปรดดูที่ [Item linking concepts](/data/data-mapping/data-item-linking/item-linking-concepts.md) เอกสารนี้เน้นตัวอย่างการใช้งานจริง

เมื่อใช้ Code node มีบางสถานการณ์ที่คุณต้องระบุข้อมูล item linking ด้วยตนเอง หากคุณต้องการใช้ `$("<node-name>").item` ในภายหลังใน workflow สถานการณ์เหล่านี้ทั้งหมดใช้ได้เฉพาะเมื่อคุณมี incoming item มากกว่าหนึ่งรายการ n8n จะจัดการ item linking สำหรับ single items โดยอัตโนมัติ

สถานการณ์เหล่านี้คือเมื่อคุณ:

* เพิ่ม items ใหม่: items ใหม่ไม่ได้เชื่อมโยงกับ input ใดๆ
* ส่งคืน items ใหม่
* ต้องการควบคุม item linking ด้วยตนเอง

[n8n's automatic item linking](/data/data-mapping/data-item-linking/item-linking-concepts.md) จัดการสถานการณ์อื่นๆ

ในการควบคุม item linking ให้ตั้งค่า `pairedItem` เมื่อส่งคืนข้อมูล ตัวอย่างเช่น เพื่อเชื่อมโยงไปยัง item ที่ index 0:

```js
[
	{
		"json": {
			. . . 
		},
		// The index of the input item that generated this output item
		"pairedItem": 0
	}
]
```


### ตัวอย่างการใช้งาน `pairedItem`

พิจารณาข้อมูล input นี้:

```json
[
  {
    "id": "23423532",
    "name": "Jay Gatsby"
  },
  {
    "id": "23423533",
    "name": "José Arcadio Buendía"
  },
  {
    "id": "23423534",
    "name": "Max Sendak"
  },
  {
    "id": "23423535",
    "name": "Zaphod Beeblebrox"
  },
  {
    "id": "23423536",
    "name": "Edmund Pevensie"
  }
]
```

และใช้มันเพื่อสร้าง items ใหม่ ซึ่งมีเพียงชื่อ พร้อมกับข้อมูลชิ้นใหม่:

```js
newItems = [];
for(let i=0; i<items.length; i++){
  newItems.push(
    {
    "json":
      {
        "name": items[i].json.name,
				"aBrandNewField": "New data for item " + i
      }
    }
  )
}

return newItems;
```

`newItems` เป็น array ของ items ที่ไม่มี `pairedItem` ซึ่งหมายความว่าไม่มีทางที่จะติดตามย้อนกลับจาก items เหล่านี้ไปยัง items ที่ใช้สร้างมันขึ้นมาได้

เพิ่ม `pairedItem` object:

```js
newItems = [];
for(let i=0; i<items.length; i++){
  newItems.push(
    {
      "json":
        {
          "name": items[i].json.name,
					"aBrandNewField": "New data for item " + i
        },
      "pairedItem": i
    }    
  )
}
return newItems;
```

ตอนนี้แต่ละ item ใหม่จะเชื่อมโยงไปยัง item ที่ใช้สร้างมันขึ้นมา
