---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Kafka credentials
description: Documentation for Kafka credentials. Use these credentials to authenticate Kafka in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Kafka credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Kafka](/integrations/builtin/app-nodes/n8n-nodes-base.kafka.md)
- [Kafka Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.kafkatrigger.md)

## Supported authentication methods

- Client ID

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับการใช้บริการนี้ได้ที่ [Kafka's documentation](https://kafka.apache.org/documentation/){:target=_blank .external-link}

หากคุณเพิ่งเริ่มใช้ Kafka โปรดดู [Apache Kafka Quickstart](https://kafka.apache.org/quickstart){:target=_blank .external-link} สำหรับการตั้งค่าเริ่มต้น

โปรดดู [Encryption and Authentication using SSL](https://kafka.apache.org/documentation/#security_ssl){:target=_blank .external-link} สำหรับการทำงานกับ SSL ใน Kafka

## Using client ID

ในการตั้งค่า credential นี้ คุณจะต้องมีสภาพแวดล้อม Kafka ที่ทำงานอยู่ และ:

- **Client ID**
- รายการ **Brokers** ที่เกี่ยวข้อง
- รายละเอียดการยืนยันตัวตนด้วย Username/password หากสภาพแวดล้อม Kafka ของคุณใช้การยืนยันตัวตน

วิธีตั้งค่า:

1.  ป้อน `CLIENT-ID` ของ client หรือ consumer group ในช่อง **Client ID** ใน credential ของคุณ
2.  ป้อนรายการ **Brokers** ที่เกี่ยวข้องที่คั่นด้วยเครื่องหมายจุลภาคเพื่อให้ credential ใช้ในรูปแบบ `<broker-service-name>:<port>` ใช้ชื่อที่คุณตั้งให้กับ broker เมื่อคุณกำหนดไว้ในรายการ `services` ตัวอย่างเช่น `kafka-1:9092,kafka-2:9092` จะเพิ่ม brokers `kafka-1` และ `kafka-2` บน port `9092`
3.  หากสภาพแวดล้อม Kafka ของคุณไม่ได้ใช้ SSL ให้ปิด toggle **SSL**
4.  หากคุณเปิดใช้งานการยืนยันตัวตนโดยใช้ SASL ในสภาพแวดล้อม Kafka ของคุณ ให้เปิด toggle **Authentication** จากนั้นเพิ่ม:
    1.  **Username**
    2.  **Password**
    3.  เลือก **SASL Mechanism** ที่กำหนดค่าไว้ของ broker ดูข้อมูลเพิ่มเติมได้ที่ [SASL configuration](https://kafka.apache.org/documentation/#security_sasl_config){:target=_blank .external-link} ตัวเลือกได้แก่:
        - `Plain`
        - `scram-sha-256`
        - `scram-sha-512`

