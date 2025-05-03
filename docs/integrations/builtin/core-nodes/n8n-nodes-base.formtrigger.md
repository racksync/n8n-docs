---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ทริกเกอร์ฟอร์ม (n8n Form Trigger)
description: คู่มือ n8n Form Trigger node สำหรับเริ่ม workflow ด้วยฟอร์มใน n8n
contentType: [integration, reference]
priority: critical
---

# n8n Form Trigger node

ใช้ n8n Form trigger เพื่อเริ่ม workflow เมื่อมีผู้ใช้ submit ฟอร์ม โดยจะรับ input data จากฟอร์ม Node นี้จะสร้างหน้าเว็บฟอร์มให้คุณใช้งาน

คุณสามารถเพิ่มหน้าอื่นๆ ต่อจากนี้ได้ด้วย [n8n Form](/integrations/builtin/core-nodes/n8n-nodes-base.form.md) node

## Build and test workflows

ขณะสร้างหรือทดสอบ workflow ให้ใช้ **Test URL** การใช้ test URL จะช่วยให้คุณดูข้อมูลที่เข้ามาใน editor UI ได้ เหมาะสำหรับ debug

มี 2 วิธีทดสอบ:

- เลือก **Test Step** n8n จะเปิดฟอร์ม เมื่อ submit แล้ว n8n จะ run node นี้ แต่ยังไม่ run workflow ทั้งหมด
- เลือก **Test Workflow** n8n จะเปิดฟอร์ม เมื่อ submit แล้ว n8n จะ run workflow

## Production workflows

เมื่อ workflow พร้อมใช้งาน ให้เปลี่ยนไปใช้ **Production URL** จากนั้น activate workflow n8n จะ run อัตโนมัติเมื่อมีผู้ใช้ submit ฟอร์ม

ถ้าใช้ production URL ต้อง save และ activate workflow ข้อมูลที่ผ่าน Form trigger จะไม่แสดงใน editor UI

## Set default selections with query parameters

คุณสามารถตั้งค่าเริ่มต้นของฟิลด์ต่างๆ ได้โดยใช้ [query parameters](https://en.wikipedia.org/wiki/Query_string#Web_forms){:target=_blank .external-link} กับ URL ที่ได้จาก n8n Form Trigger ทุกหน้าของฟอร์มจะได้รับ query parameters เดียวกัน

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

## Node parameters

นี่คือฟิลด์หลักสำหรับตั้งค่า node:

### Authentication

- **Basic Auth**
- **None**

#### Using basic auth

ถ้าต้องการใช้ credential นี้ ให้เตรียมข้อมูลดังนี้:

- **Username** ที่ใช้เข้าถึงแอปหรือบริการที่ HTTP Request ของคุณจะเชื่อมต่อ
- **Password** ที่ตรงกับ username

### Form URLs

Form Trigger node จะมี 2 URL: **Test URL** และ **Production URL** n8n จะแสดง URL เหล่านี้ที่ด้านบนของ panel node เลือก **Test URL** หรือ **Production URL** เพื่อสลับดู URL ที่ต้องการ

![Screenshot of the form URLs](/_images/integrations/builtin/core-nodes/form-trigger/form-urls.png)

- **Test URL**: n8n จะ register test webhook เมื่อเลือก **Test Step** หรือ **Test Workflow** ถ้า workflow ยังไม่ active เมื่อเรียก URL นี้ n8n จะแสดงข้อมูลใน workflow
- **Production URL**: n8n จะ register production webhook เมื่อ activate workflow เมื่อใช้ production URL ข้อมูลจะไม่แสดงใน workflow แต่สามารถดู execution ได้ใน tab **Executions**

### Form Path

ตั้ง slug สำหรับฟอร์ม

### Form Title

กรอกชื่อฟอร์ม n8n จะแสดง **Form Title** เป็น title ของเว็บและ h1 หลักในฟอร์ม

### Form Description

กรอกคำอธิบายฟอร์ม n8n จะแสดง **Form Description** เป็น subtitle ใต้ h1 หลักในฟอร์ม ใช้ `\n` หรือ `<br>` เพื่อขึ้นบรรทัดใหม่

### Form Elements

สร้างฟิลด์คำถามในฟอร์ม เลือก **Add Form Element** เพื่อเพิ่มฟิลด์ใหม่

แต่ละฟิลด์จะมีการตั้งค่าดังนี้:

- **Field Label**: ป้ายกำกับที่แสดงเหนือ input field
- **Element Type**: เลือกจาก **Custom HTML**, **Date**, **Dropdown List**, **Email**, **File**, **Hidden Field**, **Number**, **Password**, **Text**, หรือ **Textarea**
	- เลือก **Custom HTML** เพื่อแทรก HTML ที่กำหนดเอง
		- สามารถใส่ลิงก์ รูปภาพ วิดีโอ ฯลฯ แต่ไม่รองรับ `<script>`, `<style>`, หรือ `<input>`
		- โดยปกติ Custom HTML จะไม่ถูกส่งออกใน output ถ้าต้องการให้ส่งออกด้วย ให้กรอก **Element Name**
    - เลือก **Date** เพื่อเพิ่ม date picker ดูวิธี format วันที่ได้ที่ [Date and time with Luxon](/code/cookbook/luxon.md)
	- เลือก **Dropdown List** > **Add Field Option** เพื่อเพิ่มตัวเลือก dropdown โดยปกติเลือกได้ข้อเดียว ถ้าต้องการเลือกได้หลายข้อ ให้เปิด **Multiple Choice**
	- เลือก **Hidden Field** เพื่อเพิ่มฟิลด์ที่ไม่แสดงในฟอร์ม สามารถตั้งค่าเริ่มต้นใน **Field Value** หรือส่งค่าผ่าน [query parameters](#set-default-selections-with-query-parameters)
- **Required Field**: เปิดเพื่อบังคับให้ผู้ใช้กรอกฟิลด์นี้

### Respond When

เลือกเวลาที่ n8n จะตอบกลับหลัง submit ฟอร์ม สามารถเลือกได้ว่า:

- **Form Is Submitted**: ตอบกลับทันทีที่ผู้ใช้ submit
- **Workflow Finishes**: ตอบกลับหลัง workflow ทำงานเสร็จ ถ้า workflow error จะตอบกลับว่ามีปัญหา

## Node options

เลือก **Add Option** เพื่อดูตัวเลือกเพิ่มเติม:

- **Append n8n Attribution**: ปิดเพื่อซ่อนข้อความ **Form automated with n8n** ด้านล่างฟอร์ม
- **Form Response**: เลือกวิธีตอบกลับเมื่อผู้ใช้ submit ฟอร์ม
    - **Respond With** > **Form Submitted Text**: แสดงข้อความให้ผู้ใช้
    - **Respond With** > **Redirect URL**: ส่งผู้ใช้ไปหน้าใหม่
- **Ignore Bots**: เปิดเพื่อไม่รับ request จาก bot เช่น link previewer หรือ web crawler
- **Use Workflow Timezone**: เปิดเพื่อใช้ timezone จาก [Workflow settings](/workflows/settings.md) แทน UTC (ค่าเริ่มต้น) มีผลกับค่า `submittedAt` ใน output

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'n8n-form-trigger') ]]
