---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Ghost credentials
description: Documentation for Ghost credentials. Use these credentials to authenticate Ghost in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Ghost credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Ghost](/integrations/builtin/app-nodes/n8n-nodes-base.ghost.md)

## Prerequisites

สร้างบัญชี [Ghost](https://ghost.org/){:target=_blank .external-link}

## Supported authentication methods

- Admin API key
- Content API key

keys เหล่านี้สร้างขึ้นตามขั้นตอนเดียวกัน แต่ขั้นตอนการ authorization และรูปแบบ key แตกต่างกัน ดังนั้น n8n จึงจัดเก็บ credentials แยกกัน Content API ใช้ API key; Admin API ใช้ API key เพื่อสร้าง token สำหรับการยืนยันตัวตน

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการ Admin API ได้ที่ [Ghost's Admin API documentation](https://ghost.org/docs/admin-api/){:target=_blank .external-link} ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการ Content API ได้ที่ [Ghost's Content API documentation](https://ghost.org/docs/content-api/){:target=_blank .external-link}

## Using Admin API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **URL** ของ Ghost admin domain ของคุณ [admin domain](https://ghost.org/docs/admin-api/#base-url){:target=_blank .external-link} ของคุณอาจแตกต่างจาก domain หลักของคุณและอาจรวมถึง subdirectory บล็อก Ghost(Pro) ทั้งหมดมี domain `*.ghost.io` เป็น admin domain และต้องใช้ https
- **API Key**: หากต้องการสร้าง API key ใหม่ ให้สร้าง Custom Integration ใหม่ ดูคำแนะนำโดยละเอียดเพิ่มเติมได้ที่ [Ghost Admin API Token Authentication Key documentation](https://ghost.org/docs/admin-api/#token-authentication){:target=_blank .external-link} คัดลอก **Admin API Key** และใช้เป็น **API Key** ใน Ghost Admin n8n credential

## Using Content API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **URL** ของ Ghost admin domain ของคุณ [admin domain](https://ghost.org/docs/content-api/#url){:target=_blank .external-link} ของคุณอาจแตกต่างจาก domain หลักของคุณและอาจรวมถึง subdirectory บล็อก Ghost(Pro) ทั้งหมดมี domain `*.ghost.io` เป็น admin domain และต้องใช้ https
- **API Key**: หากต้องการสร้าง API key ใหม่ ให้สร้าง Custom Integration ใหม่ ดูคำแนะนำโดยละเอียดเพิ่มเติมได้ที่ [Ghost Content API Key documentation](https://ghost.org/docs/content-api/#key){:target=_blank .external-link} คัดลอก **Content API Key** และใช้เป็น **API Key** ใน Ghost Content n8n credential

