---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Community edition features
description: Differences in available features between the Community edition and other paid plans.
contentType: explanation
tags:
  - Community edition
  - Enterprise edition
hide:
  - tags
---

# Community Edition Features

Community edition จะมีฟีเจอร์เกือบครบเหมือน n8n เวอร์ชันเต็ม ยกเว้นฟีเจอร์ที่ระบุไว้ที่นี่

Community edition จะไม่มีฟีเจอร์เหล่านี้:

- [Custom Variables](/code/variables.md)
- [Environments](/source-control-environments/index.md)
- [External secrets](/external-secrets.md)
- [External storage for binary data](/hosting/scaling/external-storage.md)
- [Log streaming](/log-streaming.md) ([Logging](/hosting/logging-monitoring/logging.md) _มีให้ใช้งาน_)
- [Multi-main mode](/hosting/scaling/queue-mode.md#multi-main-setup) ([Queue mode](/hosting/scaling/queue-mode.md) _มีให้ใช้งาน_)
- [Projects](/user-management/rbac/projects.md)
- SSO ([SAML](/hosting/securing/set-up-sso.md), [LDAP](/user-management/ldap.md))
- Sharing ([workflows](/workflows/sharing.md), [credentials](/credentials/credential-sharing.md)) (เฉพาะเจ้าของ instance และผู้สร้างเท่านั้นที่เข้าถึง workflows และ credentials ได้)
- [Version control using Git](/source-control-environments/index.md)
- [Workflow history](/workflows/history.md) (Community edition จะดู workflow history ได้ 1 วัน ถ้า [register](#registered-community-edition))

ฟีเจอร์เหล่านี้จะมีใน Enterprise Cloud plan รวมถึง self-hosted Enterprise edition และบางฟีเจอร์อาจมีใน Starter หรือ Pro Cloud plan ด้วย

ดูรายละเอียด [pricing](https://n8n.io/pricing/){:target=_blank .external-link} ได้เลย

## Registered Community Edition

คุณสามารถปลดล็อกฟีเจอร์เพิ่มเติมได้โดยการ register n8n community edition ของคุณ โดยจะลงทะเบียนด้วยอีเมลและรับ license key

เมื่อ register แล้ว Community edition จะปลดล็อกฟีเจอร์เหล่านี้:

* [Folders](/release-notes.md#folders): จัดระเบียบ workflow ของคุณเป็นโฟลเดอร์
* [Debug in editor](/workflows/executions/debug.md): copy และ [pin](/glossary.md#data-pinning-n8n) ข้อมูล execution ขณะทำ workflow
* ดู [workflow history](/workflows/history.md) ได้ 1 วัน: ย้อน workflow ได้ 24 ชั่วโมง
* [Custom execution data](/workflows/executions/custom-executions-data.md): บันทึก, ค้นหา, และใส่โน้ต execution metadata

ถ้าจะ register instance ใหม่ ให้เลือกตัวเลือกนี้ตอนสร้าง account ครั้งแรก

ถ้าจะ register instance ที่มีอยู่แล้ว:

1. กด **three dots icon** <span class="inline-image">![three dots icon](/_images/common-icons/three-dots-horizontal.png){.off-glb}</span> ที่มุมซ้ายล่าง
1. เลือก **Settings** แล้วไปที่ **Usage and plan**
1. กด **Unlock** เพื่อกรอกอีเมล แล้วเลือก **Send me a free license key**
1. เช็คอีเมลที่กรอกไว้

เมื่อได้ license key แล้ว ให้ activate โดยกดปุ่มในอีเมล หรือไปที่ **Options > Settings > Usage and plan** แล้วเลือก **Enter activation key**

เมื่อ activate แล้ว license จะไม่มีวันหมดอายุ (เราอาจเปลี่ยนฟีเจอร์ที่ปลดล็อกในอนาคต แต่จะไม่กระทบฟีเจอร์ที่ปลดล็อกไปแล้ว)
