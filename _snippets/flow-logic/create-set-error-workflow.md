1. สร้าง workflow ใหม่ โดยมี Error Trigger เป็น node แรก
2. ตั้งชื่อ workflow ตัวอย่างเช่น `Error Handler`
3. เลือก **Save**
4. ใน workflow ที่คุณต้องการใช้ error workflow นี้:
	1. เลือก **Options** <span class="inline-image">![Options menu icon](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span> > **Settings**
	2. ใน **Error workflow** เลือก workflow ที่คุณเพิ่งสร้าง ตัวอย่างเช่น หากคุณใช้ชื่อ Error Handler ให้เลือก **Error handler**
	3. เลือก **Save**
	ตอนนี้ เมื่อ workflow นี้เกิด error, error workflow ที่เกี่ยวข้องจะทำงาน
