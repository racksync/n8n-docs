---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Clockify Trigger node
description: วิธีใช้ Clockify Trigger node ใน n8n พร้อมตัวอย่าง workflow
contentType: [integration, reference]
---

# Clockify Trigger node

[Clockify](https://clockify.me/){:target=_blank .external-link} เป็นแอป time tracker และ timesheet ฟรี สำหรับติดตามเวลาทำงานในแต่ละโปรเจกต์

/// note | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/clockify.md)
///

///  note  | Examples and templates
ถ้าต้องการดูตัวอย่างการใช้งานและ workflow template เพื่อเริ่มต้นใช้งาน ลองดูที่หน้า [Clockify Trigger integrations](https://n8n.io/integrations/clockify-trigger/){:target=_blank .external-link} ของ n8n ได้เลย
///

node นี้จะใช้ timezone ที่ตั้งไว้ใน workflow เพื่อกำหนดช่วงเวลาเริ่มต้นของ time entry ถ้าต้องการให้ trigger node นี้ดึงข้อมูล time entry ได้ถูกต้อง ให้ตั้งค่า timezone ใน [Workflow Settings](/workflows/settings.md)
