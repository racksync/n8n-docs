---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Lemlist node documentation
description: Learn how to use the Lemlist node in n8n. Follow technical documentation to integrate Lemlist node into your workflows.
contentType: [integration, reference]
---

# Lemlist node

ใช้ Lemlist node ในการทำงานอัตโนมัติใน Lemlist และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับการดึง activities, teams และ campaigns รวมถึงการสร้าง, อัปเดต และลบ leads.

ในหน้านี้ คุณจะพบรายการ operations ที่ Lemlist node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [Lemlist credentials](/integrations/builtin/credentials/lemlist.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

<!-- vale from-write-good.Weasel = NO -->
<!-- vale from-write-good.TooWordy = NO -->
* Activity
    * Get Many: Get many activities
* Campaign
    * Get Many: Get many campaigns
    * Get Stats: Get campaign stats
* Enrichment
	* Get: Fetches a previously completed enrichment
	* Enrich Lead: Enrich a lead using an email or LinkedIn URL
	* Enrich Person: Enrich a person using an email or LinkedIn URL
* Lead
    * Create: Create a new lead
    * Delete: Delete an existing lead
    * Get: Get an existing lead
    * Unsubscribe: Unsubscribe an existing lead
* Team
    * Get: Get an existing team
	* Get Credits: Get an existing team's credits
* Unsubscribe
    * Add: Add an email to an unsubscribe list
    * Delete: Delete an email from an unsubscribe list
    * Get Many: Get many unsubscribed emails
<!-- vale from-write-good.TooWordy = YES -->
<!-- vale from-write-good.Weasel = YES -->

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'lemlist') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
