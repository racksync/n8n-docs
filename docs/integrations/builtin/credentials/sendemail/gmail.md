---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Gmail
description: เอกสารสำหรับ Gmail Send Email credentials ใช้ credential นี้เพื่อยืนยันตัวตน Send Email กับ Gmail ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: high
---

# Gmail Send Email credentials

ทำตามขั้นตอนเหล่านี้เพื่อกำหนดค่า Send Email credentials ด้วยบัญชี Gmail

## Prerequisites

ในการทำตามคำแนะนำนี้ คุณต้องทำสิ่งต่อไปนี้ก่อน:

1. [Enable 2-step Verification](#enable-2-step-verification) บนบัญชี Gmail ของคุณ
2. [Generate an app password](#generate-an-app-password)

### Enable 2-step Verification

--8<-- "_snippets/integrations/builtin/credentials/email/gmail-two-step-verification.md"

### Generate an app password

--8<-- "_snippets/integrations/builtin/credentials/email/gmail-app-password.md"

## Set up the credential

เพื่อตั้งค่า Send Email credential ให้ใช้ Gmail:

1. ป้อนที่อยู่อีเมล Gmail ของคุณเป็น **User**
2. ป้อน app password ที่คุณสร้างขึ้นด้านบนเป็น **Password**
3. ป้อน `smtp.gmail.com` เป็น **Host**
4. สำหรับ **Port**:
    - คงค่าเริ่มต้น `465` สำหรับ SSL หรือหากคุณไม่แน่ใจว่าจะใช้อะไร
    - ป้อน `587` สำหรับ TLS
5. เปิดใช้งาน toggle **SSL/TLS**

อ้างอิงการตั้งค่า Outgoing Mail (SMTP) Server ใน [Read Gmail messages on other email clients using POP](https://support.google.com/mail/answer/7104828?hl=en){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม หากการตั้งค่าข้างต้นใช้ไม่ได้ผลสำหรับคุณ โปรดตรวจสอบกับผู้ดูแลระบบอีเมลของคุณ
