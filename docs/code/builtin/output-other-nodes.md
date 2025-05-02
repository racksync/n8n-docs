---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Methods for working with the output of other nodes.
contentType: reference
hide:
  - toc
---

# Output of other nodes

Methods สำหรับการทำงานกับ output ของ node อื่นๆ Methods และ variables บางตัวไม่สามารถใช้งานได้ใน Code node

/// note | Python support
คุณสามารถใช้ Python ใน Code node ได้ แต่ไม่สามารถใช้ใน expressions ได้
///
=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `$("<node-name>").all(branchIndex?, runIndex?)` | คืนค่า items ทั้งหมดจาก node ที่ระบุ หากไม่ได้ระบุ `branchIndex` จะใช้ output ที่เชื่อมต่อ `node-name` กับ node ที่คุณใช้ expression หรือ code เป็นค่าเริ่มต้น | :white_check_mark: |
	| `$("<node-name>").first(branchIndex?, runIndex?)` | item แรกที่ส่งออกจาก node ที่ระบุ หากไม่ได้ระบุ `branchIndex` จะใช้ output ที่เชื่อมต่อ `node-name` กับ node ที่คุณใช้ expression หรือ code เป็นค่าเริ่มต้น | :white_check_mark: |
	| `$("<node-name>").last(branchIndex?, runIndex?)` | item สุดท้ายที่ส่งออกจาก node ที่ระบุ หากไม่ได้ระบุ `branchIndex` จะใช้ output ที่เชื่อมต่อ `node-name` กับ node ที่คุณใช้ expression หรือ code เป็นค่าเริ่มต้น | :white_check_mark: |
	| `$("<node-name>").item` | item ที่เชื่อมโยงกัน นี่คือ item ใน node ที่ระบุซึ่งใช้ในการสร้าง item ปัจจุบัน โปรดดู [Item linking](/data/data-mapping/data-item-linking/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการเชื่อมโยง item | :x: |
	| `$("<node-name>").params` | Object ที่มี query settings ของ node ที่ระบุ ซึ่งรวมถึงข้อมูล เช่น operation ที่รัน, result limits และอื่นๆ | :white_check_mark: |
	| `$("<node-name>").context` | Boolean ใช้ได้เฉพาะเมื่อทำงานกับ Loop Over Items node ให้ข้อมูลเกี่ยวกับสิ่งที่เกิดขึ้นใน node ใช้เพื่อตรวจสอบว่า node ยังคงประมวลผล items อยู่หรือไม่ | :white_check_mark: |
	| `$("<node-name>").itemMatching(currentNodeInputIndex)` | ใช้แทน `$("<node-name>").item` ใน Code node หากคุณต้องการติดตามย้อนกลับจาก input item | :white_check_mark: |
=== "Python"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `_("<node-name>").all(branchIndex?, runIndex?)` | คืนค่า items ทั้งหมดจาก node ที่ระบุ หากไม่ได้ระบุ `branchIndex` จะใช้ output ที่เชื่อมต่อ `node-name` กับ node ที่คุณใช้ expression หรือ code เป็นค่าเริ่มต้น | :white_check_mark: |
	| `_("<node-name>").first(branchIndex?, runIndex?)` | item แรกที่ส่งออกจาก node ที่ระบุ หากไม่ได้ระบุ `branchIndex` จะใช้ output ที่เชื่อมต่อ `node-name` กับ node ที่คุณใช้ expression หรือ code เป็นค่าเริ่มต้น | :white_check_mark: |
	| `_("<node-name>").last(branchIndex?, runIndex?)` | item สุดท้ายที่ส่งออกจาก node ที่ระบุ หากไม่ได้ระบุ `branchIndex` จะใช้ output ที่เชื่อมต่อ `node-name` กับ node ที่คุณใช้ expression หรือ code เป็นค่าเริ่มต้น | :white_check_mark: |
	| `_("<node-name>").item` | item ที่เชื่อมโยงกัน นี่คือ item ใน node ที่ระบุซึ่งใช้ในการสร้าง item ปัจจุบัน โปรดดู [Item linking](/data/data-mapping/data-item-linking/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการเชื่อมโยง item | :x: |
	| `_("<node-name>").params` | Object ที่มี query settings ของ node ที่ระบุ ซึ่งรวมถึงข้อมูล เช่น operation ที่รัน, result limits และอื่นๆ | :white_check_mark: |
	| `_("<node-name>").context` | Boolean ใช้ได้เฉพาะเมื่อทำงานกับ Loop Over Items node ให้ข้อมูลเกี่ยวกับสิ่งที่เกิดขึ้นใน node ใช้เพื่อตรวจสอบว่า node ยังคงประมวลผล items อยู่หรือไม่ | :white_check_mark: |
	| `_("<node-name>").itemMatching(currentNodeInputIndex)` | ใช้แทน `_("<node-name>").item` ใน Code node หากคุณต้องการติดตามย้อนกลับจาก input item โปรดดู [Retrieve linked items from earlier in the workflow](/code/cookbook/builtin/itemmatching.md) สำหรับตัวอย่าง | :white_check_mark: |
