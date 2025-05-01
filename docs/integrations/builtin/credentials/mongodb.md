---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: MongoDB credentials
description: Documentation for MongoDB credentials. Use these credentials to authenticate MongoDB in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# MongoDB credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [MongoDB](/integrations/builtin/app-nodes/n8n-nodes-base.mongodb.md)
- [MongoDB Atlas Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas.md)
- [MongoDB Chat Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymongochat.md)

## Prerequisites

- สร้างบัญชีผู้ใช้ที่มี permissions ที่เหมาะสมบนเซิร์ฟเวอร์ [MongoDB](https://www.mongodb.com/){:target=_blank .external-link}
- ในฐานะ Project Owner เพิ่ม [n8n IP addresses](/manage-cloud/cloud-ip.md) ทั้งหมดลงใน IP Access List Entries ใน **Network Access** ของโปรเจกต์ อ้างอิง [Add IP Access List entries](https://www.mongodb.com/docs/atlas/security/ip-access-list/#add-ip-access-list-entries){:target=_blank .external-link} สำหรับคำแนะนำโดยละเอียด

หากคุณกำลังตั้งค่า MongoDB ตั้งแต่ต้น ให้สร้าง cluster และ database อ้างอิง [MongoDB Atlas documentation](https://www.mongodb.com/docs/atlas/){:target=_blank .external-link} สำหรับคำแนะนำโดยละเอียดเพิ่มเติมเกี่ยวกับขั้นตอนเหล่านี้

## Supported authentication methods

- Database connection - Connection string
- Database connection - Values

## Related resources

อ้างอิง [MongoDBs Atlas documentation](https://www.mongodb.com/docs/atlas/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using database connection - Connection string

ในการกำหนดค่า credential นี้ คุณจะต้องมี [Prerequisites](#prerequisites) ที่ระบุไว้ข้างต้น จากนั้น:

1. เลือก **Connection String** เป็น **Configuration Type**
2. ป้อน MongoDB **Connection String** ของคุณ หากต้องการรับ connection string ใน MongoDB ให้ไปที่ **Database > Connect**
    1. เลือก **Drivers**
    2. คัดลอกโค้ดที่คุณเห็นใน **Add your connection string into your application code** จะเป็นประมาณนี้: `mongodb+srv://yourName:yourPassword@clusterName.mongodb.net/?retryWrites=true&w=majority`
    3. แทนที่ `<password>` และ `<username>` ใน connection string ด้วย credentials ของผู้ใช้ฐานข้อมูลที่คุณจะใช้
    4. ป้อน connection string นั้นลงใน n8n
    5. อ้างอิง [Connection String](https://www.mongodb.com/docs/manual/reference/connection-string/){:target=_blank .external-link} สำหรับข้อมูลเกี่ยวกับการค้นหาและจัดรูปแบบ connection string ของคุณ
3. ป้อนชื่อ **Database** ของคุณ นี่คือชื่อของฐานข้อมูลที่ผู้ใช้ซึ่งคุณเพิ่มรายละเอียดลงใน connection string กำลังเข้าสู่ระบบ
4. เลือกว่าจะ **Use TLS**: เปิดใช้งานเพื่อใช้ TLS คุณต้องกำหนดค่าฐานข้อมูล MongoDB ของคุณให้ใช้ TLS และมีใบรับรอง x.509 ที่สร้างขึ้น เพิ่มข้อมูลสำหรับฟิลด์ใบรับรองเหล่านี้ใน n8n:
    - **CA Certificate**
    - **Public Client Certificate**
    - **Private Client Key**
    - **Passphrase**

อ้างอิง [MongoDB's x.509 documentation](https://www.mongodb.com/docs/manual/core/security-x.509/#std-label-client-x509-certificates-requirements) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับใบรับรอง x.509

## Using database connection - Values

ในการกำหนดค่า credential นี้ คุณจะต้องมี [Prerequisites](#prerequisites) ที่ระบุไว้ข้างต้น จากนั้น:

1. เลือก **Values** เป็น **Configuration Type**
2. ป้อนชื่อ **Host** หรือที่อยู่ของฐานข้อมูล
3. ป้อนชื่อ **Database**
4. ป้อน **User** ที่คุณต้องการเข้าสู่ระบบ
5. ป้อน **Password** ของผู้ใช้
6. ป้อน **Port** ที่จะเชื่อมต่อ นี่คือหมายเลข port ที่เซิร์ฟเวอร์ของคุณใช้เพื่อรอรับการเชื่อมต่อขาเข้า
7. เลือกว่าจะ **Use TLS**: เปิดใช้งานเพื่อใช้ TLS คุณต้องกำหนดค่าฐานข้อมูล MongoDB ของคุณให้ใช้ TLS และมีใบรับรอง x.509 ที่สร้างขึ้น เพิ่มข้อมูลสำหรับฟิลด์ใบรับรองเหล่านี้ใน n8n:
    - **CA Certificate**
    - **Public Client Certificate**
    - **Private Client Key**
    - **Passphrase**

อ้างอิง [MongoDB's x.509 documentation](https://www.mongodb.com/docs/manual/core/security-x.509/#std-label-client-x509-certificates-requirements) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับใบรับรอง x.509
