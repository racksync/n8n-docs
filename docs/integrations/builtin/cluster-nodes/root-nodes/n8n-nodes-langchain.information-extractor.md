---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Information Extractor node
description: วิธีใช้งาน Information Extractor node ใน n8n สำหรับดึงข้อมูลที่มีโครงสร้างจากข้อความ
contentType: [integration, reference]
---

# Information Extractor node

ใช้ Information Extractor node เพื่อดึงข้อมูลที่มีโครงสร้าง (structured information) จากข้อมูลที่เข้ามา

ในหน้านี้ คุณจะพบ node parameters สำหรับ Information Extractor node
และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

## Node parameters

*   **Text** กำหนดข้อความ input ที่จะดึงข้อมูลออกมา โดยปกติจะเป็น expression ที่อ้างอิงถึง field จาก input items ตัวอย่างเช่น อาจเป็น `{{ $json.chatInput }}` หาก input เป็น chat trigger หรือ `{{ $json.text }}` หาก node ก่อนหน้าคือ Extract from PDF
*   ใช้ **Schema Type** เพื่อเลือกว่าคุณต้องการอธิบาย format ข้อมูล output ที่ต้องการอย่างไร คุณสามารถเลือกได้ระหว่าง:
    *   **From Attribute Description**: ตัวเลือกนี้ช่วยให้คุณกำหนด schema โดยระบุ list ของ attributes และ descriptions ของมัน
    *   **Generate From JSON Example**: ป้อนตัวอย่าง JSON object เพื่อสร้าง schema โดยอัตโนมัติ Node จะใช้ types และ names ของ object property โดยไม่สนใจค่าจริง
    *   **Define Below**: ป้อน JSON schema ด้วยตนเอง อ่าน [guides and examples](https://json-schema.org/learn/miscellaneous-examples){:target=_blank .external-link} ของ JSON Schema เพื่อช่วยสร้าง JSON schema ที่ถูกต้อง

## Node options

*   **System Prompt Template**: ใช้ตัวเลือกนี้เพื่อเปลี่ยน system prompt ที่ใช้สำหรับการดึงข้อมูล n8n จะเพิ่มคำสั่งระบุ format ต่อท้าย prompt โดยอัตโนมัติ

## Related resources

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
