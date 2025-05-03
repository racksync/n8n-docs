---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การทำงานกับ File ของ Google Drive
description: เอกสารสำหรับการทำงานกับ File ใน Google Drive node ของ n8n แพลตฟอร์มอัตโนมัติเวิร์กโฟลว์ รวมถึงรายละเอียด operations การกำหนดค่า และลิงก์ไปยังตัวอย่างและข้อมูล credentials
contentType: [integration, reference]
priority: high
---

# Google Drive File operations

ใช้ Operation นี้เพื่อสร้าง, ลบ, เปลี่ยนแปลง และจัดการ Files ใน Google Drive โปรดดูข้อมูลเพิ่มเติมเกี่ยวกับ Google Drive node ที่ [Google Drive](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/index.md)

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Copy a file

ใช้ Operation นี้เพื่อคัดลอก File ไปยัง Drive

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **File**
- **Operation**: เลือก **Copy**
- **File**: เลือก File ที่คุณต้องการคัดลอก
    - เลือก **From list** เพื่อเลือก Title จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ File, หรือ **By ID** เพื่อป้อน `fileId`
    - คุณสามารถหา `fileId` ได้ใน URL ของ Google Drive file ที่แชร์ได้: `https://docs.google.com/document/d/fileId/edit#gid=0` ใน Google Drive ของคุณ เลือก **Share > Copy link** เพื่อรับ URL ของ File ที่แชร์ได้
- **File Name**: ชื่อที่จะใช้สำหรับสำเนาใหม่ของ File
- **Copy In The Same Folder**: เลือกว่าจะคัดลอก File ไปยัง Folder เดียวกันหรือไม่ หากปิดใช้งาน ให้ตั้งค่าต่อไปนี้:
	- **Parent Drive**: เลือก **From list** เพื่อเลือก Drive จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Drive, หรือ **By ID** เพื่อป้อน `driveId`
	- **Parent Folder**: เลือก **From list** เพื่อเลือก Folder จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Folder, หรือ **By ID** เพื่อป้อน `folderId`
	- คุณสามารถหา `driveId` และ `folderID` ได้โดยการเข้าไปที่ Shared drive หรือ Folder ในเบราว์เซอร์ของคุณและคัดลอกส่วนสุดท้ายของ URL: `https://drive.google.com/drive/u/1/folders/driveId`

### Options

- **Copy Requires Writer Permissions**: เลือกว่าจะอนุญาตให้ Readers และ Commenters คัดลอก, พิมพ์ หรือดาวน์โหลด File ใหม่หรือไม่
- **Description**: คำอธิบายสั้นๆ ของ File

โปรดดูเอกสาร API [Method: files.copy | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/copy){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Create from text

ใช้ Operation นี้เพื่อสร้าง File ใหม่ใน Drive จาก Text ที่ให้มา

ป้อน Parameters เหล่านี้:
- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **File**
- **Operation**: เลือก **Create From Text**
- **File Content**: ป้อนเนื้อหา File ที่จะใช้สร้าง File ใหม่
- **File Name**: ชื่อที่จะใช้สำหรับ File ใหม่
- **Parent Drive**: เลือก **From list** เพื่อเลือก Drive จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Drive, หรือ **By ID** เพื่อป้อน `driveId`
- **Parent Folder**: เลือก **From list** เพื่อเลือก Folder จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Folder, หรือ **By ID** เพื่อป้อน `folderId`

คุณสามารถหา `driveId` และ `folderID` ได้โดยการเข้าไปที่ Shared drive หรือ Folder ในเบราว์เซอร์ของคุณและคัดลอกส่วนสุดท้ายของ URL: `https://drive.google.com/drive/u/1/folders/driveId`

### Options

- **APP Properties**: ชุดของ Key-value pairs ที่กำหนดเองซึ่งเป็น Private สำหรับแอปที่ร้องขอ
- **Properties**: ชุดของ Key-value pairs ที่กำหนดเองซึ่งมองเห็นได้โดยทุกแอป
- **Keep Revision Forever**: เลือกว่าจะตั้งค่า Field `keepForever` ใน Head revision ใหม่หรือไม่ สิ่งนี้ใช้ได้กับ Files ที่มีเนื้อหา Binary เท่านั้น คุณสามารถเก็บ Revisions ได้สูงสุด 200 รายการ หลังจากนั้นคุณต้องลบ Pinned revisions
<!-- vale from-microsoft.RangeFormat = NO -->
<!-- vale from-microsoft.Ranges = NO -->
- **OCR Language**: รหัสภาษา [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) เพื่อช่วยให้ OCR ตีความเนื้อหาในระหว่างการ Import
<!-- vale from-microsoft.Ranges = YES -->
<!-- vale from-microsoft.RangeFormat = YES -->
- **Use Content As Indexable Text**: เลือกว่าจะทำเครื่องหมายเนื้อหาที่อัปโหลดเป็น Indexable text หรือไม่
- **Convert to Google Document**: เลือกว่าจะสร้าง Google Document แทนรูปแบบ `.txt` เริ่มต้นหรือไม่ คุณต้องเปิดใช้งาน Google Docs API ใน [Google API Console](https://console.cloud.google.com/apis/library/docs.googleapis.com) เพื่อให้ทำงานได้

โปรดดูเอกสาร API [Method: files.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/insert){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Delete a file

ใช้ Operation นี้เพื่อลบ File ออกจาก Drive

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **File**
- **Operation**: เลือก **Delete**
- **File**: เลือก File ที่คุณต้องการลบ
    - เลือก **From list** เพื่อเลือก Title จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ File, หรือ **By ID** เพื่อป้อน `fileId`
    - คุณสามารถหา `fileId` ได้ใน URL ของ Google Drive file ที่แชร์ได้: `https://docs.google.com/document/d/fileId/edit#gid=0` ใน Google Drive ของคุณ เลือก **Share > Copy link** เพื่อรับ URL ของ File ที่แชร์ได้

### Options

- **Delete Permanently**: เลือกว่าจะลบ File ทันทีแทนที่จะย้ายไปยัง Trash หรือไม่

โปรดดูเอกสาร API [Method: files.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/delete){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Download a file

ใช้ Operation นี้เพื่อดาวน์โหลด File จาก Drive

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **File**
- **Operation**: เลือก **Download**
- **File**: เลือก File ที่คุณต้องการดาวน์โหลด
    - เลือก **From list** เพื่อเลือก Title จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ File, หรือ **By ID** เพื่อป้อน `fileId`
    - คุณสามารถหา `fileId` ได้ใน URL ของ Google Drive file ที่แชร์ได้: `https://docs.google.com/document/d/fileId/edit#gid=0` ใน Google Drive ของคุณ เลือก **Share > Copy link** เพื่อรับ URL ของ File ที่แชร์ได้

### Options

- **Put Output File in Field**: เลือกชื่อ Field ที่จะใส่เนื้อหา Binary file เพื่อให้พร้อมใช้งานสำหรับ Nodes ถัดไป
- **Google File Conversion**: เลือก Format ที่จะ Export เมื่อดาวน์โหลด Google Files:
	* **Google Docs**: เลือก Format การ Export ที่จะใช้เมื่อดาวน์โหลด Google Docs files: **HTML**, **MS Word Document**, **Open Office Document**, **PDF**, **Rich Text (rtf)**, หรือ **Text (txt)**
	* **Google Drawings**: เลือก Format การ Export ที่จะใช้เมื่อดาวน์โหลด Google Drawing files: **JPEG**, **PDF**, **PNG**, หรือ **SVG**
	* **Google Slides**: เลือก Format การ Export ที่จะใช้เมื่อดาวน์โหลด Google Slides files: **MS PowerPoint**, **OpenOffice Presentation**, หรือ **PDF**
	* **Google Sheets**: เลือก Format การ Export ที่จะใช้เมื่อดาวน์โหลด Google Sheets files: **CSV**, **MS Excel**, **Open Office Sheet**, หรือ **PDF**
- **File Name**: ชื่อที่จะใช้สำหรับ File ที่ดาวน์โหลด

โปรดดูเอกสาร API [Method: files.get | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/get){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Move a file

ใช้ Operation นี้เพื่อย้าย File ไปยังตำแหน่งอื่นใน Drive

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **File**
- **Operation**: เลือก **Move**
- **File**: เลือก File ที่คุณต้องการย้าย
    - เลือก **From list** เพื่อเลือก Title จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ File, หรือ **By ID** เพื่อป้อน `fileId`
    - คุณสามารถหา `fileId` ได้ใน URL ของ Google Drive file ที่แชร์ได้: `https://docs.google.com/document/d/fileId/edit#gid=0` ใน Google Drive ของคุณ เลือก **Share > Copy link** เพื่อรับ URL ของ File ที่แชร์ได้
- **Parent Drive**: เลือก **From list** เพื่อเลือก Drive จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Drive, หรือ **By ID** เพื่อป้อน `driveId`
- **Parent Folder**: เลือก **From list** เพื่อเลือก Folder จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Folder, หรือ **By ID** เพื่อป้อน `folderId`

คุณสามารถหา `driveId` และ `folderID` ได้โดยการเข้าไปที่ Shared drive หรือ Folder ในเบราว์เซอร์ของคุณและคัดลอกส่วนสุดท้ายของ URL: `https://drive.google.com/drive/u/1/folders/driveId`

โปรดดูเอกสาร API [Method: parents.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/parents/insert){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Share a file

ใช้ Operation นี้เพื่อเพิ่ม Permissions การแชร์ให้กับ File

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **File**
- **Operation**: เลือก **Share**
- **File**: เลือก File ที่คุณต้องการแชร์
    - เลือก **From list** เพื่อเลือก Title จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ File, หรือ **By ID** เพื่อป้อน `fileId`
    - คุณสามารถหา `fileId` ได้ใน URL ของ Google Drive file ที่แชร์ได้: `https://docs.google.com/document/d/fileId/edit#gid=0` ใน Google Drive ของคุณ เลือก **Share > Copy link** เพื่อรับ URL ของ File ที่แชร์ได้
- **Permissions**: Permissions ที่จะเพิ่มให้กับ File:
	- **Role**: เลือกว่า Users สามารถทำอะไรกับ File ได้บ้าง สามารถเป็นหนึ่งใน **Commenter**, **File Organizer**, **Organizer**, **Owner**, **Reader**, **Writer**
	- **Type**: เลือกขอบเขตของ Permission ใหม่:
		- **User**: ให้ Permission แก่ User ที่ระบุ โดยกำหนดโดยการป้อน **Email Address** ของพวกเขา
		- **Group**: ให้ Permission แก่ Group ที่ระบุ โดยกำหนดโดยการป้อน **Email Address** ของกลุ่ม
		- **Domain**: ให้ Permission แก่ Domain ทั้งหมด โดยกำหนดโดย **Domain**
		- **Anyone**: ให้ Permission แก่ทุกคน สามารถเลือก **Allow File Discovery** เพื่อทำให้ File สามารถค้นพบได้ผ่านการค้นหา

### Options

- **Email Message**: ข้อความ Plain text ที่กำหนดเองเพื่อรวมไว้ในอีเมลแจ้งเตือน
<!-- vale from-microsoft.FirstPerson = NO -->
- **Move to New Owners Root**: ใช้ได้เมื่อพยายามถ่ายโอน Ownership ขณะแชร์ Item ที่ไม่ได้อยู่ใน Shared drive เมื่อเปิดใช้งาน จะย้าย File ไปยัง My Drive root folder ของ Owner ใหม่
<!-- vale from-microsoft.FirstPerson = YES -->
- **Send Notification Email**: ระบุว่าจะส่งอีเมลแจ้งเตือนเมื่อแชร์ไปยัง Users หรือ Groups หรือไม่
- **Transfer Ownership**: ระบุว่าจะถ่ายโอน Ownership ให้กับ User ที่ระบุและลดระดับ Permissions ของ Owner ปัจจุบันเป็น Writer หรือไม่
- **Use Domain Admin Access**: ระบุว่าจะดำเนินการในฐานะ Domain administrator หรือไม่

โปรดดูเอกสาร API [REST Resources: files | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Update a file

ใช้ Operation นี้เพื่ออัปเดต File

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **File**
- **Operation**: เลือก **Update**
- **File to Update**: เลือก File ที่คุณต้องการอัปเดต
    - เลือก **From list** เพื่อเลือก Title จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ File, หรือ **By ID** เพื่อป้อน `fileId`
    - คุณสามารถหา `fileId` ได้ใน URL ของ Google Drive file ที่แชร์ได้: `https://docs.google.com/document/d/fileId/edit#gid=0` ใน Google Drive ของคุณ เลือก **Share > Copy link** เพื่อรับ URL ของ File ที่แชร์ได้
- **Change File Content**: เลือกว่าจะส่งข้อมูล Binary ใหม่เพื่อแทนที่เนื้อหา File ที่มีอยู่หรือไม่ หากเปิดใช้งาน ให้กรอกข้อมูลต่อไปนี้:
	- **Input Data Field Name**: ชื่อของ Input field ที่มีข้อมูล Binary file ที่คุณต้องการใช้
- **New Updated File Name**: ชื่อใหม่สำหรับ File หากคุณต้องการอัปเดตชื่อไฟล์

### Options

- **APP Properties**: ชุดของ Key-value pairs ที่กำหนดเองซึ่งเป็น Private สำหรับแอปที่ร้องขอ
- **Properties**: ชุดของ Key-value pairs ที่กำหนดเองซึ่งมองเห็นได้โดยทุกแอป
- **Keep Revision Forever**: เลือกว่าจะตั้งค่า Field `keepForever` ใน Head revision ใหม่หรือไม่ สิ่งนี้ใช้ได้กับ Files ที่มีเนื้อหา Binary เท่านั้น คุณสามารถเก็บ Revisions ได้สูงสุด 200 รายการ หลังจากนั้นคุณต้องลบ Pinned revisions
<!-- vale from-microsoft.RangeFormat = NO -->
<!-- vale from-microsoft.Ranges = NO -->
- **OCR Language**: รหัสภาษา [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) เพื่อช่วยให้ OCR ตีความเนื้อหาในระหว่างการ Import
<!-- vale from-microsoft.Ranges = YES -->
<!-- vale from-microsoft.RangeFormat = YES -->
- **Use Content As Indexable Text**: เลือกว่าจะทำเครื่องหมายเนื้อหาที่อัปโหลดเป็น Indexable text หรือไม่
- **Move to Trash**: ระบุว่าจะย้าย File ไปยัง Trash หรือไม่ ทำได้เฉพาะ Owner ของ File เท่านั้น
- **Return Fields**: คืนค่า Metadata fields เกี่ยวกับ File สามารถเป็นหนึ่งหรือหลายรายการต่อไปนี้: **[All]**, **explicitlyTrashed**, **exportLinks**, **hasThumbnail**, **iconLink**, **ID**, **Kind**, **mimeType**, **Name**, **Permissions**, **Shared**, **Spaces**, **Starred**, **thumbnailLink**, **Trashed**, **Version**, หรือ **webViewLink**

โปรดดูเอกสาร API [Method: files.update | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/update){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Upload a file

ใช้ Operation นี้เพื่ออัปโหลด File

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **File**
- **Operation**: เลือก **Upload**
- **Input Data Field Name**: ชื่อของ Input field ที่มีข้อมูล Binary file ที่คุณต้องการใช้
- **File Name**: ชื่อที่จะใช้สำหรับ File ใหม่
- **Parent Drive**: เลือก **From list** เพื่อเลือก Drive จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Drive, หรือ **By ID** เพื่อป้อน `driveId`
- **Parent Folder**: เลือก **From list** เพื่อเลือก Folder จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Folder, หรือ **By ID** เพื่อป้อน `folderId`

คุณสามารถหา `driveId` และ `folderID` ได้โดยการเข้าไปที่ Shared drive หรือ Folder ในเบราว์เซอร์ของคุณและคัดลอกส่วนสุดท้ายของ URL: `https://drive.google.com/drive/u/1/folders/driveId`

### Options

- **APP Properties**: ชุดของ Key-value pairs ที่กำหนดเองซึ่งเป็น Private สำหรับแอปที่ร้องขอ
- **Properties**: ชุดของ Key-value pairs ที่กำหนดเองซึ่งมองเห็นได้โดยทุกแอป
- **Keep Revision Forever**: เลือกว่าจะตั้งค่า Field `keepForever` ใน Head revision ใหม่หรือไม่ สิ่งนี้ใช้ได้กับ Files ที่มีเนื้อหา Binary เท่านั้น คุณสามารถเก็บ Revisions ได้สูงสุด 200 รายการ หลังจากนั้นคุณต้องลบ Pinned revisions
<!-- vale from-microsoft.RangeFormat = NO -->
<!-- vale from-microsoft.Ranges = NO -->
- **OCR Language**: รหัสภาษา [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) เพื่อช่วยให้ OCR ตีความเนื้อหาในระหว่างการ Import
<!-- vale from-microsoft.Ranges = YES -->
<!-- vale from-microsoft.RangeFormat = YES -->
- **Use Content As Indexable Text**: เลือกว่าจะทำเครื่องหมายเนื้อหาที่อัปโหลดเป็น Indexable text หรือไม่
- **Simplify Output**: เลือกว่าจะคืนค่า Response ในรูปแบบที่เรียบง่ายแทนที่จะรวม Fields ทั้งหมดหรือไม่

โปรดดูเอกสาร API [Method: files.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/insert){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
