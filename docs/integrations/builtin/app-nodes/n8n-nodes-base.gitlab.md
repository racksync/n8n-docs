---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ GitLab node
description: เรียนรู้วิธีใช้ GitLab node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ GitLab node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# GitLab node

ใช้ GitLab node เพื่อทำงานอัตโนมัติใน GitLab และเชื่อมต่อ GitLab กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ GitLab หลายอย่าง เช่น การสร้าง อัปเดต ลบ และแก้ไข issues, repositories, releases และ users

ในหน้านี้จะมีรายการ operations ที่ GitLab node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [GitLab credentials](/integrations/builtin/credentials/gitlab.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
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
    * Create a new issue
    * Create a new comment on an issue
    * Edit an issue
    * Get the data of a single issue
    * Lock an issue
* Release
    * Create a new release
    * Delete a new release
    * Get a new release
    * Get all releases
    * Update a new release
* Repository
    * Get the data of a single repository
    * Returns issues of a repository
* User
    * Returns the repositories of a user

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'gitlab') ]]

## Related resources

โปรดดู [GitLab's documentation](https://docs.gitlab.com/ee/api/rest/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

n8n มี trigger node สำหรับ GitLab คุณสามารถค้นหาเอกสาร trigger node ได้ [ที่นี่](/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger.md)

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

