---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

<!-- vale from-microsoft.We = NO -->
<!-- vale from-microsoft.FirstPerson = NO -->
# 4. Setting Values for Processing Orders

ในขั้นตอนนี้ของ workflow คุณจะได้เรียนรู้วิธีเลือกและตั้งค่าข้อมูลก่อนที่จะถ่ายโอนไปยัง Airtable โดยใช้ Edit Fields (Set) node หลังจากขั้นตอนนี้ workflow ของคุณควรมีลักษณะดังนี้:

[[ workflowDemo("file:////courses/level-one/chapter-5/chapter-5.4.json") ]]

ขั้นตอนต่อไปใน workflow ของ Nathan คือการกรองข้อมูลเพื่อแทรกเฉพาะ `employeeName` และ `orderID` ของ `processing` orders ทั้งหมดลงใน Airtable

สำหรับสิ่งนี้ คุณต้องใช้ [Edit Fields (Set) node](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) ซึ่งช่วยให้คุณสามารถเลือกและตั้งค่าข้อมูลที่คุณต้องการถ่ายโอนจาก node หนึ่งไปยังอีก node หนึ่งได้

/// note | Edit Fields node
Edit Fields node สามารถตั้งค่าข้อมูลใหม่ทั้งหมดรวมถึงเขียนทับข้อมูลที่มีอยู่แล้วได้ node นี้มีความสำคัญอย่างยิ่งใน workflows ที่คาดหวังข้อมูลขาเข้าจาก nodes ก่อนหน้า เช่น เมื่อแทรกค่าลงใน spreadsheets หรือ databases
///

## Add another node before the Airtable node

ใน workflow ของคุณ ให้เพิ่ม node อีกตัวก่อน **Airtable node** จาก **If node** ในลักษณะเดียวกับที่เราทำในบทเรียน [Filtering Orders](/courses/level-one/chapter-5/chapter-5.3.md#add-if-node-before-the-airtable-node) บน connector `true` ของ If node อย่าลังเลที่จะลาก Airtable node ออกไปให้ไกลขึ้นหาก canvas ของคุณรู้สึกแออัด

## Configure the Edit Fields node

ตอนนี้ค้นหา **Edit Fields (Set) node** หลังจากที่คุณเลือกเครื่องหมาย **+** ที่ออกมาจาก connector `true` ของ If node

เมื่อหน้าต่าง Edit Fields node เปิดอยู่ ให้กำหนดค่า parameters เหล่านี้:

- Ensure **Mode** is set to **Manual Mapping**.
- ในขณะที่คุณสามารถใช้ **Expression editor** ที่เราใช้ในบทเรียน [Filtering Orders](/courses/level-one/chapter-5/chapter-5.3.md) ได้ ครั้งนี้ มาลาก fields จาก **Input** ไปยัง **Fields to Set** กัน:
    - Drag **If** > **orderID** as the first field.
    - Drag **If** > **employeeName** as the second field.
- Ensure that **Include Other Input Fields** is set to false.

เลือก **Test step** คุณควรเห็นผลลัพธ์ต่อไปนี้:

<figure><img src="/_images/courses/level-one/chapter-five/l1-c5-4-set-node.png" alt="Edit Fields (Set) node" style="width:100%"><figcaption align = "center"><i>Edit Fields (Set) node</i></figcaption></figure>

## Add data to Airtable

ต่อไป มาแทรกค่าเหล่านี้ลงใน Airtable กัน:

1. Go to your Airtable base.
2. Add a new table called `processingOrders`.
3. Replace the existing columns with two new columns:
    - `orderID` (primary field): Number
    - `employeeName`: Single line text

    ///note | Reminder
    หากคุณติดขัด โปรดดูบทเรียน [Inserting data into Airtable](/courses/level-one/chapter-5/chapter-5.2.md)
    ///

4. Delete the three empty rows in the new table.
5. In n8n, connect the Edit Fields node** connector to the **Airtable node**.
6. Update the Airtable node configuration to point to the new `processingOrders` table instead of the `orders` table.
7. Test your Airtable node to be sure it inserts records into the new `processingOrders` table.

ณ จุดนี้ workflow ของคุณควรมีลักษณะดังนี้:

[[ workflowDemo("file:////courses/level-one/chapter-5/chapter-5.4.json") ]]

## What's next?

**Nathan 🙋**: คุณ automate งานของฉันไปครึ่งหนึ่งแล้ว! ตอนนี้ฉันยังต้องคำนวณ booked orders สำหรับเพื่อนร่วมงานของฉัน เราสามารถ automate สิ่งนั้นได้ด้วยหรือไม่?

**You 👩‍🔧**: ได้! ในขั้นตอนถัดไป ฉันจะใช้ JavaScript code บางส่วนใน node เพื่อคำนวณ booked orders
