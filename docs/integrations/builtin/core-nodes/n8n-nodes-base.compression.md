---
title: บีบอัดไฟล์ (Compression)
description: คู่มือ Compression node สำหรับบีบอัดและแตกไฟล์ใน n8n
contentType: [integration, reference]
priority: medium
---

# Compression

ใช้ Compression node เพื่อบีบอัด (compress) และแตกไฟล์ (decompress) รองรับไฟล์ Zip และ Gzip

## Node parameters

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

parameter ของ node จะขึ้นอยู่กับ **Operation** ที่เลือก เลือกได้ว่า:

* **Compress**: สร้างไฟล์บีบอัดจาก input data
* **Decompress**: แตกไฟล์บีบอัดที่มีอยู่

ดูรายละเอียด parameter สำหรับแต่ละ **Operation** ด้านล่าง

### Compress

- **Input Binary Field(s)**: ใส่ชื่อ field ใน input data ที่มีไฟล์ binary ที่ต้องการบีบอัด ถ้าจะบีบอัดหลายไฟล์ให้ใส่ชื่อ field คั่นด้วย comma
- **Output Format**: เลือกว่าจะให้ output เป็น **Zip** หรือ **Gzip**
- **File Name**: ใส่ชื่อไฟล์ zip ที่ node จะสร้าง
- **Put Output File in Field**: ใส่ชื่อ field ใน output data ที่จะเก็บไฟล์

### Decompress

- **Put Output File in Field**: ใส่ชื่อ field ใน input data ที่มีไฟล์ binary ที่ต้องการแตกไฟล์ ถ้าจะแตกหลายไฟล์ให้ใส่ชื่อ field คั่นด้วย comma
- **Output Prefix**: ใส่ prefix ที่จะเติมหน้าชื่อไฟล์ output

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'compression') ]]
