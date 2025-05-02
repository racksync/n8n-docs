---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Workflow 3: Monitoring workflow errors

สุดท้ายแต่ไม่ท้ายสุด มาช่วย Nathan ให้รู้ว่ามี errors ใดๆ เกิดขึ้นในการรัน workflow หรือไม่

เพื่อให้งานนี้สำเร็จ ให้สร้าง Error workflow ที่ monitor main workflow:

1. สร้าง workflow ใหม่
2. เพิ่ม **Error Trigger node** (และ execute เพื่อทดสอบ)
3. เชื่อมต่อ **Discord node** เข้ากับ **Error Trigger node** และกำหนดค่า fields เหล่านี้:<br/>

	* **Webhook URL**: Discord URL ที่คุณได้รับในอีเมลจาก n8n เมื่อคุณลงทะเบียนสำหรับคอร์สนี้
	* **Text**: "The workflow `{workflow name}` failed, with the error message: `{execution error message}`. Last node executed: `{name of the last executed node}`. Check this workflow execution here: `{execution URL}` My Unique ID: " ตามด้วย unique ID ที่ส่งให้คุณทางอีเมลเมื่อคุณลงทะเบียนสำหรับคอร์สนี้

		โปรดทราบว่าคุณต้องแทนที่ข้อความในวงเล็บปีกกา `{}` ด้วย expressions ที่ดึงข้อมูลที่เกี่ยวข้องจาก Error Trigger node<br/>

4. Execute Discord node
5. ตั้งค่า workflow ที่สร้างขึ้นใหม่ให้เป็น **Error Workflow** สำหรับ main workflow ที่คุณสร้างในบทเรียนก่อนหน้า

workflow ควรมีลักษณะดังนี้:

<figure><img src="/_images/courses/level-two/chapter-five/workflow3.png" alt="Workflow 3 for monitoring workflow errors" style="width:100%"><figcaption align = "center"><i>Workflow 3 for monitoring workflow errors</i></figcaption></figure>

/// question | Quiz questions
* **Error Trigger node** คืนค่า fields อะไรบ้าง?
* **Error Trigger node** คืนค่าข้อมูลอะไรเกี่ยวกับ execution?
* **Error Trigger node** คืนค่าข้อมูลอะไรเกี่ยวกับ workflow?
* expression สำหรับอ้างอิง workflow name คืออะไร?
///
