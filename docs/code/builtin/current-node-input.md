---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Methods สำหรับจัดการ input ของ node ปัจจุบัน
contentType: reference
hide:
  - toc
---

# Current node input

Methods สำหรับการทำงานกับ input ของ node ปัจจุบัน Methods และ variables บางตัวไม่สามารถใช้งานได้ใน Code node

/// note | Python support
คุณสามารถใช้ Python ใน Code node ได้ แต่ไม่สามารถใช้ใน expressions ได้
///
=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `$binary` | รูปแบบย่อของ `$input.item.binary` ข้อมูล binary ที่เข้ามาจาก node | :x: |
	| `$input.item` | input item ของ node ปัจจุบันที่กำลังประมวลผล โปรดดู [Item linking](/data/data-mapping/data-item-linking/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ paired items และ item linking | :white_check_mark: |
	| `$input.all()` | input items ทั้งหมดใน node ปัจจุบัน | :white_check_mark: |
	| `$input.first()` | input item แรกใน node ปัจจุบัน | :white_check_mark: |
	| `$input.last()` | input item สุดท้ายใน node ปัจจุบัน | :white_check_mark: |
	| `$input.params` | Object ที่มี query settings ของ node ก่อนหน้า ซึ่งรวมถึงข้อมูล เช่น operation ที่รัน, result limits และอื่นๆ | :white_check_mark: |
	| `$json` | รูปแบบย่อของ `$input.item.json` ข้อมูล JSON ที่เข้ามาจาก node โปรดดู [Data structure](/data/data-structure.md) สำหรับข้อมูลเกี่ยวกับโครงสร้าง item | :white_check_mark: (เมื่อรันครั้งเดียวสำหรับแต่ละ item) |
	| `$input.context.noItemsLeft` | Boolean ใช้ได้เฉพาะเมื่อทำงานกับ Loop Over Items node ให้ข้อมูลเกี่ยวกับสิ่งที่เกิดขึ้นใน node ใช้เพื่อตรวจสอบว่า node ยังคงประมวลผล items อยู่หรือไม่ | :white_check_mark: |
=== "Python"
	| Method | Description | 
	| ------ | ----------- | 
	| `_input.item` | input item ของ node ปัจจุบันที่กำลังประมวลผล โปรดดู [Item linking](/data/data-mapping/data-item-linking/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ paired items และ item linking | 
	| `_input.all()` | input items ทั้งหมดใน node ปัจจุบัน | 
	| `_input.first()` | input item แรกใน node ปัจจุบัน | 
	| `_input.last()` | input item สุดท้ายใน node ปัจจุบัน | 
	| `_input.params` | Object ที่มี query settings ของ node ก่อนหน้า ซึ่งรวมถึงข้อมูล เช่น operation ที่รัน, result limits และอื่นๆ | 
	| `_json` | รูปแบบย่อของ `_input.item.json` ข้อมูล JSON ที่เข้ามาจาก node โปรดดู [Data structure](/data/data-structure.md) สำหรับข้อมูลเกี่ยวกับโครงสร้าง item ใช้ได้เมื่อคุณตั้งค่า **Mode** เป็น **Run Once for Each Item** | 
	| `_input.context.noItemsLeft` | Boolean ใช้ได้เฉพาะเมื่อทำงานกับ Loop Over Items node ให้ข้อมูลเกี่ยวกับสิ่งที่เกิดขึ้นใน node ใช้เพื่อตรวจสอบว่า node ยังคงประมวลผล items อยู่หรือไม่ |
