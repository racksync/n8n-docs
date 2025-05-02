---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Convert to File
description: Documentation for the Convert to File node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: critical
---

# Convert to File

ใช้ Convert to File node เพื่อแปลง input data ให้ออกมาเป็นไฟล์ (file) โดยจะเปลี่ยนข้อมูล JSON ที่รับเข้ามาให้เป็น binary format

/// note | Extract From File
ถ้าอยาก extract ข้อมูลจากไฟล์แล้วแปลงเป็น JSON ให้ใช้ [Extract from File](/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md) node
///

## Operations

* [**Convert to CSV**](#convert-to-csv)
* [**Convert to HTML**](#convert-to-html)
* [**Convert to ICS**](#convert-to-ics)
* [**Convert to JSON**](#convert-to-json)
* [**Convert to ODS**](#convert-to-ods)
* [**Convert to RTF**](#convert-to-rtf)
* [**Convert to Text File**](#convert-to-text-file)
* [**Convert to XLS**](#convert-to-xls)
* [**Convert to XLSX**](#convert-to-xlsx)
* [**Move Base64 String to File**](#move-base64-string-to-file)

parameter และ options ของ node จะขึ้นอยู่กับ operation ที่เลือก

### Convert to CSV

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter **Put Output File in Field** ใส่ชื่อ field ใน output data ที่จะเก็บไฟล์

#### Convert to CSV options

ตั้งค่าเพิ่มเติมได้ใน **Options**:

* **File Name**: ใส่ชื่อไฟล์ output ที่ต้องการ
* ถ้า row แรกของไฟล์เป็น header ให้เปิด option **Header Row**

### Convert to HTML

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter **Put Output File in Field** ใส่ชื่อ field ใน output data ที่จะเก็บไฟล์

#### Convert to HTML options

ตั้งค่าเพิ่มเติมได้ใน **Options**:

* **File Name**: ใส่ชื่อไฟล์ output ที่ต้องการ
* ถ้า row แรกของไฟล์เป็น header ให้เปิด option **Header Row**

### Convert to ICS

* **Put Output File in Field**: ใส่ชื่อ field ใน output data ที่จะเก็บไฟล์
* **Event Title**: ใส่ชื่อ event
* **Start**: ใส่วันและเวลาที่ event จะเริ่ม ถ้าเป็น all-day event จะไม่สนใจเวลา
* **End**: ใส่วันและเวลาที่ event จะจบ ถ้าเป็น all-day event จะไม่สนใจเวลา ถ้าไม่ใส่ node จะใช้ start date
* **All Day**: เลือกว่าจะเป็น all day event หรือไม่ (เปิด/ปิด)

#### Convert to ICS options

ตั้งค่าเพิ่มเติมได้ใน **Options**:

* **File Name**: ใส่ชื่อไฟล์ output ที่ต้องการ
* **Attendees**: เพิ่มผู้เข้าร่วม event ได้ โดยแต่ละคนใส่
	* **Name**
	* **Email**
	* **RSVP**: เลือกว่าต้องการให้ยืนยันการเข้าร่วมหรือไม่ (เปิด/ปิด)
* **Busy Status**: ตั้ง busy status สำหรับ Microsoft เช่น Outlook เลือกได้ **Busy** หรือ **Tentative**
* **Calendar Name**: สำหรับ Apple/Microsoft calendar ใส่ [calendar name](https://learn.microsoft.com/en-us/openspecs/exchange_server_protocols/ms-oxcical/1da58449-b97e-46bd-b018-a1ce576f3e6d)
*  **Description**: ใส่รายละเอียด event
* **Geolocation**: ใส่ **Latitude** และ **Longitude** ของสถานที่จัด event
* **Location**: ใส่สถานที่จัด event
* **Recurrence Rule**: ใส่กติกาการ repeat event (RRULE) สร้าง rule ได้ที่ [iCalendar.org RRULE Tool](https://icalendar.org/rrule-tool.html)
* **Organizer**: ใส่ **Name** และ **Email** ของผู้จัดงาน
* **Sequence**: ถ้าส่ง update event ที่มี UID เดิม ให้ใส่เลข revision
* **Status**: ตั้งสถานะ event เลือกได้ **Confirmed**, **Cancelled**, **Tentative**
* **UID**: ใส่ UID ของ event (ควร unique) ถ้าไม่ใส่ node จะ generate ให้เอง
* **URL**: ใส่ URL ที่เกี่ยวข้องกับ event
* **Use Workflow Timezone**: เลือกว่าจะใช้ timezone ของ workflow หรือไม่ (เปิด/ปิด) ตั้ง timezone ได้ที่ [Workflow Settings](/workflows/settings.md)

### Convert to JSON

เลือก **Mode** สำหรับ output ที่เหมาะกับงาน:

* **All Items to One File**: รวม input ทั้งหมดเป็นไฟล์เดียว
* **Each Item to Separate File**: สร้างไฟล์แยกสำหรับแต่ละ input

#### Convert to JSON options

ตั้งค่าเพิ่มเติมได้ใน **Options**:

* **File Name**: ใส่ชื่อไฟล์ output ที่ต้องการ
* **Format**: เลือกว่าจะจัด format JSON ให้อ่านง่าย (เปิด/ปิด)
* **Encoding**: เลือก character set ที่ใช้ encode ข้อมูล ค่า default คือ **utf8**

### Convert to ODS

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter **Put Output File in Field** ใส่ชื่อ field ใน output data ที่จะเก็บไฟล์

#### Convert to ODS options

ตั้งค่าเพิ่มเติมได้ใน **Options**:

* **File Name**: ใส่ชื่อไฟล์ output ที่ต้องการ
* **Compression**: เลือกว่าจะบีบอัดไฟล์เพื่อลดขนาดหรือไม่
* **Header Row**: เปิดถ้า row แรกเป็น header
* **Sheet Name**: ใส่ชื่อ sheet ที่จะสร้างใน spreadsheet

### Convert to RTF

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter **Put Output File in Field** ใส่ชื่อ field ใน output data ที่จะเก็บไฟล์

#### Convert to RFT options

ตั้งค่าเพิ่มเติมได้ใน **Options**:

* **File Name**: ใส่ชื่อไฟล์ output ที่ต้องการ
* ถ้า row แรกของไฟล์เป็น header ให้เปิด option **Header Row**

### Convert to Text File

ใส่ชื่อ **Text Input Field** ที่มี string ที่ต้องการแปลงเป็นไฟล์ ใช้ dot-notation สำหรับ field ซ้อน เช่น `level1.level2.currentKey`

#### Convert to Text File options

ตั้งค่าเพิ่มเติมได้ใน **Options**:

* **File Name**: ใส่ชื่อไฟล์ output ที่ต้องการ
* **Encoding**: เลือก character set ที่ใช้ encode ข้อมูล ค่า default คือ **utf8**

### Convert to XLS

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter **Put Output File in Field** ใส่ชื่อ field ใน output data ที่จะเก็บไฟล์

#### Convert to XLS options

ตั้งค่าเพิ่มเติมได้ใน **Options**:

* **File Name**: ใส่ชื่อไฟล์ output ที่ต้องการ
* **Header Row**: เปิดถ้า row แรกเป็น header
* **Sheet Name**: ใส่ชื่อ sheet ที่จะสร้างใน spreadsheet

### Convert to XLSX

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter **Put Output File in Field** ใส่ชื่อ field ใน output data ที่จะเก็บไฟล์

#### Convert to XLSX options

ตั้งค่าเพิ่มเติมได้ใน **Options**:

* **File Name**: ใส่ชื่อไฟล์ output ที่ต้องการ
* **Compression**: เลือกว่าจะบีบอัดไฟล์เพื่อลดขนาดหรือไม่
* **Header Row**: เปิดถ้า row แรกเป็น header
* **Sheet Name**: ใส่ชื่อ sheet ที่จะสร้างใน spreadsheet

### Move Base64 String to File

ใส่ชื่อ **Base64 Input Field** ที่มี Base64 string ที่ต้องการแปลงเป็นไฟล์ ใช้ dot-notation สำหรับ field ซ้อน เช่น `level1.level2.currentKey`

#### Move Base64 String to File options

ตั้งค่าเพิ่มเติมได้ใน **Options**:

* **File Name**: ใส่ชื่อไฟล์ output ที่ต้องการ
* **MIME Type**: ใส่ MIME type ของไฟล์ output ดู [Common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) สำหรับรายการ MIME type ที่ใช้บ่อย

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'convert-to-file') ]]
