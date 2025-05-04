## การทำงานของ Node: Triggers และ Actions (Node operations: Triggers and Actions)

เมื่อคุณเพิ่ม node เข้าไปใน workflow, n8n จะแสดงรายการ operations ที่มีอยู่ operation คือสิ่งที่ node ทำ เช่น การรับหรือส่งข้อมูล

มี operation สองประเภท:

*   Triggers เริ่มต้น workflow เพื่อตอบสนองต่อเหตุการณ์หรือเงื่อนไขเฉพาะในบริการของคุณ เมื่อคุณเลือก Trigger, n8n จะเพิ่ม trigger node เข้าไปใน workflow ของคุณ โดยมี Trigger operation ที่คุณเลือกไว้ล่วงหน้า เมื่อคุณค้นหา node ใน n8n, Trigger operations จะมีไอคอนรูปสายฟ้า <span class="inline-image">![Trigger icon](/_images/common-icons/trigger.png){.off-glb}</span>
*   Actions คือ operations ที่แทนงานเฉพาะภายใน workflow ซึ่งคุณสามารถใช้เพื่อจัดการข้อมูล, ดำเนินการกับระบบภายนอก, และกระตุ้นเหตุการณ์ในระบบอื่น ๆ ซึ่งเป็นส่วนหนึ่งของ workflows ของคุณ เมื่อคุณเลือก Action, n8n จะเพิ่ม node เข้าไปใน workflow ของคุณ โดยมี Action operation ที่คุณเลือกไว้ล่วงหน้า
