---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Venafi TLS Protect Cloud node
description: เรียนรู้วิธีใช้ Venafi TLS Protect Cloud node ใน n8n และเชื่อมต่อ Venafi TLS Protect Cloud node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Venafi TLS Protect Cloud node

ใช้ Venafi TLS Protect Cloud node ในการทำงานอัตโนมัติใน Venafi TLS Protect Cloud และเชื่อมต่อ Venafi TLS Protect Cloud กับแอปพลิเคชันอื่น ๆ. n8n รองรับฟีเจอร์ของ Venafi TLS Protect Cloud หลากหลาย เช่น การลบและดาวน์โหลด certificates รวมถึงการสร้าง certificate requests.

ในหน้านี้ คุณจะพบรายการของ operations ที่ Venafi TLS Protect Cloud node รองรับและลิงก์ไปยัง resource เพิ่มเติม.

/// note | Credentials
ดู [Venafi TLS Protect Cloud credentials](/integrations/builtin/credentials/venafitlsprotectcloud.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

## Operations

* Certificate
	* Delete
	* Download
	* Get
	* Get Many
	* Renew
* Certificate Request
	* Create
	* Get
	* Get Many

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'venafi-tls-protect-cloud') ]]

## Related resources

ดู [Venafi's REST API documentation](https://docs.venafi.cloud/api/vaas-rest-api/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้.

นอกจากนี้ n8n ยังมีให้:
* A [trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.venafitlsprotectcloudtrigger.md) สำหรับ Venafi TLS Protect Cloud.
* A [node](/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectdatacenter.md) สำหรับ Venafi TLS Protect Datacenter.

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
