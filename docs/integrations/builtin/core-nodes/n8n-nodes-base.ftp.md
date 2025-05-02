---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: FTP
description: Documentation for the FTP node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: medium
---

# FTP

FTP node ใช้สำหรับเข้าถึงและอัปโหลดไฟล์ไปยัง FTP หรือ SFTP server

/// note | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ที่ [FTP credentials](/integrations/builtin/credentials/ftp.md)
///

ถ้าต้องการเชื่อมต่อ SFTP server ให้ใช้ SFTP credential ดูรายละเอียดได้ที่ [FTP credentials](/integrations/builtin/credentials/ftp.md)

## Operations

- [**Delete**](#delete) ลบไฟล์หรือโฟลเดอร์
- [**Download**](#download) ดาวน์โหลดไฟล์
- [**List**](#list) ดูเนื้อหาในโฟลเดอร์
- [**Rename**](#rename) หรือย้ายไฟล์/โฟลเดอร์
- [**Upload**](#upload) อัปโหลดไฟล์

/// note | Uploading files
ถ้าต้องการแนบไฟล์เพื่ออัปโหลด ต้องใช้ node เพิ่มเติม เช่น [Read/Write Files from Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) หรือ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) เพื่อส่งไฟล์เป็น data property
///

## Delete

operation นี้มี parameter เดียวคือ **Path** ให้กรอก path ของไฟล์หรือโฟลเดอร์บน server ที่ต้องการลบ

### Delete options

delete operation จะมี option เพิ่มคือ **Folder** ถ้าเปิด option นี้ node จะสามารถลบทั้งโฟลเดอร์และไฟล์ได้ และจะมี option เพิ่มอีกหนึ่งตัวคือ:

- **Recursive**: ถ้าเปิด option นี้และลบโฟลเดอร์ node จะลบไฟล์และโฟลเดอร์ย่อยทั้งหมดใน directory เป้าหมาย

## Download

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Path**: กรอก path ของไฟล์บน server ที่ต้องการดาวน์โหลด
* **Put Output File in Field**: กรอกชื่อ field ที่จะเก็บไฟล์ output แบบ binary

## List

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Path**: กรอก path ของโฟลเดอร์บน server ที่ต้องการดูเนื้อหา
* **Recursive**: เลือกว่าจะให้แสดงเนื้อหาทั้งหมดแบบ recursive (เปิด) หรือไม่ (ปิด)

## Rename

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

- **Old Path**: กรอก path เดิมของไฟล์ที่ต้องการเปลี่ยนชื่อ
- **New Path**: กรอก path ใหม่หลังเปลี่ยนชื่อ

### Rename options

operation นี้จะมี option เพิ่มคือ **Create Directories** ถ้าเปิด option นี้ node จะสร้างโฟลเดอร์ปลายทางให้อัตโนมัติเมื่อเปลี่ยนชื่อไฟล์หรือโฟลเดอร์

## Upload

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Path**: กรอก path ของไฟล์บน server ที่ต้องการอัปโหลด
* **Binary File**: เลือกว่าจะอัปโหลดไฟล์แบบ binary (เปิด) หรือกรอกเนื้อหาไฟล์เป็น text (ปิด) parameter อื่นๆ จะเปลี่ยนไปตามที่เลือก
    * **Input Binary Field**: แสดงถ้าเปิด **Binary File** กรอกชื่อ field ที่เก็บไฟล์ binary ที่จะอัปโหลด
    * **File Content**: แสดงถ้าปิด **Binary File** กรอกเนื้อหา text ของไฟล์ที่จะอัปโหลด

/// note | Uploading files
ถ้าต้องการแนบไฟล์เพื่ออัปโหลด ต้องใช้ node เพิ่มเติม เช่น [Read/Write Files from Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) หรือ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) เพื่อส่งไฟล์เป็น data property
///

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'ftp') ]]
