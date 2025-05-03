---
title: กรองข้อมูล (Filter)
description: คู่มือ Filter node สำหรับกรองข้อมูลตามเงื่อนไขใน n8n
contentType: [integration, reference]
priority: critical
---

# Filter

Filter node ใช้สำหรับกรอง items ตามเงื่อนไขที่ตั้งไว้ ถ้า item ตรงตามเงื่อนไข Filter node จะส่ง item นั้นไปยัง node ถัดไปใน output ของ Filter node ถ้าไม่ตรงตามเงื่อนไข item นั้นจะไม่ถูกส่งออกไป

## Node parameters

สร้าง **Conditions** สำหรับเปรียบเทียบเพื่อใช้กรองข้อมูล

- ใช้ dropdown เลือก data type และประเภทการเปรียบเทียบสำหรับเงื่อนไขของคุณ เช่น ถ้าต้องการกรองวันที่ที่หลังจากวันที่ที่กำหนด ให้เลือก **Date & Time > is after**
- ช่องกรอกข้อมูลและค่าที่ต้องใส่ในเงื่อนไขจะเปลี่ยนไปตาม data type และการเปรียบเทียบที่เลือก ดูรายละเอียดเพิ่มเติมได้ที่ [Available data type comparisons](#available-data-type-comparisons) สำหรับรายการเปรียบเทียบทั้งหมดในแต่ละ data type

เลือก **Add condition** เพื่อเพิ่มเงื่อนไขใหม่

### Combining conditions

คุณสามารถเลือกได้ว่าจะเก็บ item ไว้เมื่อ:

* ตรงตามทุกเงื่อนไข: สร้างเงื่อนไขสองข้อขึ้นไปแล้วเลือก **AND** ใน dropdown ระหว่างเงื่อนไข
* ตรงตามเงื่อนไขใดเงื่อนไขหนึ่ง: สร้างเงื่อนไขสองข้อขึ้นไปแล้วเลือก **OR** ใน dropdown ระหว่างเงื่อนไข

ไม่สามารถผสม AND และ OR ในกฎเดียวกันได้

## Node options

- **Ignore Case**: เลือกว่าจะไม่สนใจตัวพิมพ์ใหญ่-เล็ก (เปิด) หรือให้แยกแยะตัวพิมพ์ใหญ่-เล็ก (ปิด)
- **Less Strict Type Validation**: เลือกให้ n8n พยายามแปลงชนิดข้อมูลตาม operator ที่เลือก (เปิด) หรือไม่แปลง (ปิด) ถ้าเจอ error "wrong type:" ให้ลองเปิด option นี้

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'filter') ]]

--8<-- "_snippets/integrations/builtin/core-nodes/data-types.md"
