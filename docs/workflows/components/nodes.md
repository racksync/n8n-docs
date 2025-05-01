---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: A node is an entry point for retrieving data, a function to process data, or an exit for sending data.
contentType: howto
---

# Nodes

[Nodes](/glossary.md#node-n8n) เป็นส่วนประกอบสำคัญของ [workflow](/glossary.md#workflow-n8n) ทำหน้าที่หลากหลาย รวมถึง:

* การเริ่มต้น workflow
* การดึงและส่งข้อมูล
* การประมวลผลและจัดการข้อมูล

n8n มีชุดของ built-in nodes ให้ใช้งาน รวมถึงความสามารถในการสร้าง nodes ของคุณเอง โปรดดูที่:

* [Built-in integrations](/integrations/builtin/node-types.md) เพื่อเรียกดู node library
* [Community nodes](/integrations/community-nodes/installation/index.md) สำหรับคำแนะนำในการค้นหาและติดตั้ง nodes ที่สร้างโดย community
* [Creating nodes](/integrations/creating-nodes/overview.md) เพื่อเริ่มต้นสร้าง nodes ของคุณเอง

## Add a node to your workflow

### Add a node to an empty workflow

1. เลือก **Add first step** n8n จะเปิด nodes panel ซึ่งคุณสามารถค้นหาหรือเรียกดู [trigger nodes](/glossary.md#trigger-node-n8n) ได้
2. เลือก trigger ที่คุณต้องการใช้

    /// note | Choose the correct app event
	หากคุณเลือก **On App Event** n8n จะแสดงรายการบริการทั้งหมดที่รองรับ ใช้รายการนี้เพื่อเรียกดู integrations ของ n8n และ trigger workflow เพื่อตอบสนองต่อ event ในบริการที่คุณเลือก ไม่ใช่ทุก integrations ที่มี triggers หากต้องการดูว่าคุณสามารถใช้ตัวใดเป็น trigger ได้ ให้เลือก node หากมี trigger ให้ใช้งาน คุณจะเห็นมันอยู่ที่ด้านบนสุดของรายการ operations ที่มีอยู่

	ตัวอย่างเช่น นี่คือ trigger สำหรับ Asana:

	![Screenshot of the Asana node operations list, showing the Recommended section at the top of the list](/_images/workflows/components/nodes/recommended-trigger.png)
	///

### Add a node to an existing workflow

เลือก connector **Add node** <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span> n8n จะเปิด nodes panel ซึ่งคุณสามารถค้นหาหรือเรียกดู nodes ทั้งหมดได้

--8<-- "_snippets/integrations/builtin/node-operations.md"

## Node controls

หากต้องการดู node controls ให้วางเมาส์เหนือ node บน canvas:

* **Test step** <span class="inline-image">![Test step icon](/_images/common-icons/play-node.png){.off-glb}</span>: รัน node
* **Deactivate** <span class="inline-image">![Deactivate node icon](/_images/common-icons/power-off.png){.off-glb}</span>: ปิดการใช้งาน node
* **Delete** <span class="inline-image">![Delete node icon](/_images/common-icons/delete-node.png){.off-glb}</span>: ลบ node
* **Node context menu** <span class="inline-image">![Node context menu icon](/_images/common-icons/node-context-menu.png){.off-glb}</span>: เลือกการกระทำของ node การกระทำที่มีอยู่:
	* Open node
	* Test step
	* Rename node
	* Deactivate node
	* Pin node
	* Copy node
	* Duplicate node
	* Select all
	* Clear selection
	* Delete node

## Node settings

การตั้งค่า node ภายใต้แท็บ **Settings** ช่วยให้คุณควบคุมพฤติกรรมของ node และเพิ่มบันทึกย่อของ node ได้

เมื่อเปิดใช้งานหรือตั้งค่า จะทำสิ่งต่อไปนี้:

* **Request Options**: เลือก **Add Option** เพื่อดูและเลือกตัวเลือกเหล่านี้
	- **Batching**: ควบคุมวิธีการ batch รายการ input จำนวนมาก
	- **Ignore SSL Issues**: ดาวน์โหลด response แม้ว่าจะไม่สามารถตรวจสอบ SSL ได้
	- **Proxy**: ใช้ตัวเลือกนี้หากคุณต้องการระบุ HTTP proxy
	- **Timeout**: ตั้งค่า timeout สำหรับ request เป็น ms
* **Always Output Data**: node จะคืนค่า item ว่างเปล่าแม้ว่า node จะไม่คืนข้อมูลใดๆ ในระหว่างการ execution โปรดระวังการตั้งค่านี้ใน IF nodes เนื่องจากอาจทำให้เกิด infinite loop ได้
* **Execute Once**: node จะ execute เพียงครั้งเดียว โดยใช้ข้อมูลจาก item แรกที่ได้รับ จะไม่ประมวลผล item เพิ่มเติมใดๆ
* **Retry On Fail**: เมื่อ execution ล้มเหลว node จะรันซ้ำจนกว่าจะสำเร็จ
* **On Error**:
    - **Stop Workflow**: หยุด workflow ทั้งหมดเมื่อเกิดข้อผิดพลาด ป้องกันการ execute node ต่อไป
    - **Continue**: ดำเนินการต่อไปยัง node ถัดไปแม้จะมีข้อผิดพลาด โดยใช้ข้อมูลที่ถูกต้องล่าสุด
    - **Continue (using error output)**: ดำเนินการ execute workflow ต่อไป โดยส่งข้อมูลข้อผิดพลาดไปยัง node ถัดไปเพื่อการจัดการที่เป็นไปได้

คุณสามารถบันทึกเอกสาร workflow ของคุณโดยใช้ node notes:

* **Notes**: บันทึกย่อที่จะบันทึกพร้อมกับ node
* **Display note in flow**: หากเปิดใช้งาน n
