---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: TheHive 5 Trigger node documentation
description: Learn how to use the TheHive 5 Trigger node in n8n. Follow technical documentation to integrate TheHive 5 Trigger node into your workflows.
contentType: [integration, reference]
---

# TheHive 5 Trigger node

ใช้ TheHive 5 Trigger node เพื่อตอบสนอง event ต่าง ๆ ใน [TheHive](https://strangebee.com/thehive/){:target=_blank .external-link} และเชื่อมต่อ TheHive กับแอปอื่น ๆ ได้ n8n รองรับ event หลากหลาย เช่น alert, case, comment, page และ task

ในหน้านี้จะมีรายการ event ที่ TheHive5 Trigger node สามารถตอบสนองได้ พร้อมลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | TheHive and TheHive 5
n8n มี node สำหรับ TheHive สองแบบ ใช้ node นี้ (TheHive 5 Trigger) ถ้าคุณต้องการใช้ API เวอร์ชัน 5 ของ TheHive ถ้าต้องการใช้เวอร์ชัน 3 หรือ 4 ให้ใช้ [TheHive Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.thehivetrigger.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่ช่วยให้เริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [TheHive 5 Trigger integrations](https://n8n.io/integrations/thehive-5-trigger/){:target=_blank .external-link} ของ n8n
///

## Events

* Alert 
	* Created
	* Deleted
	* Updated
* Case
	* Created
	* Deleted
	* Updated
* Comment
	* Created
	* Deleted
	* Updated
* Observable
	* Created
	* Deleted
	* Updated
* Page
	* Created
	* Deleted
	* Updated
* Task
	* Created
	* Deleted
	* Updated
* Task log
	* Created
	* Deleted
	* Updated

## Related resources

n8n มี app node สำหรับ TheHive 5 คุณสามารถดูเอกสาร node ได้ [ที่นี่](/integrations/builtin/app-nodes/n8n-nodes-base.thehive5.md)

ดูเอกสาร [TheHive's documentation](https://docs.strangebee.com/){:target=_blank .external-link} สำหรับรายละเอียดเกี่ยวกับบริการนี้


## Configure a webhook in TheHive

วิธีตั้งค่า webhook สำหรับ TheHive instance ของคุณ:

1. คัดลอก URL webhook สำหรับ testing และ production จาก TheHive Trigger node
2. เพิ่มบรรทัดต่อไปนี้ในไฟล์ `application.conf` (ไฟล์ config ของ TheHive):

	```
	notification.webhook.endpoints = [
		{
			name: TESTING_WEBHOOK_NAME
			url: TESTING_WEBHOOK_URL
			version: 0
			wsConfig: {}
			includedTheHiveOrganisations: ["ORGANIZATION_NAME"]
			excludedTheHiveOrganisations: []
		},
		{
			name: PRODUCTION_WEBHOOK_NAME
			url: PRODUCTION_WEBHOOK_URL
			version: 0
			wsConfig: {}
			includedTheHiveOrganisations: ["ORGANIZATION_NAME"]
			excludedTheHiveOrganisations: []
		}
	]
	```

3. แทนที่ `TESTING_WEBHOOK_URL` และ `PRODUCTION_WEBHOOK_URL` ด้วย URL ที่คัดลอกมา
4. แทนที่ `TESTING_WEBHOOK_NAME` และ `PRODUCTION_WEBHOOK_NAME` ด้วยชื่อ endpoint ที่ต้องการ
5. แทนที่ `ORGANIZATION_NAME` ด้วยชื่อองค์กรของคุณ
6. รันคำสั่ง cURL ต่อไปนี้เพื่อเปิดใช้งาน notification:
	```sh
	curl -XPUT -uTHEHIVE_USERNAME:THEHIVE_PASSWORD -H 'Content-type: application/json' THEHIVE_URL/api/config/organisation/notification -d '
	{
		"value": [
			{
			"delegate": false,
			"trigger": { "name": "AnyEvent"},
			"notifier": { "name": "webhook", "endpoint": "TESTING_WEBHOOK_NAME" }
			},
			{
			"delegate": false,
			"trigger": { "name": "AnyEvent"},
			"notifier": { "name": "webhook", "endpoint": "PRODUCTION_WEBHOOK_NAME" }
			}
		]
	}'
	```
