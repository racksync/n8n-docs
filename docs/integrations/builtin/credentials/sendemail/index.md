---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Send Email credentials
description: เอกสารสำหรับ Send Email credentials ใช้ credential นี้เพื่อยืนยันตัวตน Send Email ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: high
---

# Send Email credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตน nodes ต่อไปนี้:

- [Send Email](/integrations/builtin/core-nodes/n8n-nodes-base.sendemail.md)

## Prerequisites

- สร้างบัญชีอีเมลบนบริการที่รองรับ SMTP
- ผู้ให้บริการอีเมลบางรายต้องการให้คุณเปิดใช้งานหรือตั้งค่า SMTP ขาออก หรือสร้าง app password โปรดอ้างอิงเอกสารของผู้ให้บริการของคุณเพื่อดูว่ามีขั้นตอนอื่นที่จำเป็นหรือไม่

## Supported authentication methods

- บัญชี SMTP

## Related resources

Simple Message Transfer Protocol (SMTP) เป็นโปรโตคอลมาตรฐานสำหรับการส่งและรับอีเมล ผู้ให้บริการอีเมลส่วนใหญ่มีคำแนะนำในการตั้งค่าบริการของตนด้วย SMTP โปรดอ้างอิงคำแนะนำ SMTP ของผู้ให้บริการของคุณ

## Using SMTP account

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- ที่อยู่อีเมล **User**
- **Password**: อาจเป็นรหัสผ่านของผู้ใช้หรือ app password โปรดอ้างอิงเอกสารสำหรับผู้ให้บริการอีเมลของคุณ
- **Host**: ที่อยู่ SMTP host สำหรับผู้ให้บริการอีเมลของคุณ ซึ่งมักอยู่ในรูปแบบ `smtp.<provider>.com` โปรดตรวจสอบกับผู้ให้บริการของคุณ
- หมายเลข **Port**: ค่าเริ่มต้นคือ port `465` ซึ่งใช้กันทั่วไปสำหรับ SSL พอร์ตทั่วไปอื่นๆ คือ `587` สำหรับ TLS หรือ `25` สำหรับการไม่เข้ารหัส โปรดตรวจสอบกับผู้ให้บริการของคุณ
- **SSL/TLS**: เมื่อเปิดใช้งาน SMTP จะใช้ SSL/TLS
- **Disable STARTTLS**: เมื่อปิดใช้งาน SSL/TLS เซิร์ฟเวอร์ SMTP ยังคงสามารถพยายาม [upgrade the TCP connection using STARTTLS](https://en.wikipedia.org/wiki/Opportunistic_TLS){:target=_blank .external-link} ได้ การเปิดใช้งานตัวเลือกนี้จะป้องกันพฤติกรรมดังกล่าว
- **Client Host Name**: หากผู้ให้บริการของคุณต้องการ ให้เพิ่ม client host name ชื่อนี้จะระบุ client ให้กับ server

### Provider instructions

อ้างอิงคู่มือเริ่มต้นฉบับย่อสำหรับผู้ให้บริการอีเมลทั่วไปเหล่านี้

#### Gmail

อ้างอิง [Gmail](/integrations/builtin/credentials/sendemail/gmail.md)

#### Outlook.com

อ้างอิง [Outlook.com](/integrations/builtin/credentials/sendemail/outlook.md)

#### Yahoo

อ้างอิง [Yahoo](/integrations/builtin/credentials/sendemail/yahoo.md)

### My provider isn't listed

หากผู้ให้บริการอีเมลของคุณไม่อยู่ในรายการนี้ ให้ค้นหา `SMTP settings` เพื่อค้นหาคำแนะนำของพวกเขา (คำแนะนำเหล่านี้อาจรวมอยู่ใน `IMAP settings` หรือ `POP settings` ด้วย)
