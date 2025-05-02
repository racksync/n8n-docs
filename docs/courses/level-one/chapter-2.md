---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

<!-- vale from-microsoft.We = NO -->
<!-- vale from-microsoft.FirstPerson = NO -->
# Building a Mini-workflow

ในบทเรียนนี้ คุณจะได้สร้าง [workflow](/glossary.md#workflow-n8n) เล็กๆ ที่ดึงบทความ 10 บทความเกี่ยวกับ automation จาก Hacker News กระบวนการประกอบด้วยห้าขั้นตอน:

1. [Add a Manual Trigger node](#1-add-a-manual-trigger-node)
2. [Add the Hacker News node](#2-add-the-hacker-news-node)
3. [Configure the Hacker News node](#3-configure-the-hacker-news-node)
4. [Execute the node](#4-execute-the-node)
5. [Save the workflow](#5-save-the-workflow)

workflow ที่เสร็จแล้วจะมีลักษณะดังนี้:

[[ workflowDemo("file:////courses/level-one/chapter-2.json") ]]

## 1. Add a Manual Trigger node

เปิด nodes panel (เตือนความจำ: คุณสามารถเปิดได้โดยเลือกไอคอน **+** ที่มุมขวาบนของ [canvas](/glossary.md#canvas-n8n) หรือกด ++tab++ บนคีย์บอร์ดของคุณ)

จากนั้น:

1. Search for the **Manual Trigger** node.
2. Select it when it appears in the search.

การดำเนินการนี้จะเพิ่ม [Manual Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md) node ลงใน canvas ของคุณ ซึ่งช่วยให้คุณสามารถรัน workflow ได้ตลอดเวลาโดยเลือกปุ่ม **Test workflow**

/// note | Manual triggers
เพื่อการสร้าง workflow ที่เร็วขึ้น คุณสามารถข้ามขั้นตอนนี้ได้ในอนาคต การเพิ่ม node อื่นๆ โดยไม่มี trigger จะเป็นการเพิ่ม Manual Trigger node เข้าไปใน workflow โดยอัตโนมัติ

ในสถานการณ์จริง คุณอาจต้องการตั้งค่า schedule หรือ [trigger](/glossary.md#trigger-node-n8n) อื่นๆ เพื่อรัน workflow
///

## 2. Add the Hacker News node

เลือกไอคอน **+** ทางด้านขวาของ Manual Trigger node เพื่อเปิด nodes panel

จากนั้น:

1. Search for the **Hacker News** node.
2. Select it when it appears in the search.
3. In the **Actions** section, select **Get many items**.

n8n จะเพิ่ม node ลงใน canvas ของคุณ และหน้าต่าง node จะเปิดขึ้นเพื่อแสดงรายละเอียดการกำหนดค่า

## 3. Configure the Hacker News node

เมื่อคุณเพิ่ม node ใหม่ลงใน Editor UI, node นั้นจะถูกเปิดใช้งานโดยอัตโนมัติ รายละเอียด node จะเปิดขึ้นในหน้าต่างพร้อมตัวเลือกหลายอย่าง:

- **Parameters**: ปรับ parameters เพื่อปรับแต่งและควบคุมฟังก์ชันการทำงานของ node
- **Settings**: ปรับ settings เพื่อควบคุมการออกแบบและการ εκτέλεση (execution) ของ node
- **Docs**: เปิดเอกสาร n8n สำหรับ node นี้ในหน้าต่างใหม่


/// note | Parameters vs. Settings
* **Parameters** จะแตกต่างกันไปในแต่ละ node ขึ้นอยู่กับฟังก์ชันการทำงานของมัน
* **Settings** จะเหมือนกันสำหรับทุก nodes
///


### Parameters

เราต้องกำหนดค่า parameters หลายอย่างสำหรับ Hacker News node เพื่อให้ทำงานได้:

- **Resource**: All <br/>
Resource นี้จะเลือก data records (บทความ) ทั้งหมด
- **Operation**: Get Many <br/>
Operation นี้จะดึงบทความที่เลือกทั้งหมด
- **Limit**: 10 <br/>
Parameter นี้จะกำหนดขีดจำกัดจำนวนผลลัพธ์ที่ Get Many operation ส่งคืน
- **Additional Fields** > **Add Field** > **Keyword**: automation <br/>
**Additional fields** เป็นตัวเลือกที่คุณสามารถเพิ่มลงใน nodes บางตัวเพื่อทำให้ request ของคุณเฉพาะเจาะจงมากขึ้นหรือกรองผลลัพธ์ สำหรับตัวอย่างนี้ เราต้องการรับเฉพาะบทความที่มี keyword "automation" <br/>

การกำหนดค่า parameters สำหรับ Hacker News node ควรมีลักษณะดังนี้:

<figure><img src="/_images/courses/level-one/chapter-two/l1-c-2-hacker-news-node-parameters.png" alt="Hacker News node parameters" style="width:100%"><figcaption align = "center"><i>Hacker News node parameters</i></figcaption></figure>

### Settings

ส่วน **Settings** มีตัวเลือกหลายอย่างสำหรับการออกแบบและการ εκτέλεση (execution) ของ node ในกรณีนี้ เราจะกำหนดค่าเฉพาะสอง settings สุดท้าย ซึ่งกำหนดลักษณะที่ปรากฏของ node ใน Editor UI canvas

ใน Hacker News node Settings, แก้ไข:

- **Notes**: Get the 10 latest articles.

    /// note | Node notes
    การเพิ่มคำอธิบายสั้นๆ ใน node เกี่ยวกับสิ่งที่มันทำมักจะมีประโยชน์ สิ่งนี้มีประโยชน์อย่างยิ่งสำหรับ workflows ที่ซับซ้อนหรือแชร์กัน!
    ///

- **Display note in flow?**: toggle to true<br/>
ตัวเลือกนี้จะแสดง Note ใต้ node ใน canvas

การกำหนดค่า settings สำหรับ Hacker News node ควรมีลักษณะดังนี้:

<figure><img src="/_images/courses/level-one/chapter-two/l1-c2-hacker-news-node-setting-configuration.png" alt="Hacker News node settings" style="width:100%"><figcaption align = "center"><i>Hacker News node settings</i></figcaption></figure>


/// note | Renaming a node
คุณสามารถเปลี่ยนชื่อ node ด้วยชื่อที่สื่อความหมายมากขึ้นสำหรับ use case ของคุณ มีสามวิธีในการทำเช่นนี้:

- เลือก node ที่คุณต้องการเปลี่ยนชื่อและกดปุ่ม F2 บนคีย์บอร์ดของคุณพร้อมกัน
- ดับเบิลคลิกที่ node เพื่อเปิดหน้าต่าง node คลิกที่ชื่อของ node ที่มุมซ้ายบนของหน้าต่าง เปลี่ยนชื่อตามที่คุณต้องการ จากนั้นคลิก **Rename** เพื่อบันทึก node ภายใต้ชื่อใหม่
- คลิกขวาที่ node และเลือกตัวเลือก **Rename** หรือเลือก node แล้วกด F2 บนคีย์บอร์ดของคุณ

<figure><img src="/_images/courses/level-one/chapter-two/l1-c2-renaming-a-node-from-the-keyboard.png" alt="Renaming a node" style="width:100%"><figcaption align = "center"><i>Renaming a node from the keyboard</i></figcaption></figure>

หากต้องการค้นหาชื่อ node ดั้งเดิม (ประเภทของ node) ให้เปิดหน้าต่าง node และเลือก **Settings** ด้านล่างของหน้าจะมีประเภทและเวอร์ชันของ node
///

## 4. Execute the node

เลือกปุ่ม **Test step** ในหน้าต่างรายละเอียด node คุณควรเห็นผลลัพธ์ 10 รายการในมุมมอง **Table** ของ Output

<!--This screenshot needs updating now that the button says "Test step" rather than "Execute node"-->
<figure><img src="/_images/courses/level-one/chapter-two/l1-c2-results-in-table-view-for-the-hacker-news-node.png" alt="Results in Table view for the Hacker News node" style="width:100%"><figcaption align = "center"><i>Results in Table view for the Hacker News node</i></figcaption></figure>

### Node executions

/// note | Node execution
Node execution หมายถึงการรัน node นั้นเพื่อดึงหรือประมวลผลข้อมูลที่ระบุ
///

หาก node ทำงานสำเร็จ เครื่องหมายถูกสีเขียวเล็กๆ จะปรากฏขึ้นที่ด้านบนของ node ใน canvas

<figure><img src="/_images/courses/level-one/chapter-two/l1-c2-successfully-executed-workflow.png" alt="Successfully executed workflow" style="width:100%"><figcaption align = "center"><i>Successfully executed workflow</i></figcaption></figure>

หากไม่มีปัญหากับ parameters และทุกอย่างทำงานได้ดี ข้อมูลที่ร้องขอจะแสดงในหน้าต่าง node ในรูปแบบ **Table**, **JSON**, และ **Schema** คุณสามารถสลับระหว่างมุมมองเหล่านี้ได้โดยเลือกมุมมองที่คุณต้องการจากปุ่ม **Table | JSON | Schema** ที่ด้านบนของหน้าต่าง node

/// note | Table vs JSON views
มุมมอง **Table** เป็นค่าเริ่มต้น จะแสดงข้อมูลที่ร้องขอในตาราง โดยที่แถวคือ records และคอลัมน์คือ attributes ที่มีอยู่ของ records เหล่านั้น
///

นี่คือ output ของ Hacker News ของเราในมุมมอง JSON:

<figure><img src="/_images/courses/level-one/chapter-two/l1-c2-results-in-json-view-for-the-hacker-news-node.png" alt="Results in JSON view for the Hacker News node" style="width:100%"><figcaption align = "center"><i>Results in JSON view for the Hacker News node</i></figcaption></figure>

หน้าต่าง node จะแสดงข้อมูลเพิ่มเติมเกี่ยวกับการ εκτέλεση (execution) ของ node:

- ถัดจากชื่อ **Output** สังเกตไอคอนเล็กๆ (จะเป็นเครื่องหมายถูกสีเขียวหากการ εκτέλεση (execution) ของ node สำเร็จ) ข้างๆ กันมีไอคอนข้อมูล หากคุณวางเมาส์เหนือไอคอนนั้น คุณจะได้รับข้อมูลเพิ่มเติมอีกสองส่วนที่สามารถให้ข้อมูลเชิงลึกเกี่ยวกับประสิทธิภาพของแต่ละ node ใน workflow:
    - **Start Time**: เวลาที่การ εκτέλεση (execution) ของ node เริ่มต้น
    - **Execution Time**: ระยะเวลาที่ node ใช้ในการส่งคืนผลลัพธ์นับตั้งแต่เริ่มทำงาน
- ด้านล่างชื่อ **Output** คุณจะสังเกตเห็นข้อมูลอีกส่วนหนึ่ง: **10 items** ฟิลด์นี้แสดงจำนวน items (records) ที่ node request ส่งคืน ในตัวอย่างนี้ คาดว่าจะเป็น 10 เนื่องจากเป็นขีดจำกัดที่เราตั้งไว้ในขั้นตอนที่ 2 แต่ถ้าคุณไม่ได้ตั้งค่าขีดจำกัด การดูว่ามี records กี่รายการที่ส่งคืนจริงก็มีประโยชน์


/// warning | Error in nodes
ไอคอนคำเตือนสีแดงบน node หมายความว่า node มีข้อผิดพลาด สิ่งนี้อาจเกิดขึ้นหาก credentials ของ node หายไปหรือไม่ถูกต้อง หรือ parameters ของ node ไม่ได้กำหนดค่าอย่างถูกต้อง
///
<figure style="text-align:center;"><img src="/_images/courses/level-one/chapter-one/error-node.png" alt="Error in nodes" style="width:30%" align="center"><figcaption align = "center"><i>Error in nodes</i></figcaption></figure>

## 5. Save the workflow

เมื่อคุณแก้ไข node เสร็จแล้ว ให้เลือก **Back to canvas** เพื่อกลับไปยัง canvas หลัก

โดยค่าเริ่มต้น workflow ของคุณจะถูกบันทึกโดยอัตโนมัติเป็น "My workflow"

สำหรับบทเรียนนี้ ให้เปลี่ยนชื่อ workflow เป็น "Hacker News workflow"

/// note | Reminder
คุณสามารถเปลี่ยนชื่อ workflow ได้โดยคลิกที่ชื่อ workflow ที่ด้านบนของ Editor UI
///

เมื่อคุณเปลี่ยนชื่อ workflow แล้ว อย่าลืมบันทึก

มีสองวิธีที่คุณสามารถบันทึก workflow ได้:

- จาก Canvas ใน Editor UI คลิก **Ctrl + S** หรือ **Cmd + S** บนคีย์บอร์ดของคุณ
- เลือกปุ่ม **Save** ที่มุมขวาบนของ Editor UI คุณอาจต้องออกจาก node editor ก่อนโดยคลิกนอกกล่องโต้ตอบ

หากคุณเห็นข้อความ **Saved** สีเทาแทนปุ่ม **Save** แสดงว่า workflow ของคุณถูกบันทึกโดยอัตโนมัติแล้ว

## Summary

ขอแสดงความยินดี คุณเพิ่งสร้าง workflow แรกของคุณสำเร็จ! ในบทเรียนนี้ คุณได้เรียนรู้วิธีใช้ actions ใน app nodes, กำหนดค่า parameters และ settings, และบันทึกและ εκτέλεση (execute) workflow ของคุณ

ในบทเรียนถัดไป คุณจะได้พบกับลูกค้าใหม่ของคุณ Nathan ผู้ซึ่งต้องการ automate งานรายงานการขายของเขา คุณจะได้สร้าง workflow ที่ซับซ้อนมากขึ้นสำหรับ use case ของเขา ซึ่งจะช่วยให้เขามีประสิทธิผลในการทำงานมากขึ้น
