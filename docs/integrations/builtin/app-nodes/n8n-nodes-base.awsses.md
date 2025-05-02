---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: AWS SES node documentation
description: Learn how to use the AWS SES node in n8n. Follow technical documentation to integrate AWS SES node into your workflows.
contentType: [integration, reference]
---

# AWS SES node

ใช้ AWS SES node เพื่อทำงานอัตโนมัติใน AWS SES และผสานรวม AWS SES กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ AWS SES ในตัว รวมถึงการสร้าง, การดึงข้อมูล, การลบ, การส่ง, การอัปเดต, และการเพิ่ม templates และ emails

ในหน้านี้ คุณจะพบรายการ operations ที่ AWS SES node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [AWS SES credentials](/integrations/builtin/credentials/aws.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Custom Verification Email
    * Create a new custom verification email template
    * Delete an existing custom verification email template
    * Get the custom email verification template
    * Get all the existing custom verification email templates for your account
    * Add an email address to the list of identities
    * Update an existing custom verification email template.
* Email
    * Send
    * Send Template
* Template
    * Create a template
    * Delete a template
    * Get a template
    * Get all templates
    * Update a template

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'aws-ses') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

