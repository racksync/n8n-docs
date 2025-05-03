---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Vector Store Question Answer Tool node
description: วิธีใช้ Vector Store Question Answer Tool node ใน n8n สำหรับถาม-ตอบจาก vector store
contentType: [integration, reference]
---

# Vector Store Question Answer Tool node

Vector Store Question Answer node เป็น [tool](/glossary.md#ai-tool) ที่ช่วยให้ [agent](/glossary.md#ai-agent) สรุปผลลัพธ์และตอบคำถามโดยอิงจากข้อมูล chunk ใน [vector store](/glossary.md#ai-vector-store)

ในหน้านี้จะมี parameter ของ node Vector Store Question Answer และลิงก์ไปยัง resource อื่นๆ

/// note | Examples and templates
ดูตัวอย่างการใช้งานและ template สำหรับเริ่มต้นได้ที่ [Vector Store Question Answer Tool integrations](https://n8n.io/integrations/vector-store-tool/){:target=_blank .external-link}
///	

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

### Description of Data

ใส่คำอธิบายเกี่ยวกับข้อมูลใน vector store

### Limit

จำนวนผลลัพธ์สูงสุดที่ต้องการให้แสดง

## How n8n populates the tool description

n8n จะใช้ชื่อ node (สามารถแก้ไขได้) และ **Description of Data** เพื่อสร้าง tool description สำหรับ AI agent โดยใช้รูปแบบนี้:

> Useful for when you need to answer questions about [node name]. Whenever you need information about [Description of Data], you should ALWAYS use this. Input should be a fully formed question.

ช่องว่างในชื่อ node จะถูกแปลงเป็น _ ใน tool description

/// warning | Avoid special characters in node names
ห้ามใช้ตัวอักษรพิเศษในชื่อ node เพราะจะทำให้ agent error ตอนรัน:

![model errors from special characters](/_images/integrations/builtin/cluster-nodes/toolvectorstore/name-characters-error.png)

ควรใช้แค่ตัวอักษรภาษาอังกฤษ, ตัวเลข, ช่องว่าง, ขีดกลาง, ขีดล่าง เท่านั้นในชื่อ node
///

## Related resources

ดู [example workflows และเนื้อหาที่เกี่ยวข้อง](https://n8n.io/integrations/vector-store-tool/){:target=_blank .external-link} ได้ที่เว็บไซต์ n8n

--8<-- "_snippets/integrations/builtin/cluster-nodes/tools-link.md"

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
