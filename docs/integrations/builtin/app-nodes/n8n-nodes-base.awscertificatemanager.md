---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ AWS Certificate Manager node
description: เรียนรู้วิธีใช้ AWS Certificate Manager node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ AWS Certificate Manager node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# AWS Certificate Manager node

ใช้ AWS Certificate Manager node เพื่อทำงานอัตโนมัติใน AWS Certificate Manager และผสานรวม AWS Certificate Manager กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ AWS Certificate Manager ในตัว รวมถึงการสร้าง, การลบ, การดึงข้อมูล, และการต่ออายุ SSL certificates

ในหน้านี้ คุณจะพบรายการ operations ที่ AWS Certificate Manager node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [AWS Certificate Manager credentials](/integrations/builtin/credentials/aws.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

## Operations

* Certificate
	* Delete
	* Get
	* Get Many
	* Get Metadata
	* Renew

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'aws-certificate-manager') ]]

## Related resources

อ้างอิง [เอกสารของ AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

