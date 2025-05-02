---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: SSH
description: Documentation for the SSH node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: medium
---

# SSH

SSH node ใช้สำหรับรันคำสั่งผ่าน Secure Shell Protocol

/// note | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ที่ [ที่นี่](/integrations/builtin/credentials/ssh.md)
///

## Operations

- [**Execute** a command](#execute-command)
- [**Download** a file](#download-file)
- [**Upload** a file](#upload-file)

/// note | Uploading files
ถ้าจะอัปโหลดไฟล์ ต้องใช้ node เพิ่มเติม เช่น [Read/Write Files from Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) หรือ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) เพื่อส่งไฟล์เป็น data property
///

### Execute Command

ตั้งค่า operation นี้ด้วย parameters เหล่านี้:

- **Credential to connect with**: เลือกหรือสร้าง [SSH credential](/integrations/builtin/credentials/ssh.md) ที่จะใช้เชื่อมต่อ
- **Command**: ใส่คำสั่งที่ต้องการรันบนเครื่องปลายทาง
- **Working Directory**: ใส่ path ของ directory ที่จะรันคำสั่ง

### Download File

- **Credential to connect with**: เลือกหรือสร้าง [SSH credential](/integrations/builtin/credentials/ssh.md) ที่จะใช้เชื่อมต่อ
- **Path**: ใส่ path ของไฟล์ที่ต้องการดาวน์โหลด ต้องรวมชื่อไฟล์ด้วย ไฟล์ที่ดาวน์โหลดจะใช้ชื่อนี้ ถ้าอยากใช้ชื่ออื่น ให้ใช้ option **File Name** ดูรายละเอียดที่ [Download File options](#download-file-options)
- **File Property**: ใส่ชื่อ property ที่เก็บ binary data ที่ต้องการดาวน์โหลด

#### Download File options

ตั้งค่าเพิ่มเติมได้ด้วย option **File Name** ใช้เปลี่ยนชื่อไฟล์ binary data ที่ดาวน์โหลด

### Upload File

- **Credential to connect with**: เลือกหรือสร้าง [SSH credential](/integrations/builtin/credentials/ssh.md) ที่จะใช้เชื่อมต่อ
- **Input Binary Field**: ใส่ชื่อ field ที่เก็บ binary file ที่จะอัปโหลด
- **Target Directory**: ใส่ directory ที่จะอัปโหลดไฟล์ไป ชื่อไฟล์จะใช้ตาม binary data file name ถ้าอยากใช้ชื่ออื่น ให้ใช้ option **File Name** ดูรายละเอียดที่ [Upload File options](#upload-file-options)

#### Upload File options

ตั้งค่าเพิ่มเติมได้ด้วย option **File Name** ใช้เปลี่ยนชื่อไฟล์ binary data ที่อัปโหลด

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'ssh') ]]
