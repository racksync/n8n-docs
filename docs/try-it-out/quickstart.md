---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: A quick example to try out n8n.
contentType: tutorial
---

# The very quick quickstart

Quickstart นี้จะช่วยให้คุณเริ่มต้นใช้งาน n8n ได้เร็วที่สุด ให้คุณลองใช้ UI และแนะนำฟีเจอร์หลักสองอย่าง: [workflow templates](/glossary.md#template-n8n) และ [expressions](/glossary.md#expression-n8n) โดยไม่ได้ลงรายละเอียดหรืออธิบายแนวคิดเชิงลึก

ใน tutorial นี้ คุณจะได้:

* โหลด [workflow](/glossary.md#workflow-n8n) จาก workflow templates library
* เพิ่ม node และตั้งค่าด้วย expressions
* รัน workflow แรกของคุณ

## Step one: Sign up for n8n

Quickstart นี้ใช้ [n8n Cloud](/manage-cloud/overview.md) มีรุ่นทดลองใช้ฟรีสำหรับผู้ใช้ใหม่ ถ้ายังไม่มีบัญชี [สมัครเลย](https://app.n8n.cloud/register)

## Step two: Open a workflow template

n8n มี quickstart template ที่ใช้ training nodes คุณสามารถใช้เพื่อทดลองกับข้อมูลจำลองและไม่ต้องตั้งค่า [credentials](/glossary.md#credential-n8n)

1. ไปที่ [Templates | Very quick quickstart](https://n8n.io/workflows/1700-very-quick-quickstart/)
1. เลือก **Use workflow** เพื่อดูตัวเลือกการใช้งาน template
1. เลือก **Import template to <name> cloud workspace** เพื่อโหลด template ไปยัง Cloud instance ของคุณ

Workflow นี้จะ:

1. ดึงข้อมูลตัวอย่างจาก [Customer Datastore](/integrations/builtin/app-nodes/n8n-nodes-base.n8ntrainingcustomerdatastore.md) node
2. ใช้ [Edit Fields](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) node เพื่อดึงเฉพาะข้อมูลที่ต้องการและ map ข้อมูลนั้นให้กับตัวแปร ตัวอย่างนี้จะ map ชื่อลูกค้า, ID และคำอธิบาย

แต่ละส่วนใน n8n workflow เรียกว่า [nodes](/glossary.md#node-n8n) ดับเบิลคลิกที่ node เพื่อดูการตั้งค่าและวิธีประมวลผลข้อมูล

## Step three: Run the workflow

เลือก **Test Workflow** เพื่อรัน workflow โดยโหลดข้อมูลจาก Customer Datastore node แล้วแปลงข้อมูลด้วย Edit Fields คุณต้องมีข้อมูลนี้ใน workflow เพื่อใช้ในขั้นตอนถัดไป

## Step four: Add a node

เพิ่ม node ที่สามเพื่อส่งข้อความถึงลูกค้าแต่ละคนและแจ้งคำอธิบายของเขา ใช้ Customer Messenger node เพื่อส่งข้อความไปยังผู้รับจำลอง

1. เลือกตัวเชื่อมต่อ **Add node** <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span> บน Edit Fields node
2. ค้นหา **Customer Messenger** n8n จะแสดงรายการ nodes ที่ตรงกับที่ค้นหา
3. เลือก **Customer Messenger (n8n training)** เพื่อเพิ่ม node ลงบน [canvas](/glossary.md#canvas-n8n) n8n จะเปิด node ให้อัตโนมัติ
4. ใช้ [expressions](/code/expressions.md) เพื่อ map **Customer ID** และสร้าง **Message**:
    1. ในแผง **INPUT** เลือกแท็บ **Schema**
    2. ลาก **Edit Fields1** > **customer_id** ไปที่ช่อง **Customer ID** ในการตั้งค่า node
    2. เอาเมาส์ไปวางบน **Message** เลือกแท็บ **Expression** แล้วกดปุ่มขยาย <span class="inline-image">![Add node icon](/_images/common-icons/open-expression-editor.png){.off-glb}</span> เพื่อเปิด editor เต็ม
    3. คัดลอก expression นี้ไปใส่ใน editor:
        ```
        Hi {{ $json.customer_name }}. Your description is: {{ $json.customer_description }}
        ```
5. ปิด editor expression แล้วปิด **Customer Messenger** node โดยคลิกนอก node หรือเลือก **Back to canvas**
6. เลือก **Test Workflow** n8n จะรัน workflow

Workflow ที่สมบูรณ์ควรจะหน้าตาแบบนี้:

[[ workflowDemo("file:///try-it-out/quickstart/very-quick-quickstart-workflow.json") ]]


## Next steps

* อ่าน [tutorial ลองใช้งานที่ยาวขึ้น](/try-it-out/tutorial-first-workflow.md) ของ n8n สำหรับ workflow ที่ซับซ้อนขึ้น และแนะนำฟีเจอร์กับแนวคิดของ n8n เพิ่มเติม
* เรียน [text courses](/courses/index.md) หรือ [video courses](/video-courses.md)


