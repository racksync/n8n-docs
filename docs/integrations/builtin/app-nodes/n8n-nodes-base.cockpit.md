---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Cockpit node documentation
description: Learn how to use the Cockpit node in n8n. Follow technical documentation to integrate Cockpit node into your workflows.
contentType: [integration, reference]
---

# Cockpit node

ใช้ Cockpit node เพื่อทำงานอัตโนมัติใน Cockpit และ integrate Cockpit กับแอปพลิเคชันอื่นๆ n8n มีการรองรับในตัวสำหรับฟีเจอร์ต่างๆ ของ Cockpit รวมถึงการสร้าง collection entry, การจัดเก็บข้อมูลจากการส่ง form, และการดึง singletons

ในหน้านี้ คุณจะพบรายการ operations ที่ Cockpit node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [Cockpit credentials](/integrations/builtin/credentials/cockpit.md) สำหรับคำแนะนำในการตั้งค่า authentication
///

## Operations

* Collection
    * Create a collection entry
    * Get all collection entries
    * Update a collection entry
* Form
    * Store data from a form submission
* Singleton
    * Get a singleton

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'cockpit') ]]
