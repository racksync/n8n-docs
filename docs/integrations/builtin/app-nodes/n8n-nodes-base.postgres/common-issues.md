---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Postgres node common issues
description: Documentation for common issues and questions in the Postgres node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: high
---

# Postgres node common issues

ด้านล่างเป็นข้อผิดพลาดหรือปัญหาทั่วไปกับ [Postgres node](/integrations/builtin/app-nodes/n8n-nodes-base.postgres/index.md) และขั้นตอนในการแก้ไขหรือวิเคราะห์ปัญหา

## Dynamically populate SQL `IN` groups with parameters

ใน Postgres คุณสามารถใช้ SQL [`IN` comparison construct](https://www.postgresql.org/docs/current/functions-comparisons.html#FUNCTIONS-COMPARISONS-IN-SCALAR) เพื่อเปรียบเทียบกลุ่มของค่า:

```sql
SELECT color, shirt_size FROM shirts WHERE shirt_size IN ('small', 'medium', 'large');
```

ถึงแม้จะใช้ n8n [expressions](/code/expressions.md) เพื่อเติมค่าลงในกลุ่ม `IN` แบบไดนามิกได้ การผสานกับ [query parameters](/integrations/builtin/app-nodes/n8n-nodes-base.postgres/index.md#use-query-parameters) จะช่วยเพิ่มความปลอดภัยด้วยการ sanitize ข้อมูลให้โดยอัตโนมัติ

เพื่อสร้าง `IN` group query พร้อม query parameters:

1. ตั้ง **Operation** เป็น **Execute Query**  
2. ใน **Options** ให้เลือก **Query Parameters**  
3. ใช้ expression เพื่อดึงอาร์เรย์จาก input data เช่น `{{ $json.input_shirt_sizes }}`  
4. ในพารามิเตอร์ **Query** ให้เว้นวงเล็บ `IN` ไว้เปล่า เช่น:
    ```sql
    SELECT color, shirt_size FROM shirts WHERE shirt_size IN ();
    ```
5. ในวงเล็บ `IN` ให้ใช้ expression สร้าง placeholders (`$1`, `$2`, `$3`…) ตามจำนวนไอเท็มในอาร์เรย์ โดยเพิ่ม index แต่ละตัวขึ้นหนึ่งเพราะ placeholder เริ่มนับที่ 1:
    ```sql
    SELECT color, shirt_size FROM shirts WHERE shirt_size IN ({{ $json.input_shirt_sizes.map((i, pos) => "$" + (pos+1)).join(', ') }});
    ```

ด้วยเทคนิคนี้ n8n จะสร้าง [prepared statement placeholders](https://www.postgresql.org/docs/current/sql-prepare.html) ตามจำนวนค่าของอาร์เรย์ให้โดยอัตโนมัติ

## Working with timestamps and time zones

เพื่อหลีกเลี่ยงปัญหาเกี่ยวกับ timestamp และ time zone ระหว่าง n8n กับ Postgres ให้ทำตามเคล็ดลับเหล่านี้:

- **Use UTC when storing and passing dates**: ควรใช้ UTC ในการเก็บและส่งวันที่เพื่อป้องกันความสับสนจากการแปลง time zone ระหว่างระบบ  
- **Set the execution timezone**: กำหนด global timezone ใน n8n ผ่าน [environment variables](/hosting/configuration/configuration-examples/time-zone.md) (self-hosted) หรือผ่าน [settings](/manage-cloud/set-cloud-timezone.md) (n8n Cloud) และยังสามารถตั้ง workflow-specific timezone ใน [workflow settings](/workflows/settings.md)  
- **Use ISO 8601 format**: รูปแบบ [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) จะเก็บวัน เดือน ปี ชั่วโมง นาที และวินาทีเป็นสตริง มาตรฐาน n8n ส่งวันที่ข้ามโหนดในรูปแบบสตริงใช้ [Luxon](/code/cookbook/luxon.md) parse หากต้องการ cast เป็น ISO 8601 ให้ใช้ [Date & Time node](/integrations/builtin/core-nodes/n8n-nodes-base.datetime.md) แล้วตั้ง custom format เป็น `yyyy-MM-dd'T'HH:mm:ss`
