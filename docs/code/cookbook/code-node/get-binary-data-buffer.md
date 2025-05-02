---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Get the binary data buffer

binary data buffer ประกอบด้วยข้อมูลไฟล์ binary ทั้งหมดที่ประมวลผลโดย workflow คุณจำเป็นต้องเข้าถึงมันหากต้องการดำเนินการกับข้อมูล binary เช่น:

* จัดการข้อมูล: ตัวอย่างเช่น เพิ่ม header ของคอลัมน์ลงในไฟล์ CSV
* ใช้ข้อมูลในการคำนวณ: ตัวอย่างเช่น คำนวณค่า hash จากข้อมูลนั้น
* HTTP requests ที่ซับซ้อน: ตัวอย่างเช่น รวมการอัปโหลดไฟล์กับการส่งข้อมูลรูปแบบอื่น

/// note | Not available in Python
`getBinaryDataBuffer()` ไม่รองรับเมื่อใช้ Python
///
คุณสามารถเข้าถึง buffer โดยใช้ฟังก์ชัน `getBinaryDataBuffer()` ของ n8n:


```js
/* 
* itemIndex: number. ดัชนีของ item ในข้อมูล input
* binaryPropertyName: string. ชื่อของ binary property 
* ค่าเริ่มต้นใน node Read/Write File From Disk คือ 'data'
*/
let binaryDataBufferItem = await this.helpers.getBinaryDataBuffer(itemIndex, binaryPropertyName);
```

ตัวอย่างเช่น:

```js
let binaryDataBufferItem = await this.helpers.getBinaryDataBuffer(0, 'data');
// คืนค่าข้อมูลใน binary buffer สำหรับ input item แรก
```


คุณควรใช้ฟังก์ชัน `getBinaryDataBuffer()` เสมอ และหลีกเลี่ยงการใช้วิธีการเก่าๆ ในการเข้าถึง buffer โดยตรง เช่น การกำหนดเป้าหมายด้วย expressions อย่าง `items[0].binary.data.data`
