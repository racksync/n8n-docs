---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: overview
title: Data item linking
description: ภาพรวมของ item linking ใน n8n และวิธีใช้งาน
---

# Data item linking

Item คือข้อมูลชิ้นเดียว node จะรับ item หนึ่งรายการหรือมากกว่า ประมวลผล และส่งออก item ใหม่ แต่ละ item จะ link กลับไปยัง item ก่อนหน้า

คุณจำเป็นต้องเข้าใจพฤติกรรมนี้หากคุณกำลัง:

*   สร้าง node แบบ programmatic ที่ใช้พฤติกรรมที่ซับซ้อนกับข้อมูล input และ output
*   ใช้ Code node หรือ expressions editor เพื่อเข้าถึงข้อมูลจาก item ก่อนหน้าใน workflow
*   ใช้ Code node สำหรับพฤติกรรมที่ซับซ้อนกับข้อมูล input และ output

ส่วนนี้ให้ข้อมูล:

*   ภาพรวมแนวคิดของ [Item linking concepts](/data/data-mapping/data-item-linking/item-linking-concepts.md)
*   ข้อมูลเกี่ยวกับ [Item linking for node creators](/data/data-mapping/data-item-linking/item-linking-node-building.md)
*   การสนับสนุนสำหรับผู้ใช้ปลายทางที่ต้องการ [Work with the data path](/data/data-mapping/data-item-linking/item-linking-code-node.md) เพื่อดึงข้อมูล item จาก node ก่อนหน้า และ link item เมื่อใช้ Code node
*   คำแนะนำในการแก้ไขปัญหา [Errors](/data/data-mapping/data-item-linking/item-linking-errors.md)


