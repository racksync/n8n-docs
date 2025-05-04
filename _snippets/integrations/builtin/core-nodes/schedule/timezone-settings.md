/// note | การตั้งค่า Timezone
Node นี้ขึ้นอยู่กับการตั้งค่า timezone n8n ใช้ค่าใดค่าหนึ่งต่อไปนี้:

1. Workflow timezone หากมีการตั้งค่า โปรดดู [Workflow settings](/workflows/settings.md) สำหรับข้อมูลเพิ่มเติม
2. n8n instance timezone หากไม่ได้ตั้งค่า workflow timezone ค่าเริ่มต้นคือ `America/New York` สำหรับ self-hosted instances n8n Cloud พยายามตรวจจับ timezone ของเจ้าของ instance เมื่อลงทะเบียน โดยใช้ GMT เป็นค่าเริ่มต้น ผู้ใช้ self-hosted สามารถเปลี่ยนการตั้งค่า instance โดยใช้ [Environment variables](/hosting/configuration/environment-variables/timezone-localization.md) ผู้ดูแลระบบ Cloud สามารถเปลี่ยน instance timezone ได้ใน [Admin dashboard](/manage-cloud/set-cloud-timezone.md)
///
