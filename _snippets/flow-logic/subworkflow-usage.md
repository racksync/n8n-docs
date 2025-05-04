### สร้าง Sub-workflow


1. สร้าง workflow ใหม่

    /// note | สร้าง sub-workflows จาก workflows ที่มีอยู่
    คุณสามารถเลือกสร้าง sub-workflow โดยตรงจาก parent workflow ที่มีอยู่ได้ โดยใช้ [Execute Sub-workflow](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) node ใน node นั้น ให้เลือกตัวเลือก **Database** และ **From list** แล้วเลือก **Create a sub-workflow** ในรายการ
    ///

1. **Optional**: กำหนดค่าว่า workflows ใดสามารถเรียก sub-workflow นี้ได้:
	1. เลือกเมนู **Options** <span class="inline-image">![Options menu](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span> > **Settings** n8n จะเปิด modal **Workflow settings** ขึ้นมา
	1. เปลี่ยนการตั้งค่า **This workflow can be called by** อ้างอิงถึง [Workflow settings](/workflows/settings.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการกำหนดค่า workflows ของคุณ
1. เพิ่ม **Execute Sub-workflow** trigger node (หากคุณค้นหาภายใต้ trigger nodes หัวข้อนี้จะมีชื่อว่า **When Executed by Another Workflow**)
1. ตั้งค่า **Input data mode** เพื่อเลือกว่าคุณจะกำหนดข้อมูล input ของ sub-workflow อย่างไร:
	* **Define using fields below**: เลือกโหมดนี้เพื่อกำหนดชื่อ input และชนิดข้อมูลแต่ละรายการที่ calling workflow ต้องระบุ [Execute Sub-workflow node](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) หรือ [Call n8n Workflow Tool node](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md) ใน calling workflow จะดึงข้อมูลฟิลด์ที่กำหนดไว้ที่นี่โดยอัตโนมัติ
	* **Define using JSON example**: เลือกโหมดนี้เพื่อระบุตัวอย่าง JSON object ที่แสดงรายการ input ที่คาดหวังและชนิดข้อมูลของมัน
	* **Accept all data**: เลือกโหมดนี้เพื่อยอมรับข้อมูลทั้งหมดโดยไม่มีเงื่อนไข sub-workflow จะไม่กำหนดรายการ input ที่จำเป็นใดๆ sub-workflow นี้จะต้องจัดการกับความไม่สอดคล้องกันของ input หรือค่าที่หายไปเอง
1. เพิ่ม nodes อื่นๆ ตามต้องการเพื่อสร้างฟังก์ชันการทำงานของ sub-workflow ของคุณ
1. บันทึก sub-workflow

/// note | Sub-workflow ต้องไม่มี errors
หากมี errors ใน sub-workflow, parent workflow จะไม่สามารถ trigger มันได้
///
/// note | โหลดข้อมูลเข้าสู่ sub-workflow ก่อนสร้าง
สิ่งนี้ต้องการความสามารถในการ [load data from previous executions](/workflows/executions/debug.md) ซึ่งมีให้ใช้งานบน n8n Cloud และแผน Community ที่ลงทะเบียนแล้ว

หากคุณต้องการโหลดข้อมูลเข้าสู่ sub-workflow ของคุณเพื่อใช้ในขณะสร้าง:

1. สร้าง sub-workflow และเพิ่ม **Execute Sub-workflow Trigger**
1. ตั้งค่า **Input data mode** ของ node เป็น **Accept all data** หรือกำหนดรายการ input โดยใช้ฟิลด์หรือ JSON หากทราบอยู่แล้ว
1. ใน [settings](/workflows/settings.md) ของ sub-workflow ให้ตั้งค่า **Save successful production executions** เป็น **Save**
1. ข้ามไปตั้งค่า parent workflow แล้วรันมัน
1. ทำตามขั้นตอนเพื่อ [load data from previous executions](/workflows/executions/debug.md)
1. ปรับ **Input data mode** ให้ตรงกับ input ที่ส่งมาจาก parent workflow หากจำเป็น

ตอนนี้คุณสามารถ pin ข้อมูลตัวอย่างใน trigger node ได้แล้ว ทำให้คุณสามารถทำงานกับข้อมูลจริงในขณะที่กำหนดค่าส่วนที่เหลือของ workflow ได้
///


### เรียกใช้ Sub-workflow

1. เปิด workflow ที่คุณต้องการเรียก sub-workflow
1. เพิ่ม **Execute Sub-workflow** node
1. ใน **Execute Sub-workflow** node ให้ตั้งค่า sub-workflow ที่คุณต้องการเรียก คุณสามารถเลือกเรียก workflow ด้วย ID, โหลด workflow จากไฟล์ local, เพิ่ม workflow JSON เป็นพารามิเตอร์ใน node หรือกำหนดเป้าหมาย workflow ด้วย URL

    /// note | ค้นหา Workflow ID ของคุณ
    ID ของ sub-workflow ของคุณคือสตริงตัวอักษรและตัวเลขที่อยู่ท้ายสุดของ URL
    ///

1. กรอกข้อมูลรายการ input ที่จำเป็นซึ่งกำหนดโดย sub-workflow
1. บันทึก workflow ของคุณ

เมื่อ workflow ของคุณ execute มันจะส่งข้อมูลไปยัง sub-workflow และรันมัน

คุณสามารถติดตาม flow การ execute จาก parent workflow ไปยัง sub-workflow ได้โดยการเปิด Execute Sub-workflow node และเลือกลิงก์ **View sub-execution** ในทำนองเดียวกัน การ execute ของ sub-workflow จะมีลิงก์กลับไปยังการ execute ของ parent workflow เพื่อนำทางไปในทิศทางตรงกันข้าม
