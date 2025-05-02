---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Manual Trigger node documentation
description: Learn how to use the Manual Trigger node in n8n. Follow technical documentation to integrate Manual Trigger node into your workflows.
contentType: [integration, reference]
priority: critical
---

# Manual Trigger node

ใช้ node นี้ถ้าคุณต้องการเริ่ม workflow ด้วยการเลือก **Test Workflow** และไม่ต้องการให้ workflow ทำงานอัตโนมัติ

workflow ทุกอันต้องมี trigger หรือจุดเริ่มต้น ส่วนใหญ่ workflow จะเริ่มด้วย trigger node ที่ตอบสนองต่อ event ภายนอก หรือ [Schedule Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/index.md) ที่ตั้งเวลาไว้

Manual Trigger node ใช้เป็น trigger สำหรับ workflow ที่ไม่ต้องการ trigger อัตโนมัติ

ใช้ trigger นี้เมื่อ:

* ต้องการทดสอบ workflow ก่อนจะเพิ่ม trigger อัตโนมัติ
* ไม่ต้องการให้ workflow ทำงานเองอัตโนมัติ

## Common issues

ปัญหาที่พบบ่อยเกี่ยวกับ Manual Trigger node และวิธีแก้ไข

<!-- vale off -->
### Only one 'Manual Trigger' node is allowed in a workflow
<!-- vale on -->

ถ้าคุณพยายามเพิ่ม Manual Trigger node ใน workflow ที่มีอยู่แล้ว จะขึ้น error นี้

ให้ลบ Manual Trigger เดิมออก หรือแก้ workflow ให้เชื่อมต่อ trigger นั้นกับ node อื่น
