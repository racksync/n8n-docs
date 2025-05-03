---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Rundeck node
description: เรียนรู้วิธีใช้ Rundeck node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Rundeck node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Rundeck node

ใช้ Rundeck node ในการอัตโนมัติงานใน Rundeck และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนในตัวสำหรับการรัน job และดึง metadata.

ในหน้านี้ คุณจะพบรายการ operations ที่ Rundeck node รองรับ พร้อมทั้งลิงก์ไปยัง resources เพิ่มเติม.

/// note | Credentials
ดู [Rundeck credentials](/integrations/builtin/credentials/rundeck.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

- **Job**
    - Execute a job
    - Get metadata of a job

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'rundeck') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

## Find the job ID

1. เข้าไปที่ dashboard ของ Rundeck.
2. เปิดโปรเจคที่มี job ที่คุณต้องการใช้กับ n8n.
3. ใน sidebar ให้เลือก **JOBS**.
4. ภายใต้ **All Jobs** ให้เลือกชื่อ job ที่คุณต้องการใช้กับ n8n.
5. ที่มุมซ้ายบน ใต้ชื่อ job ให้คัดลอกข้อความที่แสดงในแบบตัวอักษรเล็ก ๆ ซึ่งเป็น job ID ของคุณ.
6. วาง job ID นี้ลงในช่อง **Job Id** ใน n8n.

