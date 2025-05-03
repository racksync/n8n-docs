---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Mailchimp node
description: เรียนรู้วิธีใช้ Mailchimp node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Mailchimp node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Mailchimp node

ใช้ Mailchimp node ในการทำงานอัตโนมัติใน Mailchimp และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับการสร้าง, อัปเดต, ลบ campaigns รวมถึงการดึงข้อมูล list groups และ members.

ในหน้านี้ คุณจะพบรายการ operations ที่ Mailchimp node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [Mailchimp credentials](/integrations/builtin/credentials/mailchimp.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Campaign
    * Delete a campaign
    * Get a campaign
    * Get all the campaigns
    * Replicate a campaign
    * Creates a Resend to Non-Openers version of this campaign
    * Send a campaign
* List Group
    * Get all groups
* Member
    * Create a new member on list
    * Delete a member on list
    * Get a member on list
    * Get all members on list
    * Update a new member on list
* Member Tag
    * Add tags from a list member
    * Remove tags from a list member

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'mailchimp') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
