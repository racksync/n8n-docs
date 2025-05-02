---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

<!-- vale from-microsoft.We = NO -->
<!-- vale from-microsoft.FirstPerson = NO -->
# 6. Notifying the Team

ในขั้นตอนนี้ของ workflow คุณจะได้เรียนรู้วิธีส่งข้อความไปยัง Discord channel โดยใช้ [Discord node](/integrations/builtin/app-nodes/n8n-nodes-base.discord/index.md) หลังจากขั้นตอนนี้ workflow ของคุณควรมีลักษณะดังนี้:

[[ workflowDemo("file:////courses/level-one/chapter-5/chapter-5.6.json") ]]

ตอนนี้คุณมีสรุปการคำนวณของ booked orders แล้ว คุณต้องแจ้งทีมของ Nathan ใน Discord channel ของพวกเขา สำหรับ workflow นี้ คุณจะส่งข้อความไปยัง [n8n server](https://discord.gg/G98WXzsjky) บน Discord

ก่อนที่คุณจะเริ่มขั้นตอนด้านล่าง ให้ใช้ลิงก์ด้านบนเพื่อเชื่อมต่อกับ n8n server บน Discord ตรวจสอบให้แน่ใจว่าคุณสามารถเข้าถึง channel `#course-level-1` ได้

/// note | Communication app nodes
คุณสามารถแทนที่ Discord node ด้วย communication app อื่นได้ ตัวอย่างเช่น n8n ยังมี nodes สำหรับ [Slack](/integrations/builtin/app-nodes/n8n-nodes-base.slack.md) และ [Mattermost](/integrations/builtin/app-nodes/n8n-nodes-base.mattermost.md)
///

ใน workflow ของคุณ ให้เพิ่ม Discord node ที่เชื่อมต่อกับ Code node

เมื่อคุณค้นหา Discord node ให้มองหา **Message Actions** และเลือก **Send a message** เพื่อเพิ่ม node

ในหน้าต่าง Discord node กำหนดค่า parameters เหล่านี้:

- **Connection Type**: Select **Webhook**.
- **Credential for Discord Webhook**: Select **- Create New Credential -**.
    - คัดลอก **Webhook URL** จากอีเมลที่คุณได้รับเมื่อคุณสมัครเข้าร่วมคอร์สนี้และวางลงในฟิลด์ **Webhook URL** ของ credentials
    - เลือก **Save** จากนั้นปิดกล่องโต้ตอบ credentials
- **Operation**: Select **Send a Message**.
- **Message**:
    - เลือกแท็บ **Expression** ทางด้านขวาของฟิลด์ Message
    - คัดลอกข้อความด้านล่างและวางลงในหน้าต่าง **Expression** หรือสร้างด้วยตนเองโดยใช้ **Expression Editor**
		```
		This week we've {{$json["totalBooked"]}} booked orders with a total value of {{$json["bookedSum"]}}. My Unique ID: {{ $('HTTP Request').params["headerParameters"]["parameters"][0]["value"] }}
		```

ตอนนี้เลือก **Test step** ใน Discord node หากทุกอย่างทำงานได้ดี คุณควรเห็น output นี้ใน n8n:

<figure><img src="/_images/courses/level-one/chapter-five/l1-c5-5-6-discord-output.png" alt="Discord node output" style="width:100%"><figcaption align = "center"><i>Discord node output</i></figcaption></figure>

และข้อความของคุณควรปรากฏใน Discord channel #course-level-1:

<figure><img src="/_images/courses/level-one/chapter-two/discord-output.png" alt="Discord message" style="width:100%"><figcaption align = "center"><i>Discord message</i></figcaption></figure>

## What's next?

**Nathan 🙋**: เหลือเชื่อ คุณช่วยประหยัดเวลาทำงานที่น่าเบื่อของฉันไปหลายชั่วโมงแล้ว! ตอนนี้ฉันสามารถ εκτέλεση (execute) workflow นี้ได้เมื่อฉันต้องการ ฉันแค่ต้องจำไว้ว่าต้องรันมันทุกเช้าวันจันทร์ เวลา 9.00 น.

**You 👩‍🔧**: ไม่ต้องกังวลเรื่องนั้น คุณสามารถ schedule workflow ให้ทำงานในวัน เวลา หรือช่วงเวลาที่ระบุได้จริง ฉันจะตั้งค่านี้ในขั้นตอนถัดไป
