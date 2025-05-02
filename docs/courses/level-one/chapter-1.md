---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

<!-- vale from-microsoft.We = NO -->
<!-- vale from-microsoft.FirstPerson = NO -->
# Navigating the Editor UI

ในบทเรียนนี้ คุณจะได้เรียนรู้วิธีนำทาง [Editor UI](/glossary.md#editor-n8n) เราจะพาคุณชม [canvas](/glossary.md#canvas-n8n) และแสดงให้คุณเห็นว่าแต่ละไอคอนหมายถึงอะไร และจะหาสิ่งที่คุณต้องการได้ที่ไหนขณะสร้าง workflows ใน n8n

/// warning | n8n version
คอร์สนี้อิงตาม n8n เวอร์ชัน 1.82.1 ในเวอร์ชันอื่น user interfaces บางอย่างอาจดูแตกต่างออกไป แต่สิ่งนี้ไม่ควรส่งผลกระทบต่อฟังก์ชันการทำงานหลัก
///

## Getting started

เริ่มต้นด้วยการตั้งค่า n8n

เราแนะนำให้เริ่มต้นด้วย [n8n Cloud](https://app.n8n.cloud/register) ซึ่งเป็น hosted solution ที่ไม่ต้องติดตั้งและมี free trial

/// note | Alternative set up
หาก n8n Cloud ไม่ใช่ตัวเลือกที่ดีสำหรับคุณ คุณสามารถ [self-host with Docker](/hosting/installation/docker.md) ได้ นี่เป็นตัวเลือกขั้นสูงที่แนะนำสำหรับผู้ใช้ทางเทคนิคที่คุ้นเคยกับการโฮสต์บริการ, Docker และ command line เท่านั้น
///

สำหรับรายละเอียดเพิ่มเติมเกี่ยวกับวิธีการต่างๆ ในการตั้งค่า n8n โปรดดู [platforms documentation](/choose-n8n.md#platforms) ของเรา

เมื่อคุณมี n8n ทำงานแล้ว ให้เปิด Editor UI ในหน้าต่างเบราว์เซอร์ ล็อกอินเข้าสู่ n8n instance ของคุณ เลือก **Overview** จากนั้นเลือก **Create Workflow** เพื่อดู canvas หลัก

ควรมีลักษณะดังนี้:

<figure><img src="/_images/courses/level-one/chapter-one/l1-c1-editor-ui.png" alt="Editor UI" style="width:100%"><figcaption align = "center"><i>Editor UI</i></figcaption></figure>

## Editor UI settings

Editor UI คือ web interface ที่คุณใช้สร้าง [workflows](/workflows/index.md) คุณสามารถเข้าถึง workflows และ [credentials](/glossary.md#credential-n8n) ทั้งหมดของคุณ รวมถึงหน้า support ได้จาก Editor UI

### Left-side panel

ทางด้านซ้ายของ **Editor UI** มี panel ที่มีฟังก์ชันการทำงานหลักและ settings สำหรับจัดการ workflows ของคุณ ขยายและยุบได้โดยเลือกไอคอนลูกศรเล็กๆ

panel ประกอบด้วยส่วนต่างๆ ดังนี้:

- **Overview**: ประกอบด้วย workflows และ credentials ทั้งหมดที่คุณเข้าถึงได้ ในระหว่างคอร์สนี้ ให้สร้าง workflows ใหม่ที่นี่
- **Projects**: (ไม่มีใน Community edition) Projects ใช้จัดกลุ่ม workflows และ credentials คุณสามารถกำหนด [roles](/user-management/rbac/role-types.md) ให้กับ users ใน project เพื่อควบคุมสิ่งที่พวกเขาสามารถทำได้ใน project โดยค่าเริ่มต้นจะมี **Personal** project ให้ใช้งาน
- **Admin Panel**: n8n Cloud เท่านั้น เข้าถึงการใช้งาน n8n instance, billing และ version settings ของคุณ
- **Templates**: คอลเลกชันของ workflows ที่สร้างไว้ล่วงหน้า เป็นจุดเริ่มต้นที่ดีสำหรับ use cases ทั่วไป
- **Variables**: ใช้เพื่อจัดเก็บและเข้าถึงข้อมูลคงที่ใน workflows ของคุณ ฟีเจอร์นี้มีให้ใน Pro และ Enterprise Plans
- **All executions**: ประกอบด้วยข้อมูลเกี่ยวกับ workflow executions ของคุณ
- **Help**: ประกอบด้วยแหล่งข้อมูลเกี่ยวกับผลิตภัณฑ์และชุมชน n8n
- **Update**: (เมื่อมีการอัปเดต) ตัวบ่งชี้สำหรับการอัปเดตผลิตภัณฑ์ล่าสุด
- **Settings**: ใต้เมนูจุดไข่ปลา (`...`) ข้างชื่อผู้ใช้ของคุณ จัดการ users และเข้าถึง settings สำหรับฟีเจอร์ต่างๆ

<figure style="text-align: center;"><img src="/_images/courses/level-one/chapter-one/l1-c1-side-panel.png" alt="Editor UI left-side menu" style="height: 600px;"><figcaption align = "center"><i>Editor UI left-side menu</i></figcaption></figure>

### Top bar

แถบด้านบนของ **Editor UI** ประกอบด้วยข้อมูลต่อไปนี้:

- **Workflow Name**: โดยค่าเริ่มต้น n8n จะตั้งชื่อ workflow ใหม่ว่า "My workflow" แต่คุณสามารถแก้ไขชื่อได้ตลอดเวลา
- **+ Add Tag**: Tags ช่วยให้คุณจัดระเบียบ workflows ตามหมวดหมู่, use case หรืออะไรก็ตามที่เกี่ยวข้องกับคุณ Tags เป็นทางเลือก
- **Inactive/active toggle**: ปุ่มนี้เปิดหรือปิดใช้งาน workflow ปัจจุบัน โดยค่าเริ่มต้น workflows จะถูกปิดใช้งาน
- **Share**: คุณสามารถแชร์และทำงานร่วมกับผู้อื่นบน workflows ได้ในแผน Starter, Pro และ Enterprise
- **Save**: ปุ่มนี้บันทึก workflow ปัจจุบัน
- **History**: เมื่อคุณบันทึก workflow ของคุณแล้ว คุณสามารถดูเวอร์ชันก่อนหน้าได้ที่นี่

<figure><img src="/_images/courses/level-one/chapter-one/l1-c1-top-bar.png" alt="Editor UI top bar" style="width:100%"><figcaption align = "center"><i>Editor UI top bar</i></figcaption></figure>

### Canvas

**canvas** คือพื้นหลังตารางกริดลายจุดสีเทาใน Editor UI จะแสดงไอคอนหลายอย่างและ node ที่มีฟังก์ชันการทำงานต่างๆ:

- ปุ่มสำหรับซูม canvas ให้พอดีกับหน้าจอ, ซูมเข้าหรือออกจาก canvas และจัดระเบียบ nodes บนหน้าจอ
- ปุ่ม **Test workflow** เมื่อคุณเพิ่ม node แรกของคุณ เมื่อคุณคลิก n8n จะ εκτέλεση (execute) nodes ทั้งหมดบน canvas ตามลำดับ
- ปุ่มที่มีเครื่องหมาย **+** อยู่ข้างใน ปุ่มนี้จะเปิด nodes panel
- ปุ่มที่มีไอคอนโน้ตอยู่ข้างใน ปุ่มนี้จะเพิ่ม [sticky note](/workflows/components/sticky-notes.md) ลงใน canvas (มองเห็นได้เมื่อวางเมาส์เหนือไอคอน + ที่มุมขวาบน)
- สี่เหลี่ยมลายจุดพร้อมข้อความ "Add first step" นี่คือที่ที่คุณเพิ่ม node แรกของคุณ

<figure><img src="/_images/courses/level-one/chapter-one/l1-c1-canvas.png" alt="Workflow canvas" style="width:100%"><figcaption align = "center"><i>Workflow canvas</i></figcaption></figure>

/// note | Moving the canvas
คุณสามารถย้าย workflow canvas ไปมาได้สามวิธี:

- เลือก ++ctrl+left-button++ บน canvas แล้วเลื่อนไปมา
- เลือก ++middle-button++ บน canvas แล้วเลื่อนไปมา
- วางสองนิ้วบน touchpad ของคุณแล้วเลื่อน
///


ไม่ต้องกังวลเกี่ยวกับ workflow execution และ activation ในตอนนี้ เราจะอธิบายแนวคิดเหล่านี้ในภายหลังในคอร์ส

## Nodes

คุณสามารถคิดว่า nodes เป็นเหมือน building blocks ที่ทำหน้าที่ต่างๆ กัน ซึ่งเมื่อนำมารวมกันแล้ว จะกลายเป็นเครื่องจักรที่ทำงานได้: automated workflow

/// note | Node
Node คือขั้นตอนแต่ละขั้นตอนใน workflow ของคุณ: ขั้นตอนที่ (a) โหลด, (b) ประมวลผล หรือ (c) ส่งข้อมูล
///

ตามฟังก์ชันการทำงาน n8n แบ่งประเภท nodes ออกเป็นสี่ประเภท:

- **App** or **Action Nodes** เพิ่ม ลบ และแก้ไขข้อมูล; ร้องขอและส่งข้อมูลภายนอก; และ trigger events ในระบบอื่น อ้างอิง [Action nodes library](/integrations/builtin/app-nodes/index.md) สำหรับรายการ nodes เหล่านี้ทั้งหมด
- **Trigger Nodes** เริ่มต้น workflow และให้ข้อมูลเริ่มต้น อ้างอิง [Trigger nodes library](/integrations/builtin/trigger-nodes/index.md) สำหรับรายการ trigger nodes
- **Core Nodes** สามารถเป็น trigger หรือ app nodes ได้ ในขณะที่ nodes ส่วนใหญ่เชื่อมต่อกับบริการภายนอกที่เฉพาะเจาะจง core nodes ให้ฟังก์ชันการทำงาน เช่น logic, scheduling หรือ generic API calls อ้างอิง [Core Nodes library](/integrations/builtin/core-nodes/index.md) สำหรับรายการ core nodes ทั้งหมด
- **Cluster Nodes** คือกลุ่มของ nodes ที่ทำงานร่วมกันเพื่อให้ฟังก์ชันการทำงานใน workflow โดยหลักสำหรับ AI workflows อ้างอิง [Cluster nodes](/integrations/builtin/cluster-nodes/index.md) สำหรับข้อมูลเพิ่มเติม

/// note | Learn more
อ้างอิง [Node types](/integrations/builtin/node-types.md) สำหรับคำอธิบายโดยละเอียดเพิ่มเติมเกี่ยวกับ node types ทั้งหมด
///

### Finding nodes

คุณสามารถค้นหา nodes ที่มีอยู่ทั้งหมดได้ใน **nodes panel** ทางด้านขวาของ Editor UI มีสามวิธีที่คุณสามารถเปิด nodes panel ได้:

- คลิกไอคอน **+** ที่มุมขวาบนของ canvas
- คลิกไอคอน **+** ทางด้านขวาของ node ที่มีอยู่บน canvas (node ที่คุณต้องการเพิ่ม node อื่นเข้าไป)
- คลิกปุ่ม ++tab++ บนคีย์บอร์ดของคุณ

<figure style="text-align: center; width:50%; margin:auto;"><img src="/_images/courses/level-one/chapter-one/l1-c1-node-menu-drilldown.gif" alt="Nodes panel"><figcaption align = "center"><i>Nodes panel</i></figcaption></figure>

ใน nodes panel สังเกตว่าเมื่อเพิ่ม node แรกของคุณ คุณจะเห็นหมวดหมู่ trigger node ต่างๆ หลังจากที่คุณเพิ่ม trigger node ของคุณแล้ว คุณจะเห็นว่า nodes panel เปลี่ยนไปเพื่อแสดง Advanced AI, Actions in an App, Data transformation, Flow, Core และ Human in the loop nodes

หากคุณต้องการค้นหา node ที่เฉพาะเจาะจง ให้ใช้ช่องค้นหาที่ด้านบนของ nodes panel


### Adding nodes

มีสองวิธีในการเพิ่ม nodes ลงใน canvas ของคุณ:

- เลือก node ที่คุณต้องการใน nodes panel node ใหม่จะเชื่อมต่อกับ node ที่เลือกบน canvas โดยอัตโนมัติ
- ลากและวาง node จาก nodes panel ไปยัง canvas

### Node buttons

หากคุณวางเมาส์เหนือ node คุณจะสังเกตเห็นว่ามีไอคอนสามอันปรากฏขึ้นด้านบน:

- Execute the node (Play icon)
- Deactivate/Activate the node (Power icon)
- Delete the node (Trash icon)

นอกจากนี้ยังมีไอคอนจุดไข่ปลา ซึ่งจะเปิด context menu ที่มี [node options](/workflows/components/nodes.md#node-controls) อื่นๆ

/// note | Moving a workflow
หากต้องการย้าย workflow ไปรอบๆ canvas ให้เลือก nodes ทั้งหมดด้วยเมาส์ของคุณหรือ ++ctrl+a++ เลือกค้างไว้ที่ node จากนั้นลากไปยังจุดใดก็ได้ที่คุณต้องการบน canvas
///

## Summary

ในบทเรียนนี้ คุณได้เรียนรู้วิธีนำทาง Editor UI, ความหมายของไอคอนต่างๆ, วิธีเข้าถึง left-side panel และ node panels และวิธีเพิ่ม nodes ลงใน canvas

ในบทเรียนถัดไป คุณจะได้สร้าง mini-workflow เพื่อฝึกฝนสิ่งที่คุณได้เรียนรู้มาจนถึงตอนนี้
