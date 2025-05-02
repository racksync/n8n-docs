---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Send Email
description: Documentation for the Send Email node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: high
---

# Send Email

Send Email node ใช้สำหรับส่งอีเมลผ่าน SMTP email server

/// note | Credential
คุณสามารถดูข้อมูลการตั้งค่าการเชื่อมต่อสำหรับ node นี้ได้ที่ [ที่นี่](/integrations/builtin/credentials/sendemail/index.md)
///

## Node parameters

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

ตั้งค่า node นี้โดยใช้ parameters ต่อไปนี้

### Credential to connect with

เลือกหรือสร้าง [SMTP account credential](/integrations/builtin/credentials/sendemail/index.md) สำหรับ node นี้

### Operation

Send Email node รองรับ operations ต่อไปนี้:

* **Send**: ส่งอีเมล
* **Send and Wait for Response**: ส่งอีเมลและรอการตอบกลับจากผู้รับ การทำงานนี้จะหยุด workflow ไว้จนกว่าผู้ใช้จะตอบกลับ

ถ้าเลือก **Send and Wait for Response** จะมี parameters และ options เพิ่มเติมตามที่อธิบายไว้ใน [waiting for a response](#waiting-for-a-response)

### From Email

ใส่อีเมลที่ต้องการใช้ส่ง สามารถใส่ชื่อด้วยรูปแบบนี้: `Name Name <email@sample.com>` เช่น `Nathan Doe <nate@n8n.io>`

### To Email

ใส่อีเมลผู้รับ สามารถใส่ชื่อด้วยรูปแบบนี้: `Name Name <email@sample.com>` เช่น `Nathan Doe <nate@n8n.io>`

### Subject

ใส่หัวข้ออีเมล

### Email Format

เลือก format ที่จะใช้ส่งอีเมล ใช้ได้เมื่อเลือก **Send** operation เลือกได้จาก:

* **Text**: ส่งอีเมลแบบ plain-text
* **HTML**: ส่งอีเมลแบบ HTML
* **Both**: ส่งทั้งสองแบบ ผู้รับจะเห็นแบบที่ client ของเขาเลือกแสดง

## Node options

ใช้ **Options** เหล่านี้เพื่อปรับแต่งการทำงานของ node

### Append n8n Attribution

เลือกว่าจะใส่ข้อความ `This email was sent automatically with n8n` ท้ายอีเมลหรือไม่ (เปิดไว้คือใส่, ปิดคือไม่ใส่)

### Attachments

ใส่ชื่อ binary properties ที่มีข้อมูลไฟล์แนบ ข้อแนะนำ:

* ใช้ [Read/Write Files from Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) หรือ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) เพื่ออัปโหลดไฟล์เข้า workflow
* แนบไฟล์หลายไฟล์ได้โดยใส่ชื่อ binary properties คั่นด้วย comma
* อ้างอิงรูปหรือเนื้อหาอื่นในอีเมล เช่น `<img src="cid:image_1">`

### CC Email

ใส่อีเมลสำหรับช่อง cc:

### BCC Email

ใส่อีเมลสำหรับช่อง bcc:

### Ignore SSL Issues

เลือกว่าจะให้ n8n ข้าม error จาก TLS/SSL certificate validation หรือไม่ (เปิดคือข้าม, ปิดคือบังคับตรวจสอบ)

### Reply To

ใส่อีเมลสำหรับ Reply To

## Waiting for a response

ถ้าเลือก **Send and Wait for a Response** จะสามารถส่งอีเมลและหยุด workflow ไว้จนกว่าผู้รับจะตอบกลับหรือยืนยัน

### Response Type

เลือกประเภทของการรอและการอนุมัติได้ดังนี้:

* **Approval**: ผู้ใช้สามารถกด approve หรือ disapprove ได้จากในอีเมล
* **Free Text**: ผู้ใช้สามารถตอบกลับด้วยข้อความผ่านฟอร์ม
* **Custom Form**: ผู้ใช้สามารถตอบกลับด้วยฟอร์มที่กำหนดเอง

แต่ละแบบจะมี options ต่างกัน

### Approval parameters and options

ถ้าใช้ Approval response type จะมี options เหล่านี้:

* **Type of Approval**: จะให้มีแค่ปุ่ม approve หรือทั้ง approve/disapprove
* **Button Label**: ป้ายชื่อปุ่ม approve/disapprove ค่าเริ่มต้นคือ `Approve` และ `Decline`
* **Button Style**: เลือก style ของปุ่ม (primary หรือ secondary)

และยังมี options เหล่านี้:

* **Limit Wait Time**: ให้ workflow ดำเนินต่ออัตโนมัติหลังเวลาที่กำหนด (เป็นช่วงเวลาหรือเวลาจริง)
* **Append n8n Attribution**: เลือกว่าจะใส่ข้อความ `This email was sent automatically with n8n` ท้ายอีเมลหรือไม่

### Free Text parameters and options

ถ้าใช้ Free Text response type จะมี options เหล่านี้:

* **Message Button Label**: ป้ายชื่อปุ่มในอีเมล ค่าเริ่มต้นคือ `Respond`
* **Response Form Title**: หัวข้อของฟอร์มตอบกลับ
* **Response Form Description**: คำอธิบายฟอร์มตอบกลับ
* **Response Form Button Label**: ป้ายชื่อปุ่ม submit ในฟอร์ม ค่าเริ่มต้นคือ `Submit`
* **Limit Wait Time**: ให้ workflow ดำเนินต่ออัตโนมัติหลังเวลาที่กำหนด
* **Append n8n Attribution**: เลือกว่าจะใส่ข้อความ `This email was sent automatically with n8n` ท้ายอีเมลหรือไม่

### Custom Form parameters and options

ถ้าใช้ Custom Form response type คุณสามารถสร้างฟอร์มเองได้ตามต้องการ

สามารถปรับแต่งแต่ละ element ของฟอร์มได้ตามที่อธิบายไว้ใน [n8n Form trigger's form elements](/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger.md#form-elements) ถ้าต้องการเพิ่ม field ให้เลือก **Add Form Element**

และยังมี options เหล่านี้:

* **Message Button Label**: ป้ายชื่อปุ่มในอีเมล ค่าเริ่มต้นคือ `Respond`
* **Response Form Title**: หัวข้อของฟอร์มตอบกลับ
* **Response Form Description**: คำอธิบายฟอร์มตอบกลับ
* **Response Form Button Label**: ป้ายชื่อปุ่ม submit ในฟอร์ม ค่าเริ่มต้นคือ `Submit`
* **Limit Wait Time**: ให้ workflow ดำเนินต่ออัตโนมัติหลังเวลาที่กำหนด
* **Append n8n Attribution**: เลือกว่าจะใส่ข้อความ `This email was sent automatically with n8n` ท้ายอีเมลหรือไม่

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'send-email') ]]
