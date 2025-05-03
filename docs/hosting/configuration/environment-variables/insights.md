---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Environment Variables สำหรับ Insights
description: ตั้งค่าการเก็บ Metrics ของ Insights ด้วย Environment Variables สำหรับ n8n Self-hosted
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
---

# Insights environment variables

--8<-- "_snippets/self-hosting/file-based-configuration.md"

Insights ช่วยให้เจ้าของ instance และ admin เห็น performance ของ workflow ย้อนหลัง ดูรายละเอียดที่ [Insights](/insights.md)

 | Variable                                                 | Type   | Default | Description                                                                             |
 |:---------------------------------------------------------|:-------|:--------|:----------------------------------------------------------------------------------------|
 | `N8N_DISABLED_MODULES`                                   | String | -       | ตั้งเป็น `insights` เพื่อปิดฟีเจอร์นี้และหยุดเก็บ metrics สำหรับ instance             |
 | `N8N_INSIGHTS_COMPACTION_BATCH_SIZE`                     | Number | 500     | จำนวน raw insights data ที่จะ compact ในแต่ละ batch                                      |
 | `N8N_INSIGHTS_COMPACTION_DAILY_TO_WEEKLY_THRESHOLD_DAYS` | Number | 180     | อายุสูงสุด (วัน) ของ daily insights data ที่จะ compact                                  |
 | `N8N_INSIGHTS_COMPACTION_HOURLY_TO_DAILY_THRESHOLD_DAYS` | Number | 90      | อายุสูงสุด (วัน) ของ hourly insights data ที่จะ compact                                 |
 | `N8N_INSIGHTS_COMPACTION_INTERVAL_MINUTES`               | Number | 60      | ความถี่ (นาที) ที่จะรัน compaction                                                      |
 | `N8N_INSIGHTS_FLUSH_BATCH_SIZE`                          | Number | 1000    | จำนวน insights data สูงสุดที่เก็บใน buffer ก่อน flush                                   |
 | `N8N_INSIGHTS_FLUSH_INTERVAL_SECONDS`                    | Number | 30      | ความถี่ (วินาที) ที่ insights data จะถูก flush ลง database                              |
