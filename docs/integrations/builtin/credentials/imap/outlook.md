---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Outlook.com
description: Documentation for Outlook.com IMAP credentials. Use these credentials to authenticate Outlook.com IMAP in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: high
---

# Outlook.com IMAP credentials

ทำตามขั้นตอนเหล่านี้เพื่อกำหนดค่า IMAP credentials ด้วยบัญชี Outlook.com

## Set up the credentials

ในการตั้งค่า IMAP credential ด้วยบัญชี Outlook.com ให้ใช้การตั้งค่าเหล่านี้:

1. ป้อนที่อยู่อีเมล Outlook.com ของคุณเป็น **User**
2. ป้อนรหัสผ่าน Outlook.com ของคุณเป็น **Password**

    /// note | App password
    Outlook.com ไม่ต้องการให้คุณใช้ app password แต่หากคุณต้องการใช้เพื่อเหตุผลด้านความปลอดภัย โปรดดูที่ [Use an app password](#use-an-app-password)
    ///

3. ป้อน `outlook.office365.com` เป็น **Host**
4. สำหรับ **Port** ให้คงหมายเลข port เริ่มต้นไว้ที่ `993`
5. เปิดใช้งาน toggle **SSL/TLS**
6. ตรวจสอบกับผู้ดูแลระบบอีเมลของคุณว่าควร **Allow Self-Signed Certificates** หรือไม่

อ้างอิงเอกสาร [POP, IMAP, and SMTP settings for Outlook.com](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){:target=_blank .external-link} ของ Microsoft สำหรับข้อมูลเพิ่มเติม

## Connection errors

คุณอาจได้รับข้อผิดพลาดในการเชื่อมต่อหากคุณกำหนดค่าบัญชี Outlook.com ของคุณเป็น IMAP ในไคลเอนต์อีเมลหลายตัว Microsoft กำลังดำเนินการแก้ไขปัญหานี้ ในระหว่างนี้ ลองใช้วิธีแก้ปัญหานี้:

1. ไปที่ [account.live.com/activity](https://account.live.com/activity) และลงชื่อเข้าใช้โดยใช้ที่อยู่อีเมลและรหัสผ่านของบัญชีที่ได้รับผลกระทบ
1. ภายใต้ **Recent activity** ค้นหาเหตุการณ์ **Session Type** ที่ตรงกับเวลาล่าสุดที่คุณได้รับข้อผิดพลาดในการเชื่อมต่อ เลือกเพื่อขยายรายละเอียด
1. เลือก **This was me** เพื่ออนุมัติการเชื่อมต่อ IMAP
1. ทดสอบ credential ของ n8n ของคุณอีกครั้ง

อ้างอิง [What is the Recent activity page?](https://support.microsoft.com/en-us/account-billing/what-is-the-recent-activity-page-23cf5556-4dbe-70da-82c8-bb3a8d8f8016){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการใช้หน้านี้

แหล่งที่มาของคำแนะนำเหล่านี้คือ [Outlook.com IMAP connection errors](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){:target=_blank .external-link} อ้างอิงเอกสารนั้นสำหรับข้อมูลเพิ่มเติม

## Use an app password

--8<-- "_snippets/integrations/builtin/credentials/email/outlook-app-password.md"
