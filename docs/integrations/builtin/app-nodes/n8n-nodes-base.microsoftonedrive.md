---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Microsoft OneDrive node
description: เรียนรู้วิธีใช้ Microsoft OneDrive node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Microsoft OneDrive node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Microsoft OneDrive node

ใช้ Microsoft OneDrive node ในการทำงานอัตโนมัติใน Microsoft OneDrive และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับการสร้าง, อัปเดต, ลบ และดึงข้อมูล files และ folders.

ในหน้านี้ คุณจะพบรายการ operations ที่ Microsoft OneDrive node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [Microsoft credentials](/integrations/builtin/credentials/microsoft.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* File
    * Copy a file
    * Delete a file
    * Download a file
    * Get a file
    * Rename a file
    * Search a file
    * Share a file
    * Upload a file up to 4MB in size
* Folder
    * Create a folder
    * Delete a folder
    * Get Children (get items inside a folder)
    * Rename a folder
    * Search a folder
    * Share a folder

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'microsoft-onedrive') ]]

## Related resources

Refer to [Microsoft's OneDrive API documentation](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/){:target=_blank .external-link} for more information about the service.

## Find the folder ID

To perform operations on folders, you need to supply the ID. You can find this:

* In the URL of the folder
* By searching for it using the node. You need to do this if using MS 365 (where OneDrive uses SharePoint behind the scenes):
	1. Select **Resource** > **Folder**.
	2. Select **Operation** > **Search**.
	3. In **Query**, enter the folder name.
	4. Select **Test step**. n8n runs the query and returns data about the folder, including an `id` field containing the folder ID.

