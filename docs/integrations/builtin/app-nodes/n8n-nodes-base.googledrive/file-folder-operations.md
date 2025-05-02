---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Drive File and Folder operations
description: Documentation for the File and Folder operations in Google Drive node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
contentType: [integration, reference]
priority: high
---

# Google Drive File and Folder operations

ใช้ Operation นี้เพื่อค้นหา Files และ Folders ใน Google Drive โปรดดูข้อมูลเพิ่มเติมเกี่ยวกับ Google Drive node ที่ [Google Drive](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/index.md)

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Search files and folders

ใช้ Operation นี้เพื่อค้นหา Files และ Folders ใน Drive

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **File/Folder**
- **Operation**: เลือก **Search**
- **Search Method**: เลือกวิธีที่คุณต้องการค้นหา:
	- **Search File/Folder Name**: กรอก **Search Query** ด้วยชื่อของ File หรือ Folder ที่คุณต้องการค้นหา คืนค่า Files และ Folders ที่ตรงกับ Query บางส่วนด้วย
	- **Advanced Search**: กรอก **Query String** เพื่อค้นหา Files และ Folders โดยใช้ [Google query string syntax](https://developers.google.com/drive/api/guides/search-files)
- **Return All**: เลือกว่าจะคืนค่าผลลัพธ์ทั้งหมด หรือคืนค่าตามจำนวนที่กำหนด
- **Limit**: จำนวน Items สูงสุดที่จะคืนค่าเมื่อ **Return All** ถูกปิดใช้งาน
- **Filter**: เลือกว่าจะจำกัดขอบเขตการค้นหาของคุณหรือไม่:
	- **Drive**: Drive ที่คุณต้องการค้นหา โดยค่าเริ่มต้นจะใช้ "My Drive" ส่วนตัวของคุณ เลือก **From list** เพื่อเลือก Drive จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Drive, หรือ **By ID** เพื่อป้อน `driveId`
		- คุณสามารถหา `driveId` ได้โดยการเข้าไปที่ Shared drive ในเบราว์เซอร์ของคุณและคัดลอกส่วนสุดท้ายของ URL: `https://drive.google.com/drive/u/1/folders/driveId`
	- **Folder**: Folder ที่จะค้นหา เลือก **From list** เพื่อเลือก Folder จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Folder, หรือ **By ID** เพื่อป้อน `folderId`
		- คุณสามารถหา `folderId` ได้โดยการเข้าไปที่ Shared folder ในเบราว์เซอร์ของคุณและคัดลอกส่วนสุดท้ายของ URL: `https://drive.google.com/drive/u/1/folders/folderId`
	- **What to Search**: ระบุว่าจะค้นหา **Files and Folders**, **Files**, หรือ **Folders**
	- **Include Trashed Items**: ระบุว่าจะคืนค่า Items ที่อยู่ใน Trash ของ Drive ด้วยหรือไม่


### Options

- **Fields**: เลือก Fields ที่จะคืนค่า สามารถเป็นหนึ่งหรือหลายรายการต่อไปนี้: **[All]**, **explicitlyTrashed**, **exportLinks**, **hasThumbnail**, **iconLink**, **ID**, **Kind**, **mimeType**, **Name**, **Permissions**, **Shared**, **Spaces**, **Starred**, **thumbnailLink**, **Trashed**, **Version**, หรือ **webViewLink**

โปรดดูเอกสาร API [Method: files.list | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/list){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
