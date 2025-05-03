---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Google BigQuery node
description: เรียนรู้วิธีใช้ Google BigQuery node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Google BigQuery node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Google BigQuery node

ใช้ Google BigQuery node เพื่อทำงานอัตโนมัติใน Google BigQuery และเชื่อมต่อ Google BigQuery กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Google BigQuery หลายอย่าง เช่น การสร้าง และดึงข้อมูล records

ในหน้านี้จะมีรายการ operations ที่ Google BigQuery node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Google BigQuery credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

- Execute Query
- Insert

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-bigquery') ]]

## Related resources

โปรดดู [Google BigQuery's documentation](https://cloud.google.com/bigquery/docs/reference/rest){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
