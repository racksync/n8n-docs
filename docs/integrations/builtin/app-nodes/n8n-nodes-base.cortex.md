---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Cortex node
description: เรียนรู้วิธีใช้ Cortex node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Cortex node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
---

# Cortex node

ใช้ Cortex node เพื่อทำงานอัตโนมัติใน Cortex และ integrate Cortex กับแอปพลิเคชันอื่นๆ n8n มีการรองรับในตัวสำหรับฟีเจอร์ต่างๆ ของ Cortex รวมถึงการ execute analyzers และ responders รวมถึงการดึงรายละเอียด job

ในหน้านี้ คุณจะพบรายการ operations ที่ Cortex node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
อ้างอิง [Cortex credentials](/integrations/builtin/credentials/cortex.md) สำหรับคำแนะนำในการตั้งค่า authentication
///

## Operations

* Analyzer
    * Execute Analyzer
* Job
    * Get job details
    * Get job report
* Responder
    * Execute Responder

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'cortex') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

