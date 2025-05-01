---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Redis Trigger node documentation
description: Learn how to use the Redis Trigger node in n8n. Follow technical documentation to integrate Redis Trigger node into your workflows.
contentType: [integration, reference]
---

# Redis Trigger node

[Redis](https://redis.io/){:target=_blank .external-link} คือ open-source in-memory data structure store ที่ใช้เป็น database, cache และ message broker ได้

ใช้ Redis Trigger node เพื่อ subscribe ไปยัง Redis channel ที่ต้องการ Workflow จะเริ่มทำงานทันทีเมื่อ channel นั้นมี message ใหม่เข้ามา

/// note | Credentials
คุณสามารถดูข้อมูลเกี่ยวกับการเชื่อมต่อบัญชี (authentication) สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/redis.md)
///

///  note  | Examples and templates
ถ้าอยากดูตัวอย่างการใช้งานหรือ template สำหรับเริ่มต้น ลองดูที่หน้า [Redis Trigger integrations](https://n8n.io/integrations/redis-trigger/){:target=_blank .external-link} ของ n8n ได้เลย
///

