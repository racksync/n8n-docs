---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: แบ่ง workflow เป็นหลายเส้นทางด้วย If และ Switch
contentType: howto
---

# Splitting workflows with conditional nodes

Splitting ใช้ [IF](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) หรือ [Switch](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md) node เพื่อแยก workflow จากเส้นทางเดียวให้เป็นหลายเส้นทาง เหมาะกับการสร้าง logic ที่ซับซ้อนใน n8n

ลองดูตัวอย่าง workflow เหล่านี้:

!["Diagram representing two workflows. One has three steps and follows a linear process, with a user submitting a bug, and the workflow emailing a support team. The second workflow starts the same way, but then splits depending on whether the user marked the issue as urgent. It then splits again depending on the user's support plan"](/_images/flow-logic/splitting/single-multi-branch-workflow.png)

นี่คือจุดเด่นของการ splitting และการใช้ conditional node ใน n8n

ดูรายละเอียดการใช้งานได้ที่ [IF](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) หรือ [Switch](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md)
