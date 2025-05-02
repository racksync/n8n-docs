---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: OpenAI File operations 
description: Documentation for the File operations in OpenAI node in n8n, a workflow automation platform. Includes details of operations and configuration, and links to examples and credentials information.
contentType: [integration, reference]
priority: critical
---

# OpenAI File operations

ใช้ operation นี้เพื่อสร้าง, ลบ, แสดงรายการ, ส่งข้อความ หรืออัปเดตไฟล์ใน OpenAI. ดูข้อมูลเพิ่มเติมที่ [OpenAI](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md).

## Delete a File

ใช้ operation นี้เพื่อลบไฟล์ออกจากเซิร์ฟเวอร์.

Enter these parameters:
- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **File**.
- **Operation**: เลือก **Delete a File**.
- **File**: ระบุ ID ของไฟล์หรือเลือกชื่อไฟล์จาก dropdown.

ดูรายละเอียดเพิ่มเติมที่ [Delete file | OpenAI](https://platform.openai.com/docs/api-reference/files/delete){:target=_blank .external-link}.

## List Files

ใช้ operation นี้เพื่อแสดงรายการไฟล์ขององค์กรผู้ใช้.

Enter these parameters:
- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **File**.
- **Operation**: เลือก **List Files**.

### Options

- **Purpose**: ใช้เพื่อคืนไฟล์ที่มีวัตถุประสงค์ตรงตามที่ระบุ. ใช้ **Assistants** สำหรับไฟล์ที่เกี่ยวกับ Assistants และ Message operations. ใช้ **Fine-Tune** สำหรับไฟล์ที่เกี่ยวข้องกับ [Fine-tuning](https://platform.openai.com/docs/api-reference/fine-tuning){:target=_blank .external-link}.

ดูรายละเอียดเพิ่มเติมที่ [List files | OpenAI](https://platform.openai.com/docs/api-reference/files/list){:target=_blank .external-link}.

## Upload a File

ใช้ operation นี้เพื่ออัปโหลดไฟล์ ซึ่งสามารถใช้ร่วมกับ operation อื่นๆ ได้.

Enter these parameters:
- **Credential to connect with**: สร้างหรือเลือก [OpenAI credential](/integrations/builtin/credentials/openai.md) ที่มีอยู่แล้ว.
- **Resource**: เลือก **File**.
- **Operation**: เลือก **Upload a File**.
- **Input Data Field Name**: ค่าเริ่มต้นคือ `data`. ระบุชื่อ property แบบ binary ที่มีไฟล์. ขนาดไฟล์สูงสุด 512 MB หรือ 2 ล้าน tokens สำหรับ Assistants.

### Options

- **Purpose**: ระบุวัตถุประสงค์ของไฟล์ที่อัปโหลด. ใช้ **Assistants** สำหรับไฟล์ที่เกี่ยวข้องกับ Assistants และ Message operations. ใช้ **Fine-Tune** สำหรับ [Fine-tuning](https://platform.openai.com/docs/api-reference/files/create){:target=_blank .external-link}.

ดูรายละเอียดเพิ่มเติมที่ [Upload file | OpenAI](https://platform.openai.com/docs/api-reference/files/create){:target=_blank .external-link}.

## Common issues

For common errors or issues and suggested resolution steps, refer to [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues.md).
