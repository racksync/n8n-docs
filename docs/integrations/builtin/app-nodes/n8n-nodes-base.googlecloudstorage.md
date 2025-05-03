---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Google Cloud Storage node
description: เรียนรู้วิธีใช้ Google Cloud Storage node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Google Cloud Storage node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Google Cloud Storage node

ใช้ Google Cloud Storage node เพื่อทำงานอัตโนมัติใน Google Cloud Storage และเชื่อมต่อ Google Cloud Storage กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Google Cloud Storage หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล buckets และ objects

ในหน้านี้จะมีรายการ operations ที่ Google Cloud Storage node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Google Cloud Storage credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Bucket
	* Create
	* Delete
	* Get
	* Get Many
	* Update
* Object
	* Create
	* Delete
	* Get
	* Get Many
	* Update

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-cloud-storage') ]]

## Related resources

โปรดดู [Cloud Storage API documentation](https://cloud.google.com/storage/docs/apis){:target=_blank .external-link} ของ Google สำหรับข้อมูลโดยละเอียดเกี่ยวกับ API ที่ node นี้ผสานรวมด้วย

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
