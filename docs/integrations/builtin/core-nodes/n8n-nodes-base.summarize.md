---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Summarize
description: Documentation for the Summarize node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: high
---

# Summarize

ใช้ Summarize node เพื่อรวมข้อมูลหลายๆ item เข้าด้วยกัน คล้ายๆ กับ pivot table ใน Excel

## Node parameters

### Fields to Summarize

ใช้ fields เหล่านี้เพื่อกำหนดว่าจะสรุปข้อมูล input ยังไง

* **Aggregation**: เลือกวิธีการรวมข้อมูลในแต่ละ field ตัวเลือกเช่น:
	* **Append**: เอาค่ามาต่อกัน
		* ถ้าเลือกอันนี้ ให้เลือกว่าจะ **Include Empty Values** หรือไม่
	* **Average**: คำนวณค่าเฉลี่ยของข้อมูลตัวเลข
	* **Concatenate**: เอาค่ามาต่อกันเป็นข้อความเดียว
		* ถ้าเลือกอันนี้ ให้เลือกว่าจะ **Include Empty Values** หรือไม่
		* **Separator**: เลือกตัวคั่นระหว่างค่าที่ต่อกัน
	* **Count**: นับจำนวนค่าทั้งหมดในข้อมูล
	* **Count Unique**: นับจำนวนค่าที่ไม่ซ้ำกันในข้อมูล
	* **Max**: หาค่าสูงสุดในข้อมูลตัวเลข
	* **Min**: หาค่าต่ำสุดในข้อมูลตัวเลข
	* **Sum**: รวมค่าตัวเลขทั้งหมดเข้าด้วยกัน
* **Field**: ใส่ชื่อ field ที่อยากจะรวมข้อมูล

### Fields to Split By

ใส่ชื่อ field ใน input ที่อยากจะแยกกลุ่มสรุปข้อมูล (คล้ายๆ กับ group by) จะได้สรุปแยกตามค่าของ field เหล่านั้น

เช่น ถ้ามีข้อมูล `Sales Rep` กับ `Deal Amount` แล้วเลือก **Sum** ที่ field `Deal Amount` และ split by `Sales Rep` จะได้ยอดรวมแยกตามแต่ละ Sales Rep

ถ้าอยากใส่หลาย field ให้คั่นด้วย comma

## Node options

### Continue if Field Not Found

โดยปกติ ถ้า **Field to Summarize** ไม่มีใน item ไหนเลย node จะ error ถ้าเปิด option นี้ (turned on) จะให้ node ทำงานต่อและคืนค่าเป็น item ว่างๆ 1 อัน แทนที่จะ error

### Disable Dot Notation

โดยปกติ n8n จะเปิดใช้ dot notation เพื่ออ้างถึง child field ในรูปแบบ `parent.child` ถ้าอยากปิดการใช้ dot notation ให้เปิด option นี้ (turned on) หรือถ้าอยากใช้ dot notation ต่อไปให้ปิด (turned off)

### Output Format

เลือก format สำหรับ output แนะนำให้ใช้ option นี้ถ้าใช้ **Fields to Split By**

* **Each Split in a Separate Item**: สร้าง output แยก item สำหรับแต่ละกลุ่มที่ split
* **All Splits in a Single Item**: สร้าง output เป็น item เดียวที่รวมทุกกลุ่มที่ split

## Ignore items without valid fields to group by

ตั้งค่าว่าจะข้าม input item ที่ไม่มี **Fields to Split By** (เปิด = ข้าม, ปิด = ไม่ข้าม)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'summarize') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md"
