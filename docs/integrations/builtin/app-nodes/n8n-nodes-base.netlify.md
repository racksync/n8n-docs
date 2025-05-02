---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Netlify node documentation
description: Learn how to use the Netlify node in n8n. Follow technical documentation to integrate Netlify node into your workflows.
contentType: [integration, reference]
---

# Netlify node

ใช้ Netlify node เพื่อทำงานอัตโนมัติใน Netlify และเชื่อมต่อกับแอปอื่น ๆ. n8n รองรับฟีเจอร์ของ Netlify เช่น การดึงและยกเลิก deployments รวมถึงการลบและดึงข้อมูล sites

ในหน้านี้ คุณจะพบรายการ operations ที่ Netlify node รองรับ พร้อมลิงก์สำหรับข้อมูลเพิ่มเติม

/// note | Credentials
ดู [Netlify credentials](/integrations/builtin/credentials/netlify.md) เพื่อดูวิธีการตั้งค่า authentication
///

## Operations

* Deploy
    * Cancel a deployment
    * Create a new deployment
    * Get a deployment
    * Get all deployments
* Site
    * Delete a site
    * Get a site
    * Returns all sites

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'netlify') ]]
