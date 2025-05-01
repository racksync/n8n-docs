---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Workflow history
description: View and restore previous versions of your workflow.
contentType: howto
---

# Workflow history

/// info | Feature availability
* Full workflow history มีให้ใช้งานบน Enterprise Cloud และ Enterprise Self-hosted
* เวอร์ชันจากห้าวันที่ผ่านมามีให้ใช้งานสำหรับผู้ใช้ Cloud Pro
* เวอร์ชันจาก 24 ชั่วโมงที่ผ่านมามีให้ใช้งานสำหรับผู้ใช้ Community ที่ลงทะเบียนแล้ว
///	

ใช้ workflow history เพื่อดูและกู้คืนเวอร์ชันก่อนหน้าของ workflows ของคุณ

## Understand workflow history

n8n สร้างเวอร์ชันใหม่เมื่อคุณ:

 * บันทึก workflow ของคุณ
 * กู้คืนเวอร์ชันเก่า n8n จะบันทึกเวอร์ชันล่าสุดก่อนที่จะกู้คืน
 * Pull จาก Git repository โดยใช้ [Source control](/source-control-environments/index.md) โปรดทราบว่า n8n บันทึกเวอร์ชันลงในฐานข้อมูลของ instance ไม่ใช่ใน Git

/// note | Workflow history and execution history
อย่าสับสนระหว่าง workflow history กับ [Workflow-level executions list](/workflows/executions/single-workflow-executions.md)

Executions คือการรัน workflow ด้วย execution list คุณสามารถดูการรันก่อนหน้าของ workflow เวอร์ชันปัจจุบันได้ คุณสามารถคัดลอก executions ก่อนหน้าไปยัง editor เพื่อ [Debug and re-run past executions](/workflows/executions/debug.md) ใน workflow ปัจจุบันของคุณ

Workflow history คือเวอร์ชันก่อนหน้าของ workflow: ตัวอย่างเช่น เวอร์ชันที่มี node แตกต่างกัน หรือตั้งค่า parameters ต่างกัน
///

## View workflow history

วิธีดูประวัติของ workflow:

1. เปิด workflow
1. เลือก **Workflow history** <span class="inline-image">![Workflow history icon](/_images/common-icons/workflow-history.png){.off-glb}</span> n8n จะเปิดเมนูแสดงเวอร์ชัน workflow ที่บันทึกไว้ และ canvas พร้อมตัวอย่างของเวอร์ชันที่เลือก

## Restore or copy previous versions

คุณสามารถกู้คืนเวอร์ชัน workflow ก่อนหน้า หรือสร้างสำเนาของมันได้:

1. ในเวอร์ชันที่คุณต้องการกู้คืนหรือคัดลอก ให้เลือก **Options** <span class="inline-image">![Options icon](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span>
1. เลือกสิ่งที่คุณต้องการทำ:
	* **Restore this version**: แทนที่ workflow ปัจจุบันของคุณด้วยเวอร์ชันที่เลือก
	* **Clone to new workflow**: สร้าง workflow ใหม่โดยอิงตามเวอร์ชันที่เลือก
	* **Open version in new tab**: เปิดแท็บที่สองแสดงเวอร์ชันที่เลือก ใช้สิ่งนี้เพื่อเปรียบเทียบเวอร์ชัน
	* **Download**: ดาวน์โหลดเวอร์ชันเป็น JSON
