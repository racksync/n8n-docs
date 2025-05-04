/// warning | การแชร์ Credentials
ไฟล์ JSON ของ workflow ที่ Export ออกไปนั้นรวมถึงชื่อและ ID ของ [credential](/glossary.md#credential-n8n) ด้วย แม้ว่า ID จะไม่ละเอียดอ่อน แต่ชื่ออาจเป็นได้ ขึ้นอยู่กับว่าคุณตั้งชื่อ credentials ของคุณอย่างไร Node ของ HTTP Request อาจมี header การยืนยันตัวตนเมื่อนำเข้าจาก cURL ลบหรือทำให้ข้อมูลนี้เป็นนิรนามออกจากไฟล์ JSON ก่อนแชร์เพื่อปกป้อง credentials ของคุณ
///
