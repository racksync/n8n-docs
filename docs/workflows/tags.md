---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Workflow tags
description: Use tags to label workflows, making it easier to browse your workflows.
contentType: howto
---

# Tags

Workflow tags ช่วยให้คุณสามารถติดป้ายกำกับ workflows ของคุณได้ จากนั้นคุณสามารถกรอง workflows ตาม tag ได้

Tags เป็นแบบ global ซึ่งหมายความว่าเมื่อคุณสร้าง tag ขึ้นมา tag นั้นจะพร้อมใช้งานสำหรับผู้ใช้ทุกคนใน n8n instance ของคุณ

## Add a tag to a workflow

วิธีเพิ่ม tag ให้กับ workflow ของคุณ:

1. ใน workflow ของคุณ เลือก **+ Add tag**
2. เลือก tag ที่มีอยู่ หรือป้อนชื่อ tag ใหม่
3. เมื่อคุณเลือก tag และคลิกออกจาก tag modal แล้ว n8n จะแสดง tag ถัดจากชื่อ workflow

คุณสามารถเพิ่มได้มากกว่าหนึ่ง tag

## Filter by tag

เมื่อเรียกดู workflows ใน instance ของคุณ คุณสามารถกรองตาม tag ได้

1. ในหน้า **Workflows** เลือก **Filters**
2. เลือก **Tags**
3. เลือก tag หรือ tags ที่คุณต้องการกรอง n8n จะแสดงรายการ workflows ที่มี tag นั้น

## Manage tags

คุณสามารถแก้ไข tags ที่มีอยู่ได้ Instance owners สามารถลบ tags ได้

1. เลือก **Manage tags** ตัวเลือกนี้มีให้จาก **Filters** > **Tags** ในหน้า **Workflows** หรือใน **+ Add tag** modal ใน workflow ของคุณ
2. วางเมาส์เหนือ tag ที่คุณต้องการเปลี่ยนแปลง
3. เลือก **Edit** <span class="inline-image">![Add node icon](/_images/common-icons/edit.png){.off-glb}</span> เพื่อเปลี่ยนชื่อ หรือ **Delete** <span class="inline-image">![Add node icon](/_images/common-icons/delete.png){.off-glb}</span> เพื่อลบ

/// warning | Global tags
Tags เป็นแบบ global หากคุณแก้ไขหรือลบ tag การเปลี่ยนแปลงนี้จะมีผลกับผู้ใช้ทุกคนใน n8n instance ของคุณ
///
