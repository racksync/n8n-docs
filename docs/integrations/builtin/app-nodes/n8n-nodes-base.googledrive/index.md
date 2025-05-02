---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Drive node documentation
description: Learn how to use the Google Drive node in n8n. Follow technical documentation to integrate Google Drive node into your workflows.
contentType: [integration, reference]
priority: high
---

# Google Drive node

ใช้ Google Drive node เพื่อทำงานอัตโนมัติใน Google Drive และเชื่อมต่อ Google Drive กับแอปพลิเคชันอื่นๆ n8n รองรับฟีเจอร์ต่างๆ ของ Google Drive ในตัว เช่น การสร้าง, อัปเดต, แสดงรายการ, ลบ และดึงข้อมูล Drives, Files และ Folders

ในหน้านี้ คุณจะพบรายการ Operations ที่ Google Drive node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
โปรดดู [Google Drive credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำในการตั้งค่า Authentication
///

## Operations

* **File**
    * [**Copy**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#copy-a-file) a file
    * [**Create from text**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#create-from-text)
    * [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#delete-a-file) a file
    * [**Download**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#download-a-file) a file
    * [**Move**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#move-a-file) a file
    * [**Share**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#share-a-file) a file
    * [**Update**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#update-a-file) a file
    * [**Upload**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#upload-a-file) a file
* **File/Folder**
    * [**Search**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations.md#search-files-and-folders) files and folders
* **Folder**
    * [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations.md#create-a-folder) a folder
    * [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations.md#delete-a-folder) a folder
    * [**Share**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations.md#share-a-folder) a folder
* **Shared Drive**
    * [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md#create-a-shared-drive) a shared drive
    * [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md#delete-a-shared-drive) a shared drive
    * [**Get**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md#get-a-shared-drive) a shared drive
    * [**Get Many**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md#get-many-shared-drives) shared drives
    * [**Update**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md#update-a-shared-drive) a shared drive

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-drive') ]]

## Common issues

สำหรับคำถามหรือปัญหาที่พบบ่อยและแนวทางแก้ไข โปรดดูที่ [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues.md)

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
