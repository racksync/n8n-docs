---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง AMQP
description: เอกสารข้อมูลรับรอง AMQP ใช้ข้อมูลนี้เพื่อยืนยันตัวตน AMQP ใน n8n
contentType: [integration, reference]
priority: medium
---

# AMQP credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [AMQP Sender](/integrations/builtin/app-nodes/n8n-nodes-base.amqp.md)
- [AMQP Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.amqptrigger.md)

## Prerequisites

ติดตั้ง message broker ที่เข้ากันได้กับ AMQP 1.0 เช่น [ActiveMQ](https://activemq.apache.org/){:target=_blank .external-link} ดูรายการตัวเลือกได้ที่ [AMQP Products](https://www.amqp.org/about/examples){:target=_blank .external-link}

## Supported authentication methods

- AMQP connection

## Related resources

Advanced Message Queuing Protocol (AMQP) เป็นโปรโตคอลชั้น application แบบเปิดสำหรับ middleware ที่เน้นข้อความ คุณสมบัติเด่นของ AMQP คือ การเน้นข้อความ, การจัดคิว, การกำหนดเส้นทาง, ความน่าเชื่อถือ และความปลอดภัย ดูข้อมูลเพิ่มเติมได้ที่ [OASIS AMQP Version 1.0 Standard](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html){:target=_blank .external-link}

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่เอกสารของผู้ให้บริการของคุณ ดู [ActiveMQ's API documentation](https://activemq.apache.org/components/classic/documentation/rest){:target=_blank .external-link} เป็นตัวอย่างหนึ่ง

## Using AMQP connection

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Hostname**: ป้อน hostname ของ AMQP message broker ของคุณ
- **Port**: ป้อนหมายเลข port ที่การเชื่อมต่อควรใช้
- **User**: ป้อนชื่อผู้ใช้เพื่อสร้างการเชื่อมต่อ
    - ตัวอย่างเช่น username เริ่มต้นใน ActiveMQ คือ `admin`
- **Password**: ป้อน password ของผู้ใช้
    - ตัวอย่างเช่น password เริ่มต้นใน ActiveMQ คือ `admin`
- _Optional:_ **Transport Type**: ป้อน `tcp` หรือ `tls`

ดูคำแนะนำโดยละเอียดเพิ่มเติมได้ที่เอกสารของผู้ให้บริการของคุณ
