---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
description: เรียก workflow จาก workflow อื่น และแบ่ง workflow ขนาดใหญ่เป็นส่วนย่อย
---

# Sub-workflows

คุณสามารถเรียก workflow หนึ่งจากอีก workflow หนึ่งได้ วิธีนี้ช่วยให้คุณสร้าง workflow แบบ modular หรือ microservice ได้ หรือถ้า workflow ใหญ่จนเจอ [memory issues](/hosting/scaling/memory-errors.md) ก็สามารถแยกเป็น sub-workflow ได้ การสร้าง sub-workflow ใช้ [Execute Workflow](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) และ [Execute Sub-workflow Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md) node

## Set up and use a sub-workflow

หัวข้อนี้จะอธิบายวิธีตั้งค่า parent workflow และ sub-workflow

--8<-- "_snippets/flow-logic/subworkflow-usage.md"

## How data passes between workflows

--8<-- "_snippets/flow-logic/subworkflow-data-flow.md"
