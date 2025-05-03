---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: If
description: เอกสารสำหรับ If node ใน n8n แพลตฟอร์ม workflow automation พร้อมคำแนะนำการใช้งานและตัวอย่าง
contentType: [integration, reference]
priority: critical
tags:
  - if
  - if node
  - If
  - If node
hide:
  - tags
---

# If

ใช้ If node เพื่อแยก workflow ตามเงื่อนไขที่กำหนดโดยใช้การเปรียบเทียบ

## Add conditions

สร้าง **Conditions** สำหรับเปรียบเทียบใน If node

- ใช้ dropdown เลือก data type และประเภทการเปรียบเทียบสำหรับเงื่อนไข เช่น ถ้าต้องการกรองวันที่ที่หลังจากวันที่ที่กำหนด ให้เลือก **Date & Time > is after**
- ช่องกรอกข้อมูลและค่าที่ต้องใส่ในเงื่อนไขจะเปลี่ยนไปตาม data type และการเปรียบเทียบที่เลือก ดูรายละเอียดเพิ่มเติมได้ที่ [Available data type comparisons](#available-data-type-comparisons) สำหรับรายการเปรียบเทียบทั้งหมดในแต่ละ data type

เลือก **Add condition** เพื่อเพิ่มเงื่อนไขใหม่

### Combining conditions

คุณสามารถเลือกได้ว่าจะเก็บข้อมูลไว้เมื่อ:

* ตรงตามทุกเงื่อนไข: สร้างเงื่อนไขสองข้อขึ้นไปแล้วเลือก **AND** ใน dropdown ระหว่างเงื่อนไข
* ตรงตามเงื่อนไขใดเงื่อนไขหนึ่ง: สร้างเงื่อนไขสองข้อขึ้นไปแล้วเลือก **OR** ใน dropdown ระหว่างเงื่อนไข

## Templates and examples

[[ templatesWidget(page.title, 'if') ]]

## Branch execution with If and Merge nodes

--8<-- "_snippets/integrations/builtin/core-nodes/merge/if-merge-branch-execution.md"

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับการใช้เงื่อนไขเพื่อสร้าง logic ที่ซับซ้อนใน n8n ได้ที่ [Splitting with conditionals](/flow-logic/splitting.md)

ถ้าต้องการ output มากกว่าสองทาง ให้ใช้ [Switch node](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md)

--8<-- "_snippets/integrations/builtin/core-nodes/data-types.md"

