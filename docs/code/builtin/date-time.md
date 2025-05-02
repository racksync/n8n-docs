---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Methods for working with date and time.
contentType: reference
hide:
  - toc
---

# Built-in date and time methods

Methods สำหรับการทำงานกับ date และ time

/// note | Python support
คุณสามารถใช้ Python ใน Code node ได้ แต่ไม่สามารถใช้ใน expressions ได้
///
=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `$now` | Luxon object ที่มี timestamp ปัจจุบัน เทียบเท่ากับ `DateTime.now()` | :white_check_mark: |
	| `$today` | Luxon object ที่มี timestamp ปัจจุบัน ปัดเศษลงเป็นวัน เทียบเท่ากับ `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })` | :white_check_mark: |
=== "Python"
	| Method | Description | 
	| ------ | ----------- | 
	| `_now` | Luxon object ที่มี timestamp ปัจจุบัน เทียบเท่ากับ `DateTime.now()` | 
	| `_today` | Luxon object ที่มี timestamp ปัจจุบัน ปัดเศษลงเป็นวัน เทียบเท่ากับ `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })` | 

n8n ส่งผ่าน dates ระหว่าง nodes เป็น strings ดังนั้นคุณต้อง parse พวกมัน Luxon ช่วยให้คุณทำสิ่งนี้ได้ โปรดดู [Date and time with Luxon](/code/cookbook/luxon.md) สำหรับข้อมูลเพิ่มเติม

n8n มี convenience functions ที่สร้างไว้ให้เพื่อรองรับการแปลงข้อมูลใน expressions สำหรับ dates โปรดดู [Data transformation functions | Dates](/code/builtin/data-transformation-functions/dates.md) สำหรับข้อมูลเพิ่มเติม
