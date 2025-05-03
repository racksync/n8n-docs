---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ GitHub node
description: เรียนรู้วิธีใช้ GitHub node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ GitHub node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# GitHub node

ใช้ GitHub node เพื่อทำงานอัตโนมัติใน GitHub และเชื่อมต่อ GitHub กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ GitHub หลายอย่าง เช่น การสร้าง อัปเดต ลบ และแก้ไข files, repositories, issues, releases, และ users

ในหน้านี้จะมีรายการ operations ที่ GitHub node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [GitHub credentials](/integrations/builtin/credentials/github.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* File
	* Create
	* Delete
	* Edit
	* Get
	* List
* Issue
	* Create
	* Create Comment
	* Edit
	* Get
	* Lock
* Organization
	* Get Repositories
* Release
	* Create
	* Delete
	* Get
	* Get Many
	* Update
* Repository
    * Get
	* Get Issues
	* Get License
	* Get Profile
	* Get Pull Requests
	* List Popular Paths
	* List Referrers
* Review
	* Create
	* Get
	* Get Many
	* Update
* User
    * Get Repositories
    * Invite
* Workflow
	* Disable
	* Dispatch
	* Enable
	* Get
	* Get Usage
	* List

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'github') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

