---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: วิธีจัดการข้อมูลของคุณบน n8n Cloud
contentType: howto
---

# Cloud data management

การจัดการข้อมูลบน Cloud มี 2 เรื่องหลักที่ต้องคำนึงถึง:

* การใช้ memory: ถ้า workflow ซับซ้อนและประมวลผลข้อมูลเยอะ อาจใช้ memory เกินขีดจำกัดของ n8n ซึ่งจะทำให้ instance crash และเข้าใช้งานไม่ได้
* การเก็บข้อมูล: ขึ้นอยู่กับการตั้งค่า execution และปริมาณงาน ฐานข้อมูล n8n อาจโตขึ้นจนเต็มพื้นที่ได้

เพื่อป้องกันปัญหาเหล่านี้ n8n แนะนำให้คุณออกแบบ workflow ให้ใช้ memory อย่างมีประสิทธิภาพ และไม่บันทึกข้อมูลที่ไม่จำเป็น

## Memory limits on each Cloud plan

แต่ละ plan มีขีดจำกัดดังนี้:

* Trial: 320MiB RAM, 10 millicore CPU burstable
* Starter: 320MiB RAM, 10 millicore CPU burstable
* Pro-1 (10k executions): 640MiB RAM, 20 millicore CPU burstable
* Pro-2 (50k executions): 1280MiB RAM, 80 millicore CPU burstable
* Enterprise: 4096MiB RAM, 80 millicore CPU burstable

แผนเก่า:

* Start: 320MiB RAM, 10 millicore CPU burstable
* Power: 1280MiB RAM, 80 millicore CPU burstable

n8n ให้พื้นที่เก็บข้อมูลสูงสุด 100GB ต่อ instance

## How to reduce memory consumption in your workflow

วิธีที่คุณสร้าง workflow มีผลต่อการใช้ memory ทุกครั้งที่รัน ถึงแม้ guideline เหล่านี้จะไม่เหมาะกับทุกกรณี แต่ก็เป็นแนวทางเบื้องต้นเพื่อป้องกันการใช้ memory เกินขีดจำกัด

--8<-- "_snippets/self-hosting/scaling/reduce-memory-consumption.md"

อย่าลืมว่า n8n เองก็ใช้ memory ในการทำงาน โดยเฉลี่ยตัวซอฟต์แวร์ใช้ประมาณ 180MiB RAM

การใช้งาน UI ก็ใช้ memory ด้วย ถ้าคุณเล่นกับ workflow UI ขณะ workflow กำลังรันงานหนัก อาจทำให้ memory เต็มได้

## How to manage execution data on Cloud

execution data รวมถึงข้อมูล node, parameters, variables, execution context และ binary data references ทั้งหมดนี้เป็นข้อมูลแบบ text

binary data คือข้อมูลที่ไม่ใช่ text เช่น ไฟล์, รูปภาพ, เอกสาร, เสียง, วิดีโอ ซึ่งขนาดใหญ่กว่าข้อมูล text มาก

ถ้า workflow ของคุณใช้ข้อมูลเยอะและผ่านช่วงทดสอบแล้ว แนะนำให้หยุดบันทึก execution ที่สำเร็จ

คุณสามารถควบคุมปริมาณ execution data ที่ n8n เก็บในฐานข้อมูลได้ 2 วิธี:

ใน admin dashboard:

1. จาก workspace หรือ editor ไปที่ **Admin Panel**
1. เลือก **Manage**
1. ใน **Executions to Save** เอา execution ที่ไม่ต้องการ log ออก

ใน workflow settings:

1. กด **Options** <span class="inline-image">![Options menu](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span>
1. เลือก **Settings** n8n จะเปิด modal **Workflow settings**
1. เปลี่ยน **Save successful production executions** เป็น **Do not save**

## Cloud data pruning and out of memory incident prevention

### Automatic data pruning

n8n จะลบ execution log อัตโนมัติเมื่อครบเวลาที่กำหนด หรือเมื่อใช้พื้นที่ถึงขีดจำกัด โดยจะลบจากข้อมูลเก่าก่อนเสมอ ขึ้นอยู่กับ Cloud plan ของคุณ:

* Start และ Starter: เก็บ execution สูงสุด 2500 รายการ และเก็บ log ได้ 7 วัน
* Pro และ Power: เก็บ execution สูงสุด 25000 รายการ และเก็บ log ได้ 30 วัน
* Enterprise: เก็บ execution สูงสุด 50000 รายการ และเก็บ log ได้ไม่จำกัดเวลา

### Manual data pruning

ถ้า execution หนักๆ หรือ use case ใหญ่ๆ ทำให้ฐานข้อมูลเต็มแม้จะมีการลบอัตโนมัติ n8n จะลบข้อมูลด้วยมือเพื่อป้องกัน instance ล่ม

1. ระบบแจ้งเตือน n8n เมื่อพื้นที่ดิสก์ถึง 85%
2. n8n จะลบ execution data โดย backup instance (workflows, users, credentials และ execution data) แล้ว restore กลับโดยไม่เอา execution data

เนื่องจากขั้นตอนนี้มีคนเกี่ยวข้อง ระบบแจ้งเตือนอาจไม่ทันใจ ถ้าแจ้งเตือนหลังเวลาทำการ หรือข้อมูลโตเร็ว อาจไม่มีเวลาลบข้อมูลก่อนพื้นที่เต็ม
