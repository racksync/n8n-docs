---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: LinkedIn node documentation
description: Learn how to use the LinkedIn node in n8n. Follow technical documentation to integrate LinkedIn node into your workflows.
contentType: [integration, reference]
priority: medium
---

# LinkedIn node

ใช้ LinkedIn node ในการทำงานอัตโนมัติใน LinkedIn และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับการสร้าง posts.

ในหน้านี้ คุณจะพบรายการ operations ที่ LinkedIn node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [LinkedIn credentials](/integrations/builtin/credentials/linkedin.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Post
    * Create

## Parameters

* **Post As**: choose whether to post as a **Person** or **Organization**.
* **Person Name or ID** and **Organization URN**: enter an identifier for the person or organization.

	/// note | Posting as organization
	If posting as an Organization enter the organization number in the URN field. For example, `03262013` not `urn:li:company:03262013`.
	///
	
* **Text**: the post contents.
* **Media Category**: use this when including images or article URLs in your post.

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'linkedin') ]]

## Related resources

Refer to [LinkedIn's API documentation](https://learn.microsoft.com/en-us/linkedin/){:target=_blank .external-link} for more information about the service.

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"


