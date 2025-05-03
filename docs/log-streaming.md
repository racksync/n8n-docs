---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
description: ส่ง events จาก n8n ไปยังเครื่องมือ logging ของคุณ
contentType: howto
---

# Log streaming

/// info | Feature availability
Log streaming มีให้ใช้งานในแผน Enterprise Self-hosted และ Cloud
///

Log streaming ช่วยให้คุณสามารถส่ง events จาก n8n ไปยัง logging tools ของคุณเองได้ สิ่งนี้ช่วยให้คุณจัดการการ monitoring n8n ของคุณในกระบวนการ alerting และ logging ของคุณเอง

## Set up log streaming

หากต้องการใช้ log streaming คุณต้องเพิ่ม streaming destination

1. ไปที่ **Settings** > **Log Streaming**
2. เลือก **Add new destination**
3. เลือกประเภท destination ของคุณ n8n จะเปิด modal **New Event Destination**
4. ใน modal **New Event Destination** ให้ป้อนข้อมูลการกำหนดค่าสำหรับ event destination ของคุณ ข้อมูลเหล่านี้ขึ้นอยู่กับประเภทของ destination ที่คุณกำลังใช้
5. เลือก **Events** เพื่อเลือก events ที่จะ stream
6. เลือก **Save**

/// note | Self-hosted users
หากคุณ self-host n8n คุณสามารถกำหนดค่าพฤติกรรม log streaming เพิ่มเติมได้โดยใช้ [Environment variables](/hosting/configuration/environment-variables/logs.md#log-streaming)
///
## Events

มี events ต่อไปนี้ให้ใช้งาน คุณสามารถเลือก events ที่จะ stream ได้ใน **Settings** > **Log Streaming** > **Events**

* Workflow
	* Started
	* Success
	* Failed
* Node executions
	* Started
	* Finished
* Audit
	* User signed up
	* User updated
	* User deleted
	* User invited
	* User invitation accepted
	* User re-invited
	* User email failed
	* User reset requested
	* User reset
	* User credentials created
	* User credentials shared
	* User credentials updated
	* User credentials deleted
	* User API created
	* User API deleted
	* Package installed
	* Package updated
	* Package deleted
	* Workflow created
	* Workflow deleted
	* Workflow updated
* AI node logs
	* Memory get messages
	* Memory added message
	* Output parser get instructions
	* Output parser parsed
	* Retriever get relevant documents
	* Embeddings embedded document
	* Embeddings embedded query
	* Document processed
	* Text splitter split
	* Tool called
	* Vector store searched
	* LLM generated
	* Vector store populated

## Destinations

n8n รองรับ destination types สามประเภท:

* A syslog server
* A generic webhook
* A Sentry client
