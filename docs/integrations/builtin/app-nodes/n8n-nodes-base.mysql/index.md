---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: MySQL node documentation
description: Learn how to use the MySQL node in n8n. Follow technical documentation to integrate MySQL node into your workflows.
contentType: [integration, reference]
priority: high
---

# MySQL node

ใช้โหนด MySQL เพื่อทำงานอัตโนมัติใน MySQL และเชื่อมต่อ MySQL กับแอปพลิเคชันอื่นๆ n8n มีการสนับสนุนฟีเจอร์ของ MySQL มากมาย รวมถึงการรันคำสั่ง SQL query การเพิ่มข้อมูล และการอัปเดตแถวในฐานข้อมูล

ในหน้านี้ คุณจะพบรายการของการดำเนินการที่โหนด MySQL รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
ดูที่ [MySQL credentials](/integrations/builtin/credentials/mysql.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

## Operations

* Delete
* Execute SQL
* Insert
* Insert or Update
* Select
* Update

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'mysql') ]]

## Related resources

อ้างอิงถึง [MySQL's Connectors and APIs documentation](https://dev.mysql.com/doc/index-connectors.html){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

อ้างอิงถึง [SELECT statement documentation](https://dev.mysql.com/doc/refman/8.4/en/select.html){:target=_blank .external-link} ของ MySQL สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการเขียนคำสั่ง SQL queries

## Use query parameters

เมื่อสร้างคำสั่ง query เพื่อรันบนฐานข้อมูล MySQL คุณสามารถใช้ฟิลด์ **Query Parameters** ในส่วน **Options** เพื่อโหลดข้อมูลเข้าไปในคำสั่ง query n8n ทำการ sanitize ข้อมูลในพารามิเตอร์ของคำสั่ง query ซึ่งช่วยป้องกันการโจมตีแบบ SQL injection

ตัวอย่างเช่น คุณต้องการค้นหาบุคคลด้วยอีเมล์ของพวกเขา จากข้อมูลนำเข้าต่อไปนี้:

```js
[
    {
        "email": "alex@example.com",
        "name": "Alex",
        "age": 21 
    },
    {
        "email": "jamie@example.com",
        "name": "Jamie",
        "age": 33 
    }
]
```

คุณสามารถเขียนคำสั่ง query แบบนี้ได้:

```sql
SELECT * FROM $1:name WHERE email = $2;
```

จากนั้นใน **Query Parameters** ให้ระบุค่าฟิลด์ที่จะใช้ คุณสามารถใส่ค่าคงที่หรือใช้นิพจน์ (expressions) สำหรับตัวอย่างนี้ ใช้นิพจน์เพื่อให้โหนดสามารถดึงอีเมล์จากแต่ละรายการนำเข้าตามลำดับ:

```js
// users is an example table name
users, {{ $json.email }} 
```

## Common issues

สำหรับข้อผิดพลาดทั่วไปหรือปัญหาและขั้นตอนการแก้ไขที่แนะนำ ดูที่ [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues.md)
