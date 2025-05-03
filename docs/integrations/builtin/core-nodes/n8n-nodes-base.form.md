---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสาร n8n Form node
description: เอกสารสำหรับ n8n Form node ใน n8n แพลตฟอร์ม workflow automation พร้อมคำแนะนำการใช้งานและตัวอย่าง
contentType: [integration, reference]
---

# n8n Form node

ใช้ n8n Form node เพื่อสร้างฟอร์มสำหรับผู้ใช้ที่มีหลายขั้นตอน คุณสามารถเพิ่ม node อื่นๆ พร้อม logic เฉพาะเพื่อประมวลผลข้อมูลที่ผู้ใช้กรอกได้ โดยต้องเริ่ม workflow ด้วย [n8n Form Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md)

[[ workflowDemo("file:///integrations/builtin/core-nodes/n8n-nodes-base.form/mutually-exclusive-branching.json") ]]

## Setting up the node

### Set default selections with query parameters

คุณสามารถตั้งค่าเริ่มต้นของฟิลด์ต่างๆ ได้โดยใช้ [query parameters](https://en.wikipedia.org/wiki/Query_string#Web_forms){:target=_blank .external-link} กับ URL ที่ได้จาก [n8n Form Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md) ทุกหน้าของฟอร์มจะได้รับ query parameters เดียวกันที่ส่งไปยัง URL ของ n8n Form Trigger

/// note | Only for production
Query parameters จะใช้ได้เฉพาะตอนใช้งานฟอร์มใน production mode เท่านั้น n8n จะไม่เติมค่าฟิลด์จาก query parameters ใน testing mode
///

<!-- vale from-microsoft.Percentages = NO -->
เมื่อใช้ query parameters ให้ [percent-encode](https://en.wikipedia.org/wiki/Percent-encoding){:target=_blank .external-link} ชื่อฟิลด์หรือค่าที่มีอักขระพิเศษ เพื่อให้ n8n ใช้ค่าเริ่มต้นได้ถูกต้อง คุณสามารถใช้เครื่องมืออย่าง [URL Encode/Decode](https://www.url-encode-decode.com/) เพื่อช่วยแปลง query parameters ให้เป็น percent-encoding

ตัวอย่างเช่น ถ้าคุณมีฟอร์มที่มีข้อมูลดังนี้:

* Production URL: `https://my-account.n8n.cloud/form/my-form`
* Fields:
	* `name`: `Jane Doe`
	* `email`: `jane.doe@example.com`

เมื่อใช้ query parameters และ percent-encoding จะได้ URL แบบนี้:

```
https://my-account.n8n.cloud/form/my-form?email=jane.doe%40example.com&name=Jane%20Doe
```

ในตัวอย่างนี้ percent-encoding จะเปลี่ยนเครื่องหมาย @ เป็น `%40` และช่องว่างเป็น `%20` ซึ่งจะตั้งค่าเริ่มต้นให้ฟิลด์เหล่านี้ในทุกหน้าของฟอร์ม
<!-- vale from-microsoft.Percentages = YES -->

### Displaying custom HTML

คุณสามารถแสดง HTML ที่กำหนดเองในฟอร์มได้โดยเพิ่มฟิลด์ **Custom HTML** จะมีช่อง **HTML** ให้ใส่โค้ด HTML ที่ต้องการแสดงในหน้าฟอร์ม

คุณสามารถใช้ HTML field เพื่อเพิ่มเนื้อหา เช่น ลิงก์ รูปภาพ วิดีโอ ฯลฯ n8n จะ render เนื้อหานี้รวมกับฟิลด์อื่นๆ ตามปกติ

เนื่องจาก custom HTML เป็นแบบ read-only ฟิลด์นี้จะไม่ถูกส่งออกใน output ของฟอร์มโดยอัตโนมัติ ถ้าต้องการให้ส่งออกด้วย ให้ตั้งชื่อใน **Element Name**

HTML field ไม่รองรับ `<script>`, `<style>`, หรือ `<input>`

### Including hidden fields

คุณสามารถเพิ่มฟิลด์ที่ซ่อนไม่ให้ผู้ใช้เห็นได้ เหมาะสำหรับส่งข้อมูลเพิ่มเติมที่ไม่ต้องการให้ผู้ใช้กรอกเอง

ให้ใช้ **Hidden Field** ในการเพิ่มฟิลด์แบบซ่อน กำหนด **Field Name** และตั้งค่าเริ่มต้นใน **Field Value** ได้

เวลาส่งฟอร์ม สามารถส่งค่าฟิลด์ hidden ผ่าน [query parameters](#set-default-selections-with-query-parameters)

### Defining the form using JSON

ใช้ **Define Form** > **Using JSON** เพื่อกำหนดฟิลด์ของฟอร์มด้วย [JSON array of objects](/data/data-structure.md) โดยแต่ละ object จะกำหนดฟิลด์หนึ่งช่อง โดยใช้ key เหล่านี้:

- `fieldLabel`: ป้ายกำกับที่แสดงเหนือ input field
- `fieldType`: เลือกจาก `date`, `dropdown`, `email`, `file`, `number`, `password`, `text`, หรือ `textarea`
    - ใช้ `date` เพื่อเพิ่ม date picker ดูวิธี format วันที่ได้ที่ [Date and time with Luxon](/code/cookbook/luxon.md)
	- ถ้าใช้ `dropdown` ให้กำหนดตัวเลือกด้วย `fieldOptions` (ดูตัวอย่าง) โดยปกติ dropdown จะเลือกได้ข้อเดียว ถ้าต้องการเลือกได้หลายข้อ ให้ตั้ง `multiselect` เป็น `true`
	- ถ้าใช้ `file` ให้ตั้ง `multipleFiles` เป็น `true` เพื่อให้เลือกไฟล์ได้หลายไฟล์ และกำหนดชนิดไฟล์ที่อนุญาตด้วย `acceptFileTypes` เป็น string รายการนามสกุลไฟล์ (ดูตัวอย่าง)
- `placeholder`: ข้อความตัวอย่างในช่อง input ใช้ได้กับทุก `fieldType` ยกเว้น `dropdown`, `date`, และ `file`
- `requiredField`: กำหนดให้ฟิลด์นี้ต้องกรอก

ตัวอย่าง JSON ที่แสดงรูปแบบและ key ที่ใช้ได้:

```javascript
// Use the "requiredField" key on any field to mark it as mandatory
// Use the "placeholder" key to specify placeholder data for all fields
//     except 'dropdown', 'date' and 'file'

[
	{
		"fieldLabel": "Date Field",
		"fieldType": "date",
		"formatDate": "mm/dd/yyyy", // how to format received date in n8n
		"requiredField": true
	},
	{
		"fieldLabel": "Dropdown Options",
		"fieldType": "dropdown",
		"fieldOptions": {
			"values": [
				{
					"option": "option 1"
				},
				{
					"option": "option 2"
				}
			]
		},
		"requiredField": true
	},
	{
		"fieldLabel": "Multiselect",
		"fieldType": "dropdown",
		"fieldOptions": {
			"values": [
				{
					"option": "option 1"
				},
				{
					"option": "option 2"
				}
			]
		},
		"multiselect": true // setting to true allows multi-select
	},
	{
		"fieldLabel": "Email",
		"fieldType": "email",
		"placeholder": "me@mail.con"
	},
	{
		"fieldLabel": "File",
		"fieldType": "file",
		"multipleFiles": true, // setting to true allows multiple files selection
		"acceptFileTypes": ".jpg, .png" // allowed file types
	},
	{
		"fieldLabel": "Number",
		"fieldType": "number"
	},
	{
		"fieldLabel": "Password",
		"fieldType": "password"
	},
	{
		// "fieldType": "text" can be omitted since it's the default type
		"fieldLabel": "Text"
	},
	{
		"fieldLabel": "Textarea",
		"fieldType": "textarea"
	}
]
```

### Form Ending

ใช้ **Form Ending** Page Type เพื่อจบฟอร์มและแสดงหน้าสำเร็จ, redirect ไป URL หรือแสดง HTML/text ที่กำหนดเอง จะมีแค่ Form Ending node เดียวที่แสดงต่อหนึ่ง execution แม้จะมีหลาย branch

เลือกได้ระหว่าง:

- **Show Completion Screen**: แสดงหน้าสำเร็จให้ผู้ใช้
	- กรอก **Completion Title** เพื่อเป็นหัวข้อหลัก
	- **Completion Message** จะเป็นข้อความย่อยด้านล่าง ใช้ `\n` หรือ `<br>` เพื่อขึ้นบรรทัดใหม่
	- เพิ่ม **Completion Page Title** เพื่อเป็น title ใน browser tab

ถ้าเลือก **Redirect to URL** ให้กรอก URL ที่ต้องการ redirect เมื่อผู้ใช้กรอกฟอร์มเสร็จ

เลือก **Show Text** เพื่อแสดงหน้าสุดท้ายด้วย HTML หรือ plain text ที่กำหนดเอง

### Forms with branches

n8n Form node จะ execute และแสดงหน้าฟอร์มทุกครั้งที่ได้รับข้อมูลจาก node ก่อนหน้า ถ้า workflow มี branch หลายทาง ควรเข้าใจการทำงานของฟอร์มในแต่ละกรณี

#### Workflows with mutually exclusive branches

ถ้า workflow มี branch ที่เลือกได้ทางเดียว n8n จะ execute branch เดียวตามข้อมูลที่ส่งมา และจบด้วย Form Ending node

ตัวอย่าง workflow แบบ mutually exclusive branching:

[[ workflowDemo("file:///integrations/builtin/core-nodes/n8n-nodes-base.form/mutually-exclusive-branching.json") ]]

#### Workflows that may execute multiple branches

ถ้า workflow ส่งข้อมูลไปหลาย branch พร้อมกัน (เช่น จาก [switch](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md)) n8n จะ execute ทุก branch ที่ได้รับข้อมูลแบบ [sequentially](/flow-logic/execution-order.md) เมื่อจบ branch หนึ่งจะไป branch ถัดไป

n8n จะ execute แค่ Form Ending node เดียวต่อ execution ถ้ามีหลาย branch ที่มี Form Ending node n8n จะเลือกแค่ node สุดท้าย

ตัวอย่าง workflow ที่ execute หลาย branch:

[[ workflowDemo("file:///integrations/builtin/core-nodes/n8n-nodes-base.form/multiple-branch-execution.json") ]]

### Node options

เลือก **Add Option** เพื่อดูตัวเลือกเพิ่มเติม:

- **Form Title**: ชื่อฟอร์ม n8n จะแสดงเป็น title และ h1
- **Form Description**: คำอธิบายฟอร์ม แสดงใต้ h1 และใช้เป็น meta description ของหน้า รองรับ HTML ใช้ `\n` หรือ `<br>` เพื่อขึ้นบรรทัดใหม่
- **Button Label**: ข้อความบนปุ่ม submit

## Running the node

### Build and test workflows

ขณะสร้างหรือทดสอบ workflow ให้ใช้ **Test URL** ใน [n8n Form Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md) เพื่อดูข้อมูลที่เข้ามาใน editor UI สะดวกสำหรับ debug

มี 2 วิธีทดสอบ:

- เลือก **Test Step** n8n จะเปิดฟอร์ม เมื่อ submit แล้วจะ run node นี้และ node ก่อนหน้า แต่ไม่ run workflow ทั้งหมด
- เลือก **Test Workflow** n8n จะเปิดฟอร์ม เมื่อ submit แล้วจะ run workflow ทั้งหมด

### Production workflows

เมื่อ workflow พร้อมใช้งาน ให้เปลี่ยนไปใช้ **Production URL** ใน n8n Form Trigger โดยเลือก Production URL ใน **From URLS** จากนั้น activate workflow n8n จะ run อัตโนมัติเมื่อมีผู้ใช้ submit ฟอร์ม

เมื่อใช้ production URL ต้อง save และ activate workflow ข้อมูลที่ผ่าน Form trigger จะไม่แสดงใน editor UI

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'n8n-form') ]]
