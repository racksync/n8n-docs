---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Snowflake credentials
description: Documentation for Snowflake credentials. Use these credentials to authenticate Snowflake in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Snowflake credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Snowflake](/integrations/builtin/app-nodes/n8n-nodes-base.snowflake.md)

## Prerequisites

สมัคร [Snowflake](https://www.snowflake.com/en/){:target=_blank .external-link} account ก่อนใช้งาน

## Supported authentication methods

- Database connection

## Related resources

ดูรายละเอียดเพิ่มเติมได้ที่ [Snowflake's API documentation](https://docs.snowflake.com/en/api-reference){:target=_blank .external-link} และ [SQL Command Reference](https://docs.snowflake.com/en/sql-reference-commands){:target=_blank .external-link}

## Using database connection

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Account** name: ชื่อ account คือส่วนที่อยู่ระหว่าง `https://` และ `snowflakecomputing.com` ใน URL ของ Snowflake เช่น ถ้า URL คือ `https://abc.eu-central-1.snowflakecomputing.com` ชื่อ account คือ `abc.eu-central-1`
- **Database**: ใส่ชื่อ [database](https://docs.snowflake.com/en/sql-reference/sql/use-database){:target=_blank .external-link} ที่ credential จะเชื่อมต่อ
- **Warehouse**: ใส่ชื่อ virtual [warehouse](https://docs.snowflake.com/en/sql-reference/sql/use-warehouse){:target=_blank .external-link} ที่จะใช้เป็นค่าเริ่มต้นหลังเชื่อมต่อ n8n จะใช้ warehouse นี้สำหรับ query, โหลดข้อมูล ฯลฯ
- **Username**
- **Password**
- **Schema**: ใส่ [schema](https://docs.snowflake.com/en/sql-reference/sql/use-schema){:target=_blank .external-link} ที่ต้องการใช้หลังเชื่อมต่อ
- **Role**: ใส่ security [role](https://docs.snowflake.com/en/sql-reference/sql/use-role){:target=_blank .external-link} ที่ต้องการใช้หลังเชื่อมต่อ
- **Client Session Keep Alive**: โดยปกติ client จะ timeout หลังจากไม่มี query ประมาณ 3-4 ชั่วโมง ถ้าเปิด option นี้จะตั้งค่า `clientSessionKeepAlive` เป็น true ทำให้ server รักษา connection ไว้ตลอดแม้ไม่มี query

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ session ได้ที่ [Session Commands](https://docs.snowflake.com/en/sql-reference/commands-session){:target=_blank .external-link}
