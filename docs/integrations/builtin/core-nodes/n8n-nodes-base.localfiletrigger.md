---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ทริกเกอร์ไฟล์ในเครื่อง (Local File Trigger)
description: คู่มือ Local File Trigger node สำหรับตรวจจับการเปลี่ยนแปลงไฟล์ใน n8n
contentType: [integration, reference]
priority: high
---

# Local File Trigger node

Local File Trigger node จะเริ่ม workflow เมื่อมีการเปลี่ยนแปลงใน file system เช่น มีไฟล์หรือโฟลเดอร์ถูกเพิ่ม เปลี่ยนแปลง หรือลบ

/// note | Self-hosted n8n only
node นี้ใช้ได้เฉพาะบน n8n ที่ติดตั้งเองเท่านั้น (ไม่รองรับบน n8n Cloud)
///

## Node parameters

คุณสามารถเลือก event ที่ต้องการตรวจจับได้โดยใช้ parameter **Trigger On**

## Changes to a Specific File

node จะ trigger เมื่อไฟล์ที่ระบุมีการเปลี่ยนแปลง

ใส่ path ของไฟล์ที่ต้องการตรวจสอบใน **File to Watch**

## Changes Involving a Specific Folder

node จะ trigger เมื่อมีการเปลี่ยนแปลงในโฟลเดอร์ที่เลือก

ตั้งค่า parameter เหล่านี้:

- **Folder to Watch**: ใส่ path ของโฟลเดอร์ที่ต้องการตรวจสอบ
- **Watch for**: เลือกประเภทของการเปลี่ยนแปลงที่ต้องการตรวจสอบ

## Node options

ใช้ **Options** ของ node เพื่อกำหนดว่าจะรวม/ยกเว้นไฟล์หรือโฟลเดอร์ใดบ้าง

- **Include Linked Files/Folders**: ตรวจสอบการเปลี่ยนแปลงของไฟล์หรือโฟลเดอร์ที่ลิงก์ด้วย
- **Ignore**: ใส่ไฟล์หรือ path ที่ต้องการยกเว้น n8n จะตรวจสอบทั้ง path ไม่ใช่แค่ชื่อไฟล์ รองรับ syntax ของ [Anymatch](https://github.com/micromatch/anymatch){:target=_blank .external-link}
- **Max Folder Depth**: กำหนดความลึกสูงสุดของโฟลเดอร์ที่จะตรวจสอบการเปลี่ยนแปลง

### Examples for Ignore

ยกเว้นไฟล์เดียว:

```sh
**/<fileName>.<suffix>
# ตัวอย่าง **/myfile.txt
```

ยกเว้น sub-directory ของโฟลเดอร์ที่กำลังตรวจสอบ:

```sh
**/<directoryName>/**
# ตัวอย่าง **/myDirectory/**
```

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'local-file-trigger') ]]
