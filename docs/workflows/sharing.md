---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Share workflows between users.
contentType: howto
---

# Workflow sharing

/// info | Feature availability
มีให้ใช้งานบน Pro และ Enterprise Cloud plans และ Enterprise self-hosted plans
///

Workflow sharing ช่วยให้คุณสามารถแชร์ workflows ระหว่างผู้ใช้ใน n8n instance เดียวกันได้

ผู้ใช้สามารถแชร์ workflows ที่พวกเขาสร้างขึ้นได้ Instance owners และผู้ใช้ที่มีบทบาท admin สามารถดูและแชร์ workflows ทั้งหมดใน instance ได้ โปรดดู [Account types](/user-management/account-types.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ owners และ admins

## Share a workflow

1. เปิด workflow ที่คุณต้องการแชร์
2. เลือก **Share**
3. ใน **Add users** ค้นหาและเลือกผู้ใช้ที่คุณต้องการแชร์ด้วย
4. เลือก **Save**

## View shared workflows

คุณสามารถเรียกดูและค้นหา workflows ได้ในรายการ **Workflows** workflows ในรายการจะขึ้นอยู่กับ project:

* **Overview** แสดงรายการ workflows ทั้งหมดที่คุณสามารถเข้าถึงได้ ซึ่งรวมถึง:
	* workflows ของคุณเอง
	* workflows ที่แชร์กับคุณ
	* workflows ใน projects ที่คุณเป็นสมาชิก
	* หากคุณเข้าสู่ระบบในฐานะ instance owner หรือ admin: workflows ทั้งหมดใน instance
* Other projects: workflows ทั้งหมดใน project นั้น

## Workflow roles and permissions

มี workflow roles สองแบบ: creator และ editor creator คือผู้ใช้ที่สร้าง workflow editors คือผู้ใช้คนอื่นๆ ที่มีสิทธิ์เข้าถึง workflow

คุณไม่สามารถเปลี่ยน workflow owner ได้ ยกเว้นเมื่อลบผู้ใช้

/// note | Credentials
Workflow sharing อนุญาตให้ editors ใช้ [credentials](/glossary.md#credential-n8n) ทั้งหมดที่ใช้ใน workflow ซึ่งรวมถึง credentials ที่ไม่ได้แชร์กับพวกเขาอย่างชัดเจนโดยใช้ [credential sharing](/credentials/credential-sharing.md)
///
### Permissions

| Permissions | Creator | Editor | 
| ----------- | ------- | ------ | 
| View workflow (read-only) | :white_check_mark: | :white_check_mark: |
| View executions | :white_check_mark: | :white_check_mark: |
| Update (including tags) | :white_check_mark: | :white_check_mark: |
| Run | :white_check_mark: | :white_check_mark: |
| Share | :white_check_mark: | :x: |
| Export | :white_check_mark: | :white_check_mark: |
| Delete | :white_check_mark: | :x: |

## Node editing restrictions with unshared credentials

การแชร์ใน n8n ทำงานบนหลักการของ least privilege ซึ่งหมายความว่าหากผู้ใช้แชร์ workflow กับคุณ แต่พวกเขาไม่ได้แชร์ credentials ของพวกเขา คุณจะไม่สามารถแก้ไข nodes ภายใน workflow ที่ใช้ credentials เหล่านั้นได้ คุณสามารถดูและรัน workflow และแก้ไข nodes ที่ไม่ได้ใช้ credentials ที่ไม่ได้แชร์ได้

โปรดดู [Credential sharing](/credentials/credential-sharing.md) สำหรับคำแนะนำในการแชร์ credentials
