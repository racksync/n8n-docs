---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Redis
description: เอกสารสำหรับข้อมูลยืนยันตัวตน Redis ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Redis ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: medium
---

# Redis credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Redis](/integrations/builtin/app-nodes/n8n-nodes-base.redis.md)
- [Redis Chat Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md)

## Supported authentication methods

- Database connection

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Redis's developer documentation](https://redis.readthedocs.io/en/stable/index.html){:target=_blank .external-link}

## Using database connection

คุณจะต้องมี user account บน [Redis](https://redis.io/){:target=_blank .external-link} server และ:

- **Password**
- ชื่อ **Host**
- หมายเลข **Port**
- **Database Number**
- **SSL**

ขั้นตอนการตั้งค่า credentials นี้:

1. กรอก **Password** ของ user account ของคุณ
2. กรอกชื่อ **Host** ของ Redis server ค่า default คือ `localhost`
3. กรอกหมายเลข **Port** ที่การเชื่อมต่อควรใช้ ค่า default คือ `6379`
    - หมายเลขนี้ควรตรงกับ `tcp_port` ที่แสดงเมื่อคุณรันคำสั่ง `INFO`
4. กรอก **Database Number** ค่า default คือ `0`
5. หากการเชื่อมต่อควรใช้ SSL ให้เปิด toggle **SSL** หากปิด toggle นี้ การเชื่อมต่อจะใช้ TCP เท่านั้น

ดูข้อมูลเพิ่มเติมที่ [Connecting to Redis | Generic client](https://redis.readthedocs.io/en/stable/connections.html){:target=_blank .external-link}
