---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Jira Software node
description: เรียนรู้วิธีใช้ Jira Software node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Jira Software node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Jira Software node

ใช้ Jira Software node เพื่อทำงานอัตโนมัติใน Jira และเชื่อมต่อ Jira กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Jira หลายอย่าง เช่น การสร้าง อัปเดต ลบ และดึงข้อมูล issues และ users

ในหน้านี้จะมีรายการ operations ที่ Jira Software node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Jira credentials](/integrations/builtin/credentials/jira.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Issue
    * Get issue changelog
    * Create a new issue
    * Delete an issue
    * Get an issue
    * Get all issues
    * Create an email notification for an issue and add it to the mail queue
    * Return either all transitions or a transition that can be performed by the user on an issue, based on the issue's status
    * Update an issue
* Issue Attachment
    * Add attachment to issue
    * Get an attachment
    * Get all attachments
    * Remove an attachment
* Issue Comment
    * Add comment to issue
    * Get a comment
    * Get all comments
    * Remove a comment
    * Update a comment
* User
    * Create a new user.
    * Delete a user.
    * Retrieve a user.

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'jira-software') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

## Related resources

ดู [official JQL documentation](https://www.atlassian.com/software/jira/guides/expand-jira/jql) เกี่ยวกับ Jira Query Language (JQL) เพื่อเรียนรู้เพิ่มเติม

## Fetch issues for a specific project

Operation **Get All** จะคืนค่า issues ทั้งหมดจาก Jira ถ้าต้องการดึง issues ของโปรเจกต์ใดโปรเจกต์หนึ่ง ให้ใช้ Jira Query Language (JQL)

ตัวอย่าง ถ้าอยากได้ issues ทั้งหมดของโปรเจกต์ชื่อ `n8n` ให้ทำแบบนี้:

- เลือก **Get All** จาก dropdown **Operation**
- เปิด **Return All** ให้เป็น true
- เลือก **Add Option** แล้วเลือก **JQL**
- ใส่ `project=n8n` ในช่อง **JQL**

Query นี้จะดึง issues ทั้งหมดในโปรเจกต์ชื่อ `n8n` ใส่ชื่อโปรเจกต์ของคุณแทน `n8n` เพื่อดึง issues ของโปรเจกต์คุณ
