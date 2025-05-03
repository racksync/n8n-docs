---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
description: วิธีจัดการ execution error
---

# Error handling

เวลาคุณออกแบบ flow logic ควรคิดถึงกรณี error และเตรียมวิธีรับมือไว้ด้วย ด้วย error workflow คุณสามารถควบคุมได้ว่า n8n จะทำอะไรเมื่อ workflow execution ล้มเหลว

/// note | Investigating errors
ถ้าต้องการตรวจสอบ execution ที่ล้มเหลว คุณสามารถ:

* ดู [Executions](/workflows/executions/index.md) ของ [workflow เดียว](/workflows/executions/single-workflow-executions.md) หรือ [ทุก workflow ที่คุณเข้าถึงได้](/workflows/executions/all-executions.md) คุณสามารถ [โหลดข้อมูลจาก execution ก่อนหน้า](/workflows/executions/debug.md) มาใช้ใน workflow ปัจจุบันได้
* เปิดใช้ [Log streaming](/log-streaming.md)
///

## Create and set an error workflow

แต่ละ workflow สามารถตั้ง error workflow ได้ใน **Workflow Settings** ถ้า execution ล้มเหลว error workflow จะถูกรัน เช่น คุณอาจตั้งให้ส่ง email หรือ Slack alert เมื่อ workflow error โดย error workflow ต้องเริ่มด้วย [Error Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md)

คุณสามารถใช้ error workflow เดียวกับหลาย workflow ก็ได้

--8<-- "_snippets/flow-logic/create-set-error-workflow.md"

## Error data

--8<-- "_snippets/integrations/builtin/core-nodes/error-trigger/error-data.md"

## Cause a workflow execution failure using Stop And Error

เมื่อคุณสร้างและตั้ง error workflow แล้ว n8n จะรัน workflow นี้เมื่อ execution ล้มเหลว ปกติจะเกิดจาก error ใน node หรือ workflow ใช้ memory เกิน

คุณสามารถเพิ่ม [Stop And Error](/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md) node ใน workflow เพื่อบังคับให้ execution ล้มเหลวตามเงื่อนไขที่คุณกำหนด และ trigger error workflow
