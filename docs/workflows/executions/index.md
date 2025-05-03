---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Execution คือการรัน workflow หนึ่งครั้ง
contentType: overview
---

# Executions

Execution คือการรัน workflow หนึ่งครั้ง

## Execution modes

มี execution modes สองแบบ:

* Manual: รัน workflows ด้วยตนเองเมื่อทำการทดสอบ เลือก **Test Workflow** เพื่อเริ่ม manual execution คุณสามารถทำ manual executions ของ workflows ที่ active ได้ แต่ n8n แนะนำให้ตั้งค่า workflow ของคุณเป็น **Inactive** ในขณะที่พัฒนาและทดสอบ
* Production: production workflow คือ workflow ที่รันโดยอัตโนมัติ หากต้องการเปิดใช้งานสิ่งนี้ ให้ตั้งค่า workflow เป็น **Active**

## Execution lists

n8n มี execution lists สองรายการ:

* [Workflow-level executions](/workflows/executions/single-workflow-executions.md): execution list นี้แสดง executions สำหรับ workflow เดียว
* [All executions](/workflows/executions/all-executions.md): รายการนี้แสดง executions ทั้งหมดสำหรับ workflows ทั้งหมดของคุณ

n8n รองรับ [adding custom data to executions](/workflows/executions/custom-executions-data.md)
