---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: จัดการการตั้งค่าสำหรับ workflow แต่ละรายการ
contentType: howto
---

# Workflow settings

คุณสามารถปรับแต่งพฤติกรรมของ workflow สำหรับแต่ละ workflow ได้โดยใช้การตั้งค่า workflow

วิธีการเปิดการตั้งค่า:

1. เปิด workflow ของคุณ
2. เลือกเมนู **Options** <span class="inline-image">![Options menu](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span>
3. เลือก **Settings** n8n จะเปิดหน้าต่าง **Workflow settings** ขึ้นมา

มีการตั้งค่าดังต่อไปนี้:

* **Execution order**: เลือกลำดับการทำงานสำหรับ workflow ที่มีหลาย branch **v0 (legacy)** จะทำงาน node แรกของแต่ละ branch ก่อน แล้วตามด้วย node ที่สองของแต่ละ branch ไปเรื่อยๆ **v1 (recommended)** จะทำงานทีละ branch จนเสร็จสมบูรณ์ก่อนที่จะเริ่ม branch ถัดไป n8n จะเรียงลำดับ branch ตามตำแหน่งบน [canvas](/glossary.md#canvas-n8n) จากบนสุดลงล่างสุด หากมีสอง branch อยู่ในระดับความสูงเดียวกัน branch ที่อยู่ซ้ายสุดจะทำงานก่อน
* **Error Workflow**: เลือก workflow ที่จะทำงานหาก workflow ปัจจุบันล้มเหลว ดูรายละเอียดเพิ่มเติมที่ [Error workflows](/flow-logic/error-handling.md)
* **This workflow can be called by**: เลือกว่า workflow อื่นสามารถเรียกใช้ workflow นี้ได้หรือไม่
* **Timezone**: ตั้งค่า timezone ที่ workflow จะใช้ timezone เริ่มต้นคือ EDT (New York) การตั้งค่า timezone มีความสำคัญสำหรับ Schedule Trigger node
* **Save failed production executions**: เลือกว่า n8n ควรบันทึกการทำงานที่ล้มเหลวสำหรับ workflow ที่ใช้งานอยู่ (active) หรือไม่
* **Save successful production executions**: เลือกว่า n8n ควรบันทึกการทำงานที่สำเร็จสำหรับ workflow ที่ใช้งานอยู่ (active) หรือไม่
* **Save manual executions**: เลือกว่า n8n ควรบันทึกการทำงานสำหรับ workflow ที่ผู้ใช้เริ่มทำงานใน editor หรือไม่
* **Save execution progress**: เลือกว่า n8n ควรบันทึกข้อมูลการทำงานสำหรับแต่ละ node หรือไม่ หากตั้งค่าเป็น **Save** workflow จะกลับมาทำงานต่อจากจุดที่หยุดในกรณีที่เกิดข้อผิดพลาด ซึ่งอาจเพิ่ม latency ได้
* **Timeout Workflow**: สลับเพื่อเปิดใช้งานการตั้งค่าระยะเวลาที่ n8n ควรยกเลิกการทำงานของ workflow ปัจจุบัน
	* **Timeout After**: ตั้งเวลาเป็นชั่วโมง นาที และวินาที หลังจากนั้น workflow ควรจะ timeout สำหรับผู้ใช้ n8n Cloud ทาง n8n จะบังคับใช้เวลา timeout สูงสุดที่แตกต่างกันไปในแต่ละ plan
