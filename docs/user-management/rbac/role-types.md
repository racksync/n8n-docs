---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ประเภท Role ใน RBAC
description: ทำความเข้าใจ Role ต่างๆ ใน RBAC ของ n8n และสิทธิ์การเข้าถึง
contentType: reference
---

# RBAC role types

/// info | Feature availability
* Project Editor role มีให้ใช้งานบน Pro Cloud และ Self-hosted Enterprise plans
* Project Viewer role มีให้ใช้งานเฉพาะบน Self-hosted Enterprise และ Cloud Enterprise plans เท่านั้น
///

ภายใน projects มี user roles อยู่สามแบบ: Admin, Editor และ Viewer roles เหล่านี้ควบคุมสิ่งที่ผู้ใช้สามารถทำได้ใน project ผู้ใช้คนหนึ่งสามารถมี roles ที่แตกต่างกันใน projects ที่ต่างกันได้

## Project Admin

Project Admin role มีระดับสิทธิ์สูงสุด Project admins สามารถ:

* Manage project settings: เปลี่ยนชื่อ, ลบ project
* Manage project members: เชิญสมาชิกและลบสมาชิก, เปลี่ยน roles ของสมาชิก
* ดู, สร้าง, อัปเดต และลบ workflows, credentials หรือ executions ใดๆ ภายใน project

## Project Editor

Project Editor สามารถดู, สร้าง, อัปเดต และลบ workflows, credentials หรือ executions ใดๆ ภายใน project

## Project Viewer

Project Viewer เป็น role แบบ `read-only` ที่สามารถเข้าถึง workflows, credentials และ executions ทั้งหมดภายใน project ได้

Viewers ไม่สามารถ execute workflows ใดๆ ที่มีอยู่ใน project ด้วยตนเองได้

/// note | Role types and account types
Role types และ [account types](/user-management/account-types.md) เป็นคนละอย่างกัน ทุก account จะมี type เพียงอย่างเดียว แต่ account นั้นสามารถมี role types ที่แตกต่างกันสำหรับ [projects](/user-management/rbac/projects.md) ที่ต่างกันได้
///

| Permission | Admin | Editor | Viewer |
| ---------- |------ | ------ | ------ |
| View workflows in the project | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| View credentials in the project | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| View executions | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Edit credentials and workflows | :white_check_mark: | :white_check_mark: | :x: |
| Add workflows and credentials | :white_check_mark: | :white_check_mark: | :x: |
| Execute workflows | :white_check_mark: | :white_check_mark: | :x: |
| Manage members | :white_check_mark: | :x: | :x: |
| Modify the project | :white_check_mark: | :x: | :x: |

[Variables](/code/variables.md) และ [tags](/workflows/tags.md) ไม่ได้รับผลกระทบจาก RBAC: สิ่งเหล่านี้เป็นแบบ global ทั่วทั้ง n8n instance
