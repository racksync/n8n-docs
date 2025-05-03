---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เพิ่มความปลอดภัยให้ task runners
description: "เพิ่มความปลอดภัยให้ task runners เพื่อ isolation ที่ดีขึ้นสำหรับ n8n instance ที่คุณโฮสต์เอง"
contentType: howto
---

# Hardening task runners

[Task runners](/hosting/configuration/task-runners.md) มีหน้าที่รันโค้ดจาก [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md) ถึงแม้ Code node จะรันอย่างปลอดภัยอยู่แล้ว แต่คุณสามารถทำตามคำแนะนำนี้เพื่อเพิ่มความปลอดภัยให้ task runners ได้อีก

## Run task runners as sidecars in external mode

เพื่อเพิ่ม isolation ระหว่าง core n8n process กับโค้ดใน Code node ให้รัน task runners แบบ [external mode](/hosting/configuration/task-runners.md#setting-up-external-mode) ซึ่งจะ launch เป็น container แยกต่างหาก ทำให้โค้ด JavaScript ที่รันใน Code node ถูกแยกออกจากกันอย่างสมบูรณ์
