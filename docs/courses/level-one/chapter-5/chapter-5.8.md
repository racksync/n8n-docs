---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

<!-- vale from-microsoft.We = NO -->
<!-- vale from-microsoft.FirstPerson = NO -->
# 8. Activating and Examining the Workflow

ในขั้นตอนนี้ของ workflow คุณจะได้เรียนรู้วิธี activate workflow ของคุณและเปลี่ยน default workflow settings

การ activate workflow หมายความว่ามันจะทำงานโดยอัตโนมัติทุกครั้งที่ trigger node ได้รับ input หรือตรงตามเงื่อนไข โดยค่าเริ่มต้น workflows ที่สร้างขึ้นใหม่ทั้งหมดจะเริ่มต้นในสถานะ deactivated

หากต้องการ activate workflow ของคุณ ให้ตั้งค่า toggle **Inactive** ในแถบนำทางด้านบนของ Editor UI เป็น **Activated** ตอนนี้ workflow ของ Nathan จะถูก εκτέλεση (execute) โดยอัตโนมัติทุกวันจันทร์ เวลา 9.00 น.:

<figure><img src="/_images/courses/level-one/chapter-five/l1-c5-5-8-activated-workflow.png" alt="Activated workflow" style="width:100%"><figcaption align = "center"><i>Activated workflow</i></figcaption></figure>

## Workflow Executions

execution หมายถึงการรัน workflow ที่เสร็จสมบูรณ์ ตั้งแต่ node แรกจนถึง node สุดท้าย n8n จะบันทึก workflow executions ซึ่งช่วยให้คุณเห็นว่า workflow สำเร็จหรือไม่ execution log มีประโยชน์สำหรับการ debugging workflow ของคุณและดูว่าขั้นตอนใดที่เกิดปัญหา

หากต้องการดู executions สำหรับ workflow ที่เฉพาะเจาะจง คุณสามารถสลับไปที่แท็บ **Executions** เมื่อ workflow เปิดอยู่บน canvas ใช้แท็บ **Editor** เพื่อสลับกลับไปยัง node editor

หากต้องการดู execution log สำหรับ n8n instance ทั้งหมด ใน Editor UI ของคุณ ให้เลือก **Overview** จากนั้นเลือกแท็บ **Executions** ใน main panel

<figure><img src="/_images/courses/level-one/chapter-five/l1-c5-5-8-execution-list.png" alt="Execution List" style="width:100%"><figcaption align = "center"><i>Execution List</i></figcaption></figure>

หน้าต่าง **Executions** จะแสดงตารางพร้อมข้อมูลต่อไปนี้:

- **Name**: The name of the workflow
- **Started At**: The date and time when the workflow started
- **Status**: The status of the workflow (Waiting, Running, Succeeded, Cancelled, or Failed) and the amount of time it took the workflow to execute
- **Execution ID**: The ID of this workflow execution

/// note | Workflow execution status
คุณสามารถกรอง **Executions** ที่แสดงตาม workflow และตาม status (**Any Status**, **Failed**, **Cancelled**, **Running**, **Success**, หรือ **Waiting**)
ข้อมูลที่แสดงที่นี่ขึ้นอยู่กับว่าคุณกำหนดค่า executions ใดให้บันทึกใน [**Workflow Settings**](/workflows/settings.md)
///


## Workflow Settings

คุณสามารถปรับแต่ง workflows และ executions ของคุณ หรือเขียนทับ global default settings บางอย่างได้ใน [**Workflow Settings**](/workflows/settings.md)

เข้าถึง settings เหล่านี้ได้โดยเลือกจุดสามจุดที่มุมขวาบนของ Editor UI เมื่อ workflow เปิดอยู่บน canvas จากนั้นเลือก **Settings**

<figure><img src="/_images/courses/level-one/chapter-five/l1-c5-5-8-workflow-settings.png" alt="Workflow Settings" style="width:100%"><figcaption align = "center"><i>Workflow Settings</i></figcaption></figure>

ในหน้าต่าง **Workflow Settings** คุณสามารถกำหนดค่า settings ต่อไปนี้ได้:

- **Execution Order**: Choose the execution logic for multi-branch workflows. You should leave this set to `v1` if you don't have workflows that rely on the legacy execution ordering.
- [**Error Workflow**](/flow-logic/error-handling.md): A workflow to run if the execution of the current workflow fails.
- **This workflow can be called by**: Workflows allowed to call this workflow using the [Execute Sub-workflow node](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md).
- **Timezone**: The timezone to use in the current workflow. If not set, the global timezone. In particular, this setting is important for the [Schedule Trigger node](/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/index.md), as you want to make sure that the workflow gets executed at the right time.
- **Save failed production executions**: If n8n should save the Execution data of the workflow when it fails. Default is to save.
- **Save successful production executions**: If n8n should save the Execution data of the workflow when it succeeds. Default is to save.
- **Save manual executions**: If n8n should save executions started from the Editor UI. Default is to save.
- **Save execution progress**: If n8n should save the execution data of each node. If set to Save, you can resume the workflow from where it stopped in case of an error, though keep in mind that this might make the execution slower. Default is to not save.
- **Timeout Workflow**: Whether to cancel a workflow execution after a specific period of time. Default is to not timeout.


## What's next?

**You 👩‍🔧**: แค่นั้นแหละ! ตอนนี้คุณมี workflow 7-node ที่จะทำงานโดยอัตโนมัติทุกเช้าวันจันทร์ คุณไม่ต้องกังวลเกี่ยวกับการจำต้องจัดการข้อมูลอีกต่อไป แต่คุณสามารถเริ่มต้นสัปดาห์ของคุณด้วยงานที่มีความหมายหรือน่าตื่นเต้นมากขึ้น

**Nathan 🙋**: workflow นี้น่าเหลือเชื่อมาก ขอบคุณ! แล้วต่อไปคุณจะทำอะไร?

**You 👩‍🔧**: ฉันอยากจะสร้าง workflows เพิ่มเติม แชร์ให้คนอื่น และใช้ workflows บางส่วนที่คนอื่นสร้างขึ้น
