---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Venafi TLS Protect Datacenter node
description: เรียนรู้วิธีใช้ Venafi TLS Protect Datacenter node ใน n8n และเชื่อมต่อ Venafi TLS Protect Datacenter node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---
<!-- vale off -->
<!-- disabled vale because of "Datacenter" Don't want to general approve it, but it's the brand name -->
# Venafi TLS Protect Datacenter node

ใช้ Venafi TLS Protect Datacenter node ในการทำงานอัตโนมัติใน Venafi TLS Protect Datacenter และเชื่อมต่อ Venafi TLS Protect Datacenter กับแอปพลิเคชันอื่น ๆ. n8n รองรับฟีเจอร์ของ Venafi TLS Protect Datacenter หลากหลาย เช่น การสร้าง, การลบ และการดึงข้อมูล certificates.

ในหน้านี้ คุณจะพบรายการของ operations ที่ Venafi TLS Protect Datacenter node รองรับและลิงก์ไปยัง resource เพิ่มเติม.

/// note | Credentials
ดู [Venafi TLS Protect Datacenter credentials](/integrations/builtin/credentials/venafitlsprotectdatacenter.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

## Operations

* Certificate
	* Create
	* Delete
	* Download
	* Get
	* Get Many
	* Renew
* Policy
	* Get

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'venafi-tls-protect-datacenter') ]]

## Related resources

นอกจากนี้ n8n ยังมีให้:
* A [node](/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectcloud.md) และ [trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.venafitlsprotectcloudtrigger.md) node สำหรับ Venafi TLS Protect Cloud.

<!-- vale on -->

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
