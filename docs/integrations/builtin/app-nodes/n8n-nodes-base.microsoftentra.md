---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Microsoft Entra ID node
description: เรียนรู้วิธีใช้ Microsoft Entra ID node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Microsoft Entra ID node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Microsoft Entra ID node

ใช้ Microsoft Entra ID node ในการทำงานอัตโนมัติใน Microsoft Entra ID และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับฟีเจอร์ต่าง ๆ เช่น การสร้าง, ดึง, อัปเดต และลบ users และ groups พร้อมทั้งการจัดการผู้ใช้ในกลุ่ม.

ในหน้านี้ คุณจะพบรายการ operations ที่ Microsoft Entra ID node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

///  note  | Credentials
ดู [Microsoft Entra ID credentials] สำหรับคำแนะนำในการตั้งค่า authentication.
///


## Operations

* **Group**
	* **Create**: Create a new group
	* **Delete**: Delete an existing group
	* **Get**: Retrieve data for a specific group
	* **Get Many**: Retrieve a list of groups
	* **Update**: Update a group
* **User**
	* **Create**: Create a new user
	* **Delete**: Delete an existing user
	* **Get**: Retrieve data for a specific user
	* **Get Many**: Retrieve a list of users
	* **Update**: Update a user
	* **Add to Group**: Add user to a group
	* **Remove from Group**: Remove user from a group

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'microsoft-entra-id-azure-active-directory') ]]

## Related resources

<!-- vale from-microsoft.We = NO -->
Refer to [Microsoft Entra ID's documentation](https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview?view=graph-rest-1.0){:target=_blank .external-link} for more information about the service.
<!-- vale from-microsoft.We = YES -->

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

## Common issues

Here are some common errors and issues with the Microsoft Entra ID node and steps to resolve or troubleshoot them.

### Updating the Allow External Senders and Auto Subscribe New Members options fails

You can't update the **Allow External Senders** and **Auto Subscribe New Members** options directly after creating a new group. You must wait after creating a group before you can change the values of these options.

When designing workflows that use multiple Microsoft Entra ID nodes to first create groups and then update these options, add a [Wait](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md) node between the two operations. A Wait node configured to pause for at least two seconds allows time for the group to fully initialize. After the wait, the update operation can complete without erroring.
