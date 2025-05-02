---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: AWS DynamoDB node documentation
description: Learn how to use the AWS DynamoDB node in n8n. Follow technical documentation to integrate AWS DynamoDB node into your workflows.
contentType: [integration, reference]
---

# AWS DynamoDB node

ใช้ AWS DynamoDB node เพื่อทำงานอัตโนมัติใน AWS DynamoDB และผสานรวม AWS DynamoDB กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ AWS DynamoDB ในตัว รวมถึงการสร้าง, การอ่าน, การอัปเดต, การลบ items และ records บนฐานข้อมูล

ในหน้านี้ คุณจะพบรายการ operations ที่ AWS DynamoDB node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [AWS credentials](/integrations/builtin/credentials/aws.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

## Operations

* Item
  * Create a new record, or update the current one if it already exists (upsert/put)
  * Delete an item
  * Get an item
  * Get all items

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'aws-dynamodb') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

