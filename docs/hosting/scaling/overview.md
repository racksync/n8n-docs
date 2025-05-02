---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: overview
---

# Scaling n8n

ถ้าคุณรัน n8n ในระดับใหญ่ มีผู้ใช้, workflow หรือ execution จำนวนมาก คุณต้องปรับ config ของ n8n เพื่อให้ performance ดี

n8n สามารถรันได้หลาย [modes](/hosting/scaling/queue-mode.md) ตามความต้องการ โดย `queue` mode จะขยายระบบได้ดีที่สุด ดูวิธีตั้งค่าที่ [Queue mode](/hosting/scaling/queue-mode.md)

คุณสามารถตั้งค่าการบันทึกและลบข้อมูล execution เพื่อช่วยให้ database ทำงานเร็วขึ้น ดูรายละเอียดที่ [Execution data](/hosting/scaling/execution-data.md)
