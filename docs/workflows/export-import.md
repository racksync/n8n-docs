---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Export และ import workflows
description: วิธีต่างๆ ในการ export และ import workflows ใน n8n
contentType: howto
---

# Export and import workflows

n8n บันทึก workflows ในรูปแบบ JSON คุณสามารถ export workflows ของคุณเป็นไฟล์ JSON หรือ import ไฟล์ JSON เข้าสู่ n8n library ของคุณได้
คุณสามารถ export และ import workflows ได้หลายวิธี

--8<-- "_snippets/workflows/sharing-credentials.md"

## Copy-Paste

คุณสามารถคัดลอกและวาง workflow หรือบางส่วนของมันได้โดยการเลือก nodes ที่คุณต้องการคัดลอกไปยังคลิปบอร์ด (`Ctrl + c` หรือ `cmd +c`) และวาง (`Ctrl + v` หรือ `cmd + v`) ลงใน Editor UI

ในการเลือก nodes ทั้งหมดหรือกลุ่มของ nodes ให้คลิกและลาก:
  ![Select a group of nodes](/_images/workflows/export-import/selectingnodes.gif)

## From the Editor UI menu

จากแถบนำทางด้านบน เลือกจุดสามจุดที่มุมขวาบน <img alt="Workflow menu icon" class="off-glb" src="/_images/common-icons/three-dots-horizontal.png"> เพื่อดูตัวเลือกต่อไปนี้:

<figure><img src="/_images/courses/level-one/chapter-six/l1-c6-import-export-menu.png" alt="Import/Export menu" style="width:100%"><figcaption align = "center"><i>Import & Export workflows menu</i></figcaption></figure>

* **Download**: ดาวน์โหลด workflow ปัจจุบันของคุณเป็นไฟล์ JSON ลงในคอมพิวเตอร์ของคุณ
* **Import from URL**: นำเข้า workflow JSON จาก URL ตัวอย่างเช่น [ไฟล์ workflow JSON นี้บน GitHub](https://raw.githubusercontent.com/n8n-io/demo-setup/main/n8n/backup/workflows/srOnR8PAY3u4RSwb.json){:target=_blank .external-link}
* **Import from File**: นำเข้า workflow เป็นไฟล์ JSON จากคอมพิวเตอร์ของคุณ

## From the command line

* Export: ดู [รายการคำสั่งทั้งหมด](/hosting/cli-commands.md#export-workflows-and-credentials){:target="_blank" .external} สำหรับการ export workflows หรือ credentials
* Import: ดู [รายการคำสั่งทั้งหมด](/hosting/cli-commands.md#import-workflows-and-credentials){:target="_blank" .external} สำหรับการ import workflows หรือ credentials