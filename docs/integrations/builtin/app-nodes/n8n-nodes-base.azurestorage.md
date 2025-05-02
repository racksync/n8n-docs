---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Azure Storage node documentation
description: Learn how to use the Azure Storage node in n8n. Follow technical documentation to integrate Azure Storage node into your workflows.
contentType: [integration, reference]
---

# Azure Storage node

Azure Storage node มีการรองรับฟีเจอร์หลากหลายในตัว ซึ่งรวมถึงการสร้าง, การดึงข้อมูล, และการลบ blobs และ containers ใช้ node นี้เพื่อทำงานอัตโนมัติภายในบริการ Azure Storage หรือผสานรวมกับบริการอื่นๆ ใน workflow ของคุณ

ในหน้านี้ คุณจะพบรายการ operations ที่ Azure Storage node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

///  note  | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/azurestorage.md)
///


## Operations

* **Blob**
	* **Create blob**: Create a new blob or replace an existing one.
	* **Delete blob**: Delete an existing blob.
	* **Get blob**: Retrieve data for a specific blob.
	* **Get many blobs**: Retrieve a list of blobs.
* **Container**
	* **Create container**: Create a new container.
	* **Delete container**: Delete an existing container.
	* **Get container**: Retrieve data for a specific container.
	* **Get many containers**: Retrieve a list of containers.

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'azure-storage') ]]

## Related resources

<!-- add a link to the service's documentation. This should usually go direct to the API docs -->
อ้างอิง [เอกสาร Azure Storage ของ Microsoft](https://learn.microsoft.com/en-us/rest/api/storageservices/) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
