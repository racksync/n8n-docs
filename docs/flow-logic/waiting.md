---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: การรอ
description: วิธีทำให้ workflow execution รอ
contentType: howto
---

# Waiting

Waiting คือการหยุด workflow ชั่วคราวระหว่าง execution แล้ว resume ต่อจากจุดเดิมพร้อมข้อมูลเดิม เหมาะกับกรณีที่ต้องการ rate limit การเรียก service หรือรอ event ภายนอกเสร็จสิ้น คุณสามารถรอเป็นระยะเวลาที่กำหนด หรือรอจน webhook ถูกเรียกก็ได้

การทำให้ workflow รอ ใช้ [Wait](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md) node ดูรายละเอียดการใช้งานได้ที่เอกสาร node

n8n มี workflow template ตัวอย่าง [Rate limiting and waiting for external events](https://n8n.io/workflows/1749-rate-limiting-and-waiting-for-external-events/){:target=_blank .external-link}
