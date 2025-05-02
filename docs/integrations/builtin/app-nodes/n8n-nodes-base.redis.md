---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Redis node documentation
description: Learn how to use the Redis node in n8n. Follow technical documentation to integrate Redis node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Redis node

ใช้ Redis node ในการอัตโนมัติงานใน Redis และเชื่อมต่อกับแอปพลิเคชันอื่น ๆ. n8n มีการสนับสนุนฟีเจอร์ต่าง ๆ ของ Redis รวมถึงการลบ keys, การดึงค่า key, การตั้งค่า key, และการส่งข้อความไปยัง Redis channel.

ในหน้านี้ คุณจะพบรายการ operations ที่ Redis node รองรับ พร้อมลิงก์ไปยัง resources เพิ่มเติม.

/// note | Credentials
ดู [Redis credentials](/integrations/builtin/credentials/redis.md) สำหรับคำแนะนำในการตั้งค่า authentication.
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Delete a key from Redis.
* Get the value of a key from Redis.
* Returns generic information about the Redis instance.
* Atomically increments a key by 1. Creates the key if it doesn't exist.
* Returns all the keys matching a pattern.
* Set the value of a key in Redis.
* Publish message to Redis channel.

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'redis') ]]
