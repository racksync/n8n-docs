---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
---

# Data editing

n8n อนุญาตให้คุณแก้ไข [pinned data](/data/data-pinning.md) ซึ่งหมายความว่าคุณสามารถตรวจสอบสถานการณ์ต่างๆ ได้โดยไม่ต้องตั้งค่าแต่ละสถานการณ์และส่งข้อมูลที่เกี่ยวข้องจากระบบภายนอกของคุณ ทำให้ง่ายต่อการทดสอบ edge cases

/// note | For development only
Data editing ไม่สามารถใช้ได้กับการ execute workflow ใน production เป็นฟีเจอร์ที่ช่วยทดสอบ workflow ระหว่างการพัฒนาเท่านั้น
///
## Edit output data

วิธีแก้ไข output data:

1. รัน node เพื่อโหลดข้อมูล
2. ในมุมมอง **OUTPUT** เลือก **JSON** เพื่อสลับไปยังมุมมอง JSON
3. เลือก **Edit** <span class="inline-image">![Edit data icon](/_images/data/data-pinning/edit-data.png){.off-glb}</span>
4. แก้ไขข้อมูลของคุณ
5. เลือก **Save** n8n จะบันทึกการเปลี่ยนแปลงข้อมูลของคุณและ pin ข้อมูลของคุณ

## Use data from previous executions

คุณสามารถคัดลอกข้อมูลจาก nodes ในการ execute workflow ก่อนหน้าได้:

1. เปิดเมนูด้านซ้าย
2. เลือก **Executions**
3. เรียกดูรายการ workflow executions เพื่อค้นหารายการที่มีข้อมูลที่คุณต้องการคัดลอก
4. เลือก **Open Past Execution** <span class="inline-image">![Open past execution icon](/_images/data/data-pinning/open-execution.png){.off-glb}</span>
5. ดับเบิลคลิกที่ node ที่คุณต้องการคัดลอกข้อมูล
6. หากเป็น layout แบบ table ให้เลือก **JSON** เพื่อสลับไปยังมุมมอง JSON
7. มีสองวิธีในการคัดลอก JSON:
  1. เลือก JSON ที่คุณต้องการโดยการไฮไลต์เหมือนการเลือกข้อความ จากนั้นใช้ `ctrl` + `c` เพื่อคัดลอก
  2. เลือก JSON ที่คุณต้องการคัดลอกโดยคลิกที่ parameter จากนั้น:
    1. วางเมาส์เหนือ JSON n8n จะแสดงปุ่ม **Copy** <span class="inline-image">![Copy data icon](/_images/data/data-pinning/copy-data.png){.off-glb}</span>
    2. เลือก **Copy** <span class="inline-image">![Copy data icon](/_images/data/data-pinning/copy-data.png){.off-glb}</span>
    3. คุณสามารถเลือกสิ่งที่จะคัดลอกได้:
        * **Copy Item Path** และ **Copy Parameter Path** จะให้ expressions ที่เข้าถึงส่วนต่างๆ ของ JSON
        * **Copy Value**: คัดลอก JSON ที่เลือกทั้งหมด
8. กลับไปที่ workflow ที่คุณกำลังทำงานอยู่:
    1. เปิดเมนูด้านซ้าย
    2. เลือก **Workflows**
    3. เลือก **Open**
    4. เลือก workflow ที่คุณต้องการเปิด
9. เปิด node ที่คุณต้องการใช้ข้อมูลที่คัดลอกมา
10. หากไม่มีข้อมูล ให้รัน node เพื่อโหลดข้อมูล
11. ในมุมมอง **OUTPUT** เลือก **JSON** เพื่อสลับไปยังมุมมอง JSON
12. เลือก **Edit** <span class="inline-image">![Edit data icon](/_images/data/data-pinning/edit-data.png){.off-glb}</span>
15. วางข้อมูลจากการ execute ก่อนหน้า
16. เลือก **Save** n8n จะบันทึกการเปลี่ยนแปลงข้อมูลของคุณและ pin ข้อมูลของคุณ
