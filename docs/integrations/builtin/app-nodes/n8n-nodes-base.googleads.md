---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารคู่มือ Google Ads node
description: เรียนรู้วิธีใช้ Google Ads node ใน n8n และดูเอกสารทางเทคนิคเพื่อเชื่อมต่อ Google Ads node เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: medium
---

# Google Ads node

ใช้ Google Ads node เพื่อทำงานอัตโนมัติใน Google Ads และเชื่อมต่อ Google Ads กับแอปอื่นๆ ได้เลย n8n รองรับฟีเจอร์ของ Google Ads หลายอย่าง เช่น การดึงข้อมูล campaigns

ในหน้านี้จะมีรายการ operations ที่ Google Ads node รองรับ พร้อมลิงก์ไปยังแหล่งข้อมูลอื่นๆ

/// note | Credentials
โปรดดู [Google Ads credentials](/integrations/builtin/credentials/google/index.md) สำหรับคำแนะนำการตั้งค่าการยืนยันตัวตน
///

## Operations

* Campaign
  * Get all campaigns
  * Get a campaign

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-ads') ]]

## Related resources

โปรดดู [Google Ads' documentation](https://developers.google.com/google-ads/api/docs/start){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"
