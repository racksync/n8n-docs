ตัวอย่างเช่น สมมติว่าคุณมี Execute Sub-workflow node ใน **Workflow A** Execute Sub-workflow node นี้จะเรียก workflow อื่นที่ชื่อว่า **Workflow B**:

1. Execute Sub-workflow node ส่งข้อมูลไปยัง Execute Sub-workflow Trigger node (มีชื่อว่า "When executed by another node" ใน canvas) ของ **Workflow B**
2. node สุดท้ายของ **Workflow B** ส่งข้อมูลกลับไปยัง Execute Sub-workflow node ใน **Workflow A**
