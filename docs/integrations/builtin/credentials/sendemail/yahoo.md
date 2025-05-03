---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Yahoo
description: เอกสารสำหรับ Yahoo Send Email credentials ใช้ credential นี้เพื่อยืนยันตัวตน Send Email กับ Yahoo ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: high
---

# Yahoo Send Email credentials

ทำตามขั้นตอนเหล่านี้เพื่อกำหนดค่า Send Email credentials ด้วยบัญชี Yahoo

## Prerequisites

ในการทำตามคำแนะนำนี้ คุณต้องสร้าง app password ก่อน:

--8<-- "_snippets/integrations/builtin/credentials/email/yahoo-app-password.md"

## Set up the credential

เพื่อกำหนดค่า Send Email credential ให้ใช้ Yahoo Mail:

1. ป้อนที่อยู่อีเมล Yahoo ของคุณเป็น **User**
2. ป้อน app password ที่คุณสร้างขึ้นด้านบนเป็น **Password**
3. ป้อน `smtp.mail.yahoo.com` เป็น **Host**
4. สำหรับ **Port**:
    - คงค่าเริ่มต้น `465` สำหรับ SSL หรือหากคุณไม่แน่ใจว่าจะใช้อะไร
    - ป้อน `587` สำหรับ TLS
5. เปิดใช้งาน toggle **SSL/TLS**

อ้างอิง [IMAP server settings for Yahoo Mail](https://help.yahoo.com/kb/sln4075.html){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม หากการตั้งค่าข้างต้นใช้ไม่ได้ผลสำหรับคุณ โปรดตรวจสอบกับผู้ดูแลระบบอีเมลของคุณ
