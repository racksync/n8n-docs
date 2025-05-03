---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: จัดการ Variables
description: จัดการค่า variable ใน n8n โดยใช้ API และ source control
contentType: howto
---

# Manage variables

n8n จะไม่ sync ค่า variable กับ Git คุณต้องตั้งค่า credentials เองตอนตั้ง instance ใหม่ คุณเลือกได้ว่าจะตั้งค่า variable เอง หรือ [ใช้ API](#manage-variables-using-the-api)

## Manage variables using the API

n8n จะ sync เฉพาะชื่อ variable แต่จะไม่ push ค่า variable ไปที่ Git provider คุณสามารถเลือกได้ว่า

* ตั้งค่า variable ใน n8n เอง
* ตั้งค่า variable ผ่าน n8n API โดยใช้ endpoint `/pull`

การจัดการ variable ผ่าน API มีข้อดีหลายอย่าง:

* อัปเดตค่า variable อัตโนมัติได้ด้วย CI (continuous integration) tool
* อาจจะป้องกันค่าไม่ให้รั่วไหลได้ด้วย

เช่น คุณเก็บค่าไว้ใน [GitHub secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets){:target=_blank .external-link} แล้ว populate variable ใน n8n ด้วย API call จาก [GitHub Action](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions){:target=_blank .external-link}

ถ้าจะจัดการ variable ด้วย API ให้ส่ง `POST` ไปที่ `/source-control/pull`:

```curl
	curl --location '<YOUR-INSTANCE-URL>/api/v1/source-control/pull' \
	--header 'Content-Type: application/json' \
	--header 'X-N8N-API-KEY: <YOUR-API-KEY>' \
	--data '{
	"force": true,
	"variables": { 
			"key1": "value1",
			"key2": "value2"
	}
	}
	'
```

ถ้ามี key อยู่แล้วใน n8n, API call จะ update ค่า ถ้ายังไม่มีจะสร้าง variable ใหม่

หลังตั้งค่าด้วย API แล้ว คุณสามารถแก้ไข variable ใน n8n ได้ตามปกติ แล้ว push/pull ได้เหมือนเดิม
