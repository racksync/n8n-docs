---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: What you can do
description: What you can do to improve privacy and data security when using n8n.
contentType: howto
---
<!-- vale off -->
# What you can do

เป็นความรับผิดชอบของคุณในฐานะลูกค้าเช่นกันที่จะต้องแน่ใจว่าคุณกำลังรักษาความปลอดภัย code และ data ของคุณ เอกสารนี้แสดงรายการขั้นตอนบางอย่างที่คุณสามารถทำได้

## All users

* รายงานปัญหาด้านความปลอดภัยและการละเมิด [terms of service](https://n8n.io/legal/#terms){:target=_blank .external-link} ไปที่ security@n8n.io
* หากมีผู้ใช้ n8n instance ของคุณมากกว่าหนึ่งคน ให้ตั้งค่า [User management](/user-management/index.md) และปฏิบัติตาม [Best practices](/user-management/best-practices.md)
* ใช้ OAuth เพื่อเชื่อมต่อ integrations เมื่อใดก็ตามที่เป็นไปได้

## Self-hosted users

หากคุณ self-host n8n มีขั้นตอนเพิ่มเติมที่คุณสามารถทำได้:

* ตั้งค่า reverse proxy เพื่อจัดการ TLS เพื่อให้แน่ใจว่าข้อมูลถูกเข้ารหัสในระหว่างการส่ง (encrypted in transit)
* ตรวจสอบให้แน่ใจว่าข้อมูลถูกเข้ารหัสเมื่อไม่ได้ใช้งาน (encrypted at rest) โดยใช้ encrypted partitions หรือการเข้ารหัสที่ระดับฮาร์ดแวร์ และตรวจสอบให้แน่ใจว่า n8n และฐานข้อมูลของมันถูกเขียนไปยังตำแหน่งนั้น
* รัน [Security audit](/hosting/securing/security-audit.md)
* ตระหนักถึง [Risks](/integrations/community-nodes/risks.md) เมื่อติดตั้ง community nodes หรือเลือกที่จะปิดใช้งานพวกมัน
* ตรวจสอบให้แน่ใจว่าผู้ใช้ไม่สามารถ import external modules ใน Code node ได้ โปรดดู [Environment variables | Nodes](https://docs.n8n.io/hosting/configuration/environment-variables/nodes) สำหรับข้อมูลเพิ่มเติม
* เลือกที่จะ exclude nodes บางตัว ตัวอย่างเช่น คุณสามารถปิดใช้งาน nodes เช่น Execute Command หรือ SSH โปรดดู [Environment variables | Nodes](https://docs.n8n.io/hosting/configuration/environment-variables/nodes) สำหรับข้อมูลเพิ่มเติม
* เพื่อความเป็นส่วนตัวสูงสุด คุณสามารถ [Isolate n8n](/hosting/configuration/configuration-examples/isolation.md)

### GDPR for self-hosted users

--8<-- "_snippets/privacy-security/gdpr-self-hosted.md"

<!-- vale on -->
