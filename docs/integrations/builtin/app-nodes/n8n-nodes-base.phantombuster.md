---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: PhantomBuster node documentation
description: Learn how to use the PhantomBuster node in n8n. Follow technical documentation to integrate PhantomBuster node into your workflows.
contentType: [integration, reference]
---

# PhantomBuster node

ใช้ PhantomBuster node เพื่อช่วยทำงานใน PhantomBuster แบบอัตโนมัติและเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนคุณสมบัติของ PhantomBuster หลากหลาย เช่น การเพิ่ม, ลบ, และดึงข้อมูล agents.

ในหน้านี้ คุณจะพบรายการของ operations ที่ PhantomBuster node รองรับและลิงก์สำหรับข้อมูลเพิ่มเติม.

/// note | Credentials
ดูรายละเอียดเพิ่มเติมได้ที่ [PhantomBuster credentials](/integrations/builtin/credentials/phantombuster.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

## Operations

* Agent
    * Delete an agent by ID.
    * Get an agent by ID.
    * Get all agents of the current user's organization.
    * Get the output of the most recent container of an agent.
    * Add an agent to the launch queue.

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'phantombuster') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
