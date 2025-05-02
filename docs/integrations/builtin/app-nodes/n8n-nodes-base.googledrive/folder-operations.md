---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Drive Folder operations
description: Documentation for the Folder operations in Google Drive node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
contentType: [integration, reference]
priority: high
---

# Google Drive Folder operations

ใช้ Operation นี้เพื่อสร้าง, ลบ และแชร์ Folders ใน Google Drive โปรดดูข้อมูลเพิ่มเติมเกี่ยวกับ Google Drive node ที่ [Google Drive](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/index.md)

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Create a folder

ใช้ Operation นี้เพื่อสร้าง Folder ใหม่ใน Drive

ป้อน Parameters เหล่านี้:
- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Folder**
- **Operation**: เลือก **Create**
- **Folder Name**: ชื่อที่จะใช้สำหรับ Folder ใหม่
- **Parent Drive**: เลือก **From list** เพื่อเลือก Drive จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Drive, หรือ **By ID** เพื่อป้อน `driveId`
- **Parent Folder**: เลือก **From list** เพื่อเลือก Folder จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Folder, หรือ **By ID** เพื่อป้อน `folderId`

คุณสามารถหา `driveId` และ `folderID` ได้โดยการเข้าไปที่ Shared drive หรือ Folder ในเบราว์เซอร์ของคุณและคัดลอกส่วนสุดท้ายของ URL: `https://drive.google.com/drive/u/1/folders/driveId`

### Options

- **Simplify Output**: เลือกว่าจะคืนค่า Response ในรูปแบบที่เรียบง่ายแทนที่จะรวม Fields ทั้งหมดหรือไม่
- **Folder Color**: สีของ Folder ในรูปแบบ RGB hex string

โปรดดูเอกสาร API [Method: files.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/insert){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Delete a folder

ใช้ Operation นี้เพื่อลบ Folder ออกจาก Drive

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Folder**
- **Operation**: เลือก **Delete**
- **Folder**: เลือก Folder ที่คุณต้องการลบ
    - เลือก **From list** เพื่อเลือก Folder จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Folder, หรือ **By ID** เพื่อป้อน `folderId`
    - คุณสามารถหา `folderId` ได้ใน URL ของ Google Drive folder: `https://drive.google.com/drive/u/0/folders/folderID`

### Options

- **Delete Permanently**: เลือกว่าจะลบ Folder ทันทีแทนที่จะย้ายไปยัง Trash หรือไม่

โปรดดูเอกสาร API [Method: files.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/delete){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Share a folder

ใช้ Operation นี้เพื่อเพิ่ม Permissions การแชร์ให้กับ Folder

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Folder**
- **Operation**: เลือก **Share**
- **Folder**: เลือก Folder ที่คุณต้องการย้าย
    - เลือก **From list** เพื่อเลือก Folder จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Folder, หรือ **By ID** เพื่อป้อน `folderId`
    - คุณสามารถหา `folderId` ได้ใน URL ของ Google Drive folder: `https://drive.google.com/drive/u/0/folders/folderID`
- **Permissions**: Permissions ที่จะเพิ่มให้กับ Folder:
	- **Role**: เลือกว่า Users สามารถทำอะไรกับ Folder ได้บ้าง สามารถเป็นหนึ่งใน **Commenter**, **File Organizer**, **Organizer**, **Owner**, **Reader**, **Writer**
	- **Type**: เลือกขอบเขตของ Permission ใหม่:
		- **User**: ให้ Permission แก่ User ที่ระบุ โดยกำหนดโดยการป้อน **Email Address** ของพวกเขา
		- **Group**: ให้ Permission แก่ Group ที่ระบุ โดยกำหนดโดยการป้อน **Email Address** ของกลุ่ม
		- **Domain**: ให้ Permission แก่ Domain ทั้งหมด โดยกำหนดโดย **Domain**
		- **Anyone**: ให้ Permission แก่ทุกคน สามารถเลือก **Allow File Discovery** เพื่อทำให้ File สามารถค้นพบได้ผ่านการค้นหา

### Options

- **Email Message**: ข้อความ Plain text ที่กำหนดเองเพื่อรวมไว้ในอีเมลแจ้งเตือน
<!-- vale from-microsoft.FirstPerson = NO -->
- **Move to New Owners Root**: ใช้ได้เมื่อพยายามถ่ายโอน Ownership ขณะแชร์ Item ที่ไม่ได้อยู่ใน Shared drive เมื่อเปิดใช้งาน จะย้าย Folder ไปยัง My Drive root folder ของ Owner ใหม่
<!-- vale from-microsoft.FirstPerson = YES -->
- **Send Notification Email**: ระบุว่าจะส่งอีเมลแจ้งเตือนเมื่อแชร์ไปยัง Users หรือ Groups หรือไม่
- **Transfer Ownership**: ระบุว่าจะถ่ายโอน Ownership ให้กับ User ที่ระบุและลดระดับ Permissions ของ Owner ปัจจุบันเป็น Writer หรือไม่
- **Use Domain Admin Access**: ระบุว่าจะดำเนินการในฐานะ Domain administrator หรือไม่

โปรดดูเอกสาร API [REST Resources: files | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
