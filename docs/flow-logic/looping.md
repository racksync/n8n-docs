---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Looping in n8n

Looping มีประโยชน์เวลาคุณต้องการ process ข้อมูลหลายรายการ หรือทำ action เดิมซ้ำๆ เช่น ส่งข้อความหาทุก contact ใน address book ของคุณ n8n จะจัดการการวน loop ให้โดยอัตโนมัติ คุณไม่ต้องสร้าง loop เองใน workflow (ยกเว้นบาง node ดู [node exceptions](#node-exceptions))

## Using loops in n8n

node ใน n8n จะรับข้อมูลเข้ามากี่ item ก็ได้ แล้ว process ทีละ item จากนั้นส่งผลลัพธ์ออกไป คุณสามารถนึกถึงแต่ละ item ว่าเป็นข้อมูลหนึ่งแถวในตาราง output ของ node

![The Customer Datastore node output](/_images/flow-logic/looping/customer_datastore_node.png)

โดยปกติ node จะทำงานหนึ่งครั้งต่อหนึ่ง item เช่น ถ้าคุณต้องการส่งชื่อและ note ของลูกค้าแต่ละคนใน Customer Datastore node ไปที่ Slack คุณแค่

1. เชื่อม Slack node กับ Customer Datastore node
2. ตั้งค่าพารามิเตอร์
3. Execute node

คุณจะได้รับข้อความ 5 ข้อความ (ถ้ามี 5 item) คือ 1 ข้อความต่อ 1 ลูกค้า

นี่คือวิธีที่คุณ process ข้อมูลหลายรายการโดยไม่ต้องสร้าง loop เอง

### Executing nodes once

ถ้าคุณไม่ต้องการให้ node process ทุก item เช่น อยากส่ง Slack message แค่ลูกค้าคนแรก ให้เปิด **Execute Once** ใน **Settings** ของ node นั้น เหมาะกับกรณีที่ข้อมูลเข้ามาหลาย item แต่คุณอยาก process แค่ตัวแรก

## Creating loops

โดยปกติ n8n จะวน loop ให้ทุก item ที่เข้ามา แต่บางกรณีคุณต้องสร้าง loop เอง ดู [Node exceptions](#node-exceptions) สำหรับ node ที่ไม่วน loop อัตโนมัติ

### Loop until a condition is met

ถ้าต้องการวน loop จนกว่าจะตรงเงื่อนไข ให้เชื่อม output ของ node หนึ่งกลับไป input ของ node ก่อนหน้า แล้วใช้ [IF](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) node เพื่อตรวจสอบว่าจะหยุด loop เมื่อไหร่

ดู [ตัวอย่าง workflow](https://n8n.io/workflows/1130) ที่ใช้ IF node สร้าง loop:

![Editor UI view of sample workflow](/_images/flow-logic/looping/example_workflow.png)

### Loop until all items are processed

ใช้ [Loop Over Items](/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md) node ถ้าต้องการวน loop จนครบทุก item ถ้าอยาก process ทีละ item ให้ตั้ง **Batch Size** เป็น `1`

คุณสามารถแบ่งข้อมูลเป็นกลุ่มๆ เพื่อ process ทีละ batch วิธีนี้เหมาะกับกรณีที่ต้องการหลีกเลี่ยง API rate limit หรืออยาก process ข้อมูลเป็นกลุ่ม

Loop Over Items node จะหยุดทำงานเมื่อแบ่งข้อมูลครบทุก batch แล้วส่งต่อไป node ถัดไป ดังนั้นไม่ต้องใช้ IF node เพื่อหยุด loop

## Node exceptions

node และ operation ที่คุณต้องออกแบบ loop เองใน workflow:

* [CrateDB](/integrations/builtin/app-nodes/n8n-nodes-base.cratedb.md) execute ครั้งเดียวสำหรับ `insert` และ `update`
* [Code](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md) node ในโหมด **Run Once for All Items**: process ทุก item ตาม code ที่เขียน
* [Execute Workflow](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) node ในโหมด **Run Once for All Items**
* [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md): คุณต้อง handle pagination เอง ถ้า API คืนข้อมูลแบบแบ่งหน้า ต้องสร้าง loop เพื่อดึงทีละหน้า
* [Microsoft SQL](/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsql.md) execute ครั้งเดียวสำหรับ `insert`, `update`, และ `delete`
* [MongoDB](/integrations/builtin/app-nodes/n8n-nodes-base.mongodb.md) execute ครั้งเดียวสำหรับ `insert` และ `update`
* [QuestDB](/integrations/builtin/app-nodes/n8n-nodes-base.questdb.md) execute ครั้งเดียวสำหรับ `insert`
* [Redis](/integrations/builtin/app-nodes/n8n-nodes-base.redis.md):
	* Info: operation นี้ execute แค่ครั้งเดียว ไม่ว่าจะมี item กี่ตัวในข้อมูลเข้า
* [RSS Read](/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedread.md) execute ครั้งเดียวต่อ 1 URL ที่ขอ
* [TimescaleDB](/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb.md) execute ครั้งเดียวสำหรับ `insert` และ `update`
