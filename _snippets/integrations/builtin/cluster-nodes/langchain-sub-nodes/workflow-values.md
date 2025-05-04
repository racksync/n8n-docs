### Workflow Values (ค่าสำหรับ Workflow)

ตั้งค่าที่จะส่งต่อไปยัง workflow ที่คุณกำลังเรียกใช้

ค่าเหล่านี้จะปรากฏในข้อมูล output ของ trigger node ใน workflow ที่คุณเรียก คุณสามารถเข้าถึงค่าเหล่านี้ใน expression ภายใน workflow ตัวอย่างเช่น ถ้าคุณมี:

*   **Workflow Values** ที่มี **Name** เป็น `myCustomValue`
*   Workflow ที่มี Execute Sub-workflow Trigger node เป็น trigger

Expression เพื่อเข้าถึงค่าของ `myCustomValue` คือ `{{ $('Execute Sub-workflow Trigger').item.json.myCustomValue }}`
