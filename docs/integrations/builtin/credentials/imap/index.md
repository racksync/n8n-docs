---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: IMAP credentials
description: เอกสารสำหรับ IMAP credentials ใช้ credential นี้เพื่อยืนยันตัวตน IMAP ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: high
---

# IMAP credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตน node ต่อไปนี้:

- [IMAP Email](/integrations/builtin/core-nodes/n8n-nodes-base.emailimap.md)

## Prerequisites

สร้างบัญชีอีเมลบนบริการที่รองรับ IMAP

## Supported authentication methods

- User account

## Related resources

Internet Message Access Protocol (IMAP) เป็นโปรโตคอลมาตรฐานสำหรับการรับอีเมล ผู้ให้บริการอีเมลส่วนใหญ่มีคำแนะนำในการตั้งค่าบริการของตนด้วย IMAP โปรดอ้างอิงคำแนะนำ IMAP ของผู้ให้บริการของคุณ

## Using user account

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **User** name: ที่อยู่อีเมลที่คุณกำลังดึงอีเมล
- **Password**: อาจเป็นรหัสผ่านที่คุณใช้ตรวจสอบอีเมล หรือ app password ผู้ให้บริการของคุณจะแจ้งให้คุณทราบว่าควรใช้รหัสผ่านของคุณเองหรือสร้าง app password
- **Host**: ที่อยู่ IMAP host สำหรับผู้ให้บริการอีเมลของคุณ ซึ่งมักอยู่ในรูปแบบ `imap.<provider>.com` ตรวจสอบกับผู้ให้บริการของคุณ
- **Port** number: ค่าเริ่มต้นคือ port `993` ใช้ port นี้เว้นแต่ผู้ให้บริการหรือผู้ดูแลระบบอีเมลของคุณจะบอกให้ใช้ค่าอื่น

เลือกว่าจะใช้ **SSL/TLS** หรือไม่ และจะ **Allow Self-Signed Certificates** หรือไม่

### Provider instructions

อ้างอิงคู่มือเริ่มต้นฉบับย่อสำหรับผู้ให้บริการอีเมลทั่วไปเหล่านี้

#### Gmail

อ้างอิง [Gmail](/integrations/builtin/credentials/imap/gmail.md)

#### Outlook.com

อ้างอิง [Outlook.com](/integrations/builtin/credentials/imap/outlook.md)

#### Yahoo

อ้างอิง [Yahoo](/integrations/builtin/credentials/imap/yahoo.md)

### My provider isn't listed

หากผู้ให้บริการอีเมลของคุณไม่อยู่ในรายการนี้ ให้ค้นหา `IMAP settings` หรือ `IMAP instructions` ของพวกเขา
