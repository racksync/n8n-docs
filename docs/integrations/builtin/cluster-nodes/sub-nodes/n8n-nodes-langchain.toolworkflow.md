---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Call n8n Workflow Tool node documentation
description: Learn how to use the Call n8n Workflow Tool node in n8n. Follow technical documentation to integrate Call n8n Workflow Tool node into your workflows.
contentType: [integration, reference]
priority: high
---

# Call n8n Workflow Tool node

Call n8n Workflow Tool node เป็น [tool](/glossary.md#ai-tool) ที่ช่วยให้ [agent](/glossary.md#ai-agent) สามารถรัน workflow อื่นใน n8n และดึงข้อมูล output ของ workflow นั้นมาใช้งานได้

ในหน้านี้จะมี parameter ของ node Call n8n Workflow Tool และลิงก์ไปยัง resource อื่นๆ

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

### Description

ใส่คำอธิบาย custom code ของคุณ ตรงนี้จะช่วยบอก agent ว่าควรใช้ tool นี้เมื่อไหร่ เช่น

> Call this tool to get a random color. The input should be a string with comma separated names of colors to exclude.

### Source

บอก n8n ว่าจะเรียก workflow ไหน คุณเลือกได้ระหว่าง:

* **Database** เพื่อเลือก workflow จากลิสต์หรือกรอก workflow ID
* **Define Below** แล้ว copy [workflow JSON](/workflows/export-import.md) มาใส่

### Workflow Inputs

ถ้าใช้ **Database** เป็น workflow source หลังจากเลือก sub-workflow (และกำหนด **Workflow Input Schema** ใน sub-workflow) คุณจะสามารถกำหนด **Workflow Inputs** ได้

กดปุ่ม **Refresh** เพื่อดึง input field จาก sub-workflow

คุณสามารถกำหนดค่า input ของ workflow ได้หลายวิธี เช่น

* กำหนดค่าแบบ fix
* ใช้ expression เพื่ออ้างอิงข้อมูลจาก workflow ปัจจุบัน
* [ให้ AI model กำหนด parameter](/advanced-ai/examples/using-the-fromai-function.md) โดยกดปุ่ม AI ด้านขวาของช่อง
* ใช้ [`$fromAI()` function](/advanced-ai/examples/using-the-fromai-function.md#use-the-fromai-function) ใน expression เพื่อควบคุมวิธีที่ model เติมข้อมูล หรือผสม input ที่ AI สร้างกับ input อื่น

ถ้าต้องการอ้างอิงข้อมูลจาก workflow ปัจจุบัน ให้ลาก field จาก input panel ไปยังช่องที่เปิด Expression mode

ถ้าอยากเริ่มใช้ `$fromAI()` function ให้กดปุ่ม "Let the model define this parameter" ด้านขวาของช่อง แล้วใช้ปุ่ม **X** เพื่อกลับไปใช้ค่าที่ผู้ใช้กำหนดเอง ช่องจะเปลี่ยนเป็น expression field ที่มี `$fromAI()` expression อยู่แล้ว คุณสามารถปรับแต่ง expression นี้ต่อได้ตามต้องการ

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'workflow-tool') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/cluster-nodes/tools-link.md"

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
