---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาที่พบบ่อยใน Google Drive node
description: เอกสารสำหรับคำถามและวิธีแก้ปัญหาที่พบบ่อยใน Google Drive node ของ n8n แพลตฟอร์มอัตโนมัติเวิร์กโฟลว์ รวมถึงรายละเอียดปัญหาและแนวทางแก้ไขที่แนะนำ
contentType: [integration, reference]
priority: high
---

# Google Drive node common issues

นี่คือข้อผิดพลาดและปัญหาที่พบบ่อยเกี่ยวกับ [Google Drive node](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/index.md) พร้อมขั้นตอนในการแก้ไขหรือแก้ไขปัญหา

## Google hasn't verified this app

--8<-- "_snippets/integrations/builtin/credentials/google/unverified-app.md"

## Google Cloud app becoming unauthorized

--8<-- "_snippets/integrations/builtin/credentials/google/app-becoming-unauthorized.md"

## Google Drive OAuth error

หากใช้วิธี Authentication แบบ OAuth คุณอาจเห็นข้อผิดพลาดที่ระบุว่าคุณไม่สามารถลงชื่อเข้าใช้ได้เนื่องจากแอปไม่เป็นไปตามความคาดหวังของ Google ในการรักษาความปลอดภัยของแอป

ส่วนใหญ่มักเกิดจาก URL ไม่ตรงกันระหว่างการกำหนดค่า OAuth ของ Google และ n8n เพื่อหลีกเลี่ยงปัญหานี้ ให้เริ่มต้นด้วยการตรวจสอบลิงก์ใดๆ ที่รวมอยู่ในข้อความแสดงข้อผิดพลาดของ Google ซึ่งจะมีรายละเอียดเกี่ยวกับข้อผิดพลาดที่เกิดขึ้นจริง

หากคุณ Self-host n8n ให้ตรวจสอบรายการการกำหนดค่า n8n ที่ใช้สร้าง URL ภายนอก ตรวจสอบว่าตัวแปรสภาพแวดล้อม [`N8N_EDITOR_BASE_URL`](/hosting/configuration/environment-variables/deployment.md) และ [`WEBHOOK_URL`](/hosting/configuration/configuration-examples/webhook-url.md) ใช้ Fully qualified domains

## Get recent files from Google Drive

ในการดึง Files ล่าสุดจาก Google Drive คุณต้องเรียงลำดับ Files ตามเวลาที่แก้ไข (Modification time) ในการทำเช่นนี้ คุณต้องค้นหา Files ที่มีอยู่และดึงข้อมูลเวลาที่แก้ไข จากนั้นคุณสามารถเรียงลำดับ Files เพื่อค้นหา File ล่าสุดและใช้ Google Drive node อีกตัวเพื่อกำหนดเป้าหมาย File ด้วย ID

กระบวนการมีลักษณะดังนี้:

1.  เพิ่ม **Google Drive** node ลงใน Canvas ของคุณ
2.  เลือก Resource **File/Folder** และ Operation **Search**
3.  เปิดใช้งาน **Return All** เพื่อเรียงลำดับ Files ทั้งหมด
4.  ตั้งค่า Filter **What to Search** เป็น **Files**
5.  ใน **Options**, ตั้งค่า **Fields** เป็น **All**
6.  เชื่อมต่อ **Sort** node เข้ากับ Output ของ **Google Drive** node
7.  เลือก Sort type เป็น **Simple**
8.  ป้อน `modifiedTime` เป็น **Field Name** ในส่วน **Fields To Sort By**
9.  เลือก Sort order เป็น **Descending**
10. เพิ่ม **Limit** node เข้ากับ Output ของ **Sort** node
11. ตั้งค่า **Max Items** เป็น **1** เพื่อเก็บเฉพาะ File ล่าสุด
12. เชื่อมต่อ **Google Drive** node อีกตัวเข้ากับ Output ของ **Limit** node
13. เลือก **File** เป็น **Resource** และ Operation ที่คุณต้องการ
14. ในการเลือก **File**, เลือก **By ID**
15. เลือก **Expression** และป้อน `{{ $json.id }}` เป็น Expression

[[ workflowDemo("file:///integrations/builtin/app-nodes/n8n-nodes-base.googledrive/get-most-recent-file.json") ]]
