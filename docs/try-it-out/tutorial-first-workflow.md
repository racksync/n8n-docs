--- 
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Workflow แรกของคุณ
description: สร้าง workflow แรกของคุณใน n8n และเรียนรู้แนวคิดสำคัญ
contentType: tutorial
---

# Your first workflow

คู่มือนี้จะแสดงวิธีสร้าง [workflow](/glossary.md#workflow-n8n) ใน n8n พร้อมอธิบายแนวคิดหลักๆ ไปด้วย คุณจะได้เรียนรู้:

* สร้าง workflow ตั้งแต่เริ่มต้น
* เข้าใจแนวคิดและทักษะสำคัญ เช่น:
    * การเริ่ม workflow ด้วย trigger nodes
    * การตั้งค่า [credentials](/glossary.md#credential-n8n)
    * การประมวลผลข้อมูล
    * การใส่ logic ใน n8n workflow
    * การใช้ [expressions](/glossary.md#expression-n8n)

!["Screenshot of the completed workflow"](/_images/try-it-out/tutorial-first.png)

Quickstart นี้ใช้ [n8n Cloud](/manage-cloud/overview.md) ซึ่งเหมาะกับมือใหม่ มีรุ่นทดลองใช้ฟรี - ถ้ายังไม่มีบัญชี [สมัครเลย](https://app.n8n.cloud/register)

## Step one: Create a new workflow

เมื่อคุณเปิด n8n คุณจะเจออย่างใดอย่างหนึ่ง:

* หน้าต่างต้อนรับพร้อมปุ่มใหญ่สองปุ่ม: เลือก **Start from Scratch** เพื่อสร้าง workflow ใหม่
* รายการ **Workflows** ในหน้า **Overview**: เลือก **Create Workflow** เพื่อสร้าง workflow ใหม่

## Step two: Add a trigger node

n8n มีสองวิธีในการเริ่ม workflow:

* กดเอง โดยเลือก **Test Workflow**
* อัตโนมัติ โดยใช้ trigger node เป็น node แรก trigger node จะรัน workflow ตามเหตุการณ์ภายนอกหรือที่คุณตั้งไว้

สำหรับ tutorial นี้ เราจะใช้ [Schedule trigger](/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/index.md) เพื่อให้ workflow ทำงานตามเวลาที่กำหนด:

1. เลือก **Add first step**
1. ค้นหา **Schedule** n8n จะแสดงรายการ nodes ที่ตรงกับที่ค้นหา
1. เลือก **Schedule Trigger** เพื่อเพิ่ม node ลงบน canvas n8n จะเปิด node ให้เลย
1. ที่ **Trigger Interval** เลือก **Weeks**
1. ที่ **Weeks Between Triggers** ใส่ `1`
1. ตั้งเวลาและวัน ตัวอย่างนี้เลือก **Monday** ใน **Trigger on Weekdays**, เลือก **9am** ใน **Trigger at Hour** และใส่ `0` ใน **Trigger at Minute**
1. ปิดหน้ารายละเอียด node เพื่อกลับไปที่ canvas

## Step three: Add the NASA node and set up credentials

[NASA node](/integrations/builtin/app-nodes/n8n-nodes-base.nasa.md) จะเชื่อมต่อกับ [public APIs](https://api.nasa.gov/){:target=_blank .external-link} ของ NASA เพื่อดึงข้อมูลที่น่าสนใจ เราจะใช้ข้อมูลเรียลไทม์จาก API เพื่อดูเหตุการณ์เกี่ยวกับดวงอาทิตย์

??? explanation "Credentials"
    Credentials คือข้อมูลส่วนตัวที่แอปหรือบริการต่างๆ ออกให้เพื่อยืนยันตัวตนคุณ และอนุญาตให้เชื่อมต่อหรือแชร์ข้อมูลระหว่างแอป/บริการกับ n8n node ข้อมูลที่ต้องใช้จะแตกต่างกันไปตามแต่ละแอป/บริการ คุณควรระวังในการแชร์หรือเปิดเผย credentials นอก n8n

1. เลือกตัวเชื่อมต่อ **Add node** <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span> บน Schedule Trigger node
1. ค้นหา **NASA** n8n จะแสดงรายการ nodes ที่ตรงกับที่ค้นหา
1. เลือก **NASA** เพื่อดูรายการ operations
1. ค้นหาและเลือก **Get a DONKI solar flare** อันนี้จะดึงรายงาน solar flares ล่าสุด เมื่อเลือกแล้ว n8n จะเพิ่ม node ลงบน canvas และเปิด node ให้เลย
1. ถ้าจะใช้ NASA APIs ต้องตั้งค่า credentials:
    1. เลือก dropdown **Credential for NASA API**
    1. เลือก **Create new credential** n8n จะเปิดหน้าตั้งค่า credentials
    1. ไปที่ [NASA APIs](https://api.nasa.gov/){:target=_blank .external-link} แล้วกรอกฟอร์มที่ลิงก์ **Generate API Key** เว็บไซต์ NASA จะสร้าง key และส่งไปที่อีเมลที่คุณกรอก
    1. เช็คอีเมล หา API key แล้ว copy ไปวางใน **API Key** ใน n8n
    1. เลือก **Save**
    1. ปิดหน้าจอ credentials กลับมาที่ node credentials ใหม่จะถูกเลือกให้อัตโนมัติใน **Credential for NASA API**

1. โดยปกติ DONKI Solar Flare จะให้ข้อมูลย้อนหลัง 30 วัน ถ้าอยากดูแค่สัปดาห์ล่าสุด ให้ใช้ **Additional Fields**:
    1. เลือก **Add field**
    1. เลือก **Start date**
    1. ถ้าอยากให้รายงานเริ่มจากหนึ่งสัปดาห์ก่อน ใช้ expression: ข้าง **Start date** เลือกแท็บ **Expression** แล้วกดปุ่มขยาย <span class="inline-image">![Add node icon](/_images/common-icons/open-expression-editor.png){.off-glb}</span> เพื่อเปิด editor เต็ม
    1. ในช่อง **Expression** ใส่โค้ดนี้:
    ```js
    {{ $today.minus(7, 'days') }}
    ```
    อันนี้จะสร้างวันที่ย้อนหลัง 7 วันจากวันนี้

    ![image showing the expression above generating a date](/_images/try-it-out/tutorial-date.png)

    ??? explanation "Date and time formats in n8n..."
        n8n ใช้ Luxon ในการจัดการวันที่และเวลา และมีตัวแปร `$now` กับ `$today` ให้ใช้สะดวกๆ ดูเพิ่มที่ [Expressions > Luxon](/code/cookbook/luxon.md)

1. ปิด modal **Edit Expression** เพื่อกลับไปที่ NASA node
1. ตอนนี้ลองเช็คว่า node ทำงานถูกไหมและคืนวันที่ที่ต้องการหรือเปล่า: เลือก **Test step** เพื่อรัน node ด้วยตัวเอง n8n จะเรียก NASA API และแสดงรายละเอียด solar flares 7 วันที่ผ่านมาใน **OUTPUT**
1. ปิด NASA node เพื่อกลับไปที่ workflow canvas

## Step four: Add logic with the If node

n8n รองรับ logic ที่ซับซ้อนใน workflow ใน tutorial นี้เราจะใช้ [If node](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) เพื่อสร้างสอง branch ที่แต่ละอันจะสร้างรายงานจากข้อมูล NASA Solar flares มีการแบ่งคลาส 5 แบบ เราจะใส่ logic ให้รายงานคลาสต่ำไปออกทางหนึ่ง คลาสสูงไปอีกทาง

เพิ่ม If node:

1. เลือกตัวเชื่อมต่อ **Add node** <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span> บน NASA node
1. ค้นหา **If** n8n จะแสดงรายการ nodes ที่ตรงกับที่ค้นหา
1. เลือก **If** เพื่อเพิ่ม node ลงบน canvas n8n จะเปิด node ให้เลย
1. ต้องเช็คค่าของ property `classType` ในข้อมูล NASA ทำแบบนี้:
    1. ลาก **classType** ไปใส่ **Value 1**

        /// note | Make sure you ran the NASA node in the previous section
        ถ้ายังไม่ได้รัน NASA node ในขั้นตอนก่อนหน้า จะไม่เห็นข้อมูลให้เลือกในขั้นตอนนี้
        ///

    1. เปลี่ยนการเปรียบเทียบเป็น **String > Contains**
    1. ที่ **Value 2** ใส่ **X** อันนี้คือคลาสสูงสุดของ solar flare ขั้นถัดไปจะสร้างรายงานสองแบบ: อันหนึ่งสำหรับ solar flares คลาส X อีกอันสำหรับคลาสที่เล็กกว่า
1. ตอนนี้ลองเช็คว่า node ทำงานถูกไหมและคืนค่าตามที่ต้องการหรือเปล่า: เลือก **Test step** เพื่อรัน node ด้วยตัวเอง n8n จะทดสอบข้อมูลกับเงื่อนไข และแสดงผลลัพธ์ที่ตรงกับ true หรือ false ใน **OUTPUT**

    /// note | Weeks without large solar flares
    ใน tutorial นี้ใช้ข้อมูลสด ถ้าไม่มี solar flares คลาส X ตอนรัน workflow ให้ลองเปลี่ยน **X** ใน **Value 2** เป็น **A**, **B**, **C** หรือ **M** แทน
    ///

1. ถ้าพอใจว่า node คืนเหตุการณ์ได้แล้ว ปิด node กลับไปที่ canvas

## Step five: Output data from your workflow

ขั้นตอนสุดท้ายของ workflow คือส่งรายงานสองแบบเกี่ยวกับ solar flares ตัวอย่างนี้จะส่งข้อมูลไปที่ [Postbin](https://www.toptal.com/developers/postbin/){:target=_blank .external-link} ซึ่งเป็นบริการรับข้อมูลและแสดงผลบนเว็บชั่วคราว

1. ที่ If node เลือกตัวเชื่อมต่อ **Add node** <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span> ที่ป้าย **true**
1. ค้นหา **PostBin** n8n จะแสดงรายการ nodes ที่ตรงกับที่ค้นหา
1. เลือก **PostBin**
1. เลือก **Send a request** n8n จะเพิ่ม node ลงบน canvas และเปิด node ให้เลย
1. ไปที่ [Postbin](https://www.toptal.com/developers/postbin/){:target=_blank .external-link} แล้วเลือก **Create Bin** เปิดแท็บนี้ทิ้งไว้เพื่อกลับมาดูผลตอนทดสอบ workflow
1. คัดลอก bin ID จะหน้าตาประมาณ `1651063625300-2016451240051`
1. ใน n8n วาง Postbin ID ลงใน **Bin ID**
1. ตั้งค่าข้อมูลที่จะส่งไป Postbin ข้าง **Bin Content** เลือกแท็บ **Expression** (ต้องเอาเมาส์ไปวางบน **Bin Content** ก่อนถึงจะเห็นแท็บนี้) แล้วกดปุ่มขยาย <span class="inline-image">![Add node icon](/_images/common-icons/open-expression-editor.png){.off-glb}</span> เพื่อเปิด editor เต็ม
1. ตอนนี้สามารถลากฟิลด์ที่ต้องการจาก output ของ If Node ไปใส่ใน editor ได้เลยเพื่อสร้าง reference อัตโนมัติ กรณีนี้คือ 'classType'
1. พอลากลง editor แล้วจะกลายเป็น reference แบบนี้: `{{$json["classType"]}}` เติมข้อความเข้าไปให้เต็มเป็น:

    ```js
    There was a solar flare of class {{$json["classType"]}}
    ```

    ![image showing the expression above generating output](/_images/try-it-out/tutorial-expression.png)

1. ปิด editor expression กลับไปที่ node
1. ปิด Postbin node กลับไปที่ canvas
1. เพิ่ม Postbin node อีกอันสำหรับ path **false** จาก If node:
    1. เอาเมาส์ไปวางบน Postbin node แล้วเลือก **Node context menu** <span class="inline-image">![Node context menu icon](/_images/common-icons/node-context-menu.png){.off-glb}</span> > **Duplicate node** เพื่อก็อปปี้ Postbin node แรก
    1. ลากตัวเชื่อมต่อ **false** จาก If node ไปที่ด้านซ้ายของ Postbin node ใหม่

## Step six: Test the workflow

1. ตอนนี้ลองทดสอบ workflow ทั้งหมดได้เลย เลือก **Test Workflow** n8n จะรัน workflow และแสดงแต่ละขั้นตอน
1. กลับไปที่ Postbin bin ของคุณ รีเฟรชหน้าดู output
1. ถ้าอยากให้ workflow นี้ทำงานอัตโนมัติทุกสัปดาห์ ต้องเปิดใช้งานโดยเลือกสวิตช์ **Active**

/// note | Time limit
Bin ของ Postbin จะอยู่ได้ 30 นาทีหลังสร้าง ถ้าเกินเวลานี้อาจต้องสร้าง bin ใหม่และอัปเดต ID ใน Postbin nodes
///

## Congratulations

ตอนนี้คุณมี workflow ที่ใช้งานได้จริงและทำอะไรที่มีประโยชน์แล้ว! หน้าตาควรจะประมาณนี้:

[[ workflowDemo("file:///try-it-out/quickstart/tutorial.json") ]]

ระหว่างทางคุณได้เรียนรู้ว่า:

- วิธีหา node ที่ต้องการและเชื่อมต่อกัน
- วิธีใช้ expressions เพื่อจัดการข้อมูล
- วิธีสร้าง credentials และแนบกับ node
- วิธีใส่ logic ใน workflow

คุณสามารถต่อยอดเพิ่มอะไรอีกเยอะ (เช่น เพิ่ม credentials กับ node เพื่อส่งอีเมลผลลัพธ์ให้ตัวเอง) หรืออาจมีโปรเจกต์เฉพาะในใจอยู่แล้ว ไม่ว่าขั้นตอนต่อไปจะเป็นอะไร ลองดู resources ด้านล่างนี้ได้เลย

## Next steps

- สนใจว่า AI ทำอะไรได้บ้าง? ดู [how to build an AI chat agent with n8n](/advanced-ai/intro-tutorial.md)
- เรียน [text courses](/courses/index.md) หรือ [video courses](/video-courses.md) ของ n8n
- ดูตัวอย่าง workflow เพิ่มเติมใน [workflow templates](https://n8n.io/workflows/){:target=_blank .external-link}
