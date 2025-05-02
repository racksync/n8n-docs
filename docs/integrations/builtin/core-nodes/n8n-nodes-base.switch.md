---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Switch
description: Documentation for the Switch node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: critical
---

# Switch

ใช้ Switch node เพื่อกำหนดเส้นทาง workflow ตามเงื่อนไขที่ตั้งไว้ คล้ายกับ [IF](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) node แต่รองรับหลายเส้นทาง output

## Node parameters

เลือก **Mode** ที่ node จะใช้:

* **Rules**: เลือก mode นี้เพื่อสร้าง rule สำหรับแต่ละ output
* **Expression**: เลือก mode นี้เพื่อเขียน expression เพื่อคืนค่า output index แบบโปรแกรม

การตั้งค่า node จะขึ้นอยู่กับ **Mode** ที่เลือก

### Rules

ตั้งค่า node ด้วย operation นี้โดยใช้ parameters เหล่านี้:

* สร้าง **Routing Rules** เพื่อกำหนดเงื่อนไขเปรียบเทียบ
    * ใช้ dropdown data type เพื่อเลือกชนิดข้อมูลและประเภทการเปรียบเทียบ เช่น ถ้าอยากสร้าง rule สำหรับวันที่หลังจากวันที่ที่กำหนด ให้เลือก **Date & Time > is after**
    * field และค่าที่ต้องใส่ในเงื่อนไขจะเปลี่ยนไปตาม data type และการเปรียบเทียบที่เลือก ดูรายละเอียดที่ [Available data type comparisons](#available-data-type-comparisons) สำหรับรายการเปรียบเทียบทั้งหมด
* **Rename Output**: เปิด option นี้เพื่อเปลี่ยนชื่อ output field ที่จะใส่ข้อมูลที่ตรงกับเงื่อนไข ใส่ **Output Name** ที่ต้องการ

เลือก **Add Routing Rule** เพื่อเพิ่ม rule เพิ่มเติม

#### Rule options

ตั้งค่าเพิ่มเติมได้ด้วย **Options** เหล่านี้:

- **Fallback Output**: เลือกว่าจะให้ workflow ไปทางไหนถ้า item ไม่ตรงกับ rule หรือเงื่อนไขใดๆ
    - **None**: ข้าม item นั้น (default)
    - **Extra Output**: ส่ง item ไป output พิเศษแยกต่างหาก
    - **Output 0**: ส่ง item ไป output เดียวกับที่ตรงกับ rule แรก
- **Ignore Case**: ตั้งค่าว่าจะไม่สนใจตัวพิมพ์เล็ก/ใหญ่ตอนเช็คเงื่อนไข (เปิด = ไม่สนใจ, ปิด = สนใจ)
- **Less Strict Type Validation**: ตั้งค่าว่าให้ n8n พยายามแปลง type ของค่าตาม operator ที่เลือก (เปิด = แปลง, ปิด = ไม่แปลง)
- **Send data to all matching outputs**: ตั้งค่าว่าจะส่งข้อมูลไปทุก output ที่ตรงเงื่อนไข (เปิด = ส่งทุกอัน, ปิด = ส่งเฉพาะอันแรกที่ตรง)

### Expression

ตั้งค่า node ด้วย operation นี้โดยใช้ parameters เหล่านี้:

- **Number of Outputs**: กำหนดจำนวน output ที่ node จะมี
- **Output Index**: สร้าง expression เพื่อคำนวณว่า input item ไหนควรไป output ไหน expression ต้องคืนค่าเป็นตัวเลข

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'switch') ]]

## Related resources

ดู [Splitting with conditionals](/flow-logic/splitting.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการใช้เงื่อนไขสร้าง logic ซับซ้อนใน n8n

--8<-- "_snippets/integrations/builtin/core-nodes/data-types.md"

