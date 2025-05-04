/// note | เฉพาะ Programmatic-style nodes เท่านั้น
คำแนะนำนี้ใช้กับ programmatic-style nodes หากคุณใช้ declarative style, n8n จะจัดการ paired items ให้คุณโดยอัตโนมัติ
///

ใช้ item linking ของ n8n เพื่อเข้าถึงข้อมูลจาก items ที่อยู่ก่อนหน้า item ปัจจุบัน n8n จำเป็นต้องรู้ว่า output item ใดมาจาก input item ใด หากข้อมูลนี้หายไป expressions ใน nodes อื่นอาจเสียหาย ในฐานะนักพัฒนา node คุณต้องแน่ใจว่า items ใดๆ ที่ node ของคุณส่งคืนนั้นรองรับสิ่งนี้

สิ่งนี้ใช้กับ programmatic nodes (รวมถึง trigger nodes) คุณไม่จำเป็นต้องพิจารณา item linking เมื่อสร้าง declarative-style node อ้างอิงถึง [Choose your node building approach](/integrations/creating-nodes/plan/choose-node-method.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ node styles

เริ่มต้นด้วยการอ่าน [Item linking concepts](/data/data-mapping/data-item-linking/item-linking-concepts.md) ซึ่งให้ภาพรวมแนวคิดของ item linking และรายละเอียดของสถานการณ์ที่ n8n สามารถจัดการการเชื่อมโยงโดยอัตโนมัติได้

หากคุณต้องการจัดการ item linking ด้วยตนเอง ให้ทำโดยการตั้งค่า `pairedItem` ในแต่ละ item ที่ node ของคุณส่งคืน:

```typescript
// Use the pairedItem information of the incoming item
newItem = {
	"json": { . . . },
	"pairedItem": {
		"item": item.pairedItem,
		// Optional: choose the input to use
		// Set this if your node combines multiple inputs
		"input": 0
};

// Or set the index manually
newItem = {
		"json": { . . . }
		"pairedItem": {
			"item": i,
			// Optional: choose the input to use
			// Set this if your node combines multiple inputs
			"input": 0
		},
};
```
