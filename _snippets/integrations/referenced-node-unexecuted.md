<!-- vale off -->
## Node ที่อ้างอิงยังไม่ได้ทำงาน
<!-- vale on -->

ข้อผิดพลาดนี้จะแสดงขึ้นเมื่อ node ก่อนหน้าใน workflow ยังไม่ได้ทำงานและไม่ได้ให้ output ที่ node นี้ต้องการเป็น input

ข้อความเต็มของข้อผิดพลาดนี้จะบอกคุณถึง node ที่แน่นอนที่ไม่ได้ทำงานในรูปแบบนี้:
```
An expression references the node '<node-name>', but it hasn’t been executed yet. Either change the expression, or re-wire your workflow to make sure that node executes first.
```

ในการเริ่มต้นแก้ไขปัญหา ให้ทดสอบ workflow จนถึง node ที่ระบุชื่อไว้

สำหรับ nodes ที่เรียกใช้ JavaScript หรือ custom code อื่นๆ ให้ตรวจสอบว่า node ได้ทำงานแล้วหรือไม่ก่อนที่จะพยายามใช้ค่าโดยการเรียกใช้:

```js
$("<node-name>").isExecuted
```