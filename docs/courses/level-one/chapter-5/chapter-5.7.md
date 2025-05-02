---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

<!-- vale from-microsoft.We = NO -->
<!-- vale from-microsoft.FirstPerson = NO -->
# 7. Scheduling the Workflow

ในขั้นตอนนี้ของ workflow คุณจะได้เรียนรู้วิธี schedule workflow ของคุณเพื่อให้ทำงานโดยอัตโนมัติตามเวลา/ช่วงเวลาที่กำหนดโดยใช้ Schedule Trigger node หลังจากขั้นตอนนี้ workflow ของคุณควรมีลักษณะดังนี้:

[[ workflowDemo("file:////courses/level-one/finished.json") ]]

workflow ที่คุณสร้างขึ้นมาจนถึงตอนนี้จะ εκτέλεση (execute) เฉพาะเมื่อคุณคลิก **Test Workflow** เท่านั้น แต่ Nathan ต้องการให้มันทำงานโดยอัตโนมัติทุกเช้าวันจันทร์ คุณสามารถทำได้ด้วย [Schedule Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/index.md) ซึ่งช่วยให้คุณสามารถ schedule workflows ให้ทำงานเป็นระยะตามวันที่ เวลา หรือช่วงเวลาที่กำหนด

เพื่อให้บรรลุเป้าหมายนี้ เราจะลบ Manual Trigger node ที่เราเริ่มต้นด้วยออก และแทนที่ด้วย Schedule Trigger node แทน

## Remove the Manual Trigger node

ขั้นแรก มาลบ Manual Trigger node กัน:

1. Select the Manual Trigger node connected to your HTTP Request node.
2. Select the trash can icon to delete.

การดำเนินการนี้จะลบ Manual Trigger node ออก และคุณจะเห็นตัวเลือก "Add first step"

## Add the Schedule Trigger node

1. Open the nodes panel and search for **Schedule Trigger**.
2. Select it when it appears in the search results.

ในหน้าต่าง Schedule Trigger node กำหนดค่า parameters เหล่านี้:

- **Trigger Interval**: Select **Weeks**.
- **Weeks Between Triggers**: Enter `1`.
- **Trigger on weekdays**: Select **Monday** (and remove **Sunday** if added by default).
- **Trigger at Hour**: Select **9am**.
- **Trigger at Minute**: Enter `0`.

Schedule Trigger node ของคุณควรมีลักษณะดังนี้:

<figure><img src="/_images/courses/level-one/chapter-five/l1-c5-5-7-schedule-trigger-node.png" alt="Schedule Trigger Node" style="width:100%"><figcaption align = "center"><i>Schedule Trigger Node</i></figcaption></figure>

/// warning | Keep in mind
เพื่อให้แน่ใจว่าการ scheduling ด้วย Schedule Trigger node ถูกต้องแม่นยำ อย่าลืมตั้งค่า timezone ที่ถูกต้องสำหรับ [n8n instance](/manage-cloud/set-cloud-timezone.md) ของคุณ หรือ [workflow's settings](/workflows/settings.md) Schedule Trigger node จะใช้ timezone ของ workflow หากมีการตั้งค่าไว้; มันจะใช้ timezone ของ n8n instance หากไม่ได้ตั้งค่าไว้
///

## Connect the Schedule Trigger node

กลับไปที่ canvas และเชื่อมต่อ Schedule Trigger node ของคุณเข้ากับ HTTP Request node โดยลากลูกศรจากมันไปยัง HTTP Request node

workflow เต็มของคุณควรมีลักษณะดังนี้:

[[ workflowDemo("file:////courses/level-one/finished.json") ]]

## What's next?

**You 👩‍🔧**: นั่นคือทั้งหมดสำหรับ workflow! ฉันได้เพิ่มและกำหนดค่า nodes ที่จำเป็นทั้งหมดแล้ว ตอนนี้ทุกครั้งที่คุณคลิก **Test workflow**, n8n จะ εκτέλεση (execute) nodes ทั้งหมด: การรับ, การกรอง, การคำนวณ และการถ่ายโอนข้อมูลการขาย

**Nathan 🙋**: นี่คือสิ่งที่ฉันต้องการเลย! workflow ของฉันจะทำงานโดยอัตโนมัติทุกเช้าวันจันทร์ ถูกต้องไหม?

**You 👩‍🔧**: ไม่เร็วขนาดนั้น หากต้องการทำเช่นนั้น คุณต้อง activate workflow ของคุณ ฉันจะทำสิ่งนี้ในขั้นตอนถัดไปและแสดงวิธีตีความ execution log ให้คุณดู
<!-- vale from-microsoft.We = YES -->
