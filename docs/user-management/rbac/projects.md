---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Project ใน RBAC
description: ทำความเข้าใจวิธีที่ n8n ใช้ Project สำหรับ RBAC เรียนรู้วิธีสร้างและจัดการ Project
contentType: howto
---

/// info | Feature availability
RBAC มีให้ใช้งานในทุก plan ยกเว้น Community edition แต่ละ plan จะมีจำนวน projects และ roles ที่แตกต่างกัน โปรดดูรายละเอียด plan ได้ที่ [pricing page](https://n8n.io/pricing/){:target=_blank .external-link} ของ n8n
///

n8n ใช้ projects เพื่อจัดกลุ่ม workflows และ [credentials](/glossary.md#credential-n8n) และกำหนด [roles](/user-management/rbac/role-types.md) ให้กับผู้ใช้ในแต่ละ project ซึ่งหมายความว่าผู้ใช้คนเดียวสามารถมี roles ที่แตกต่างกันใน projects ที่ต่างกันได้ ทำให้พวกเขามีระดับการเข้าถึงที่แตกต่างกัน

## Create a project

Instance owners และ instance admins สามารถสร้าง projects ได้

วิธีสร้าง project:

1. เลือก <span class="inline-image">![Plus icon](/_images/common-icons/plus.png)</span> **Add project**
2. กรอก project settings
3. เลือก **Save**

## Add and remove users in a project

Project admins สามารถเพิ่มและลบผู้ใช้ได้

วิธีเพิ่มผู้ใช้ใน project:

1. เลือก project
2. เลือก **Project settings**
3. ใต้ **Project members**, ค้นหาผู้ใช้หรือค้นหาด้วย username หรือ email address
4. เลือกผู้ใช้ที่คุณต้องการเพิ่ม
5. ตรวจสอบ [role type](/user-management/rbac/role-types.md) และเปลี่ยนหากจำเป็น
6. เลือก **Save**

วิธีลบผู้ใช้จาก project:

1. เลือก project
2. เลือก **Project settings**
3. ใน dropdown ของ role type สำหรับผู้ใช้ที่คุณต้องการลบ ให้เลือก **Remove access**
4. เลือก **Save**

## Delete a project

วิธีลบ project:

1. เลือก project
2. เลือก **Project settings**
3. เลือก **Delete project**
4. เลือกสิ่งที่จะทำกับ workflows และ credentials คุณสามารถเลือก:
    * **Transfer its workflows and credentials to another project**: n8n จะแจ้งให้คุณเลือก project ที่จะย้ายข้อมูลไป
    * **Delete its workflows and credentials**: n8n จะแจ้งให้คุณยืนยันว่าต้องการลบข้อมูลทั้งหมดใน project

## Move workflows and credentials between projects or users

เจ้าของ Workflow และ credential สามารถย้าย workflows หรือ credentials (เปลี่ยนความเป็นเจ้าของ) ไปยังผู้ใช้อื่นหรือ projects อื่นที่พวกเขามีสิทธิ์เข้าถึงได้

/// warning | Moving revokes sharing
การย้าย workflows หรือ credentials จะลบการแชร์ที่มีอยู่ทั้งหมด โปรดทราบว่าสิ่งนี้อาจส่งผลกระทบต่อ workflows อื่นๆ ที่กำลังแชร์ทรัพยากรเหล่านี้อยู่
///

1. เลือก **Workflow menu** <span class="inline-image">![Workflow menu icon](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span> หรือ **Credential menu** <span class="inline-image">![Workflow menu icon](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span> > **Move**

    /// info | Moving workflows with credentials
    เมื่อย้าย workflow พร้อมกับ credentials ที่คุณมีสิทธิ์แชร์ คุณสามารถเลือกที่จะแชร์ credentials ด้วยได้ สิ่งนี้ช่วยให้มั่นใจว่า workflow ยังคงสามารถเข้าถึง credentials ที่จำเป็นต้องใช้ในการ execute ได้ n8n จะบันทึก credentials ใดๆ ที่ไม่สามารถย้ายได้ (credentials ที่คุณไม่มีสิทธิ์แชร์)
    ///

2. เลือก project หรือ user ที่คุณต้องการย้ายไป
3. เลือก **Next**
4. ยืนยันว่าคุณเข้าใจผลกระทบของการย้าย: workflows อาจหยุดทำงานหาก credentials ที่ต้องการไม่มีอยู่ใน project ปลายทาง และ n8n จะลบการแชร์ส่วนบุคคลที่มีอยู่ในปัจจุบันทั้งหมด
5. เลือก **Confirm move to new project**

## Using external secrets in projects

หากต้องการใช้ [external secrets](/external-secrets.md) ใน project คุณต้องมี [instance owner หรือ instance admin](/user-management/account-types.md) เป็นสมาชิกของ project นั้น
