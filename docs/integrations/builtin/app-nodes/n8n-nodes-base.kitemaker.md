---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Kitemaker node documentation
description: Learn how to use the Kitemaker node in n8n. Follow technical documentation to integrate Kitemaker node into your workflows.
contentType: [integration, reference]
---

# Kitemaker node

ใช้ Kitemaker node เพื่อทำงานอัตโนมัติใน Kitemaker และเชื่อมต่อ Kitemaker กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Kitemaker หลายอย่าง เช่น การดึงข้อมูล organizations, spaces, users รวมถึงการสร้าง ดึงข้อมูล และอัปเดต work items

ในหน้านี้จะมีรายการ operations ที่ Kitemaker node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Kitemaker credentials](/integrations/builtin/credentials/kitemaker.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Organization
    * Retrieve data on the logged-in user's organization.
* Space
    * Retrieve data on all the spaces in the logged-in user's organization.
* User
    * Retrieve data on all the users in the logged-in user's organization.
* Work Item
    * Create
    * Get
    * Get All
    * Update

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'kitemaker') ]]
