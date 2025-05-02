---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Supabase node common issues
description: Documentation for common issues and questions in the Supabase node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: high
---

# Supabase node common issues

ด้านล่างนี้คือข้อผิดพลาดและปัญหาที่พบบ่อยกับ [Supabase node](/integrations/builtin/app-nodes/n8n-nodes-base.supabase/index.md) พร้อมขั้นตอนแนะนำวิธีแก้ไขหรือวิเคราะห์ปัญหา 

## Filtering rows by metadata

ในการกรองแถวตาม [Supabase metadata](https://supabase.com/docs/guides/ai/python/metadata) ให้ตั้ง **Select Type** เป็น **String** 

จากนั้นคุณก็สามารถเขียน query ลงในพารามิเตอร์ **Filters (String)** เพื่อกรอง metadata ตามภาษาของ [Supabase metadata query language](https://supabase.com/docs/guides/ai/python/metadata#metadata-query-language) ซึ่งได้แรงบันดาลใจจาก [MongoDB selectors](https://www.mongodb.com/docs/manual/reference/operator/query/) โดยเข้าไปยัง property ใน metadata ด้วยตัวดำเนินการ Postgres `->>` JSON arrow แบบนี้ (ใช้วงเล็บปีกกาแทนส่วนที่ต้องกรอก)

```
metadata->>{your-property}={comparison-operator}.{comparison-value}
```

ตัวอย่างเช่น ถ้าต้องการเข้าถึง property `age` ใน metadata แล้วเลือกเฉพาะข้อมูลที่มีค่าไม่ต่ำกว่า 21 ก็ให้กรอกตามนี้ในฟิลด์ **Filters (String)** 

```
metadata->>age=gte.21
```

คุณสามารถรวมตัวดำเนินการเหล่านี้เพื่อสร้าง query ที่ซับซ้อนขึ้นได้ 

## Can't connect to a local Supabase database when using Docker

เวลาที่รัน Supabase ใน Docker จะต้องตั้งค่าเครือข่ายให้ n8n ติดต่อกับ Supabase ได้ 

วิธีแก้ไขจะแตกต่างกันตามรูปแบบการโฮสต์ 

### If only Supabase is in Docker

ถ้าแค่ Supabase อยู่ใน Docker ตัว Docker Compose ที่ใช้ใน [self-hosting guide](https://supabase.com/docs/guides/self-hosting/docker) จะตั้งค่าให้ Supabase รันบน interface ที่ถูกต้องแล้ว 

เมื่อเซ็ตค่า [Supabase credentials](/integrations/builtin/credentials/supabase.md) ให้ใส่ **Host** เป็น `localhost` ได้เลยโดยไม่ต้องแก้ไขอะไรเพิ่มเติม 

### If Supabase and n8n are running in separate Docker containers

ถ้า n8n กับ Supabase แยกคอนเทนเนอร์กันใน Docker ให้ใช้ Docker networking เชื่อมสองตัวนี้เข้าด้วยกัน 

ตั้งค่า Supabase ให้ฟังบนทุก interface โดย bind ไปที่ `0.0.0.0` ในคอนเทนเนอร์ (ของ official [Docker compose configuration](https://supabase.com/docs/guides/self-hosting/docker) ทำไว้แล้ว) แล้วให้ใส่คอนเทนเนอร์ของ Supabase และ n8n ไว้ใน [user-defined bridge network](https://docs.docker.com/engine/network/drivers/bridge/) เดียวกัน ถ้ายังไม่ได้ทำใน Compose file เดียวกัน 

เมื่อเซ็ต [Supabase credentials](/integrations/builtin/credentials/supabase.md) ให้ใช้ชื่อคอนเทนเนอร์ของ API gateway (ค่าเริ่มต้นคือ `supabase-kong`) แทน `localhost` เช่น ตั้ง **Host** เป็น `http://supabase-kong:8000` 

## Records are accessible through Postgres but not Supabase

ถ้าใช้ Supabase node แล้วผลลัพธ์กลับมาเป็นว่าง ทั้งที่ใน [Postgres](/integrations/builtin/app-nodes/n8n-nodes-base.postgres/index.md) node หรือ Postgres client มีข้อมูล แปลว่ามีปัญหากับนโยบาย [Row Level Security (RLS)](https://supabase.com/docs/guides/database/postgres/row-level-security) ของ Supabase 

Supabase จะเปิด RLS อัตโนมัติเมื่อสร้างตารางใน public schema ผ่าน Table Editor พอ RLS ทำงาน API จะไม่คืนข้อมูลใดๆ ให้กับ public `anon` key จนกว่าจะสร้าง policy ขึ้นมา นี่เป็นมาตรการด้านความปลอดภัยเพื่อให้แน่ใจว่าคุณจะเปิดเผยข้อมูลเท่าที่ตั้งใจไว้เท่านั้น 

ถ้าต้องการเข้าถึงข้อมูลจากตารางที่เปิด RLS แล้วในบทบาท `anon` ให้ [สร้าง policy](https://supabase.com/docs/guides/database/postgres/row-level-security#creating-policies) ตามรูปแบบการเข้าถึงที่คุณต้องการ 
