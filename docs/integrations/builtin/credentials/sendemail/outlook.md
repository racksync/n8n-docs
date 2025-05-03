---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Outlook.com
description: เอกสารสำหรับ Outlook.com Send Email credentials ใช้ credential นี้เพื่อยืนยันตัวตน Send Email กับ Outlook.com ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: high
---

# Outlook.com Send Email credentials

ทำตามขั้นตอนเหล่านี้เพื่อกำหนดค่า Send Email credentials ด้วยบัญชี Outlook.com

## Set up the credential

เพื่อกำหนดค่า Send Email credential ให้ใช้บัญชี Outlook.com:

1. ป้อนที่อยู่อีเมล Outlook.com ของคุณเป็น **User**
2. ป้อนรหัสผ่าน Outlook.com ของคุณเป็น **Password**

	/// note | App password
	Outlook.com ไม่จำเป็นต้องใช้ app password แต่หากคุณต้องการใช้เพื่อเหตุผลด้านความปลอดภัย โปรดอ้างอิง [Use an app password](#use-an-app-password)
	///

4. ป้อน `smtp-mail.outlook.com` เป็น **Host**
5. ป้อน `587` สำหรับ **Port**
6. เปิดใช้งาน toggle **SSL/TLS**

อ้างอิงเอกสารของ Microsoft [POP, IMAP, and SMTP settings for Outlook.com](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม หากการตั้งค่าข้างต้นใช้ไม่ได้ผลสำหรับคุณ โปรดตรวจสอบกับผู้ดูแลระบบอีเมลของคุณ

## Use an app password

--8<-- "_snippets/integrations/builtin/credentials/email/outlook-app-password.md"
