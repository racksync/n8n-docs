---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: reference
---

# Item linking errors

ใน n8n คุณสามารถอ้างอิงข้อมูลจาก node ก่อนหน้าใดก็ได้ ไม่จำเป็นต้องเป็น node ที่อยู่ก่อนหน้าทันที: สามารถเป็น node ใดก็ได้ที่อยู่ก่อนหน้าในสายโซ่ เมื่ออ้างอิง node ที่อยู่ห่างออกไป คุณจะใช้ expression syntax `$(node_name).item`

<figure markdown>
![A diagram showing the threads linking multiple items back through a workflow](/_images/data/data-mapping/data-item-linking/item-linking-multiple-lines.png)
<figcaption markdown>แผนภาพแสดงสายใย (threads) สำหรับ item ต่างๆ เนื่องจากการ link item คุณสามารถรับนักแสดงสำหรับภาพยนตร์แต่ละเรื่องได้โดยใช้ `$('Get famous movie actors').item`</figcaption>
</figure>

เนื่องจาก node ก่อนหน้าสามารถมี item ได้หลายรายการ n8n จึงจำเป็นต้องรู้ว่าจะใช้รายการใด เมื่อใช้ `.item` n8n จะคำนวณสิ่งนี้ให้คุณเบื้องหลัง โปรดดู [Item linking concepts](/data/data-mapping/data-item-linking/item-linking-concepts.md) สำหรับข้อมูลโดยละเอียดเกี่ยวกับวิธีการทำงานนี้

`.item` จะล้มเหลวหากข้อมูลหายไป ในการหาว่า item ใดที่จะใช้ n8n จะรักษา thread ย้อนกลับไปผ่าน node ต่างๆ ของ workflow สำหรับแต่ละ item สำหรับ item ที่กำหนด thread นี้จะบอก n8n ว่า item ใดใน node ก่อนหน้าที่สร้างมันขึ้นมา ในการค้นหา item ที่ตรงกันใน node ก่อนหน้าที่กำหนด n8n จะตาม thread นี้ย้อนกลับไปจนกว่าจะถึง node ดังกล่าว

เมื่อใช้ `.item` n8n จะแสดงข้อผิดพลาดเมื่อ:

-   thread ขาดหาย
-   thread ชี้ไปยัง item มากกว่าหนึ่งรายการใน node ก่อนหน้า (เนื่องจากไม่ชัดเจนว่าจะใช้รายการใด)

ในการแก้ไขข้อผิดพลาดเหล่านี้ คุณสามารถหลีกเลี่ยงการใช้ `.item` หรือแก้ไขสาเหตุที่แท้จริง

คุณสามารถหลีกเลี่ยง `.item` ได้โดยใช้ `.first()`, `.last()` หรือ `.all()[index]` แทน วิธีการเหล่านี้ต้องการให้คุณทราบตำแหน่งของ item ที่คุณกำลังกำหนดเป้าหมายภายใน output item ของ node เป้าหมาย โปรดดู [Built in methods and variables | Output of other nodes](/code/builtin/output-other-nodes.md) สำหรับรายละเอียดเพิ่มเติมเกี่ยวกับ method เหล่านี้

การแก้ไขสาเหตุที่แท้จริงขึ้นอยู่กับข้อผิดพลาดที่แน่นอน

### Fix for 'Info for expressions missing from previous node'

หากคุณเห็นข้อความแสดงข้อผิดพลาดนี้:

> ERROR: Info for expression missing from previous node

มี node ในสายโซ่ที่ไม่ส่งคืนข้อมูลการจับคู่ (pairing information) วิธีแก้ปัญหาที่นี่ขึ้นอยู่กับประเภทของ node ก่อนหน้า:

-   Code nodes: ตรวจสอบให้แน่ใจว่าคุณส่งคืน input item ใดที่ node ใช้ในการผลิตแต่ละ output item โปรดดู [Item linking in the code node](/data/data-mapping/data-item-linking/item-linking-code-node.md) สำหรับข้อมูลเพิ่มเติม
-   Custom หรือ community nodes: ผู้สร้าง node จำเป็นต้องอัปเดต node เพื่อส่งคืน input item ใดที่ใช้ในการผลิตแต่ละ output item โปรดดู [Item linking for node creators](/data/data-mapping/data-item-linking/item-linking-node-building.md) สำหรับข้อมูลเพิ่มเติม

### Fix for 'Multiple matching items for expression'

นี่คือข้อความแสดงข้อผิดพลาด:

> ERROR: Multiple matching items for expression

บางครั้ง n8n ใช้หลาย item เพื่อสร้าง item เดียว ตัวอย่างเช่น node Summarize, Aggregate และ Merge node เหล่านี้สามารถรวมข้อมูลจากหลาย item ได้

เมื่อคุณใช้ `.item` และมีรายการที่ตรงกันหลายรายการที่เป็นไปได้ n8n จะไม่รู้ว่าจะใช้รายการใด ในการแก้ปัญหานี้ คุณสามารถ:

-   ใช้ `.first()`, `.last()` หรือ `.all()[index]` แทน โปรดดู [Built in methods and variables | Output of other nodes](/code/builtin/output-other-nodes.md) สำหรับรายละเอียดเพิ่มเติมเกี่ยวกับ method เหล่านี้
-   อ้างอิง node อื่นที่มีข้อมูลเดียวกัน แต่ไม่มี item ที่ตรงกันหลายรายการ
