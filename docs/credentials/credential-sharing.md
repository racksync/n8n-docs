---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การแชร์ Credential
description: แชร์ credentials ภายในองค์กร
contentType: howto
---

# Credential sharing


/// info | Feature availability
Available on all Cloud plans, and Enterprise self-hosted plans.
///

คุณสามารถแชร์ credential ให้กับผู้ใช้อื่นโดยตรงเพื่อใช้ใน workflow ของพวกเขาเอง หรือแชร์ credential ใน [project](/glossary.md#project-n8n) เพื่อให้สมาชิกทุกคนใน project นั้นใช้งานได้ ผู้ใช้ที่ใช้ credential ที่แชร์จะไม่สามารถดูหรือแก้ไขรายละเอียดของ credential ได้

ผู้ใช้สามารถแชร์ credentials ที่ตนเองสร้างและเป็นเจ้าของได้ เฉพาะ project admins เท่านั้นที่สามารถแชร์ credentials ที่สร้างขึ้นและเป็นของ project ได้ Instance owners และ instance admins สามารถดูและแชร์ credentials ทั้งหมดบน instance ได้

อ้างอิง [Account types](/user-management/account-types.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ owners และ admins

ใน [projects](/user-management/rbac/index.md) บทบาทของผู้ใช้จะควบคุมวิธีที่พวกเขาสามารถโต้ตอบกับ workflows และ credentials ที่เกี่ยวข้องกับ projects ที่พวกเขาเป็นสมาชิก

## Share a credential

วิธีแชร์ credential:

1. จากเมนูด้านซ้าย เลือก **Overview** หรือ project
2. เลือก **Credentials** เพื่อดูรายการ credentials ของคุณ
3. เลือก credential ที่คุณต้องการแชร์
4. เลือก **Sharing**
5. ในดรอปดาวน์ **Share with projects or users** เรียกดูหรือค้นหา user หรือ project ที่คุณต้องการแชร์ credentials ด้วย
6. เลือก user หรือ project
7. เลือก **Save** เพื่อบันทึกการเปลี่ยนแปลง

## Remove access to a credential

วิธีเลิกแชร์ credential:

1. จากเมนูด้านซ้าย เลือก **Overview** หรือ project
2. เลือก **Credentials** เพื่อดูรายการ credentials ของคุณ
3. เลือก credential ที่คุณต้องการเลิกแชร์
4. เลือก **Sharing**
5. เลือก **trash icon**<span class="inline-image">![Trash icon](/_images/common-icons/delete-node.png){.off-glb}</span> บน user หรือ project ที่คุณต้องการลบออกจากรายการที่แชร์ด้วย
6. เลือก **Save** เพื่อบันทึกการเปลี่ยนแปลง
