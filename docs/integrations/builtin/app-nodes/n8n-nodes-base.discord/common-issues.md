---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Discord node common issues
description: Documentation for common issues and questions in the Discord node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: high
---

# Discord node common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปบางประการเกี่ยวกับ [Discord node](/integrations/builtin/app-nodes/n8n-nodes-base.discord/index.md) และขั้นตอนในการแก้ไขหรือแก้ไขปัญหา

## Add extra fields to embeds

ข้อความ Discord สามารถเลือกที่จะรวม `embeds` ซึ่งเป็นส่วนประกอบ rich preview ที่สามารถรวม title, description, image, link และอื่นๆ ได้

Discord node รองรับ `embeds` เมื่อใช้ operation **Send** บน resource **Message** เลือก **Add Embeds** เพื่อตั้งค่าฟิลด์เพิ่มเติม รวมถึง Description, Author, Title, URL และ URL Image

หากต้องการเพิ่มฟิลด์ที่ไม่ได้รวมไว้ตามค่าเริ่มต้น ให้ตั้งค่า **Input Method** เป็น **Raw JSON** จากตรงนี้ ให้เพิ่ม JSON object ไปยัง parameter **Value** เพื่อกำหนด [field names](https://discord.com/developers/docs/resources/message#embed-object) และค่าที่คุณต้องการรวม

ตัวอย่างเช่น หากต้องการรวม `footer` และ `fields` ซึ่งไม่มีให้ใช้งานโดยใช้ Input Method **Enter Fields** คุณสามารถใช้ JSON object เช่นนี้:

```json
{
    "author": "My Name",
	"url": "https://discord.js.org",
	"fields": [
		{
			"name": "Regular field title",
			"value": "Some value here"
		}
	],
	"footer": {
		"text": "Some footer text here",
		"icon_url": "https://i.imgur.com/AfFp7pu.png"
	}
}
```

คุณสามารถเรียนรู้เพิ่มเติมเกี่ยวกับ embeds ได้ใน [Using Webhooks and Embeds | Discord](https://discord.com/safety/using-webhooks-and-embeds)

หากคุณประสบปัญหาเมื่อทำงานกับ embeds ด้วย Discord node คุณสามารถใช้ [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) กับ credentials ของ Discord ที่มีอยู่ของคุณเพื่อ `POST` ไปยัง URL ต่อไปนี้:

```
https://discord.com/api/v10/channels/<CHANNEL_ID>/messages
```

ใน `body` ให้รวมข้อมูล embed ของคุณใน `content` ของข้อความดังนี้:

```json
{
	"content": "Test",
	"embeds": [
		{
			"author": "My Name",
			"url": "https://discord.js.org",
			"fields": [
				{
					"name": "Regular field title",
					"value": "Some value here"
				}
			],
			"footer": {
				"text": "Some footer text here",
				"icon_url": "https://i.imgur.com/AfFp7pu.png"
			}
		}
	]
}
```

## Mention users and channels

หากต้องการ mention ผู้ใช้และช่องในข้อความ Discord คุณต้องจัดรูปแบบข้อความของคุณตาม [Discord's message formatting guidelines](https://discord.com/developers/docs/reference#message-formatting)

หากต้องการ mention ผู้ใช้ คุณจำเป็นต้องทราบ `user ID` ของผู้ใช้ Discord โปรดทราบว่า `user ID` แตกต่างจากชื่อที่แสดงของผู้ใช้ ในทำนองเดียวกัน คุณต้องมี `channel ID` เพื่อลิงก์ไปยังช่องเฉพาะ

คุณสามารถเรียนรู้วิธีเปิดใช้งาน `developer mode` และคัดลอก `user ID` หรือ `channel ID` ได้ใน [Discord's documentation on finding User/Server/Message IDs](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID)

เมื่อคุณมี `user ID` หรือ `channel ID` แล้ว คุณสามารถจัดรูปแบบข้อความของคุณด้วย syntax ต่อไปนี้:

* **User**: `<@USER_ID>`
* **Channel**: `<#CHANNEL_ID>`
* **Role**: `<@&ROLE_ID>`
