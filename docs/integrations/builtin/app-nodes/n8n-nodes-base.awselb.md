---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: AWS Elastic Load Balancing node documentation
description: Learn how to use the AWS Elastic Load Balancing node in n8n. Follow technical documentation to integrate AWS Elastic Load Balancing node into your workflows.
contentType: [integration, reference]
---

# AWS Elastic Load Balancing node

ใช้ AWS Elastic Load Balancing node เพื่อทำงานอัตโนมัติใน AWS ELB และผสานรวม AWS ELB กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ AWS ELB ในตัว รวมถึงการเพิ่ม, การดึงข้อมูล, การลบ certificates และ load balancers

ในหน้านี้ คุณจะพบรายการ operations ที่ AWS ELB node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [AWS ELB credentials](/integrations/builtin/credentials/aws.md){:target=_blank .external-link} สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

## Operations

* Listener Certificate
	* Add
	* Get Many
	* Remove
* Load Balancer
	* Create
	* Delete
	* Get
	* Get Many

Node นี้รองรับการสร้างและจัดการ application และ network load balancers ปัจจุบันยังไม่รองรับ gateway load balancers

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'aws-elb') ]]

## Related resources

อ้างอิง [เอกสารของ AWS ELB](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

