---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Telegram node File operations documentation
description: Documentation for the File operations in the Telegram node in n8n, a workflow automation platform. Includes details to configure all File operations.
contentType: [integration, reference]
priority: critical
---

# Telegram node File operations

ใช้ operation นี้เพื่อดึงไฟล์จาก Telegram ดูรายละเอียดเพิ่มเติมเกี่ยวกับ Telegram node ได้ที่ [Telegram](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/index.md)

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Get File

ใช้ operation นี้เพื่อดึงไฟล์จาก Telegram ผ่าน Bot API [getFile](https://core.telegram.org/bots/api#getfile){:target=_blank .external-link}

ป้อนพารามิเตอร์เหล่านี้:

* **Credential to connect with**: สร้างหรือเลือก [Telegram credential](/integrations/builtin/credentials/telegram.md) ที่มีอยู่
* **Resource**: เลือก **File**
* **Operation**: เลือก **Get**
* **File ID**: ใส่ ID ของไฟล์ที่ต้องการดึง
* **Download**: เลือกว่าจะให้ node ดาวน์โหลดไฟล์ให้อัตโนมัติ (เปิด) หรือไม่ (ปิด)

ดูเอกสาร Bot API [getFile](https://core.telegram.org/bots/api#getfile){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
