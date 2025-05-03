---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Edit Image
description: เอกสารสำหรับ Edit Image node ใน n8n แพลตฟอร์ม workflow automation พร้อมคำแนะนำการใช้งานและตัวอย่าง
contentType: [integration, reference]
priority: medium
---

# Edit Image

ใช้ Edit Image node เพื่อปรับแต่งและแก้ไขรูปภาพ

/// note | Dependencies
1. ถ้าไม่ได้รัน n8n บน Docker ต้องติดตั้ง [GraphicsMagick](http://www.graphicsmagick.org/README.html)
2. ต้องใช้ node เช่น [Read/Write Files from Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) หรือ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) เพื่อส่งไฟล์รูปภาพเป็น data property ให้ Edit Image node
///

## Operations

- **Blur** ภาพเพื่อลดความคมชัด
- **Border** เพิ่มขอบให้ภาพ
- **Composite** วางภาพซ้อนบนอีกภาพ
- **Create** สร้างภาพใหม่
- **Crop** ตัดภาพ
- **Draw** วาดบนภาพ
- **Get Information** ดูข้อมูลของภาพ
- **Multi Step** ทำหลาย operation กับภาพในครั้งเดียว
- **Resize**: เปลี่ยนขนาดภาพ
- **Rotate** หมุนภาพ
- **Shear** เอียงภาพตามแกน X หรือ Y
- **Text** ใส่ข้อความบนภาพ
- **Transparent** ทำให้สีในภาพโปร่งใส

## Node parameters

parameter ของ node จะขึ้นอยู่กับ operation ที่เลือก

### Blur parameters

* **Property Name**: ใส่ชื่อ binary property ที่เก็บข้อมูลภาพ
* **Blur**: ใส่ตัวเลขกำหนดความเบลอ 0-1000 ยิ่งมากยิ่งเบลอ
* **Sigma**: ใส่ตัวเลขกำหนด sigma สำหรับ blur 0-1000 ยิ่งมากยิ่งเบลอ

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Border parameters

* **Property Name**: ใส่ชื่อ binary property ที่เก็บข้อมูลภาพ
* **Border Width**: ใส่ความกว้างขอบ
* **Border Height**: ใส่ความสูงขอบ
* **Border Color**: เลือกสีขอบ ใส่ hex หรือเลือกจาก color picker

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Composite parameters

* **Property Name**: ใส่ชื่อ binary property ของภาพหลัก
* **Composite Image Property**: ใส่ชื่อ binary property ของภาพที่จะวางซ้อน
* **Operator**: เลือก composite operator เช่น:
	* **Add**
	* **Atop**
	* **Bumpmap**
	* **Copy**
	* **Copy Black**
	* **Copy Blue**
	* **Copy Cyan**
	* **Copy Green**
	* **Copy Magenta**
	* **Copy Opacity**
	* **Copy Red**
	* **Copy Yellow**
	* **Difference**
	* **Divide**
	* **In**
	* **Minus**
	* **Multiply**
	* **Out**
	* **Over**
	* **Plus**
	* **Subtract**
	* **Xor**
* **Position X**: ใส่ตำแหน่งแนวนอนของภาพซ้อน
* **Position Y**: ใส่ตำแหน่งแนวตั้งของภาพซ้อน

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Create parameters

* **Property Name**: ใส่ชื่อ binary property ที่เก็บข้อมูลภาพ
* **Background Color**: เลือกสีพื้นหลัง ใส่ hex หรือเลือกจาก color picker
* **Image Width**: ใส่ความกว้างภาพ
* **Image Height**: ใส่ความสูงภาพ

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Crop parameters

* **Property Name**: ใส่ชื่อ binary property ที่เก็บข้อมูลภาพ
* **Width**: ใส่ความกว้างที่ต้องการ crop
* **Height**: ใส่ความสูงที่ต้องการ crop
* **Position X**: ใส่ตำแหน่งแนวนอนเริ่ม crop
* **Position Y**: ใส่ตำแหน่งแนวตั้งเริ่ม crop

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Draw parameters

* **Property Name**: ใส่ชื่อ binary property ที่เก็บข้อมูลภาพ
* **Primitive**: เลือกรูปทรงที่จะวาด เช่น:
	* **Circle**
	* **Line**
	* **Rectangle**
* **Color**: เลือกสี ใส่ hex หรือเลือกจาก color picker
* **Start Position X**: ตำแหน่งแนวนอนเริ่มวาด
* **Start Position Y**: ตำแหน่งแนวตั้งเริ่มวาด
* **End Position X**: ตำแหน่งแนวนอนหยุดวาด
* **End Position Y**: ตำแหน่งแนวตั้งหยุดวาด
* **Corner Radius**: ใส่เลขกำหนดความโค้งมุม

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Get Information parameters

operation นี้แค่ใส่ **Property Name** ของ binary property ที่เก็บข้อมูลภาพ

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Multi Step parameters

* **Property Name**: ใส่ชื่อ binary property ที่เก็บข้อมูลภาพ
* **Operations**: เพิ่ม operation ที่ต้องการให้ multi step ทำ สามารถใช้ operation อื่นๆ ได้ทุกอัน

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Resize parameters

* **Property Name**: ใส่ชื่อ binary property ที่เก็บข้อมูลภาพ
* **Width**: ใส่ความกว้างใหม่
* **Height**: ใส่ความสูงใหม่
* **Option**: เลือกวิธี resize เช่น:
	* **Ignore Aspect Ratio**
	* **Maximum Area**
	* **Minimum Area**
	* **Only if Larger**
	* **Only if Smaller**
	* **Percent**

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Rotate parameters

* **Property Name**: ใส่ชื่อ binary property ที่เก็บข้อมูลภาพ
* **Rotate**: ใส่จำนวนองศาที่ต้องการหมุน --360 ถึง 360
* **Background Color**: เลือกสีพื้นหลัง ใส่ hex หรือเลือกจาก color picker สีนี้จะเติมพื้นหลังเวลาหมุนภาพที่ไม่ใช่ 90 องศา ถ้าหมุนทีละ 90 องศา สีนี้จะไม่ถูกใช้

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Shear parameters

* **Property Name**: ใส่ชื่อ binary property ที่เก็บข้อมูลภาพ
* **Degrees X**: ใส่องศาเอียงตามแกน x
* **Degrees Y**: ใส่องศาเอียงตามแกน y

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Text parameters

* **Property Name**: ใส่ชื่อ binary property ที่เก็บข้อมูลภาพ
* **Text**: ใส่ข้อความที่ต้องการเขียนบนภาพ
* **Font Size**: เลือกขนาด font
* **Font Color**: เลือกสี font ใส่ hex หรือเลือกจาก color picker
* **Position X**: ตำแหน่งแนวนอนเริ่มข้อความ
* **Position Y**: ตำแหน่งแนวตั้งเริ่มข้อความ
* **Max Line Length**: ใส่จำนวนตัวอักษรสูงสุดต่อบรรทัด

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

### Transparent parameters

* **Property Name**: ใส่ชื่อ binary property ที่เก็บข้อมูลภาพ
* **Color**: เลือกสีที่จะทำให้โปร่งใส ใส่ hex หรือเลือกจาก color picker

ดู [Node options](#node-options) สำหรับ option เพิ่มเติม

## Node options

- **File Name**: ใส่ชื่อไฟล์ output
- **Format**: เลือก format ของไฟล์ output เช่น:
	- **bmp**
	- **gif**
	- **jpeg**
	- **png**
	- **tiff**
	- **WebP**

operation **Text** จะมี option **Font Name or ID** เพิ่ม สามารถเลือก font จาก dropdown หรือใส่ ID ด้วย [expression](/code/expressions.md)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'edit-image') ]]
