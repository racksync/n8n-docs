---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
---

# Prerequisites

--8<-- "_snippets/embed-license.md"

ข้อกำหนดที่ให้ไว้ตรงนี้เป็นตัวอย่างที่อ้างอิงจาก n8n Cloud เพื่อให้เห็นภาพเท่านั้น ความต้องการจริงอาจแตกต่างกันไปขึ้นอยู่กับจำนวนผู้ใช้, workflows, และ executions ของคุณ ถ้าต้องการข้อมูลเพิ่มเติมสามารถติดต่อ n8n ได้เลย

| Component | Sizing | Supported |
| :-------- | :----- | :-------- |
| CPU/vCPU  | ขั้นต่ำ 10 CPU cycles, สามารถปรับขนาดได้ตามต้องการ | ใช้ได้กับ public หรือ private cloud ทุกเจ้า |
| Database  | 512 MB - 4 GB SSD | SQLite หรือ PostgreSQL |
| Memory    | 320 MB - 2 GB | |

## CPU considerations

n8n ไม่ได้ใช้ CPU หนักมาก ดังนั้น instance ขนาดเล็ก (เช่นของ AWS หรือ GCP) ก็เพียงพอสำหรับการใช้งานส่วนใหญ่ โดยปกติแล้ว memory จะสำคัญกว่า CPU เวลาวางแผน infrastructure ให้เน้นไปที่ memory เป็นหลัก

## Database considerations

n8n ใช้ database เพื่อเก็บ [credentials](/glossary.md#credential-n8n), ประวัติการรัน, และ workflows

จุดเด่นของ n8n คือความยืดหยุ่นในการเลือก database ได้เอง ฐานข้อมูลแต่ละแบบที่รองรับจะมีข้อดีข้อเสียต่างกัน คุณควรพิจารณาและเลือกแบบที่เหมาะกับงานของคุณมากที่สุด โดยปกติถ้าไม่มี database อยู่ที่ path ที่กำหนด n8n จะสร้าง SQLite database ให้เอง

แนะนำให้แต่ละ instance ของ n8n มี database แยกกัน จะช่วยลดปัญหา dependency และปัญหาด้าน performance ถ้าไม่สามารถแยก database ได้จริงๆ แนะนำให้ใช้ feature schema ของ Postgres แทน

สำหรับ Postgres, database ต้องถูกสร้างไว้ก่อนแล้วใน DB-instance และ user ที่ใช้รัน n8n ต้องมีสิทธิ์เต็มกับทุก table ที่ใช้หรือสร้าง n8n จะสร้างและดูแล schema เอง

### Best practices

* ใช้ SSD storage
* ถ้าอยู่ใน containerized cloud environment ให้แน่ใจว่า volume ถูก persist และ mount ทุกครั้งที่หยุด/เริ่ม container ไม่งั้นข้อมูลจะหายหมด
* ถ้าใช้ Postgres ไม่ควรใช้ option `tablePrefix` เพราะจะถูกยกเลิกในอนาคต
* คอยดู changelog เวอร์ชันใหม่ๆ และถ้าจะ downgrade ให้พิจารณา revert migration ด้วย
* ตั้งค่าความปลอดภัยและเสถียรภาพของ database อย่างน้อย เช่น IP allow list และ backup

## Memory considerations

โดยปกติ n8n instance ไม่ต้องใช้ memory เยอะมาก เช่น n8n Cloud ที่ idle ใช้แค่ประมาณ 100MB ขึ้นอยู่กับลักษณะ workflow และข้อมูลที่ process

ตัวอย่างเช่น ส่วนใหญ่ node จะส่งข้อมูลต่อไปยัง node ถัดไป แต่ [Code node](/code/code-node.md) จะสร้างสำเนาข้อมูลทั้งก่อนและหลังประมวลผล ถ้าต้องจัดการไฟล์ binary ขนาดใหญ่ อาจใช้ resource เยอะจนหมดได้
