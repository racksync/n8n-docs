---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

<!-- vale from-microsoft.We = NO -->
<!-- vale from-microsoft.FirstPerson = NO -->
# Exporting and importing workflows

ในบทนี้ คุณจะได้เรียนรู้วิธี export และ import workflows

## Exporting and importing workflows

คุณสามารถบันทึก n8n workflows ไว้ในเครื่องเป็นไฟล์ JSON ได้ ซึ่งมีประโยชน์หากคุณต้องการแชร์ workflow ของคุณกับคนอื่น หรือ import workflow จากคนอื่น

--8<-- "_snippets/workflows/sharing-credentials.md"

<figure><img src="/_images/courses/level-one/chapter-six/l1-c6-import-export-menu.png" alt="Import/Export menu" style="width:100%"><figcaption align = "center"><i>Import & Export workflows menu</i></figcaption></figure>

คุณสามารถ export และ import workflows ได้สามวิธี:

* From the **Editor UI** menu:
    * Export: จากแถบนำทางด้านบน เลือกจุดสามจุดที่มุมขวาบน จากนั้นเลือก **Download** การดำเนินการนี้จะดาวน์โหลด workflow ปัจจุบันของคุณเป็นไฟล์ JSON ลงในคอมพิวเตอร์ของคุณ
    * Import: จากแถบนำทางด้านบน เลือกจุดสามจุดที่มุมขวาบน จากนั้นเลือก **Import from URL** (เพื่อ import workflow ที่เผยแพร่แล้ว) หรือ **Import from File** (เพื่อ import workflow เป็นไฟล์ JSON)
* From the **Editor UI** canvas:
	* Export: เลือก nodes ทั้งหมดบน canvas และใช้ ++ctrl+c++ เพื่อคัดลอก workflow JSON คุณสามารถวางสิ่งนี้ลงในไฟล์หรือแชร์โดยตรงกับผู้อื่นได้
	* Import: คุณสามารถวาง workflow JSON ที่คัดลอกมาลงใน canvas ได้โดยตรงด้วย ++ctrl+v++
* From the command line:
    * Export: ดู [full list of commands ](/hosting/cli-commands.md) สำหรับการ export workflows หรือ credentials
    * Import: ดู [full list of commands ](/hosting/cli-commands.md#import-workflows-and-credentials) สำหรับการ import workflows หรือ credentials
