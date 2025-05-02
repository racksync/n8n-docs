---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Data filtering

/// info | Feature availability
มีให้ใช้งานในแผน Cloud Pro และ Enterprise
///

ค้นหาและกรองข้อมูลใน panel **INPUT** และ **OUTPUT** ของ node ใช้สิ่งนี้เพื่อตรวจสอบข้อมูลของ node ของคุณ

วิธีค้นหา:

1. ใน node เลือก **Search** <span class="inline-image">![Search icon](/_images/common-icons/search.png){.off-glb}</span> ใน panel **INPUT** หรือ **OUTPUT**
1. ป้อนคำค้นหาของคุณ

n8n จะกรองขณะที่คุณพิมพ์คำค้นหา โดยแสดง objects หรือ rows ที่มีคำนั้น

การกรองเป็นการแสดงผลเท่านั้น: n8n ไม่ได้เปลี่ยนแปลงหรือลบข้อมูล ตัวกรองจะรีเซ็ตเมื่อคุณปิดและเปิด node ใหม่
