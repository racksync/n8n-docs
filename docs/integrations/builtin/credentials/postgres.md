---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Postgres credentials
description: Documentation for Postgres credentials. Use these credentials to authenticate Postgres in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: high
---

# Postgres credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Postgres](/integrations/builtin/app-nodes/n8n-nodes-base.postgres/index.md)
- [Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md)
- [Postgres Chat Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md) 
- [PGVector Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector.md) 

/// note | Agent node users
Agent node ยังไม่รองรับ SSH tunnels.
///

## Prerequisites

[สร้าง user account](https://www.postgresql.org/docs/current/sql-createuser.html) บน Postgres server

## Supported authentication methods

- Database connection

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Postgres's documentation](https://www.postgresql.org/docs/16/index.html){:target=_blank .external-link}

## Using database connection

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Host** หรือ domain name ของ server
- ชื่อ **Database**
- ชื่อ **User**
- **Password** ของ user
- **Ignore SSL Issues**: ตั้งค่าว่าจะให้เชื่อมต่อแม้ SSL validation จะล้มเหลวหรือไม่
- **SSL**: เลือกว่าจะใช้ SSL ในการเชื่อมต่อหรือไม่
- หมายเลข **Port** ที่จะใช้เชื่อมต่อ
- **SSH Tunnel**: เลือกว่าจะใช้ SSH เพื่อเข้ารหัสการเชื่อมต่อกับ Postgres server หรือไม่

ขั้นตอนการตั้งค่าการเชื่อมต่อ database:

1. กรอก **Host** หรือ domain name ของ Postgres server คุณสามารถใช้คำสั่ง `/conninfo` เพื่อดู host name หรือรัน query นี้:

    ```
    SELECT inet_server_addr();
    ```

2. กรอกชื่อ **Database** สามารถใช้คำสั่ง `/conninfo` เพื่อดูชื่อ database ได้
3. กรอกชื่อ **User** ที่ต้องการเชื่อมต่อ
4. กรอก **Password** ของ user
5. **Ignore SSL Issues**: ถ้าเปิดใช้งาน credential จะเชื่อมต่อแม้ SSL validation จะล้มเหลว
6. **SSL**: เลือกว่าจะใช้ SSL ในการเชื่อมต่อหรือไม่ ดูรายละเอียดเพิ่มเติมที่ [Postgres SSL Support](https://www.postgresql.org/docs/16/libpq-ssl.html){:target=_blank .external-link} ตัวเลือกที่มี:
    - **Allow**: ตั้งค่า `ssl-mode` เป็น `allow` จะลองเชื่อมต่อแบบ non-SSL ก่อน ถ้าไม่สำเร็จจะลองแบบ SSL
    - **Disable**: ตั้งค่า `ssl-mode` เป็น `disable` จะเชื่อมต่อแบบ non-SSL เท่านั้น
    - **Require**: ตั้งค่า `ssl-mode` เป็น `require` จะเชื่อมต่อแบบ SSL เท่านั้น ถ้ามี root CA file จะตรวจสอบว่า certificate ออกโดย CA ที่เชื่อถือได้
7. กรอกหมายเลข **Port** ที่จะใช้เชื่อมต่อ สามารถใช้คำสั่ง `/conninfo` หรือรัน query นี้:

    ```
    SELECT inet_server_port();
    ```

8. **SSH Tunnel**: เปิดใช้งานถ้าต้องการเชื่อมต่อ database ผ่าน SSH ดูรายละเอียดข้อจำกัดการใช้ SSH ได้ที่ [SSH tunnel limitations](#ssh-tunnel-limitations) ถ้าเปิดใช้งาน จะต้องกรอกข้อมูลเพิ่มเติมดังนี้:
    1. เลือก **SSH Authenticate with** เพื่อกำหนดประเภท SSH Tunnel ที่จะใช้:
        - เลือก **Password** ถ้าต้องการเชื่อมต่อ SSH ด้วยรหัสผ่าน
        - เลือก **Private Key** ถ้าต้องการเชื่อมต่อ SSH ด้วยไฟล์ private key และ passphrase
    2. กรอก **SSH Host** เป็น remote bind address ที่ต้องการเชื่อมต่อ
    3. **SSH Port**: กรอกหมายเลข port ฝั่ง local สำหรับ SSH tunnel
    4. **SSH Postgres Port**: กรอกหมายเลข port ฝั่ง remote ที่ database server ใช้งาน
    5. **SSH User**: กรอกชื่อผู้ใช้สำหรับ SSH
    6. ถ้าเลือก **Password** สำหรับ SSH Authenticate with ให้กรอก **SSH Password**
    7. ถ้าเลือก **Private Key** สำหรับ SSH Authenticate with:
        1. กรอกเนื้อหา **Private Key** หรือไฟล์ identity ที่ใช้สำหรับ SSH
        2. ถ้า **Private Key** มี passphrase ให้กรอก **Passphrase** ถ้าไม่มีให้เว้นว่าง

ดูรายละเอียดเพิ่มเติมที่ [Secure TCP/IP Connections with SSH Tunnels](https://www.postgresql.org/docs/16/ssh-tunnels.html){:target=_blank .external-link}

### SSH tunnel limitations

ควรใช้ **SSH Tunnel** เฉพาะกรณีต่อไปนี้:

- ใช้ credential นี้กับ [Postgres](/integrations/builtin/app-nodes/n8n-nodes-base.postgres/index.md) node เท่านั้น (Agent node ยังไม่รองรับ SSH tunnels)
- มี SSH server รันอยู่บนเครื่องเดียวกับ Postgres server
- มี user account ที่สามารถล็อกอินด้วย `ssh`
