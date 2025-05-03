---
title: รันซับเวิร์กโฟลว์ (Execute Sub-workflow)
description: คู่มือ Execute Sub-workflow node สำหรับเรียก workflow อื่นใน n8n
contentType: [integration, reference]
priority: high
---

# Execute Sub-workflow

ใช้ Execute Sub-workflow node เพื่อรัน workflow อื่นบนเครื่องที่รัน n8n

## Node parameters

### Source

เลือกแหล่งข้อมูลของ sub-workflow ที่จะรัน:

- **Database**: โหลด workflow จาก database โดยใช้ ID ต้องกรอกอย่างใดอย่างหนึ่ง:
	- **From list**: เลือก workflow จาก list ที่มีใน account
	- **Workflow ID**: ใส่ ID ของ workflow ดูได้จาก URL หลัง `/workflow/` เช่น `https://my-n8n-acct.app.n8n.cloud/workflow/abCDE1f6gHiJKL7` **Workflow ID** คือ `abCDE1f6gHiJKL7`
- **Local File**: โหลด workflow จากไฟล์ JSON ที่บันทึกไว้ในเครื่อง ต้องกรอก:
	- **Workflow Path**: ใส่ path ของไฟล์ workflow JSON ที่ต้องการรัน
- **Parameter**: โหลด workflow จาก parameter ต้องกรอก:
	- **Workflow JSON**: ใส่ JSON code ที่ต้องการรัน
- **URL**: โหลด workflow จาก URL ต้องกรอก:
	- **Workflow URL**: ใส่ URL ที่ต้องการโหลด workflow

### Workflow Inputs

ถ้าเลือก sub-workflow แบบ **database** และ **From list** input items ของ sub-workflow จะโชว์ให้กรอกหรือ map ค่าได้

สามารถลบ input item ที่ไม่ต้องการได้ ถ้าลบ sub-workflow จะได้ค่า `null` สำหรับ item นั้นๆ สามารถเปิด **Attempt to convert types** เพื่อให้ n8n พยายามแปลง type ให้ตรงกับที่ sub-workflow ต้องการ

input item จะไม่โชว์ถ้า sub-workflow ใช้ Workflow Input Trigger node แบบ "Accept all data"

### Mode

parameter นี้ควบคุม mode การรัน node เลือกได้:

- **Run once with all items**: ส่ง input ทั้งหมดไปรันใน execution เดียว
- **Run once for each item**: รัน node ทีละรอบสำหรับแต่ละ input

## Node options

node นี้มี option เดียวคือ **Wait for Sub-Workflow Completion** เลือกได้ว่า workflow หลักจะรอ sub-workflow รันเสร็จก่อนค่อยไปขั้นต่อไป (เปิด) หรือจะไปต่อเลยโดยไม่รอ (ปิด)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'execute-workflow') ]]

## Set up and use a sub-workflow

ส่วนนี้อธิบายการตั้งค่า parent workflow และ sub-workflow

--8<-- "_snippets/flow-logic/subworkflow-usage.md"

## How data passes between workflows

--8<-- "_snippets/flow-logic/subworkflow-data-flow.md"
