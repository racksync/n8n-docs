---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: จัดการผู้ใช้ด้วย SAML
description: วิธีจัดการผู้ใช้และการ login ของผู้ใช้เมื่อเปิดใช้งาน SAML
contentType: howto
---

# Manage users with SAML

มีงานจัดการผู้ใช้บางอย่างที่ได้รับผลกระทบจาก SAML

## Exempt users from SAML

คุณสามารถอนุญาตให้ผู้ใช้ login โดยไม่ต้องใช้ SAML ได้ โดยทำดังนี้:

1. ไปที่ **Settings** > **Users**
2. เลือกไอคอนเมนูข้างผู้ใช้ที่คุณต้องการยกเว้นจาก SAML
3. เลือก **Allow Manual Login**

## Deleting users

หากคุณลบผู้ใช้ออกจาก IdP ของคุณ พวกเขาจะยังคง login อยู่ใน n8n คุณต้องลบพวกเขาออกจาก n8n ด้วยตนเอง โปรดดู [Manage users](/user-management/manage-users.md) สำหรับคำแนะนำในการลบผู้ใช้
