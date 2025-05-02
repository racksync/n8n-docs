---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Nextcloud node documentation
description: Learn how to use the Nextcloud node in n8n. Follow technical documentation to integrate Nextcloud node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Nextcloud node

ใช้ Nextcloud node เพื่อทำงานอัตโนมัติใน Nextcloud และเชื่อมต่อกับแอปอื่น ๆ. n8n รองรับฟีเจอร์ของ Nextcloud เช่น การสร้าง, การอัปเดต, การลบ และการดึงข้อมูลไฟล์และโฟลเดอร์ รวมถึงการดึงข้อมูลและเชิญผู้ใช้

ในหน้านี้ คุณจะพบรายการ operations ที่ Nextcloud node รองรับ พร้อมลิงก์สำหรับข้อมูลเพิ่มเติม

/// note | Credentials
ดู [Nextcloud credentials](/integrations/builtin/credentials/nextcloud.md) เพื่อดูวิธีการตั้งค่า authentication
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* File
    * Copy a file
    * Delete a file
    * Download a file
    * Move a file
    * Share a file
    * Upload a file
* Folder
    * Copy a folder
    * Create a folder
    * Delete a folder
    * Return the contents of a given folder
    * Move a folder
    * Share a folder
* User
    * Invite a user to a Nextcloud organization
    * Delete a user.
    * Retrieve information about a single user.
    * Retrieve a list of users.
    * Edit attributes related to a user.

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'nextcloud') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
