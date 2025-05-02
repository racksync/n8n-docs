---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Onfleet node documentation
description: Learn how to use the Onfleet node in n8n. Follow technical documentation to integrate Onfleet node into your workflows.
contentType: [integration, reference]
---

# Onfleet node

ใช้ Onfleet node เพื่อทำงานอัตโนมัติใน Onfleet และเชื่อมต่อกับแอปอื่น ๆ. n8n รองรับฟีเจอร์หลากหลายของ Onfleet เช่น การสร้างและลบงาน รวมถึงการดึงรายละเอียดขององค์กร

ในหน้านี้ คุณจะพบรายการ operations ที่ Onfleet node รองรับ พร้อมลิงก์สำหรับข้อมูลเพิ่มเติม

/// note | Credentials
ดู [Onfleet credentials](/integrations/builtin/credentials/onfleet.md) เพื่อดูวิธีการตั้งค่า authentication
///

## Operations

* Admin
    * Create a new Onfleet admin
    * Delete an Onfleet admin
    * Get all Onfleet admins
    * Update an Onfleet admin
* Container
    * Add task at index (or append)
    * Get container information
    * Fully replace a container's tasks
* Destination
    * Create a new destination
    * Get a specific destination
* Hub
    * Create a new Onfleet hub
    * Get all Onfleet hubs
    * Update an Onfleet hub
* Organization
    * Retrieve your own organization's details
    * Retrieve the details of an organization with which you are connected
* Recipient
    * Create a new Onfleet recipient
    * Get a specific Onfleet recipient
    * Update an Onfleet recipient
* Task
    * Create a new Onfleet task
    * Clone an Onfleet task
    * Force-complete a started Onfleet task
    * Delete an Onfleet task
    * Get all Onfleet tasks
    * Get a specific Onfleet task
    * Update an Onfleet task
* Team
    * Automatically dispatch tasks assigned to a team to on-duty drivers
    * Create a new Onfleet team
    * Delete an Onfleet team
    * Get a specific Onfleet team
    * Get all Onfleet teams
    * Get estimated times for upcoming tasks for a team, returns a selected driver
    * Update an Onfleet team
* Worker
    * Create a new Onfleet worker
    * Delete an Onfleet worker
    * Get a specific Onfleet worker
    * Get all Onfleet workers
    * Get a specific Onfleet worker schedule
    * Update an Onfleet worker

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'onfleet') ]]
