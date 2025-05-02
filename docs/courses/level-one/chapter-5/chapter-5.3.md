---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

<!-- vale from-microsoft.We = NO -->
<!-- vale from-microsoft.FirstPerson = NO -->
# 3. Filtering Orders

ในขั้นตอนนี้ของ workflow คุณจะได้เรียนรู้วิธีกรองข้อมูลโดยใช้ conditional logic และวิธีใช้ expressions ใน nodes โดยใช้ [If node](/integrations/builtin/core-nodes/n8n-nodes-base.if.md)

หลังจากขั้นตอนนี้ workflow ของคุณควรมีลักษณะดังนี้:

[[ workflowDemo("file:////courses/level-one/chapter-5/chapter-5.3.json") ]]

ในการแทรกเฉพาะ processing orders ลงใน Airtable เราต้องกรองข้อมูลของเราตาม `orderStatus` โดยพื้นฐานแล้ว เราต้องการบอกโปรแกรมว่า _ถ้า_ `orderStatus` เป็น processing _แล้ว_ ให้แทรก records ทั้งหมดที่มีสถานะนี้ลงใน Airtable; _มิฉะนั้น_ ตัวอย่างเช่น ถ้า `orderStatus` ไม่ใช่ *processing* ให้คำนวณผลรวมของ orders ทั้งหมดที่มี `orderStatus` อื่น (`booked`)

คำสั่ง if-then-else นี้คือ conditional logic ใน n8n workflows คุณสามารถเพิ่ม conditional logic ด้วย [If node](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) ซึ่งจะแยก workflow ตามเงื่อนไขตาม comparison operations

/// note | If vs. Switch
หากคุณต้องการกรองข้อมูลตามค่าที่ไม่ใช่แค่ boolean (true และ false) ให้ใช้ [Switch node](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md) Switch node คล้ายกับ If node แต่รองรับ output connectors หลายตัว
///

## Add If node before the Airtable node

ขั้นแรก มาเพิ่ม If node ระหว่างการเชื่อมต่อจาก HTTP Request node ไปยัง Airtable node กัน:

1. Hover over the arrow connection the **HTTP Request** node and the **Airtable** node.
2. Select the **+** sign between the HTTP Request node and the Airtable node.

## Configure the If node

การเลือกเครื่องหมายบวกจะลบการเชื่อมต่อของ Airtable node กับ HTTP request ตอนนี้ มาเพิ่ม If node ที่เชื่อมต่อกับ HTTP Request node กัน:

1. Search for the If node.
2. Select it when it appears in the search.

สำหรับ If node เราจะใช้ expression

/// note | Expressions
[expression](/glossary.md#expression-n8n) คือสตริงของอักขระและสัญลักษณ์ในภาษาโปรแกรมที่สามารถประเมินค่าเพื่อให้ได้ค่า ซึ่งมักจะเป็นไปตาม input ของมัน ใน n8n workflows คุณสามารถใช้ expressions ใน node เพื่ออ้างอิงถึง node อื่นสำหรับ input data ในตัวอย่างของเรา If node อ้างอิงถึง data ที่ output โดย HTTP Request node
///

ในหน้าต่าง If node กำหนดค่า parameters:

- ตั้งค่า placeholder `value1` เป็น `{{ $json.orderStatus }}` ด้วยขั้นตอนต่อไปนี้:
    1. Hover over the value1 field.
    2. Select the **Expression** tab on the right side of the `value1` field.
    3. Next, open the expression editor by selecting the link icon:
    <figure><img src="/_images/courses/level-one/chapter-five/l1-c5-5-3-if-node-open-editor.png" alt="Opening the Expression Editor" style="width:100%"><figcaption align = "center"><i>Opening the Expression Editor</i></figcaption></figure>
    4. Use the left-side panel to select **HTTP Request** >  **orderStatus** and drag it into the **Expression** field in the center of the window.
    <figure><img src="/_images/courses/level-one/chapter-five/l1-c5-5-3-if-node-expression-editor.png" alt="Expression Editor in the IF node" style="width:100%"><figcaption align = "center"><i>Expression Editor in the If node</i></figcaption></figure>
    6. Once you add the expression, close the **Edit Expression** dialog.

- **Operation**: Select **String** > **is equal to**
- Set the `value2` placeholder to `processing`.

/// warning | Data Type
ตรวจสอบให้แน่ใจว่าได้เลือก data type ที่ถูกต้อง (boolean, date & time, number หรือ string) เมื่อคุณเลือก **Operation**
///

เลือก **Test step** เพื่อทดสอบ If node

ผลลัพธ์ของคุณควรมีลักษณะดังนี้:

<figure><img src="/_images/courses/level-one/chapter-five/l1-c5-5-3-if-node-output.png" alt="If node output" style="width:100%"><figcaption align = "center"><i>If node output</i></figcaption></figure>

โปรดทราบว่า orders ที่มี `processing` order status ควรแสดงสำหรับ output **True Branch** ในขณะที่ orders ที่มี `booked` order status ควรแสดงใน output **False Branch**

ปิดมุมมองรายละเอียด If node เมื่อคุณทำเสร็จแล้ว

## Insert data into Airtable

ต่อไป เราต้องการแทรกข้อมูลนี้ลงใน Airtable จำสิ่งที่ Nathan พูดในตอนท้ายของบทเรียน [Inserting data into Airtable](/courses/level-one/chapter-5/chapter-5.2.md) ได้ไหม?

> ฉันต้องการแทรกเฉพาะ processing orders ลงในตารางจริงๆ...

เนื่องจาก Nathan ต้องการเฉพาะ `processing` orders ในตาราง เราจะเชื่อมต่อ Airtable node เข้ากับ connector `true` ของ If node

ในกรณีนี้ เนื่องจาก Airtable node อยู่บน canvas ของเราแล้ว ให้เลือก connector `true` ของ **If node** แล้วลากไปยัง Airtable node

ณ จุดนี้ เป็นความคิดที่ดีที่จะทดสอบ Airtable node อีกครั้ง ก่อนที่คุณจะทำ ให้เปิดตารางของคุณใน Airtable และลบแถวที่มีอยู่ทั้งหมด จากนั้นเปิดหน้าต่าง Airtable node ใน n8n แล้วเลือก **Test step**

ตรวจสอบข้อมูลของคุณใน Airtable เพื่อให้แน่ใจว่า workflow ของคุณเพิ่มเฉพาะ orders ที่ถูกต้อง (orders ที่มี `orderStatus` เป็น `processing`) ตอนนี้ควรมี 14 records แทนที่จะเป็น 30

ณ จุดนี้ workflow ของคุณควรมีลักษณะดังนี้:

[[ workflowDemo("file:////courses/level-one/chapter-5/chapter-5.3.json") ]]

## What's next?

**Nathan 🙋**: If node นี้มีประโยชน์มากสำหรับการกรองข้อมูล! ตอนนี้ฉันมีข้อมูลทั้งหมดเกี่ยวกับ processing orders แล้ว จริงๆ แล้วฉันต้องการแค่ `employeeName` และ `orderID` แต่ฉันเดาว่าฉันสามารถเก็บ fields อื่นๆ ทั้งหมดไว้เผื่อกรณีฉุกเฉินได้

**You 👩‍🔧**: จริงๆ แล้ว ฉันไม่แนะนำให้ทำอย่างนั้น การแทรกข้อมูลมากขึ้นต้องใช้พลังการประมวลผลมากขึ้น การถ่ายโอนข้อมูลช้าลงและใช้เวลานานขึ้น และใช้ทรัพยากรพื้นที่จัดเก็บในตารางของคุณมากขึ้น ในกรณีเฉพาะนี้ 14 records ที่มี 5 fields อาจดูเหมือนไม่สร้างความแตกต่างอย่างมีนัยสำคัญ แต่ถ้าธุรกิจของคุณเติบโตเป็นพัน records และหลายสิบ fields สิ่งต่างๆ จะเพิ่มขึ้นและแม้แต่คอลัมน์พิเศษเพียงคอลัมน์เดียวก็อาจส่งผลต่อประสิทธิภาพได้

**Nathan 🙋**: โอ้ นั่นเป็นเรื่องดีที่ได้รู้ คุณสามารถเลือกเพียงสอง fields จาก processing orders ได้หรือไม่?

**You 👩‍🔧**: แน่นอน ฉันจะทำในขั้นตอนถัดไป
