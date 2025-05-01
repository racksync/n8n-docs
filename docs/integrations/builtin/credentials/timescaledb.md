---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: TimescaleDB credentials
description: Documentation for TimescaleDB credentials. Use these credentials to authenticate TimescaleDB in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# TimescaleDB credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [TimescaleDB](/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb.md)

## Prerequisites

ต้องมี instance ของ [TimescaleDB](https://www.timescale.com/){:target=_blank .external-link} ที่พร้อมใช้งานก่อน

## Supported authentication methods

- Database connection

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Timescale's documentation](https://docs.timescale.com/){:target=_blank .external-link}

## Using database connection

ในการตั้งค่า credential นี้ คุณจะต้องมีข้อมูลดังต่อไปนี้:

- **Host**: ชื่อเซิร์ฟเวอร์หรือ IP address ของ TimescaleDB server ที่ต้องการเชื่อมต่อ
- **Database**: ชื่อ database ที่ต้องการเชื่อมต่อ
- **User**: ชื่อผู้ใช้ที่ต้องการล็อกอิน
- **Password**: รหัสผ่านของ database user ที่ใช้เชื่อมต่อ
- **Ignore SSL Issues**: ถ้าเปิดใช้งาน n8n จะเชื่อมต่อแม้ว่า SSL certificate validation จะล้มเหลว และคุณจะไม่เห็นตัวเลือก **SSL**
- **SSL**: ตัวเลือกนี้จะควบคุมค่า `ssl-mode` ใน connection string สำหรับการเชื่อมต่อ โดยมีตัวเลือกดังนี้:
    - **Allow**: ตั้งค่า `ssl-mode` เป็น `allow` โดยจะพยายามเชื่อมต่อแบบ non-SSL ก่อน ถ้าไม่สำเร็จจะลองเชื่อมต่อแบบ SSL
    - **Disable**: ตั้งค่า `ssl-mode` เป็น `disable` จะเชื่อมต่อแบบ non-SSL เท่านั้น
    - **Require**: ตั้งค่า `ssl-mode` เป็น `require` ซึ่งเป็นค่า default สำหรับ TimescaleDB connection string จะเชื่อมต่อแบบ SSL เท่านั้น ถ้ามี root CA file จะตรวจสอบว่า certificate ออกโดย CA ที่เชื่อถือได้
- **Port**: หมายเลข port ของ TimescaleDB server

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการตั้งค่าการเชื่อมต่อแบบ non-SSL ได้ที่ [Timescale's connection settings documentation](https://docs.timescale.com/use-timescale/latest/integrations/query-admin/qstudio/#connection-settings){:target=_blank .external-link} และดูข้อมูลเกี่ยวกับ SSL options ได้ที่ [Connect with a stricter SSL](https://docs.timescale.com/use-timescale/latest/security/strict-ssl/){:target=_blank .external-link}
