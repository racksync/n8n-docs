---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: วันที่และเวลา (Date & Time)
description: คู่มือ Date & Time node สำหรับจัดการข้อมูลวันที่และเวลาใน n8n
contentType: [integration, reference]
priority: high
---

# Date & Time

Date & Time node ใช้สำหรับจัดการข้อมูลวันที่และเวลา และแปลงให้อยู่ใน format ต่างๆ

--8<-- "_snippets/integrations/builtin/core-nodes/schedule/timezone-settings.md"

/// note | Date and time in other nodes
สามารถจัดการข้อมูลวันที่และเวลาใน Code node และใน expression ของทุก node ได้ n8n รองรับ Luxon สำหรับจัดการวันที่และเวลาใน JavaScript ดูรายละเอียดที่ [Date and time with Luxon](/code/cookbook/luxon.md)
///

## Operations

* **Add to a Date**: เพิ่มเวลาตามที่กำหนดให้กับวันที่
* **Extract Part of a Date**: ดึงบางส่วนของวันที่ เช่น ปี เดือน หรือวัน
* **Format a Date**: แปลง format ของวันที่เป็นแบบใหม่ โดยใช้ preset หรือ custom expression
* **Get Current Date**: ดึงวันที่ปัจจุบัน เลือกได้ว่าจะรวมเวลาปัจจุบันด้วยหรือไม่ เหมาะสำหรับ trigger flow อื่นหรือ logic เงื่อนไข
* **Get Time Between Dates**: คำนวณเวลาระหว่างวันที่สองวันในหน่วยที่เลือก
* **Round a Date**: ปัดวันที่ขึ้นหรือลงเป็นหน่วยที่เลือก เช่น เดือน วัน หรือชั่วโมง
* **Subtract From a Date**: ลบเวลาตามที่กำหนดออกจากวันที่

ดูรายละเอียด parameter และ options ของแต่ละ operation ด้านล่าง

## Add to a Date

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter เหล่านี้:

* **Date to Add To**: ใส่วันที่ที่ต้องการเปลี่ยน
* **Time Unit to Add**: เลือกหน่วยเวลาสำหรับ **Duration**
* **Duration**: ใส่จำนวนหน่วยเวลาที่ต้องการเพิ่ม
* **Output Field Name**: ใส่ชื่อ field ที่จะเก็บวันที่ใหม่

### Add to a Date options

operation นี้มี option เดียวคือ **Include Input Fields** ถ้าเปิดไว้ output จะรวม field เดิมทั้งหมดด้วย ถ้าปิดไว้ output จะมีแค่ **Output Field Name** กับค่าของมัน

## Extract Part of a Date

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter เหล่านี้:

* **Date**: ใส่วันที่ที่ต้องการปัดหรือดึงบางส่วน
* **Part**: เลือกส่วนของวันที่ที่ต้องการดึง เลือกได้:
    * **Year**
    * **Month**
    * **Week**
    * **Day**
    * **Hour**
    * **Minute**
    * **Second**
* **Output Field Name**: ใส่ชื่อ field ที่จะเก็บค่าที่ดึงออกมา

### Extract Part of a Date options

operation นี้มี option เดียวคือ **Include Input Fields** ถ้าเปิดไว้ output จะรวม field เดิมทั้งหมดด้วย ถ้าปิดไว้ output จะมีแค่ **Output Field Name** กับค่าของมัน

## Format a Date

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter เหล่านี้:

* **Date**: ใส่วันที่ที่ต้องการ format
* **Format**: เลือก format ที่ต้องการแปลงเป็น เลือกได้:
    * **Custom Format**: ใส่ format เองโดยใช้ Luxon [special tokens](https://moment.github.io/luxon/#/formatting?id=table-of-tokens) (case-sensitive)
    * **MM/DD/YYYY**: เช่น `4 September 1986` จะได้ `09/04/1986`
    * **YYYY/MM/DD**: เช่น `4 September 1986` จะได้ `1986/09/04`
    * **MMMM DD YYYY**: เช่น `4 September 1986` จะได้ `September 04 1986`
    * **MM-DD-YYYY**: เช่น `4 September 1986` จะได้ `09-04-1986`
    * **YYYY-MM-DD**: เช่น `4 September 1986` จะได้ `1986-09-04`
* **Output Field Name**: ใส่ชื่อ field ที่จะเก็บวันที่ที่ format แล้ว

### Format a Date options

operation นี้มี options ดังนี้:

* **Include Input Fields**: ถ้าเปิดไว้ output จะรวม field เดิมทั้งหมดด้วย ถ้าปิดไว้ output จะมีแค่ **Output Field Name** กับค่าของมัน
* **From Date Format**: ถ้า node ไม่รู้จัก format ของ **Date** ให้ใส่ format ที่ถูกต้องตรงนี้ ใช้ Luxon [special tokens](https://moment.github.io/luxon/#/formatting?id=table-of-tokens) (case-sensitive)
* **Use Workflow Timezone**: เลือกว่าจะใช้ timezone ของ input (ปิด) หรือ timezone ของ workflow (เปิด)

## Get Current Date

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter เหล่านี้:

* **Include Current Time**: เลือกว่าจะรวมเวลาปัจจุบันด้วยหรือไม่ (เปิด/ปิด)
* **Output Field Name**: ใส่ชื่อ field ที่จะเก็บวันที่ปัจจุบัน

### Get Current Date options

operation นี้มี options ดังนี้:

* **Include Input Fields**: ถ้าเปิดไว้ output จะรวม field เดิมทั้งหมดด้วย ถ้าปิดไว้ output จะมีแค่ **Output Field Name** กับค่าของมัน
* **Timezone**: ตั้ง timezone ที่จะใช้ ถ้าเว้นว่าง node จะใช้ timezone ของ n8n instance

/// note | +00:00 timezone
ใช้ `GMT` สำหรับ timezone +00:00
///

## Get Time Between Dates

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter เหล่านี้:

* **Start Date**: ใส่วันที่เริ่มต้น
* **End Date**: ใส่วันที่สิ้นสุด
* **Units**: เลือกหน่วยเวลาที่ต้องการคำนวณ เลือกได้หลายอัน:
    * **Year**
    * **Month**
    * **Week**
    * **Day**
    * **Hour**
    * **Minute**
    * **Second**
    * **Millisecond**
* **Output Field Name**: ใส่ชื่อ field ที่จะเก็บค่าที่คำนวณได้

### Get Time Between Dates options

operation นี้มี option **Include Input Fields** และ **Output as ISO String** ถ้าปิดไว้แต่ละ unit ที่เลือกจะคืนค่าคำนวณแยก เช่น

    timeDifference
    years : 1
    months : 3
    days : 13

ถ้าเปิด **Output as ISO String** node จะ format output เป็น ISO duration string เดียว เช่น `P1Y3M13D`

ISO duration format จะเป็น `P<n>Y<n>M<n>DT<n>H<n>M<n>S` โดย `<n>` คือจำนวนของแต่ละหน่วย

* P = period (duration) ขึ้นต้น ISO duration ทุกอัน
* Y = ปี
* M = เดือน
* W = สัปดาห์
* D = วัน
* T = คั่นระหว่างวันที่กับเวลา
* H = ชั่วโมง
* M = นาที
* S = วินาที

Milliseconds จะเป็นทศนิยมของวินาที เช่น 2.1 milliseconds คือ `0.0021S`

## Round a Date

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter เหล่านี้:

* **Date**: ใส่วันที่ที่ต้องการปัด
* **Mode**: เลือกว่าจะ **Round Down** หรือ **Round Up**
* **To Nearest**: เลือกหน่วยที่ต้องการปัด เลือกได้:
    * **Year**
    * **Month**
    * **Week**
    * **Day**
    * **Hour**
    * **Minute**
    * **Second**
* **Output Field Name**: ใส่ชื่อ field ที่จะเก็บวันที่ที่ปัดแล้ว

### Round a Date options

operation นี้มี option เดียวคือ **Include Input Fields** ถ้าเปิดไว้ output จะรวม field เดิมทั้งหมดด้วย ถ้าปิดไว้ output จะมีแค่ **Output Field Name** กับค่าของมัน

## Subtract From a Date

ตั้งค่า node สำหรับ operation นี้โดยใช้ parameter เหล่านี้:

* **Date to Subtract From**: ใส่วันที่ที่ต้องการลบ
* **Time Unit to Subtract**: เลือกหน่วยเวลาสำหรับ **Duration**
* **Duration**: ใส่จำนวนหน่วยเวลาที่ต้องการลบ
* **Output Field Name**: ใส่ชื่อ field ที่จะเก็บวันที่ที่ลบแล้ว

### Subtract From a Date options

operation นี้มี option เดียวคือ **Include Input Fields** ถ้าเปิดไว้ output จะรวม field เดิมทั้งหมดด้วย ถ้าปิดไว้ output จะมีแค่ **Output Field Name** กับค่าของมัน

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'date-and-time') ]]

## Related resources

Date & Time node ใช้ [Luxon](https://moment.github.io/luxon) สามารถใช้ Luxon ใน [Code](/code/code-node.md) node และ [expressions](/code/expressions.md) ได้ ดูรายละเอียดที่ [Date and time with Luxon](/code/cookbook/luxon.md)

### Supported date formats

n8n รองรับทุก format วันที่ที่ [Luxon](https://moment.github.io/luxon/#/formatting?id=table-of-tokens) รองรับ (case-sensitive)
