---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Default Data Loader node documentation
description: Learn how to use the Default Data Loader node in n8n. Follow technical documentation to integrate Default Data Loader node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Default Data Loader node

ใช้ Default Data Loader node เพื่อโหลดไฟล์ข้อมูลไบนารี (binary data files) หรือข้อมูล JSON สำหรับ [vector stores](/glossary.md#ai-vector-store) หรือการสรุปผล (summarization)

ในหน้านี้ คุณจะพบรายการพารามิเตอร์ที่ Default Data Loader node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Type of Data**: เลือก **Binary** หรือ **JSON**
* **Data Format**: แสดงเมื่อคุณตั้งค่า **Type of Data** เป็น **Binary** เลือกประเภท MIME ของไฟล์สำหรับข้อมูลไบนารีของคุณ ตั้งค่าเป็น **Automatically Detect by MIME Type** หากคุณต้องการให้ n8n ตั้งค่ารูปแบบข้อมูลให้คุณ หากคุณตั้งค่ารูปแบบข้อมูลเฉพาะและประเภท MIME ของไฟล์ที่เข้ามาไม่ตรงกัน โหนดจะเกิดข้อผิดพลาด หากคุณใช้ **Automatically Detect by MIME Type** โหนดจะกลับไปใช้รูปแบบข้อความ (text format) หากไม่สามารถจับคู่ประเภท MIME ของไฟล์กับรูปแบบข้อมูลที่รองรับได้
* **Mode**: แสดงเมื่อคุณตั้งค่า **Type of Data** เป็น **JSON** เลือกจาก:
	* **Load All Input Data**: ใช้ข้อมูลอินพุตทั้งหมดของโหนด
	* **Load Specific Data**: ใช้ [expressions](/code/expressions.md) เพื่อกำหนดข้อมูลที่คุณต้องการโหลด คุณสามารถเพิ่มข้อความและ expressions ได้ ซึ่งหมายความว่าคุณสามารถสร้างเอกสารที่กำหนดเองจากส่วนผสมของข้อความและ expressions ได้

## Node options

* **Metadata**: ตั้งค่า metadata ที่ควรมาพร้อมกับเอกสารใน vector store นี่คือสิ่งที่คุณจับคู่โดยใช้ตัวเลือก **Metadata Filter** เมื่อดึงข้อมูลโดยใช้โหนด vector store

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'default-data-loader') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-doc-loaders-link.md"

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
