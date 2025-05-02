---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: PagerDuty node documentation
description: Learn how to use the PagerDuty node in n8n. Follow technical documentation to integrate PagerDuty node into your workflows.
contentType: [integration, reference]
---

# PagerDuty node

ใช้ PagerDuty node เพื่อช่วยทำงานใน PagerDuty แบบอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนคุณสมบัติของ PagerDuty หลากหลาย เช่น การสร้าง incident notes รวมถึงการอัปเดตและดึงข้อมูล log entries และ users.

ในหน้านี้ คุณจะพบรายการของ operations ที่ PagerDuty node รองรับและลิงก์สำหรับข้อมูลเพิ่มเติม.

/// note | Credentials
ดูรายละเอียดเพิ่มเติมได้ที่ [PagerDuty credentials](/integrations/builtin/credentials/pagerduty.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Incident
    * Create an incident
    * Get an incident
    * Get all incidents
    * Update an incident
* Incident Note
    * Create an incident note
    * Get all incident's notes
* Log Entry
    * Get a log entry
    * Get all log entries
* User
    * Get a user

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'pagerduty') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"


