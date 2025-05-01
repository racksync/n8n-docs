---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: KoboToolbox Trigger node documentation
description: Learn how to use the KoboToolbox Trigger node in n8n. Follow technical documentation to integrate KoboToolbox Trigger node into your workflows.
contentType: [integration, reference]
---

# KoboToolbox Trigger node

[KoboToolbox](https://www.kobotoolbox.org/){:target=_blank .external-link} เป็นเครื่องมือสำหรับสำรวจภาคสนามและเก็บข้อมูล ช่วยให้คุณออกแบบฟอร์มแบบ interactive ที่สามารถกรอกแบบออฟไลน์ผ่านมือถือได้ มีทั้งแบบ cloud ฟรีและ self-hosted

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/kobotoolbox.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่จะช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [KoboToolbox Trigger integrations](https://n8n.io/integrations/kobotoolbox-trigger/){:target=_blank .external-link} ของ n8n
///

node นี้จะเริ่ม workflow เมื่อมี submission ใหม่ในฟอร์มที่กำหนด ตัว trigger จะจัดการสร้าง/ลบ webhook ให้อัตโนมัติ คุณไม่ต้องตั้งค่าอะไรใน KoboToolbox เพิ่มเติม

การทำงานจะเหมือนกับ operation Get Submission ใน [KoboToolbox](/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox.md) node รวมถึงรองรับตัวเลือกการจัดรูปแบบข้อมูลแบบเดียวกันด้วย
