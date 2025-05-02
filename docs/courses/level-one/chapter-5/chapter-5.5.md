---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

<!-- vale from-microsoft.We = NO -->
<!-- vale from-microsoft.FirstPerson = NO -->
# 5. Calculating Booked Orders

ในขั้นตอนนี้ของ workflow คุณจะได้เรียนรู้ว่า n8n จัดโครงสร้างข้อมูลอย่างไร และวิธีเพิ่ม custom JavaScript code เพื่อทำการคำนวณโดยใช้ Code node หลังจากขั้นตอนนี้ workflow ของคุณควรมีลักษณะดังนี้:

[[ workflowDemo("file:////courses/level-one/chapter-5/chapter-5.5.json") ]]

ขั้นตอนต่อไปใน workflow ของ Nathan คือการคำนวณค่าสองค่าจาก booked orders:

- The total number of booked orders
- The total value of all booked orders

ในการคำนวณข้อมูลและเพิ่มฟังก์ชันการทำงานเพิ่มเติมให้กับ workflows ของคุณ คุณสามารถใช้ Code node ซึ่งช่วยให้คุณเขียน custom JavaScript code ได้

## About the Code node

/// warning | Code node modes
Code node มี **modes** การทำงานสองแบบ ขึ้นอยู่กับว่าคุณต้องการประมวลผล items อย่างไร:

* **Run Once for All Items** ช่วยให้คุณเขียน code เพื่อประมวลผล input items ทั้งหมดพร้อมกันเป็นกลุ่ม
* **Run Once for Each Item** εκτέλεση (execute) code ของคุณหนึ่งครั้งสำหรับแต่ละ input item

เรียนรู้เพิ่มเติมเกี่ยวกับวิธีใช้ [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md)
///

ใน n8n ข้อมูลที่ส่งผ่านระหว่าง nodes คือ array ของ objects ที่มีโครงสร้าง JSON ดังต่อไปนี้:

```json
[
    {
   	 "json": { // (1)!
   		 "apple": "beets",
   		 "carrot": {
   			 "dill": 1
   		 }
   	 },
   	 "binary": { // (2)!
   		 "apple-picture": { // (3)!
   			 "data": "....", // (4)!
   			 "mimeType": "image/png", // (5)!
   			 "fileExtension": "png", // (6)!
   			 "fileName": "example.png", // (7)!
   		 }
   	 }
    },
    ...
]
```

1. (required) n8n จัดเก็บข้อมูลจริงภายใน `json` key ที่ซ้อนกัน property นี้จำเป็น แต่สามารถตั้งค่าเป็นอะไรก็ได้ตั้งแต่อ็อบเจกต์ว่าง (เช่น `{}`) ไปจนถึง arrays และข้อมูลที่ซ้อนกันลึกๆ Code node จะห่อหุ้มข้อมูลใน `json` object และ parent array (`[]`) โดยอัตโนมัติหากไม่มีอยู่
2. (optional) Binary data ของ item items ส่วนใหญ่ใน n8n ไม่มี binary data
3. (required) ชื่อ key ที่กำหนดเองสำหรับ binary data
4. (required) Base64-encoded binary data
5. (optional) ควรตั้งค่าหากเป็นไปได้
6. (optional) ควรตั้งค่าหากเป็นไปได้
7. (optional) ควรตั้งค่าหากเป็นไปได้

คุณสามารถเรียนรู้เพิ่มเติมเกี่ยวกับรูปแบบที่คาดหวังได้ในหน้า [n8n data structure](/data/data-structure.md)

## Configure the Code node

ตอนนี้มาดูกันว่าจะทำงานของ Nathan ให้สำเร็จโดยใช้ Code node ได้อย่างไร

ใน workflow ของคุณ ให้เพิ่ม **Code node** ที่เชื่อมต่อกับ `false` branch ของ **If node**

เมื่อหน้าต่าง Code node เปิดอยู่ ให้กำหนดค่า parameters เหล่านี้:

- **Mode**: Select **Run Once for All Items**.
- **Language**: Select **JavaScript**.

	/// note | Using Python in code nodes
	แม้ว่าเราจะใช้ JavaScript ด้านล่าง แต่คุณสามารถใช้ Python ใน Code node ได้เช่นกัน หากต้องการเรียนรู้เพิ่มเติม โปรดดูเอกสาร [Code node](/code/code-node.md)
	///

- คัดลอก Code ด้านล่างและวางลงในกล่อง **Code** เพื่อแทนที่ code ที่มีอยู่:

	```javascript
	let items = $input.all();
	let totalBooked = items.length;
	let bookedSum = 0;

	for (let i=0; i < items.length; i++) {
	  bookedSum = bookedSum + items[i].json.orderPrice;
	}

	return [{ json: {totalBooked, bookedSum} }];
	```

สังเกตรูปแบบที่เราส่งคืนผลลัพธ์ของการคำนวณ:

```javascript
return [{ json: {totalBooked, bookedSum} }]
```

/// warning | Data structure error
หากคุณไม่ได้ใช้ data structure ที่ถูกต้อง คุณจะได้รับข้อความแสดงข้อผิดพลาด: `Error: Always an Array of items has to be returned!`
///

ตอนนี้เลือก **Test step** และคุณควรเห็นผลลัพธ์ต่อไปนี้:

<figure><img src="/_images/courses/level-one/chapter-five/l1-c5-5-5-code-node.png" alt="Code node output" style="width:100%"><figcaption align = "center"><i>Code node output</i></figcaption></figure>

## What's next?

**Nathan 🙋**: ว้าว Code node ทรงพลังมาก! นี่หมายความว่าถ้าฉันมีทักษะ JavaScript พื้นฐาน ฉันสามารถเพิ่มพลังให้กับ workflows ของฉันได้

**You 👩‍🔧**: ใช่! คุณสามารถก้าวหน้าจาก no-code ไปสู่ low-code ได้!

**Nathan 🙋**: ตอนนี้ ฉันจะส่งการคำนวณสำหรับ booked orders ไปยัง Discord channel ของทีมฉันได้อย่างไร?

**You 👩‍🔧**: มี n8n node สำหรับสิ่งนั้น ฉันจะตั้งค่าในขั้นตอนถัดไป
