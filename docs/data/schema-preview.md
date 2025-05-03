---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การแสดงตัวอย่าง Schema
description: 
contentType: overview
---

# Schema Preview

Schema Preview แสดงข้อมูล schema ที่คาดหวังจาก node ก่อนหน้าใน Node Editor โดยที่ผู้ใช้ไม่ต้องให้ข้อมูล credentials หรือ execute node ซึ่งทำให้สามารถสร้าง workflow ได้โดยไม่ต้องให้ข้อมูล credentials ล่วงหน้า การ preview ไม่ได้รวมข้อมูล mock data แต่จะแสดง field ที่คาดหวัง ทำให้สามารถเลือกและรวมเข้ากับ input ของ node ถัดไปได้

## Using the preview 

1. ต้องมี node ที่มี Schema Preview อยู่ใน workflow ของคุณ
1. เมื่อคลิกที่รายละเอียดของ node ถัดไปในลำดับ ข้อมูล Schema Preview จะปรากฏขึ้นใน Node Editor ซึ่งเป็นที่ที่ข้อมูล schema จะแสดงตามปกติ
1. ใช้ข้อมูลจาก Schema Preview เช่นเดียวกับที่คุณใช้ schema อื่นๆ - ลากและวาง field เป็น input ลงใน parameters และ settings ของ node ของคุณ
