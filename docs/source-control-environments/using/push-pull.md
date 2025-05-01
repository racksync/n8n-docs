---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Push and pull
description: Send work to Git, and fetch work from Git to your instance.
contentType: howto
---

# Push and pull

ถ้า n8n instance ของคุณเชื่อมกับ Git repository คุณต้อง sync งานของคุณกับ Git อยู่เสมอ

เอกสารนี้สมมติว่าคุณรู้จัก concept และคำศัพท์ของ Git มาบ้างแล้ว ดู [Git and n8n](/source-control-environments/understand/git.md) สำหรับแนะนำการทำงานของ n8n กับ Git

--8<-- "_snippets/source-control-environments/one-direction.md"

## Fetch other people's work

/// note | Restricted feature
user ทั่วไปจะ fetch งานจาก Git ไม่ได้ คุณต้องเป็น n8n instance owner, admin หรือ project owner ถึงจะ fetch งานจาก Git ได้
///
ถ้าจะ pull งานจาก Git ให้เลือก **Pull** <span class="inline-image">![Pull icon](/_images/source-control-environments/pull-icon.png){.off-glb}</span> ในเมนูหลัก

--8<-- "_snippets/source-control-environments/push-pull-menu-state.md"

n8n อาจจะแจ้งเตือนว่ากำลังจะ override งาน local ของคุณ ให้เลือก **Pull and override** ถ้าต้องการ override งาน local ด้วยเนื้อหาใน Git

ถ้ามีการเปลี่ยนแปลงที่มี variable หรือ credential stub ใหม่ n8n จะแจ้งว่าคุณต้องเติมค่าให้กับ item เหล่านั้นก่อนใช้งาน

/// info | How deleted resources are handled
ถ้า workflow, credential, variable, tag ถูกลบจาก repository งาน local ของคุณจะไม่ถูกลบอัตโนมัติ ตอน pull n8n จะแจ้งเตือน resource ที่ตกค้างและถามว่าต้องการลบไหม
///

### Workflow and credential owner may change on pull

เวลาคุณ pull จาก Git เข้า n8n instance, n8n จะพยายาม assign workflow กับ credential ให้กับ user หรือ project ที่ตรงกัน

ถ้า owner เดิมเป็น user:

ถ้ามี owner เดิมอยู่ทั้งสอง instance (email ตรงกัน) owner จะเหมือนเดิม ถ้าไม่มี n8n จะตั้ง user ที่ pull เป็น owner

ถ้า owner เดิมเป็น [project](/user-management/rbac/index.md):

n8n จะพยายาม match ชื่อ project เดิมกับชื่อ project ใน instance ใหม่ ถ้าไม่มี n8n จะสร้าง project ใหม่ให้, ตั้ง user ปัจจุบันเป็น project owner แล้ว import workflow กับ credential เข้า project นั้น

### Pulling may cause brief service interruption

ถ้าคุณ pull งานเข้า workflow ที่กำลัง active, n8n จะ set workflow เป็น inactive ระหว่าง pull แล้วค่อย reactivate อาจจะมี downtime สั้นๆ ไม่กี่วินาที

## Send your work to Git

/// note | Restricted feature
user ทั่วไปจะส่งงานไป Git ไม่ได้ คุณต้องเป็น n8n instance owner, admin หรือ project owner ถึงจะ push งานไป Git ได้
///

--8<-- "_snippets/source-control-environments/push.md"

## What gets committed

n8n จะ commit สิ่งเหล่านี้ไปที่ Git:

* Workflow รวม tag และ email ของ workflow owner คุณเลือกได้ว่าจะ push workflow ไหน
* Credential stub (ID, name, type)
* Variable stub (ID และ name)
* Project
* Folder

คุณสามารถ [Manage variables](/source-control-environments/using/manage-variables.md) ด้วย n8n API ได้

## Merge behaviors and conflicts

source control ของ n8n มีแนวคิดเฉพาะตัว n8n จะ resolve merge conflict ของ credential กับ variable ให้อัตโนมัติ แต่ workflow จะตรวจ conflict ไม่ได้

### Workflows

คุณต้องบอก n8n โดยตรงว่าจะให้ทำอะไรกับ workflow ตอน push หรือ pull Git repository จะเป็น source of truth

ตอน pull อาจจะมีแจ้งเตือนว่า workflow local ของคุณต่างจาก Git ถ้ายอมรับ workflow local จะถูก override ระวังอย่าให้ข้อมูลสำคัญหาย

ตอน push, workflow local ของคุณจะ override ของเดิมใน Git ดังนั้นควรแน่ใจว่าเป็นเวอร์ชันล่าสุด ไม่งั้นอาจจะทับงานใหม่

เพื่อป้องกันปัญหานี้ ควร push งานทันทีหลังทำ workflow เสร็จ แล้วค่อย pull

เพื่อไม่ให้ข้อมูลหาย:

* ออกแบบ source control ให้ workflow ไหลทางเดียว เช่น แก้ไขที่ development instance, push ไป Git แล้ว pull เข้า production อย่าแก้ไขที่ production แล้ว push กลับ
* อย่า push workflow ทั้งหมด เลือกเฉพาะที่ต้องการ
* ระวังการแก้ไฟล์ใน Git repository ด้วยตัวเอง

### Credentials, variables and workflow tags

credential กับ variable จะไม่มี merge issue เพราะ n8n จะเลือกเวอร์ชันที่ต้องการให้เอง

ตอน pull:

* ถ้า tag, variable หรือ credential ยังไม่มี n8n จะสร้างใหม่
* ถ้ามีอยู่แล้ว n8n จะไม่ update เว้นแต่:
	* คุณ set ค่า variable ผ่าน API หรือภายนอก ค่าใหม่จะทับของเดิม
	* credential name เปลี่ยน n8n จะใช้เวอร์ชันใน Git
	* tag name เปลี่ยน n8n จะ update ชื่อ tag ระวังเวลา rename tag เพราะ tag name ต้อง unique อาจจะมีปัญหา database ได้

ตอน push:

* n8n จะ overwrite ไฟล์ variables กับ tags ทั้งหมด
* ถ้ามี credential อยู่แล้ว n8n จะ overwrite ด้วยของใหม่ แต่จะไม่ apply การเปลี่ยนแปลง credential ตอน pull

/// note | Manage credentials with an external secrets vault
ถ้าคุณต้องการ credential ต่างกันในแต่ละ n8n environment ให้ใช้ [external secrets](/external-secrets.md)
///
