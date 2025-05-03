---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Onfleet Trigger node
description: วิธีใช้ Onfleet Trigger node ใน n8n เพื่อเชื่อมต่อ Onfleet กับ workflow ของคุณ
contentType: [integration, reference]
---

# Onfleet Trigger node

[Onfleet](https://onfleet.com/){:target=_blank .external-link} คือแพลตฟอร์มด้านโลจิสติกส์ที่ให้บริการโซลูชันสำหรับการจัดส่งระยะสุดท้าย (last-mile delivery)

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อ (authentication) สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/onfleet.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ workflow template เพื่อเริ่มต้นใช้งาน ดูได้ที่หน้า [Onfleet Trigger integrations](https://n8n.io/integrations/onfleet-trigger/){:target=_blank .external-link} ของ n8n
///

## Events

Trigger workflow เมื่อเกิดเหตุการณ์เหล่านี้:

* SMS recipient opt out
* SMS recipient response missed
* Task arrival
* Task assigned
* Task cloned
* Task completed
* Task created
* Task delayed
* Task ETA
* Task failed
* Task started
* Task unassigned
* Task updated
* Worker created
* Worker deleted
* Worker duty

