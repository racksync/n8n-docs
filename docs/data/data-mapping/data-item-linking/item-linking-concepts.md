---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
title: แนวคิด Item linking
description: ภาพรวมแนวคิดเบื้องหลัง item linking ใน n8n
---

# Item linking concepts

แต่ละ output item ที่สร้างโดย node จะมี metadata ที่ link พวกมันไปยัง input item (หรือ item ต่างๆ) ที่ node ใช้ในการสร้างพวกมันขึ้นมา สิ่งนี้สร้างสายโซ่ของ item ที่คุณสามารถทำงานย้อนกลับไปเพื่อเข้าถึง item ก่อนหน้าได้ สิ่งนี้อาจซับซ้อนในการทำความเข้าใจ โดยเฉพาะอย่างยิ่งหาก node แยก (split) หรือรวม (merge) ข้อมูล คุณจำเป็นต้องเข้าใจ item linking เมื่อสร้าง node แบบ programmatic ของคุณเอง หรือในบางสถานการณ์ที่ใช้ Code node

เอกสารนี้ให้ภาพรวมแนวคิดของคุณลักษณะนี้ สำหรับรายละเอียดการใช้งาน โปรดดูที่:

*   [Item linking for node creators](/data/data-mapping/data-item-linking/item-linking-node-building.md), สำหรับรายละเอียดเกี่ยวกับวิธีจัดการ item linking เมื่อสร้าง node
*   [Item linking in the Code node](/data/data-mapping/data-item-linking/item-linking-code-node.md), เพื่อเรียนรู้วิธีจัดการ item linking ใน Code node
*   [Item linking errors](/data/data-mapping/data-item-linking/item-linking-errors.md), เพื่อทำความเข้าใจข้อผิดพลาดที่คุณอาจพบใน editor UI

## n8n's automatic item linking

หาก node ไม่ได้ควบคุมวิธีการ link input item ไปยัง output item n8n จะพยายามเดาว่าจะ link item โดยอัตโนมัติอย่างไร:

*   Single input, single output: output จะ link ไปยัง input
*   Single input, multiple outputs: output ทั้งหมดจะ link ไปยัง input นั้น
*   Multiple inputs and outputs:
    *   หากคุณเก็บ input item ไว้ แต่เปลี่ยนลำดับ (หรือลบบางส่วนออกแต่เก็บส่วนอื่นไว้) n8n สามารถเพิ่มข้อมูล linked item ที่ถูกต้องได้โดยอัตโนมัติ
    *   หากจำนวน input และ output เท่ากัน n8n จะ link item ตามลำดับ ซึ่งหมายความว่า output-1 link ไปยัง input-1, output-2 link ไปยัง input-2 และต่อไปเรื่อยๆ
    *   หากจำนวนไม่เท่ากัน หรือคุณสร้าง item ใหม่ทั้งหมด n8n จะไม่สามารถ link item โดยอัตโนมัติได้

หาก n8n ไม่สามารถ link item โดยอัตโนมัติ และ node ไม่ได้จัดการ item linking n8n จะแสดงข้อผิดพลาด โปรดดู [Item linking errors](/data/data-mapping/data-item-linking/item-linking-errors.md) สำหรับข้อมูลเพิ่มเติม

## Item linking example

![A diagram showing the threads linking multiple items back through a workflow](/_images/data/data-mapping/data-item-linking/item-linking-multiple-lines.png)

ในตัวอย่างนี้ เป็นไปได้ที่ n8n จะ link item ใน node หนึ่งย้อนกลับไปหลายขั้นตอน แม้ว่าลำดับ item จะเปลี่ยนไป ซึ่งหมายความว่า node ที่จัดเรียงภาพยนตร์ตามตัวอักษรสามารถเข้าถึงข้อมูลเกี่ยวกับ linked item ใน node ที่ดึงข้อมูลนักแสดงภาพยนตร์ชื่อดังได้

วิธีการเข้าถึง linked item จะแตกต่างกันไปขึ้นอยู่กับว่าคุณกำลังใช้ UI, expressions หรือ Code node สำรวจแหล่งข้อมูลต่อไปนี้:

*   [Mapping in the UI](/data/data-mapping/data-mapping-ui.md)
*   [Mapping in the expressions editor](/data/data-mapping/data-mapping-expressions.md)
*   [Item linking in the Code node](/data/data-mapping/data-item-linking/item-linking-code-node.md)
*   [Item linking errors](/data/data-mapping/data-item-linking/item-linking-errors.md)




