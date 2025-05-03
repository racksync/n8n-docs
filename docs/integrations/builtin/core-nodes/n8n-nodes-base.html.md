---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: HTML
description: คู่มือ HTML node สำหรับจัดการและแปลงข้อมูล HTML ใน n8n
contentType: [integration, reference]
priority: high
---

# HTML

HTML node ใช้สำหรับจัดการกับ HTML ใน n8n

/// note | HTML Extract node
HTML node มาแทนที่ HTML Extract node ตั้งแต่เวอร์ชัน 0.213.0 ถ้าใช้ n8n เวอร์ชันเก่า สามารถดู [HTML Extract node documentation](https://github.com/n8n-io/n8n-docs/blob/86fe33b681621e618e3adcab9a27e8605dbc23ad/docs/integrations/builtin/core-nodes/n8n-nodes-base.htmlextract.md){:target=_blank .external-link}
///
/// warning | Cross-site scripting
ถ้าใช้ HTML node เพื่อสร้าง HTML template อาจเกิด [XSS (cross-site scripting)](https://owasp.org/www-community/attacks/xss/){:target=_blank .external-link} ได้ ซึ่งเป็นความเสี่ยงด้านความปลอดภัย ควรระวัง input ที่ไม่ไว้ใจ
///

## Operations

* [**Generate HTML template**](#generate-html-template): ใช้สร้าง HTML template สามารถนำข้อมูลจาก workflow มาแสดงเป็น HTML ได้
* [**Extract HTML content**](#extract-html-content): ดึงข้อมูลจาก HTML source ซึ่งอาจอยู่ใน JSON หรือไฟล์ binary (`.html`)
* [**Convert to HTML Table**](#convert-to-html-table): แปลงข้อมูลเป็น HTML table

parameter และ options ของ node จะเปลี่ยนไปตาม operation ที่เลือก ดูรายละเอียดแต่ละ operation ด้านล่าง

## Generate HTML template

สร้าง HTML template สามารถนำข้อมูลจาก workflow มาแสดงเป็น HTML ได้

คุณสามารถใส่:

* HTML มาตรฐาน
* CSS ใน `<style>` tag
* JavaScript ใน `<script>` tag (n8n จะไม่ execute JavaScript)
* Expressions ที่ครอบด้วย `{{}}`

สามารถใช้ [Expressions](/code/expressions.md) ใน template ได้ รวมถึง [Built-in methods and variables](/code/builtin/overview.md) ของ n8n

## Extract HTML Content

ดึงข้อมูลจาก HTML source ซึ่งอาจอยู่ใน JSON หรือไฟล์ binary (`.html`)

ตั้งค่าดังนี้:

### Source Data

เลือกประเภท source ของ HTML ที่ต้องการดึงข้อมูล มีให้เลือก:

* **JSON**: ถ้าเลือกแบบนี้ ให้กรอก **JSON Property** คือชื่อ property ที่เก็บ HTML ที่ต้องการดึง (อาจเป็น string หรือ array ของ string)
* **Binary**: ถ้าเลือกแบบนี้ ให้กรอก **Input Binary Field** คือชื่อ field ที่เก็บ HTML ที่ต้องการดึง (อาจเป็น string หรือ array ของ string)

### Extraction Values

- **Key**: กรอกชื่อ key ที่จะใช้เก็บค่าที่ดึงได้
- **CSS Selector**: กรอก CSS selector ที่ต้องการค้นหา
- **Return Value**: เลือกประเภทข้อมูลที่ต้องการคืนค่า มีให้เลือก:
	- **Attribute**: คืนค่า attribute เช่น `class` ของ element
		- ถ้าเลือกแบบนี้ ให้กรอกชื่อ **Attribute** ที่ต้องการดึงค่า
	- **HTML**: คืนค่า HTML ที่อยู่ใน element
	- **Text**: คืนค่า text content ของ element
		- ถ้าเลือกแบบนี้ สามารถกรอก selector ที่ต้องการข้าม (skip) ใน **Skip Selectors** (คั่นด้วย comma)
	- **Value**: คืนค่า value ของ input, select หรือ textarea
- **Return Array**: เลือกว่าจะคืนค่าหลายรายการเป็น array (เปิด) หรือ string เดียว (ปิด)

### Extract HTML Content options

ตั้งค่าเพิ่มเติมสำหรับ operation นี้:

* **Trim Values**: เลือกว่าจะลบช่องว่างและขึ้นบรรทัดใหม่ที่ต้น/ท้ายค่าทั้งหมด (เปิด) หรือไม่ลบ (ปิด)
* **Clean Up Text**: เลือกว่าจะลบช่องว่างต้น/ท้ายและขึ้นบรรทัดใหม่ และลดช่องว่างซ้อนกันให้เหลือช่องว่างเดียว (เปิด) หรือไม่ (ปิด)

## Convert to HTML Table

operation นี้ต้องรับข้อมูลจาก node อื่น ไม่มี parameter ให้ตั้งค่า มี options ดังนี้:

* **Capitalize Headers**: เลือกว่าจะให้ header ของ table เป็นตัวพิมพ์ใหญ่ (เปิด) หรือไม่ (ปิด)
* **Custom Styling**: เลือกว่าจะใช้ custom styling (เปิด) หรือไม่ (ปิด)
* **Caption**: กรอก caption ที่ต้องการแสดงบน table
* **Table Attributes**: กรอก attributes ที่ต้องการใส่ใน `<table>` เช่น style
* **Header Attributes**: กรอก attributes ที่ต้องการใส่ใน `<th>`
* **Row Attributes**: กรอก attributes ที่ต้องการใส่ใน `<tr>`
* **Cell Attributes**: กรอก attributes ที่ต้องการใส่ใน `<td>`

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'html') ]]
