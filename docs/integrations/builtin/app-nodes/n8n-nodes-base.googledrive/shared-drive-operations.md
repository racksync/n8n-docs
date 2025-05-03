---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การทำงานกับ Shared Drive ของ Google Drive
description: เอกสารสำหรับการทำงานกับ Shared Drive ใน Google Drive node ของ n8n แพลตฟอร์มอัตโนมัติเวิร์กโฟลว์ รวมถึงรายละเอียด operations การกำหนดค่า และลิงก์ไปยังตัวอย่างและข้อมูล credentials
contentType: [integration, reference]
priority: high
---

# Google Drive Shared Drive operations

ใช้ Operation นี้เพื่อสร้าง, ลบ, ดึงข้อมูล และอัปเดต Shared drives ใน Google Drive โปรดดูข้อมูลเพิ่มเติมเกี่ยวกับ Google Drive node ที่ [Google Drive](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/index.md)

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Create a shared drive

ใช้ Operation นี้เพื่อสร้าง Shared drive ใหม่

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Shared Drive**
- **Operation**: เลือก **Create**
- **Name**: ชื่อที่จะใช้สำหรับ Shared drive ใหม่

### Options

- **Capabilities**: Capabilities ที่จะตั้งค่าสำหรับ Shared drive ใหม่ (ดูรายละเอียดเพิ่มเติมที่ [REST Resources: drives | Google Drive](https://developers.google.com/drive/api/reference/rest/v3/drives)):
	- **Can Add Children**: ระบุว่า User ปัจจุบันสามารถเพิ่ม Children ไปยัง Folders ใน Shared drive นี้ได้หรือไม่
	- **Can Change Copy Requires Writer Permission Restriction**: ระบุว่า User ปัจจุบันสามารถเปลี่ยนข้อจำกัด `copyRequiresWriterPermission` ใน Shared drive นี้ได้หรือไม่
	- **Can Change Domain Users Only Restriction**: ระบุว่า User ปัจจุบันสามารถเปลี่ยนข้อจำกัด `domainUsersOnly` ใน Shared drive นี้ได้หรือไม่
	- **Can Change Drive Background**: ระบุว่า User ปัจจุบันสามารถเปลี่ยน Background ของ Shared drive นี้ได้หรือไม่
	- **Can Change Drive Members Only Restriction**: ระบุว่า User ปัจจุบันสามารถเปลี่ยนข้อจำกัด `driveMembersOnly` ใน Shared drive นี้ได้หรือไม่
	- **Can Comment**: ระบุว่า User ปัจจุบันสามารถแสดงความคิดเห็นเกี่ยวกับ Files ใน Shared drive นี้ได้หรือไม่
	- **Can Copy**: ระบุว่า User ปัจจุบันสามารถคัดลอก Files ใน Shared drive นี้ได้หรือไม่
	- **Can Delete Children**: ระบุว่า User ปัจจุบันสามารถลบ Children ออกจาก Folders ใน Shared drive นี้ได้หรือไม่
	- **Can Delete Drive**: ระบุว่า User ปัจจุบันสามารถลบ Shared drive นี้ได้หรือไม่ Operation นี้อาจยังคงล้มเหลวหากมี Items ที่ไม่ได้อยู่ใน Trash ใน Shared drive
	- **Can Download**: ระบุว่า User ปัจจุบันสามารถดาวน์โหลด Files จาก Shared drive นี้ได้หรือไม่
	- **Can Edit**: ระบุว่า User ปัจจุบันสามารถแก้ไข Files จาก Shared drive นี้ได้หรือไม่
	- **Can List Children**: ระบุว่า User ปัจจุบันสามารถแสดงรายการ Children ของ Folders ใน Shared drive นี้ได้หรือไม่
	- **Can Manage Members**: ระบุว่า User ปัจจุบันสามารถเพิ่ม, ลบ หรือเปลี่ยน Role ของ Members ใน Shared drive นี้ได้หรือไม่
	- **Can Read Revisions**: ระบุว่า User ปัจจุบันสามารถอ่าน Revisions resource ของ Files ใน Shared drive นี้ได้หรือไม่
	- **Can Rename Drive**: ระบุว่า User ปัจจุบันสามารถเปลี่ยนชื่อ Shared drive นี้ได้หรือไม่
	- **Can Share**: ระบุว่า User ปัจจุบันสามารถแชร์ Files หรือ Folders ใน Shared drive นี้ได้หรือไม่
	- **Can Trash Children**: ระบุว่า User ปัจจุบันสามารถย้าย Children จาก Folders ไปยัง Trash ใน Shared drive นี้ได้หรือไม่
- **Color RGB**: สีของ Shared drive นี้ในรูปแบบ RGB hex string
- **Hidden**: ระบุว่าจะซ่อน Shared drive นี้ในมุมมองเริ่มต้นหรือไม่
- **Restrictions**: ข้อจำกัดที่จะเพิ่มให้กับ Shared drive นี้ (ดูรายละเอียดเพิ่มเติมที่ [REST Resources: drives | Google Drive](https://developers.google.com/drive/api/reference/rest/v3/drives)):
	- **Admin Managed Restrictions**: เมื่อเปิดใช้งาน ข้อจำกัดที่นี่จะ Override field ที่มีชื่อคล้ายกันเป็น True สำหรับ File ใดๆ ภายใน Shared drive นี้
	- **Copy Requires Writer Permission**: ระบุว่าตัวเลือกในการคัดลอก, พิมพ์ หรือดาวน์โหลด Files ภายใน Shared drive นี้ควรถูกปิดใช้งานสำหรับ Readers และ Commenters หรือไม่
	- **Domain Users Only**: ระบุว่าจะจำกัดการเข้าถึง Shared drive นี้และ Items ภายใน Shared drive นี้เฉพาะ Users ของ Domain ที่ Shared drive นี้เป็นส่วนหนึ่งหรือไม่
	- **Drive Members Only**: ระบุว่าจะจำกัดการเข้าถึง Items ภายใน Shared drive นี้เฉพาะ Members ของมันหรือไม่

โปรดดูเอกสาร API [Method: drives.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/insert){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Delete a shared drive

ใช้ Operation นี้เพื่อลบ Shared drive

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Shared Drive**
- **Operation**: เลือก **Delete**
- **Shared Drive**: เลือก Shared drive ที่คุณต้องการลบ
    - เลือก **From list** เพื่อเลือก Title จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Drive, หรือ **By ID** เพื่อป้อน `driveId`
    - คุณสามารถหา `driveId` ได้ใน URL ของ Shared Google Drive: `https://drive.google.com/drive/u/0/folders/driveID`

โปรดดูเอกสาร API [Method: drives.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/delete){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Get a shared drive

ใช้ Operation นี้เพื่อดึงข้อมูล Shared drive

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Shared Drive**
- **Operation**: เลือก **Get**
- **Shared Drive**: เลือก Shared drive ที่คุณต้องการดึงข้อมูล
    - เลือก **From list** เพื่อเลือก Title จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Drive, หรือ **By ID** เพื่อป้อน `driveId`
    - คุณสามารถหา `driveId` ได้ใน URL ของ Shared Google Drive: `https://drive.google.com/drive/u/0/folders/driveID`

### Options

- **Use Domain Admin Access**: ระบุว่าจะส่ง Request ในฐานะ Domain administrator หรือไม่ เมื่อเปิดใช้งาน จะให้สิทธิ์การเข้าถึงแก่ Requester หากพวกเขาเป็น Administrator ของ Domain ที่ Shared drive นั้นเป็นส่วนหนึ่ง

โปรดดูเอกสาร API [Method: drives.get | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/get){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

<!-- vale from-write-good.Weasel = NO -->
## Get many shared drives

ใช้ Operation นี้เพื่อดึงข้อมูล Shared drives หลายรายการ
<!-- vale from-write-good.Weasel = YES -->

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Shared Drive**
- **Operation**: เลือก **Get Many**
- **Return All**: เลือกว่าจะคืนค่าผลลัพธ์ทั้งหมด หรือคืนค่าตามจำนวนที่กำหนด
- **Limit**: จำนวน Items สูงสุดที่จะคืนค่าเมื่อ **Return All** ถูกปิดใช้งาน
- **Shared Drive**: เลือก Shared drive ที่คุณต้องการดึงข้อมูล
    - เลือก **From list** เพื่อเลือก Title จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Drive, หรือ **By ID** เพื่อป้อน `driveId`
    - คุณสามารถหา `driveId` ได้ใน URL ของ Shared Google Drive: `https://drive.google.com/drive/u/0/folders/driveID`

### Options

- **Query**: Query string ที่จะใช้ในการค้นหา Shared drives ดูข้อมูลเพิ่มเติมที่ [Search for shared drives | Google Drive](https://developers.google.com/drive/api/guides/search-shareddrives)
- **Use Domain Admin Access**: ระบุว่าจะส่ง Request ในฐานะ Domain administrator หรือไม่ เมื่อเปิดใช้งาน จะให้สิทธิ์การเข้าถึงแก่ Requester หากพวกเขาเป็น Administrator ของ Domain ที่ Shared drive นั้นเป็นส่วนหนึ่ง

โปรดดูเอกสาร API [Method: drives.get | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/get){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Update a shared drive

ใช้ Operation นี้เพื่ออัปเดต Shared drive

ป้อน Parameters เหล่านี้:

- **Credential to connect with**: สร้างหรือเลือก [Google Drive credentials](/integrations/builtin/credentials/google/index.md) ที่มีอยู่
- **Resource**: เลือก **Shared Drive**
- **Operation**: เลือก **Update**
- **Shared Drive**: เลือก Shared drive ที่คุณต้องการอัปเดต
    - เลือก **From list** เพื่อเลือก Drive จากรายการ Dropdown, **By URL** เพื่อป้อน URL ของ Drive, หรือ **By ID** เพื่อป้อน `driveId`
    - คุณสามารถหา `driveId` ได้ใน URL ของ Shared Google Drive: `https://drive.google.com/drive/u/0/folders/driveID`

### Update Fields

- **Color RGB**: สีของ Shared drive นี้ในรูปแบบ RGB hex string
- **Name**: ชื่อที่อัปเดตสำหรับ Shared drive
- **Restrictions**: ข้อจำกัดสำหรับ Shared drive นี้ (ดูรายละเอียดเพิ่มเติมที่ [REST Resources: drives | Google Drive](https://developers.google.com/drive/api/reference/rest/v3/drives)):
	- **Admin Managed Restrictions**: เมื่อเปิดใช้งาน ข้อจำกัดที่นี่จะ Override field ที่มีชื่อคล้ายกันเป็น True สำหรับ File ใดๆ ภายใน Shared drive นี้
	- **Copy Requires Writer Permission**: ระบุว่าตัวเลือกในการคัดลอก, พิมพ์ หรือดาวน์โหลด Files ภายใน Shared drive นี้ควรถูกปิดใช้งานสำหรับ Readers และ Commenters หรือไม่
	- **Domain Users Only**: ระบุว่าจะจำกัดการเข้าถึง Shared drive นี้และ Items ภายใน Shared drive นี้เฉพาะ Users ของ Domain ที่ Shared drive นี้เป็นส่วนหนึ่งหรือไม่
	- **Drive Members Only**: ระบุว่าจะจำกัดการเข้าถึง Items ภายใน Shared drive นี้เฉพาะ Members ของมันหรือไม่

โปรดดูเอกสาร API [Method: drives.update | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/update){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
