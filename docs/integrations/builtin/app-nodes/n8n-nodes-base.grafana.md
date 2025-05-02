---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Grafana node documentation
description: เรียนรู้วิธีการใช้ Grafana node ใน n8n ทำตามเอกสารทางเทคนิคเพื่อรวม Grafana node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Grafana node

ใช้ Grafana node เพื่อทำงานอัตโนมัติใน Grafana และเชื่อมต่อ Grafana กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Grafana หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล dashboards, teams, และ users

ในหน้านี้จะมีรายการ operations ที่ Grafana node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Grafana credentials](/integrations/builtin/credentials/grafana.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Dashboard
    * Create a dashboard
    * Delete a dashboard
    * Get a dashboard
    * Get all dashboards
    * Update a dashboard
* Team
    * Create a team
    * Delete a team
    * Get a team
    * Retrieve all teams
    * Update a team
* Team Member
    * Add a member to a team
    * Retrieve all team members
    * Remove a member from a team
* User
    * Delete a user from the current organization
    * Retrieve all users in the current organization
    * Update a user in the current organization

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'grafana') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
