---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือโหนด Sentry.io
description: เรียนรู้วิธีใช้โหนด Sentry.io ใน n8n ดูเอกสารทางเทคนิคเพื่อผสานโหนด Sentry.io เข้ากับ workflow ของคุณ
contentType: [integration, reference]
---

# Sentry.io node

ใช้ Sentry.io node เพื่อช่วยให้งานใน Sentry.io เป็นไปโดยอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ ได้อย่างมีประสิทธิภาพ. n8n รองรับฟีเจอร์ของ Sentry.io หลากหลาย เช่น การสร้าง, อัปเดต, ลบ, และดึงข้อมูล issues, projects, releases รวมถึงการดึง events ทั้งหมด.

/// note | Credentials
ดู [Sentry.io credentials](/integrations/builtin/credentials/sentryio.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Event
    * Get event by ID
    * Get all events
* Issue
    * Delete an issue
    * Get issue by ID
    * Get all issues
    * Update an issue
* Project
    * Create a new project
    * Delete a project
    * Get project by ID
    * Get all projects
    * Update a project
* Release
    * Create a release
    * Delete a release
    * Get release by version identifier
    * Get all releases
    * Update a release
* Organization
    * Create an organization
    * Get organization by slug
    * Get all organizations
    * Update an organization
* Team
    * Create a new team
    * Delete a team
    * Get team by slug
    * Get all teams
    * Update a team

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'sentryio') ]]

## Related resources

Refer to [Sentry.io's documentation](https://docs.sentry.io/api/){:target=_blank .external-link} for more information about the service.

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
