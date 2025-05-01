---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
---

# Cloud concurrency

/// info | Only for n8n Cloud
เอกสารนี้พูดถึง concurrency ใน n8n Cloud ถ้าใช้ self-hosted n8n ดู [self-hosted n8n concurrency control](/hosting/scaling/concurrency-control.md) เพื่อดูวิธีจัดการ concurrency สำหรับ self-hosted
///

ถ้ามี execution พร้อมกันมากเกินไป อาจทำให้ประสิทธิภาพลดลงหรือ instance ไม่ตอบสนอง เพื่อป้องกันปัญหานี้และเพิ่มเสถียรภาพ n8n จะกำหนดขีดจำกัด concurrency สำหรับ production executions ในโหมดปกติ

execution ที่เกินขีดจำกัดจะถูกนำไปเข้า queue เพื่อรอประมวลผล เมื่อมี capacity ว่าง execution จะถูกนำออกจาก queue ตามลำดับ FIFO

## Concurrency limits

n8n จำกัดจำนวน execution พร้อมกันใน Cloud ตาม plan ดังนี้:

* Starter และ Trial: 5
* Pro (10k workflow executions, 15 active workflows): 20
* Pro (50k workflow executions, 50 active workflows): 50
* Enterprise (โหมดปกติ): 200

คุณสามารถดูจำนวน execution ที่กำลังทำงานและขีดจำกัด concurrency ของ plan ได้ที่ด้านบนของแท็บ executions ของ project หรือ workflow

## Details

รายละเอียดอื่นๆ เกี่ยวกับ concurrency ที่ควรรู้:

- concurrency control ใช้กับ production executions เท่านั้น (ที่เริ่มจาก webhook หรือ trigger node) ไม่รวม execution แบบ manual, sub-workflow หรือ error executions
- [Test evaluations](/glossary.md#evaluation-n8n) จะไม่ถูกนับรวมในขีดจำกัด concurrency โดยขีดจำกัด test evaluation จะเท่ากับขีดจำกัด concurrency ปกติของ plan แต่แยกกัน
- ไม่สามารถ retry execution ที่อยู่ใน queue ได้ ถ้ายกเลิกหรือลบ execution ที่อยู่ใน queue จะถูกลบออกจาก queue ทันที
- ตอน instance เริ่มต้น n8n จะ resume execution ที่อยู่ใน queue ตามขีดจำกัด concurrency และนำที่เหลือกลับเข้า queue

## Comparison to queue mode

/// info | Feature availability
queue mode มีเฉพาะใน Cloud Enterprise plan ถ้าต้องการเปิดใช้งาน [ติดต่อ n8n](https://n8n-community.typeform.com/to/y9X2YuGa){:target=_blank .external-link}
///

concurrency ใน queue mode จะต่างจากโหมดปกติ โดย queue mode จะกำหนดจำนวน job ที่แต่ละ worker รันพร้อมกันได้ ส่วนโหมดปกติ ขีดจำกัด concurrency จะใช้กับทั้ง instance
