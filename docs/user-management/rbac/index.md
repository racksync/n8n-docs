---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: overview
title: Role-based access control (RBAC)
description: Set up and use role-based access control (RBAC) in n8n.
---

# Role-based access control (RBAC)

/// info | Feature availability
RBAC มีให้ใช้งานในทุก plan ยกเว้น Community edition แต่ละ plan จะมีจำนวน projects และ roles ที่แตกต่างกัน โปรดดูรายละเอียด plan ได้ที่ [pricing page](https://n8n.io/pricing/){:target=_blank .external-link} ของ n8n
///

/// note | Role types and account types
Role types และ [account types](/user-management/account-types.md) เป็นคนละอย่างกัน ทุก account จะมี type เพียงอย่างเดียว แต่ account นั้นสามารถมี role types ที่แตกต่างกันสำหรับ [projects](/user-management/rbac/projects.md) ที่ต่างกันได้
///

RBAC เป็นวิธีการจัดการการเข้าถึง workflows และ [credentials](/glossary.md#credential-n8n) โดยอิงตาม user roles และ projects คุณสามารถจัดกลุ่ม workflows ลงใน projects และการเข้าถึงของผู้ใช้จะขึ้นอยู่กับ project role ของผู้ใช้นั้นๆ ส่วนนี้จะให้คำแนะนำเกี่ยวกับการใช้ RBAC ใน n8n

[[% import "_macros/section-toc.html" as sectionToc %]]

[[ sectionToc.sectionToc(page) ]]





