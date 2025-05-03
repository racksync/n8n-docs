---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการใช้งาน Autopilot Trigger node
description: วิธีใช้ Autopilot Trigger node กับ n8n สำหรับเชื่อมต่อและเริ่ม workflow อัตโนมัติ
contentType: [integration, reference]
---

# Autopilot Trigger node

[Autopilot](https://www.autopilothq.com/){:target=_blank .external-link} เป็นซอฟต์แวร์การตลาดแบบ visual ที่ช่วยให้คุณ automate และ personalize การตลาดตลอด customer journey

/// note | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/autopilot.md)
///

///  note  | Examples and templates
ถ้าต้องการดูตัวอย่างการใช้งานและ workflow template เพื่อเริ่มต้นใช้งาน ลองดูที่หน้า [Autopilot Trigger integrations](https://n8n.io/integrations/autopilot-trigger/){:target=_blank .external-link} ของ n8n ได้เลย
///

## Events

- Contact added
- Contact added to a list
- Contact entered to a segment
- Contact left a segment
- Contact removed from a list
- Contact unsubscribed
- Contact updated
