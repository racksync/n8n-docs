---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Yahoo
description: เอกสารสำหรับ Yahoo IMAP credentials ใช้ credential นี้เพื่อยืนยันตัวตน Yahoo IMAP ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: high
---

# Yahoo IMAP credentials

ทำตามขั้นตอนเหล่านี้เพื่อกำหนดค่า IMAP credentials ด้วยบัญชี Yahoo

## Prerequisites

ในการทำตามคำแนะนำเหล่านี้ คุณต้องสร้าง app password ก่อน:

--8<-- "_snippets/integrations/builtin/credentials/email/yahoo-app-password.md"

## Set up the credential

ในการตั้งค่า IMAP credential ด้วยบัญชี Yahoo Mail ให้ใช้การตั้งค่าเหล่านี้:

1. ป้อนที่อยู่อีเมล Yahoo ของคุณเป็น **User**
2. ป้อน app password ที่คุณสร้างขึ้นด้านบนเป็น **Password**
3. ป้อน `imap.mail.yahoo.com` เป็น **Host**
4. คงหมายเลข **Port** เริ่มต้นไว้ที่ `993` ตรวจสอบกับผู้ดูแลระบบอีเมลของคุณหาก port นี้ใช้งานไม่ได้
5. เปิดใช้งาน toggle **SSL/TLS**
6. ตรวจสอบกับผู้ดูแลระบบอีเมลของคุณว่าควร **Allow Self-Signed Certificates** หรือไม่

อ้างอิง [Set up IMAP for Yahoo mail account](https://help.yahoo.com/kb/sln4075.html){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
