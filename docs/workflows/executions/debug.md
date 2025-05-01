---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
title: Debug and re-run past executions
description: How to copy execution data into your current workflow in order to debug previous executions.
---

# Debug and re-run past executions

/// info | Feature availability
มีให้ใช้งานบน n8n Cloud และ registered Community plans
///

คุณสามารถโหลดข้อมูลจาก execution ก่อนหน้าเข้ามาใน workflow ปัจจุบันของคุณได้ สิ่งนี้มีประโยชน์สำหรับการ debug ข้อมูลจาก production executions ที่ล้มเหลว: คุณสามารถดู execution ที่ล้มเหลว ทำการเปลี่ยนแปลง workflow ของคุณเพื่อแก้ไข แล้วรันซ้ำด้วยข้อมูล execution ก่อนหน้า

## Load data

วิธีโหลดข้อมูลจาก execution ก่อนหน้า:

1. ใน workflow ของคุณ เลือกแท็บ **Executions** เพื่อดูรายการ **Executions**
1. เลือก execution ที่คุณต้องการ debug n8n จะแสดงตัวเลือกขึ้นอยู่กับว่า workflow สำเร็จหรือล้มเหลว:
	* สำหรับ executions ที่ล้มเหลว: เลือก **Debug in editor**
	* สำหรับ executions ที่สำเร็จ: เลือก **Copy to editor**
1. n8n จะคัดลอกข้อมูล execution เข้ามาใน workflow ปัจจุบันของคุณ และ [pins the data](/data/data-pinning.md) ใน node แรกของ workflow

/// note | Check which executions you save
Executions ที่มีอยู่ในรายการ **Executions** ขึ้นอยู่กับ [Workflow settings](/workflows/settings.md) ของคุณ
///
