---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: Creating and editing credentials.
contentType: howto
---

# Create and edit credentials

Credentials คือข้อมูลการยืนยันตัวตนที่จัดเก็บอย่างปลอดภัย ใช้เพื่อเชื่อมต่อ n8n workflows กับบริการภายนอก เช่น APIs หรือ databases

## Create a credential

1. เลือก <span class="inline-image">![universal create resource icon](/_images/common-icons/universal-resource-button.png){.off-glb}</span> **button** ที่มุมบนซ้ายของเมนูด้านข้าง เลือก credential
2. หาก n8n instance ของคุณรองรับ [projects](/glossary.md#project-n8n) คุณจะต้องเลือกว่าจะสร้าง credential ในพื้นที่ส่วนตัวของคุณหรือใน project เฉพาะที่คุณมีสิทธิ์เข้าถึง หากคุณใช้เวอร์ชัน community คุณจะสร้าง credential ในพื้นที่ส่วนตัวของคุณ
3. เลือกแอปหรือบริการที่คุณต้องการเชื่อมต่อ

หรือ:

1. ใช้ปุ่ม <span class="inline-image">![universal create resource icon](/_images/common-icons/universal-resource-button.png){.off-glb}</span> **Create** ที่มุมบนขวาจากหน้า **Overview** หรือจาก project เฉพาะ เลือก Credential
2. หากคุณทำสิ่งนี้จากหน้า **Overview** คุณจะสร้าง credential ในพื้นที่ส่วนตัวของคุณ หากคุณทำสิ่งนี้จากภายใน project คุณจะสร้าง credential ภายใน project นั้น
3. เลือกแอปหรือบริการที่คุณต้องการเชื่อมต่อ

คุณยังสามารถสร้าง credential ใหม่ได้ในดรอปดาวน์ credential เมื่อแก้ไข node บน workflow editor

เมื่ออยู่ใน credential modal ให้ป้อนรายละเอียดที่บริการของคุณต้องการ อ้างอิงหน้าของบริการของคุณใน [credentials library](/integrations/builtin/credentials/index.md) สำหรับคำแนะนำ

เมื่อคุณบันทึก credential แล้ว n8n จะทดสอบเพื่อยืนยันว่าใช้งานได้

/// note | Credentials naming
n8n จะตั้งชื่อ credentials ใหม่เป็น "*node name* account" ตามค่าเริ่มต้น คุณสามารถเปลี่ยนชื่อ credentials ได้โดยคลิกที่ชื่อ เช่นเดียวกับการเปลี่ยนชื่อ nodes เป็นแนวทางปฏิบัติที่ดีในการตั้งชื่อที่ระบุแอปหรือบริการ ประเภท และวัตถุประสงค์ของ credential การมีแบบแผนการตั้งชื่อจะช่วยให้ติดตามและระบุ credentials ของคุณได้ง่ายขึ้น
///

## Expressions in credentials

คุณสามารถใช้ [expressions](/glossary.md#expression-n8n) เพื่อตั้งค่า credentials แบบไดนามิกขณะที่ workflow ของคุณทำงาน:

1. ใน workflow ของคุณ ค้นหา data path ที่มี credential ซึ่งจะแตกต่างกันไปขึ้นอยู่กับชื่อ parameter ที่แน่นอนในข้อมูลของคุณ ตรวจสอบให้แน่ใจว่าข้อมูลที่มี credential นั้นพร้อมใช้งานใน workflow เมื่อคุณไปถึง node ที่ต้องการ
1. เมื่อสร้าง credential ของคุณ ให้วางเมาส์เหนือฟิลด์ที่คุณต้องการใช้ expression
1. สลับเปิด **Expression**
1. ป้อน expression ของคุณ

### Example workflow

[[ workflowDemo("file:///credentials/dynamic_credentials_using_expressions.json") ]]

#### Using the example

--8<-- "_snippets/examples-color-key.md"
