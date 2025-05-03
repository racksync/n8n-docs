---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Split Out
description: เอกสารสำหรับ Split Out node ใน n8n แพลตฟอร์ม workflow automation พร้อมคำแนะนำการใช้งานและตัวอย่าง
contentType: [integration, reference]
priority: high
---

# Split Out

ใช้ Split Out node เพื่อแยกข้อมูลที่เป็น list ใน item เดียวออกมาเป็นหลายๆ item เช่น ถ้ามี list ของลูกค้า แล้วอยากแยกให้แต่ละลูกค้าเป็น item ของตัวเอง

## Node parameters

ตั้งค่า node นี้ด้วย parameters ต่อไปนี้

### Field to Split Out

ใส่ชื่อ field ที่มี list ที่อยากแยกออกมาเป็น item เดี่ยวๆ

ถ้าทำงานกับ binary data input ให้ใช้ `$binary` ใน expression เพื่อกำหนด field ที่จะ split out

### Include

เลือกว่าจะให้ n8n เก็บ field อื่นๆ จาก input data ไว้กับแต่ละ item ใหม่ยังไง

คุณเลือกได้ว่า:

* **No Other Fields**: จะไม่รวม field อื่นๆ เลย
* **All Other Fields**: จะรวม field อื่นๆ ทั้งหมด
* **Selected Other Fields**: จะรวมเฉพาะ field ที่เลือกไว้
    * **Fields to Include**: ใส่ชื่อ field ที่อยากรวม โดยคั่นด้วย comma

## Node options

### Disable Dot Notation

โดยปกติ n8n จะเปิดใช้ dot notation เพื่ออ้างถึง child field ในรูปแบบ `parent.child` ถ้าอยากปิดการใช้ dot notation ให้เปิด option นี้ (turned on) หรือถ้าอยากใช้ dot notation ต่อไปให้ปิด (turned off)

### Destination Field Name

ใส่ชื่อ field ใน output ที่จะเก็บค่าที่ split ออกมา

### Include Binary

เลือกว่าจะรวม binary data จาก input ใน output ใหม่ด้วยหรือไม่ (เปิด = รวม, ปิด = ไม่รวม)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'split-out') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md"
