---
title: ตัวช่วยดีบัก (Debug Helper)
description: คู่มือ Debug Helper node สำหรับทดสอบและจำลองข้อมูลใน n8n
contentType: [integration, reference]
priority: medium
---

# Debug Helper

ใช้ Debug Helper node เพื่อ trigger error แบบต่างๆ หรือ generate ข้อมูลสุ่ม เพื่อช่วยทดสอบ workflow ใน n8n

## Operations

กำหนด operation โดยเลือก **Category**:

* **Do Nothing**: ไม่ทำอะไรเลย
* [**Throw Error**](#throw-error): สร้าง error ตาม type และ message ที่กำหนด
* [**Out Of Memory**](#out-of-memory): สร้างข้อมูลขนาดใหญ่เพื่อจำลอง out of memory
* [**Generate Random Data**](#generate-random-data): สร้างข้อมูลสุ่มใน format ที่เลือก

## Node parameters

parameter ของ node จะขึ้นอยู่กับ **Category** ที่เลือก **Do Nothing** ไม่มี parameter อื่น

### Throw Error

* **Error Type**: เลือก type ของ error ที่จะ throw เลือกได้:
	* **NodeApiError**
	* **NodeOperationError**
	* **Error**
* **Error Message**: ใส่ข้อความ error ที่จะ throw

### Out Of Memory

Category นี้มี parameter เดียวคือ **Memory Size to Generate** ใส่ขนาด memory ที่ต้องการจำลอง

### Generate Random Data

* **Data Type**: เลือกประเภทข้อมูลสุ่มที่ต้องการสร้าง เลือกได้:
	* **Address**
	* **Coordinates**
	* **Credit Card**
	* **Email**
	* **IPv4**
	* **IPv6**
	* **MAC**
	* **Nanoids**: ถ้าเลือกอันนี้ต้องใส่เพิ่ม:
		* **Nanoid Alphabet**: alphabet ที่ใช้ generate nanoid
		* **Nanoid Length**: ความยาวของแต่ละ nanoid
	* **URL**
	* **User Data**
	* **UUID**
	* **Version**
* **Seed**: ถ้าอยากให้ generate ข้อมูลเดิมทุกครั้ง ให้ใส่ seed ถ้าไม่ใส่จะสุ่มใหม่ทุกครั้ง
* **Number of Items to Generate**: ใส่จำนวนข้อมูลสุ่มที่ต้องการสร้าง
* **Output as Single Array**: เลือกว่าจะ output เป็น array เดียว (เปิด) หรือหลาย item (ปิด)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'debughelper') ]]
