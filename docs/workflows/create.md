---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: สร้าง, รัน, และ activate workflows
contentType: howto
---

# Create a workflow

[Workflow](/glossary.md#workflow-n8n) คือชุดของ nodes ที่เชื่อมต่อเข้าด้วยกันเพื่อทำให้กระบวนการเป็นอัตโนมัติ คุณสามารถสร้าง workflows ด้วยการลากและวาง nodes ที่คุณต้องการใช้จากแถบด้านข้างไปยัง [canvas](/glossary.md#canvas-n8n) 

## Create a workflow

1. เลือกปุ่ม <span class="inline-image">![universal create resource icon](/_images/common-icons/universal-resource-button.png){.off-glb}</span> **button** ที่มุมบนซ้ายของเมนูด้านข้าง เลือก workflow
2. หาก n8n instance ของคุณรองรับ projects คุณจะต้องเลือกว่าจะสร้าง workflow ภายใน **personal space** ของคุณ หรือ **project** เฉพาะที่คุณมีสิทธิ์เข้าถึง หากคุณใช้เวอร์ชัน community คุณจะสร้าง workflows ภายใน personal space ของคุณเสมอ
3. เริ่มต้นโดยการเพิ่ม trigger node: เลือก **Add first step...**

หรือ:

1. เลือกปุ่ม <span class="inline-image">![universal create resource icon](/_images/common-icons/universal-resource-button.png){.off-glb}</span> **create** ที่มุมบนขวาจากหน้า **Overview** หรือ **project** เฉพาะ เลือก workflow
2. หากคุณทำสิ่งนี้จากหน้า **Overview** คุณจะสร้าง workflow ภายใน personal space ของคุณ หากคุณทำสิ่งนี้จากภายใน project คุณจะสร้าง workflow ภายใน project นั้น
3. เริ่มต้นโดยการเพิ่ม trigger node: เลือก **Add first step...**

หากนี่เป็นครั้งแรกที่คุณสร้าง workflow คุณอาจต้องการใช้ [quickstart guides](/try-it-out/index.md) เพื่อลองใช้ฟีเจอร์ต่างๆ ของ n8n อย่างรวดเร็ว

## Run workflows manually

คุณอาจต้องรัน workflow ของคุณด้วยตนเองเมื่อสร้างและทดสอบ หรือหาก workflow ของคุณไม่มี trigger node

ในการรันด้วยตนเอง ให้เลือก **Test Workflow**

## Run workflows automatically

Workflows ใหม่ทั้งหมดจะอยู่ในสถานะ inactive ตามค่าเริ่มต้น

คุณต้อง activate workflows ที่เริ่มต้นด้วย trigger node หรือ Webhook node เพื่อให้สามารถรันโดยอัตโนมัติได้ เมื่อ workflow อยู่ในสถานะ inactive คุณต้องรันด้วยตนเอง

ในการ activate หรือ deactivate workflow ของคุณ ให้เปิด workflow ของคุณแล้วสลับ **Inactive** / **Active**

เมื่อ workflow active แล้ว มันจะรันเมื่อใดก็ตามที่เงื่อนไข trigger ของมันเป็นจริง
