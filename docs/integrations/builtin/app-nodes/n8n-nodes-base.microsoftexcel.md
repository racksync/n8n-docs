---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Microsoft Excel 365 node
description: เรียนรู้วิธีใช้ Microsoft Excel node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Microsoft Excel node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: high
---

# Microsoft Excel 365 node

ใช้ Microsoft Excel node ในการทำงานอัตโนมัติใน Microsoft Excel และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ โดย n8n รองรับการจัดการ table data, workbooks และ worksheets.

ในหน้านี้ คุณจะพบรายการ operations ที่ Microsoft Excel node รองรับและลิงก์ไปยังข้อมูลเพิ่มเติม.

/// note | Credentials
ดู [Microsoft credentials](/integrations/builtin/credentials/microsoft.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Table
    * Adds rows to the end of the table
    * Retrieve a list of table columns
    * Retrieve a list of table rows
    * Looks for a specific column value and then returns the matching row
* Workbook
    * Adds a new worksheet to the workbook.
    * Get data of all workbooks
* Worksheet
    * Get all worksheets
    * Get worksheet content

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'microsoft-excel') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
