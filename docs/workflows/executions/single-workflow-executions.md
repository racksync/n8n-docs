---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: View and filter all executions for the workflow currently open on the canvas.
contentType: howto
---

# Workflow-level executions list

รายการ **Executions** ใน workflow จะแสดง executions ทั้งหมดสำหรับ workflow นั้น

/// note | Deleted workflows
เมื่อคุณลบ workflow, n8n จะลบประวัติ execution ของมันด้วย ซึ่งหมายความว่าคุณไม่สามารถดู executions สำหรับ workflows ที่ถูกลบได้
///

/// note | Execution history and workflow history
อย่าสับสนระหว่าง execution list กับ [Workflow history](/workflows/history.md)

Executions คือการรัน workflow ด้วย execution list คุณสามารถดูการรันก่อนหน้าของ workflow เวอร์ชันปัจจุบันได้ คุณสามารถคัดลอก executions ก่อนหน้าไปยัง editor เพื่อ [Debug and re-run past executions](/workflows/executions/debug.md) ใน workflow ปัจจุบันของคุณ

Workflow history คือเวอร์ชันก่อนหน้าของ workflow: ตัวอย่างเช่น เวอร์ชันที่มี node แตกต่างกัน หรือตั้งค่า parameters ต่างกัน
///

## View executions for a single workflow

ใน workflow ให้เลือกแท็บ **Executions** ในเมนูด้านบน คุณสามารถดูตัวอย่าง executions ทั้งหมดของ workflow นั้นได้

## Filter executions

คุณสามารถกรองรายการ executions ได้

1. ใน workflow ของคุณ เลือก **Executions**
2. เลือก **Filters**
3. ป้อนตัวกรองของคุณ คุณสามารถกรองตาม:
	* **Status**: เลือกจาก **Failed**, **Running**, **Success**, หรือ **Waiting**
	* **Execution start**: ดู executions ที่เริ่มต้นในเวลาที่กำหนด
	* **Saved custom data**: นี่คือข้อมูลที่คุณสร้างขึ้นภายใน workflow โดยใช้ Code node ป้อน key และ value เพื่อกรอง โปรดดู [Custom executions data](/workflows/executions/custom-executions-data.md) สำหรับข้อมูลเกี่ยวกับการเพิ่มข้อมูลแบบกำหนดเอง

		--8<-- "_snippets/workflows/executions/custom-execution-data-availability.md"

## Retry failed workflows

หาก workflow execution ของคุณล้มเหลว คุณสามารถลองรัน execution นั้นใหม่ได้ วิธีลองรัน workflow ที่ล้มเหลวใหม่:

1. เปิดรายการ **Executions**
2. สำหรับ workflow execution ที่คุณต้องการลองรันใหม่ ให้เลือก **Refresh** <span class="inline-image">![Refresh icon](/_images/common-icons/refresh.png){.off-glb}</span>
--8<-- "_snippets/workflows/executions/retry-options.md"
