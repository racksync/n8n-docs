---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Figma Trigger (Beta) node
description: วิธีใช้ Figma Trigger node ใน n8n พร้อมตัวอย่าง workflow
contentType: [integration, reference]
---

# Figma Trigger (Beta) node

[Figma](https://www.figma.com/){:target=_blank .external-link} เป็นเครื่องมือสำหรับออกแบบ prototype ที่เน้นการใช้งานผ่านเว็บ และมีแอปสำหรับ macOS กับ Windows เพื่อใช้งานแบบออฟไลน์ได้มากขึ้น

/// warning | Supported Figma Plans
Figma ไม่รองรับ webhook บนแผนฟรี "Starter" ทีมของคุณต้องใช้แผน "Professional" ขึ้นไปถึงจะใช้ node นี้ได้
///

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/figma.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template เพื่อช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [Figma Trigger integrations ของ n8n](https://n8n.io/integrations/figma-trigger-beta/){:target=_blank .external-link}
///

## Events

- **File Commented**: แจ้งเตือนเมื่อมีคนคอมเมนต์ในไฟล์
- **File Deleted**: แจ้งเตือนเมื่อมีคนลบไฟล์เดี่ยว (ไม่แจ้งเตือนถ้าลบทั้งโฟลเดอร์)
- **File Updated**: แจ้งเตือนเมื่อมีการบันทึกหรือการลบไฟล์ การบันทึกจะเกิดขึ้นเมื่อมีคนปิดไฟล์หลังจากแก้ไขภายใน 30 วินาที
- **File Version Updated**: แจ้งเตือนเมื่อมีการสร้าง named version ในประวัติไฟล์
- **Library Publish**: แจ้งเตือนเมื่อมีการ publish library file

