---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: QuestDB credentials
description: Documentation for QuestDB credentials. Use these credentials to authenticate QuestDB in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# QuestDB credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [QuestDB](/integrations/builtin/app-nodes/n8n-nodes-base.questdb.md)

## Prerequisites

สร้าง user account บน instance ของ [QuestDB](https://questdb.io/){:target=_blank .external-link}

## Supported authentication methods

- Database connection

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [QuestDB's documentation](https://questdb.io/docs){:target=_blank .external-link}

## Using database connection

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Host**: กรอก host name หรือ IP address ของ server
- **Database**: กรอกชื่อ database เช่น `qdb`
- **User**: กรอก username สำหรับ user account ตามที่กำหนดค่าใน property `pg.user` หรือ `pg.readonly.user` ใน `server.conf` ค่า default คือ `admin`
- **Password**: กรอก password สำหรับ user account ตามที่กำหนดค่าใน property `pg.password` หรือ `pg.readonly.password` ใน `server.conf` ค่า default คือ `quest`
- **SSL**: เลือกว่าการเชื่อมต่อควรใช้ SSL หรือไม่ ซึ่งจะตั้งค่า parameter `sslmode` ตัวเลือกที่มี:
    - **Allow**
    - **Disable**
    - **Require**
- **Port**: กรอกหมายเลข port ที่จะใช้สำหรับการเชื่อมต่อ ค่า default คือ `8812`

ดูข้อมูลเพิ่มเติมที่ [List of supported connection properties](https://questdb.io/docs/reference/api/postgres/#list-of-supported-connection-properties){:target=_blank .external-link}
