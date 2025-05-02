---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: n8n
description: Documentation for the n8n node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: medium
---

# n8n

Node นี้ใช้สำหรับเชื่อมต่อกับ n8n เอง ช่วยให้คุณสามารถใช้งาน [n8n API](/api/index.md) ใน workflow ของคุณได้

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ [n8n REST API documentation](/api/index.md) สำหรับวิธีใช้งาน n8n API และดู [API endpoint reference](/api/api-reference.md) สำหรับการใช้งาน endpoint โดยตรง

/// note | Credentials
คุณสามารถดูข้อมูลเกี่ยวกับการยืนยันตัวตน (authentication) สำหรับ node นี้ได้ที่ [API authentication](/api/authentication.md)
///

/// warning | SSL
Node นี้ไม่รองรับ SSL ถ้า server ของคุณต้องการเชื่อมต่อแบบ SSL ให้ใช้ [HTTP Request node](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) เพื่อเรียก [n8n API](/api/index.md) แทน
โดย HTTP Request node จะมีตัวเลือกให้ [provide the SSL certificate](/integrations/builtin/credentials/httprequest.md#provide-an-ssl-certificate)
///

## Operations

* Audit
	* [**Generate** a security audit](#generate-audit)
* Credential
	* [**Create** a credential](#create-credential)
	* [**Delete** a credential](#delete-credential)
	* [**Get Schema**](#get-credential-schema): ใช้สำหรับดึง schema ของ credential ตาม type ที่ต้องการ
* Execution
	* [**Get** an execution](#get-execution)
	* [**Get Many** executions](#get-many-executions)
	* [**Delete** an execution](#delete-execution)
* Workflow
	* [**Activate** a workflow](#activate-deactivate-delete-and-get-workflow)
	* [**Create** a workflow](#create-workflow)
	* [**Deactivate** a workflow](#activate-deactivate-delete-and-get-workflow)
	* [**Delete** a workflow](#activate-deactivate-delete-and-get-workflow)
	* [**Get** a workflow](#activate-deactivate-delete-and-get-workflow)
	* [**Get Many** workflows](#get-many-workflows)
	* [**Update** a workflow](#update-workflow)

## Generate audit

operation นี้ไม่มี parameter ให้ตั้งค่า สามารถตั้งค่า option ได้ดังนี้:

* **Categories**: เลือกประเภทความเสี่ยง (risk categories) ที่ต้องการให้ audit รวมไว้ เช่น
	* **Credentials**
	* **Database**
	* **Filesystem**
	* **Instance**
	* **Nodes**
* **Days Abandoned Workflow**: ตั้งค่าจำนวนวันที่ workflow ไม่ถูกใช้งาน (ไม่มี execution) หลังจากนั้นจะถือว่า workflow นั้นถูกละทิ้ง ค่า default คือ `90`

## Create credential

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Name**: กรอกชื่อ credential ที่ต้องการสร้าง
* **Credential Type**: กรอกประเภทของ credential ประเภทที่มีขึ้นอยู่กับ node ที่ติดตั้งใน n8n ตัวอย่างเช่น `githubApi`, `notionApi`, `slackApi`
* **Data**: กรอก JSON object ที่มี property ตามที่ credential type นั้นต้องการ สามารถดู format ที่ต้องการได้จาก operation **Get Schema**

## Delete credential

ตั้งค่า operation นี้ด้วย parameter นี้:

* **Credential ID**: กรอก ID ของ credential ที่ต้องการลบ

## Get credential schema

ตั้งค่า operation นี้ด้วย parameter นี้:

* **Credential Type**: กรอกประเภทของ credential ประเภทที่มีขึ้นอยู่กับ node ที่ติดตั้งใน n8n ตัวอย่างเช่น `githubApi`, `notionApi`, `slackApi`

## Get execution

ตั้งค่า operation นี้ด้วย parameter นี้:

* **Execution ID**: กรอก ID ของ execution ที่ต้องการดึงข้อมูล

### Get execution option

สามารถตั้งค่า option เพิ่มเติมได้ดังนี้:

* **Include Execution Details**: เลือกว่าจะให้แสดงรายละเอียด execution เพิ่มเติมหรือไม่ (เปิด/ปิด)

## Get many executions

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Return All**: เลือกว่าจะดึงข้อมูลทั้งหมดหรือจำกัดจำนวนผลลัพธ์ตาม **Limit**
* **Limit**: กำหนดจำนวนผลลัพธ์ที่จะดึง ถ้า **Return All** ปิดอยู่

### Get many executions filters

สามารถตั้งค่า filter เพิ่มเติมได้ดังนี้:

* **Workflow**: กรอง execution ตาม workflow โดยเลือกได้จาก
	* **From list**: เลือก workflow จาก list
	* **By URL**: กรอก workflow URL
	* **By ID**: กรอก workflow ID
* **Status**: กรอง execution ตามสถานะ เช่น
	* **Error**
	* **Success**
	* **Waiting**

### Get many execution options

สามารถตั้งค่า option เพิ่มเติมได้ดังนี้:

* **Include Execution Details**: เลือกว่าจะให้แสดงรายละเอียด execution เพิ่มเติมหรือไม่ (เปิด/ปิด)

## Delete execution

ตั้งค่า operation นี้ด้วย parameter นี้:

* **Execution ID**: กรอก ID ของ execution ที่ต้องการลบ

## Activate, deactivate, delete, and get workflow

operation **Activate**, **Deactivate**, **Delete**, และ **Get** workflow จะมี parameter เดียวกันสำหรับเลือก workflow ที่ต้องการ โดยเลือกได้จาก:

* **From list**: เลือก workflow จาก list
* **By URL**: กรอก URL ของ workflow
* **By ID**: กรอก ID ของ workflow

## Create workflow

ตั้งค่า operation นี้ด้วย parameter นี้:

* **Workflow Object**: กรอก JSON object ที่มีรายละเอียด workflow ใหม่ โดยต้องมี field ดังนี้:
	* `name`
	* `nodes`
	* `connections`
	* `settings`

ดูรายละเอียดเพิ่มเติมได้ที่ [n8n API | Create a workflow documentation](/api/api-reference.md/#tag/Workflow/paths/~1workflows/post)

## Get many workflows

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Return All**: เลือกว่าจะดึงข้อมูลทั้งหมดหรือจำกัดจำนวนผลลัพธ์ตาม **Limit**
* **Limit**: กำหนดจำนวนผลลัพธ์ที่จะดึง ถ้า **Return All** ปิดอยู่

### Get many workflows filters

สามารถตั้งค่า filter เพิ่มเติมได้ดังนี้:

* **Return Only Active Workflows**: เลือกว่าจะให้แสดงเฉพาะ workflow ที่ active หรือแสดงทั้ง active/inactive
* **Tags**: กรอก tag (comma-separated) ที่ workflow ต้องมี

## Update workflow

ตั้งค่า operation นี้ด้วย parameter เหล่านี้:

* **Workflow**: เลือก workflow ที่ต้องการอัปเดต โดยเลือกได้จาก
	* **From list**: เลือก workflow จาก list
	* **By URL**: กรอก URL ของ workflow
	* **By ID**: กรอก ID ของ workflow
* **Workflow Object**: กรอก JSON object ที่จะใช้ update workflow โดยต้องมี field ดังนี้:
	* `name`
	* `nodes`
	* `connections`
	* `settings`

ดูรายละเอียดเพิ่มเติมได้ที่ [n8n API | Update a workflow documentation](https://docs.n8n.io/api/api-reference/#tag/Workflow/paths/~1workflows~1%7Bid%7D/put)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'n8n') ]]
