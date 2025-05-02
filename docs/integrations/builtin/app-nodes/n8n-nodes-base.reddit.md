---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Reddit node documentation
description: Learn how to use the Reddit node in n8n. Follow technical documentation to integrate Reddit node into your workflows.
contentType: [integration, reference]
---

# Reddit node

ใช้ Reddit node ในการอัตโนมัติงานใน Reddit และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนฟีเจอร์หลากหลายของ Reddit ไม่ว่าจะเป็นการดึง profiles และ users, การดึง comment ของ post และข้อมูล subreddit รวมทั้งการส่ง, ดึง, และลบ posts.

ในหน้านี้ คุณจะพบรายการ operations ที่ Reddit node รองรับ พร้อมลิงก์ไปยัง resources เพิ่มเติม.

/// note | Credentials
ดู [Reddit credentials](/integrations/builtin/credentials/reddit.md) สำหรับคำแนะนำในการตั้งค่า authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Post
    * Submit a post to a subreddit
    * Delete a post from a subreddit
    * Get a post from a subreddit
    * Get all posts from a subreddit
    * Search posts in a subreddit or in all of Reddit.
* Post Comment
    * Create a top-level comment in a post
    * Retrieve all comments in a post
    * Remove a comment from a post
    * Write a reply to a comment in a post
* Profile
    * Get
* Subreddit
    * Retrieve background information about a subreddit.
    * Retrieve information about subreddits from all of Reddit.
* User
    * Get

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'reddit') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
