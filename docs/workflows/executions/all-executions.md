---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: View and filter all executions for all workflows.
contentType: howto
---

# All executions

หากต้องการดู **all executions** จาก n8n instance ให้ไปที่หน้า **Overview** แล้วคลิกเข้าไปที่แท็บ Executions ซึ่งจะแสดง executions ทั้งหมดจาก workflows ที่คุณมีสิทธิ์เข้าถึง

หาก n8n instance ของคุณรองรับ **projects** คุณจะสามารถดูแท็บ executions ภายใน projects ที่คุณมีสิทธิ์เข้าถึงได้ด้วย ซึ่งจะแสดงเฉพาะ executions จาก workflows ภายใน project ที่ระบุ

/// note | Deleted workflows
เมื่อคุณลบ workflow, n8n จะลบประวัติ execution ของมันด้วย ซึ่งหมายความว่าคุณไม่สามารถดู executions สำหรับ workflows ที่ถูกลบได้
///

## Filter executions

คุณสามารถกรองรายการ executions ได้:

1. เลือกแท็บ **Executions** จากภายในหน้า **Overview** หรือ **project** ที่ต้องการ เพื่อเปิดรายการ
2. เลือก **Filters**
3. ป้อนตัวกรองของคุณ คุณสามารถกรองตาม:
	* **Workflows**: เลือก workflows ทั้งหมด หรือชื่อ workflow ที่ต้องการ
	* **Status**: เลือกจาก **Failed**, **Running**, **Success**, หรือ **Waiting**
	* **Execution start**: ดู executions ที่เริ่มต้นในเวลาที่กำหนด
	* **Saved custom data**: นี่คือข้อมูลที่คุณสร้างขึ้นภายใน workflow โดยใช้ Code node ป้อน key และ value เพื่อกรอง โปรดดู [Custom executions data](/workflows/executions/custom-executions-data.md) สำหรับข้อมูลเกี่ยวกับการเพิ่มข้อมูลแบบกำหนดเอง

--8<-- "_snippets/workflows/executions/custom-execution-data-availability.md"

## Retry failed workflows

หาก workflow execution ของคุณล้มเหลว คุณสามารถลองรัน execution นั้นใหม่ได้ วิธีลองรัน workflow ที่ล้มเหลวใหม่:

1. เลือกแท็บ **Executions** จากภายในหน้า **Overview** หรือ **project** ที่ต้องการ เพื่อเปิดรายการ
2. ใน execution ที่คุณต้องการลองรันใหม่ ให้เลือก **Retry execution** <span class="inline-image">![Options menu icon](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span>
--8<-- "_snippets/workflows/executions/retry-options.md"

## Load data from previous executions into your current workflow

คุณสามารถโหลดข้อมูลจาก workflow ก่อนหน้ากลับเข้ามาใน canvas ได้ โปรดดู [Debug executions](/workflows/executions/debug.md) สำหรับข้อมูลเพิ่มเติม
