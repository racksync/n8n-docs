---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Methods ที่ช่วยให้ทำงานทั่วไปใน expressions ได้ง่ายขึ้น
contentType: reference
hide:
  - toc
---

# HTTP node variables

Variables สำหรับการทำงานกับ requests และ responses ของ HTTP node เมื่อใช้ pagination

โปรดดู [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) สำหรับคำแนะนำในการใช้ HTTP node รวมถึงการกำหนดค่า pagination

โปรดดู [HTTP Request node cookbook | Pagination](/code/cookbook/http-node/pagination.md) สำหรับตัวอย่างการกำหนดค่า pagination

/// note | HTTP node only
Variables เหล่านี้ใช้สำหรับ expressions ใน HTTP node เท่านั้น คุณไม่สามารถใช้ใน node อื่นๆ ได้
///
--8<-- "_snippets/integrations/builtin/core-nodes/http/pagination-variables.md"
