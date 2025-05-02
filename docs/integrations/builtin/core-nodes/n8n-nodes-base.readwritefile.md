---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Read/Write Files from Disk
description: Documentation for the Read/Write Files from Disk node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: critical
---

# Read/Write Files from Disk

ใช้ Read/Write Files from Disk node เพื่ออ่านหรือเขียนไฟล์จาก/ไปยังเครื่องที่รัน n8n อยู่

/// note | Self-hosted n8n only
node นี้ใช้ได้เฉพาะกับ n8n แบบ self-hosted เท่านั้น
///

## Operations

- [**Read File(s) From Disk**](#read-files-from-disk): ใช้ operation นี้เพื่อดึงไฟล์หนึ่งไฟล์หรือหลายไฟล์จากเครื่องที่รัน n8n
- [**Write File to Disk**](#write-file-to-disk): ใช้ operation นี้เพื่อสร้างไฟล์ binary บนเครื่องที่รัน n8n

ดูรายละเอียดการตั้งค่าแต่ละ operation ได้ในหัวข้อด้านล่าง

## Read File(s) From Disk

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **File(s) Selector**: กรอก path ของไฟล์ที่ต้องการอ่าน
	- ถ้าต้องการอ่านหลายไฟล์ ให้กรอก pattern ของ path โดยสามารถใช้ตัวอักษรพิเศษเหล่านี้:
		- `*`: ตรงกับอักขระใด ๆ ศูนย์ตัวหรือมากกว่า ยกเว้น path separator
		- `**`: ตรงกับอักขระใด ๆ ศูนย์ตัวหรือมากกว่า รวม path separator ด้วย
		- `?`: ตรงกับอักขระใด ๆ ยกเว้น path separator หนึ่งตัว
		- `[]`: ตรงกับอักขระใด ๆ ที่อยู่ในวงเล็บ ตัวอย่างเช่น `[abc]` จะตรงกับ `a`, `b` หรือ `c` เท่านั้น

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ pattern ได้ที่ [Picomatch's Basic globbing](https://github.com/micromatch/picomatch#basic-globbing){:target=_blank .external-link}

### Read File(s) From Disk options

สามารถตั้งค่า option เพิ่มเติมได้ดังนี้:

* **File Extension**: กรอกนามสกุลไฟล์ที่ต้องการให้แสดงใน output
* **File Name**: กรอกชื่อไฟล์ที่ต้องการให้แสดงใน output
* **MIME Type**: กรอก MIME type ของไฟล์ใน output ดูตัวอย่าง MIME type ได้ที่ [Common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types){:target=_blank .external-link}
* **Put Output File in Field**: กรอกชื่อ field ใน output data ที่จะเก็บไฟล์

## Write File to Disk

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **File Path and Name**: กรอก path ปลายทาง ชื่อไฟล์ และนามสกุลไฟล์
* **Input Binary Field**: กรอกชื่อ field ใน input data ที่จะเก็บไฟล์ binary

### Write File to Disk options

operation นี้จะมี option ให้เลือกเพียงอย่างเดียว คือ **Append** เลือกว่าจะเพิ่มข้อมูลเข้าไฟล์เดิม (เปิด) หรือสร้างไฟล์ใหม่แทน (ปิด)

## Templates and examples

[[ templatesWidget(page.title, 'readwrite-files-from-disk') ]]

## File locations

ถ้าคุณรัน n8n ใน Docker คำสั่งจะถูกรันใน container ของ n8n ไม่ใช่บน host ของ Docker

node นี้จะมองหาไฟล์โดยอิงจาก path ที่ติดตั้ง n8n แนะนำให้ใช้ absolute path เพื่อป้องกัน error
