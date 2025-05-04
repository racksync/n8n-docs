วิธีการ push งานไปยัง Git:

1. เลือก **Push** <span class="inline-image">![Push icon](/_images/source-control-environments/push-icon.png){.off-glb}</span> ในเมนูหลัก

	--8<-- "_snippets/source-control-environments/push-pull-menu-state.md"

1. ใน modal **Commit and push changes** ให้เลือก workflows ที่คุณต้องการ push คุณสามารถกรองตามสถานะ (new, modified, deleted) และค้นหา workflows ได้ n8n จะ push tags, และ variable และ credential stubs โดยอัตโนมัติ
1. ป้อน commit message ซึ่งควรเป็นคำอธิบายหนึ่งประโยคเกี่ยวกับการเปลี่ยนแปลงที่คุณทำ
1. เลือก **Commit and Push** n8n จะส่งงานไปยัง Git และแสดงข้อความแจ้งความสำเร็จเมื่อเสร็จสิ้น
