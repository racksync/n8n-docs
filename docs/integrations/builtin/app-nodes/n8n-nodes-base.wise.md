---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Wise node documentation
description: Learn how to use the Wise node in n8n. Follow technical documentation to integrate Wise node into your workflows.
contentType: [integration, reference]
---

# Wise node

ใช้ Wise node ในการทำงานอัตโนมัติใน Wise และเชื่อมต่อ Wise กับแอปพลิเคชันอื่น ๆ. n8n รองรับฟีเจอร์ของ Wise หลากหลาย เช่น การดึง profiles, exchange rates และ recipients.

ในหน้านี้ คุณจะพบรายการของ operations ที่ Wise node รองรับและลิงก์ไปยัง resource เพิ่มเติม.

/// note | Credentials
ดู [Wise credentials](/integrations/builtin/credentials/wise.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

## Operations

* Account
    * Retrieve balances for all account currencies of this user.
    * Retrieve currencies in the borderless account of this user.
    * Retrieve the statement for the borderless account of this user.
* Exchange Rate
    * Get
* Profile
    * Get
    * Get All
* Recipient
    * Get All
* Quote
    * Create
    * Get
* Transfer
    * Create
    * Delete
    * Execute
    * Get
    * Get All

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'wise') ]]
