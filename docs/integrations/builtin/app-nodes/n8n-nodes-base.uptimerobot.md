---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ UptimeRobot node
description: เรียนรู้วิธีใช้ UptimeRobot node ใน n8n และเชื่อมต่อ UptimeRobot node เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# UptimeRobot node

ใช้ UptimeRobot node เพื่อช่วยให้งานใน UptimeRobot เป็นอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับฟีเจอร์ของ UptimeRobot ในด้านต่าง ๆ เช่น การสร้างและลบ alert รวมถึงการดึงข้อมูลบัญชี

ในหน้านี้ คุณจะพบรายการ operations ที่ UptimeRobot node รองรับ พร้อมทั้งลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
ดู [UptimeRobot credentials](/integrations/builtin/credentials/uptimerobot.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Account
    * Get account details
* Alert Contact
    * Create an alert contact
    * Delete an alert contact
    * Get an alert contact
    * Get all alert contacts
    * Update an alert contact
* Maintenance Window
    * Create a maintenance window
    * Delete a maintenance window
    * Get a maintenance window
    * Get all a maintenance windows
    * Update a maintenance window
* Monitor
    * Create a monitor
    * Delete a monitor
    * Get a monitor
    * Get all monitors
    * Reset a monitor
    * Update a monitor
* Public Status Page
    * Create a public status page
    * Delete a public status page
    * Get a public status page
    * Get all a public status pages

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'uptimerobot') ]]
