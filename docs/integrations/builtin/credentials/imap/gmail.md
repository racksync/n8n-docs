---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Gmail
description: Documentation for Gmail IMAP credentials. Use these credentials to authenticate Gmail IMAP in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: high
---

# Gmail IMAP credentials

ทำตามขั้นตอนเหล่านี้เพื่อกำหนดค่า IMAP credentials ด้วยบัญชี Gmail

## Prerequisites

ในการทำตามคำแนะนำเหล่านี้ คุณต้องทำสิ่งต่อไปนี้ก่อน:

1. [Enable 2-step Verification](#enable-2-step-verification) บนบัญชี Gmail ของคุณ
2. [Generate an app password](#generate-an-app-password)

### Enable 2-step Verification

--8<-- "_snippets/integrations/builtin/credentials/email/gmail-two-step-verification.md"

### Generate an app password

--8<-- "_snippets/integrations/builtin/credentials/email/gmail-app-password.md"

## Set up the credential

ในการตั้งค่า IMAP credential ด้วยบัญชี Gmail ให้ใช้การตั้งค่าเหล่านี้:

1. ป้อนที่อยู่อีเมล Gmail ของคุณเป็น **User**
2. ป้อน app password ที่คุณสร้างขึ้นด้านบนเป็น **Password**
3. ป้อน `imap.gmail.com` เป็น **Host**
4. สำหรับ **Port** ให้คงหมายเลข port เริ่มต้นไว้ที่ `993` ตรวจสอบกับผู้ดูแลระบบอีเมลของคุณหาก port นี้ใช้งานไม่ได้
5. เปิดใช้งาน toggle **SSL/TLS**
6. ตรวจสอบกับผู้ดูแลระบบอีเมลของคุณว่าควร **Allow Self-Signed Certificates** หรือไม่

อ้างอิง [Add Gmail to another client](https://support.google.com/mail/answer/7126229?hl=en){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม คุณอาจต้อง **Enable IMAP** หากคุณใช้บัญชี Google ส่วนตัวก่อนเดือนมิถุนายน 2024
