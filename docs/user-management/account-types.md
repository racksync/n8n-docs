---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: n8n account types
contentType: reference
---

# Account types

มี account types สามแบบ: owner, admin และ member account type จะส่งผลต่อสิทธิ์และการเข้าถึงของผู้ใช้

/// info | Feature availability
หากต้องการใช้ admin accounts คุณต้องมี pro หรือ enterprise plan
///

/// note | Account types and role types
Account types และ role types เป็นคนละอย่างกัน Role types เป็นส่วนหนึ่งของ [RBAC](/user-management/rbac/index.md)

ทุก account จะมี type เพียงอย่างเดียว แต่ account นั้นสามารถมี [role types](/user-management/rbac/role-types.md) ที่แตกต่างกันสำหรับ [projects](/user-management/rbac/projects.md) ที่ต่างกันได้
///

/// note | Create a member-level account for the owner
n8n แนะนำให้ owners สร้าง member-level account สำหรับตนเอง Owners สามารถเห็นและแก้ไข workflows, credentials และ projects ทั้งหมดได้ อย่างไรก็ตาม ไม่มีวิธีดูว่าใครเป็นคนสร้าง workflow นั้นๆ ดังนั้นจึงมีความเสี่ยงที่จะเขียนทับงานของผู้อื่นหากคุณสร้างและแก้ไข workflows ในฐานะ owner
///


| Permission | Owner | Admin | Member |
| ---------- |------ | ----- | ------ |
| Manage own email and password | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Manage own workflows | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| View, create, and use tags | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Delete tags | :white_check_mark: | :white_check_mark: | :x: |
| View and share all workflows | :white_check_mark: | :white_check_mark: | :x: |
| View, edit, and share all credentials | :white_check_mark: | :white_check_mark: | :x: |
| Set up and use [Source control](/source-control-environments/index.md) | :white_check_mark: | :white_check_mark: | :x: |
| Create [projects](/user-management/rbac/projects.md) | :white_check_mark: | :white_check_mark: | :x: |
| View all projects | :white_check_mark: | :white_check_mark: | :x: |
| Add and remove users | :white_check_mark: | :white_check_mark: | :x: |
| Access the Cloud dashboard | :white_check_mark: | :x: | :x: |


