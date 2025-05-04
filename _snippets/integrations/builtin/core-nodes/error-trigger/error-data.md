ข้อมูล error เริ่มต้นที่ Error Trigger ได้รับคือ:

```json
[
	{
		"execution": {
			"id": "231",
			"url": "https://n8n.example.com/execution/231",
			"retryOf": "34",
			"error": {
				"message": "Example Error Message",
				"stack": "Stacktrace"
			},
			"lastNodeExecuted": "Node With Error",
			"mode": "manual"
		},
		"workflow": {
			"id": "1",
			"name": "Example Workflow"
		}
	}
]

```

ข้อมูลทั้งหมดมีอยู่เสมอ ยกเว้น:

- `execution.id`: ต้องการให้ execution ถูกบันทึกในฐานข้อมูล จะไม่มีอยู่หาก error เกิดขึ้นใน trigger node ของ workflow หลัก เนื่องจาก workflow ไม่ได้ execute
- `execution.url`: ต้องการให้ execution ถูกบันทึกในฐานข้อมูล จะไม่มีอยู่หาก error เกิดขึ้นใน trigger node ของ workflow หลัก เนื่องจาก workflow ไม่ได้ execute
- `execution.retryOf`: มีอยู่เฉพาะเมื่อ execution เป็นการ retry ของ execution ที่ล้มเหลว

หาก error เกิดจาก trigger node ของ workflow หลัก แทนที่จะเป็นขั้นตอนต่อมา ข้อมูลที่ส่งไปยัง error workflow จะแตกต่างกัน มีข้อมูลใน `execution{}` น้อยลง และมีข้อมูลใน `trigger{}` มากขึ้น:

```json
{
  "trigger": {
    "error": {
      "context": {},
      "name": "WorkflowActivationError",
      "cause": {
        "message": "",
        "stack": ""
      },
      "timestamp": 1654609328787,
      "message": "",
      "node": {
        . . . 
      }
    },
    "mode": "trigger"
  },
  "workflow": {
    "id": "",
    "name": ""
  }
}
```
