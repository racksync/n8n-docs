---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: tutorial
---

# Dealing with errors in workflows

บางครั้งคุณสร้าง workflow ที่ดี แต่กลับล้มเหลวเมื่อพยายาม execute มัน การ execute workflow อาจล้มเหลวได้จากหลายสาเหตุ ตั้งแต่ปัญหาตรงไปตรงมา เช่น การตั้งค่า node ไม่ถูกต้อง หรือความล้มเหลวใน third-party service ไปจนถึง error ที่ลึกลับกว่านั้น

แต่อย่าเพิ่งตกใจ ในบทเรียนนี้ คุณจะได้เรียนรู้วิธีแก้ไขปัญหา error เพื่อให้ workflow ของคุณกลับมาทำงานได้โดยเร็วที่สุด


## Checking failed workflows

n8n จะติดตามการ executions ของ workflows ของคุณ

เมื่อ workflow ของคุณล้มเหลว คุณสามารถตรวจสอบ Executions log เพื่อดูว่าเกิดอะไรขึ้น Executions log จะแสดงรายการของเวลา execution ล่าสุด, status, mode, และ running time ของ workflows ที่คุณบันทึกไว้

เปิด Executions log โดยเลือก [**Executions**](/workflows/executions/index.md#execution-modes) ในแผงด้านซ้าย

หากต้องการตรวจสอบ execution ที่ล้มเหลวจากรายการ ให้เลือกชื่อหรือปุ่ม **View** ที่ปรากฏขึ้นเมื่อคุณวางเมาส์เหนือแถวของ execution นั้นๆ

<figure><img src="/_images/courses/level-two/chapter-four/explanation_workflowexecutions.png" alt="Executions log" style="width:100%"><figcaption align = "center"><i>Executions log</i></figcaption></figure>


การทำเช่นนี้จะเปิด workflow ในโหมด read-only ซึ่งคุณสามารถดู execution ของแต่ละ node ได้ การแสดงผลแบบนี้สามารถช่วยให้คุณระบุได้ว่า workflow เกิดปัญหาที่จุดใด

หากต้องการสลับระหว่างการดู execution และ editor ให้เลือกปุ่ม **Editor | Executions** ที่ด้านบนของหน้า

<figure><img src="/_images/courses/level-two/chapter-four/explanation_workflowexecutions_readonly.png" alt="Workflow execution view" style="width:100%"><figcaption align = "center"><i>Workflow execution view</i></figcaption></figure>

## Catching erroring workflows

หากต้องการดักจับ workflows ที่ล้มเหลว ให้สร้าง [**Error Workflow**](/flow-logic/error-handling.md) แยกต่างหากด้วย [**Error Trigger node**](/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md) workflow นี้จะ execute ก็ต่อเมื่อ main workflow execution ล้มเหลวเท่านั้น

ใช้ nodes เพิ่มเติมใน **Error Workflow** ของคุณตามความเหมาะสม เช่น การส่งการแจ้งเตือนเกี่ยวกับ workflow ที่ล้มเหลวและ errors ของมันโดยใช้อีเมลหรือ Slack

หากต้องการรับ error messages สำหรับ workflow ที่ล้มเหลว ให้ตั้งค่า **Error Workflow** ใน [Workflow Settings](/workflows/settings.md) เป็น Error Workflow ที่ใช้ **Error Trigger node**

ความแตกต่างเพียงอย่างเดียวระหว่าง workflow ปกติและ Error Workflow คือ workflow หลังจะมี **Error Trigger node** ตรวจสอบให้แน่ใจว่าคุณสร้าง node นี้ก่อนที่จะตั้งค่าให้เป็น Error Workflow ที่กำหนดสำหรับ workflow อื่น

/// note | Error workflows
- หาก workflow ใช้ Error Trigger node คุณไม่จำเป็นต้อง activate workflow นั้น
- หาก workflow มี Error Trigger node โดย default แล้ว workflow นั้นจะใช้ตัวเองเป็น error workflow
- คุณไม่สามารถทดสอบ error workflows เมื่อรัน workflows ด้วยตนเองได้ Error trigger จะทำงานก็ต่อเมื่อ workflow อัตโนมัติเกิด error เท่านั้น
- คุณสามารถตั้งค่า Error Workflow เดียวกันสำหรับหลาย workflows ได้
///

### Exercise

ในบทก่อนหน้านี้ คุณได้สร้าง workflows เล็กๆ หลายอัน ตอนนี้ เลือก workflow หนึ่งที่คุณต้องการ monitor และสร้าง Error Workflow สำหรับมัน:

1. สร้าง Error Workflow ใหม่
2. เพิ่ม **Error Trigger node**
3. เชื่อมต่อ node สำหรับ communication platform ที่คุณเลือกเข้ากับ Error Trigger node เช่น [Slack](/integrations/builtin/app-nodes/n8n-nodes-base.slack.md), [Discord](/integrations/builtin/app-nodes/n8n-nodes-base.discord/index.md), [Telegram](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/index.md), หรือแม้แต่ [Gmail](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md) หรือ [Send Email](/integrations/builtin/core-nodes/n8n-nodes-base.sendemail.md) ทั่วไป
4. ใน workflow ที่คุณต้องการ monitor ให้เปิด [Workflow Settings](/workflows/settings.md) และเลือก Error Workflow ใหม่ที่คุณเพิ่งสร้าง โปรดทราบว่า workflow นี้ต้องทำงานโดยอัตโนมัติเพื่อ trigger error workflow

??? note "Show me the solution"

	workflow สำหรับแบบฝึกหัดนี้มีลักษณะดังนี้:

	<figure><img src="/_images/courses/level-two/chapter-four/exercise_errors_errortriggernode_workflow.png" alt="" style="width:100%"><figcaption align = "center"><i>Error workflow</i></figcaption></figure>

	หากต้องการตรวจสอบการกำหนดค่าของ nodes คุณสามารถคัดลอกโค้ด JSON workflow ด้านล่างและวางลงใน Editor UI ของคุณ:

	```json
	{
		"nodes": [
			{
				"parameters": {},
				"name": "Error Trigger",
				"type": "n8n-nodes-base.errorTrigger",
				"typeVersion": 1,
				"position": [
					720,
					-380
				]
			},
			{
				"parameters": {
					"channel": "channelname",
					"text": "=This workflow {{$node[\"Error Trigger\"].json[\"workflow\"][\"name\"]}}failed.\nHave a look at it here: {{$node[\"Error Trigger\"].json[\"execution\"][\"url\"]}}",
					"attachments": [],
					"otherOptions": {}
				},
				"name": "Slack",
				"type": "n8n-nodes-base.slack",
				"position": [
					900,
					-380
				],
				"typeVersion": 1,
				"credentials": {
					"slackApi": {
						"id": "17",
						"name": "slack_credentials"
					}
				}
			}
		],
		"connections": {
			"Error Trigger": {
				"main": [
					[
						{
							"node": "Slack",
							"type": "main",
							"index": 0
						}
					]
				]
			}
		}
	}
	```



## Throwing exceptions in workflows

อีกวิธีในการแก้ไขปัญหา workflows คือการใส่ [**Stop and Error node**](/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md) ใน workflow ของคุณ node นี้จะ throw error คุณสามารถระบุประเภทของ error ได้:

- **Error Message**: คืนค่า custom message เกี่ยวกับ error
- **Error Object**: คืนค่าประเภทของ error

คุณสามารถใช้ **Stop and Error node** เป็น node สุดท้ายใน workflow เท่านั้น

/// note | When to throw errors
การ throw exceptions ด้วย **Stop and Error node** มีประโยชน์สำหรับการตรวจสอบข้อมูล (หรือสมมติฐานเกี่ยวกับข้อมูล) จาก node และคืนค่า custom error messages

หากคุณกำลังทำงานกับข้อมูลจาก third-party service คุณอาจพบปัญหาเช่น:

- ผลลัพธ์ JSON ที่จัดรูปแบบไม่ถูกต้อง
- ข้อมูลที่มีประเภทผิด (เช่น ข้อมูลตัวเลขที่มีค่าที่ไม่ใช่ตัวเลข)
- ค่าที่หายไป
- Errors จาก remote servers

แม้ว่าข้อมูลที่ไม่ถูกต้องประเภทนี้อาจไม่ทำให้ workflow ล้มเหลวในทันที แต่อาจทำให้เกิดปัญหาในภายหลัง และจากนั้นอาจเป็นเรื่องยากที่จะติดตาม source error นี่คือเหตุผลว่าทำไมจึงควร throw error ณ เวลาที่คุณรู้ว่าอาจมีปัญหา

<figure><img src="/_images/courses/level-two/chapter-four/exercise_errors_stopanderror.png" alt="Stop and Error node with error message" style="width:100%"><figcaption align = "center"><i>Stop and Error node with error message</i></figcaption></figure>
///

