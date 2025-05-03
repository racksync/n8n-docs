---
title: คู่มือ TheHive 5 credentials
description: คู่มือการตั้งค่า TheHive 5 credentials สำหรับเชื่อมต่อ TheHive 5 กับ n8n
contentType: [integration, reference]
---

# TheHive 5 credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ของ TheHive 5

- [TheHive 5](/integrations/builtin/app-nodes/n8n-nodes-base.thehive5.md)

/// note | TheHive and TheHive 5
n8n มี node สำหรับ TheHive สองแบบ ใช้ credentials นี้กับ TheHive 5 node ถ้าใช้ TheHive node สำหรับ TheHive 3 หรือ TheHive 4 ให้ใช้ [TheHive credentials](/integrations/builtin/credentials/thehive.md)
///

## Prerequisites

ติดตั้ง [TheHive 5](https://docs.strangebee.com/thehive/download/){:target=_blank .external-link} บนเซิร์ฟเวอร์ของคุณ

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [TheHive's API documentation](https://docs.strangebee.com/thehive/api-docs/){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **API Key**: ผู้ใช้ที่มีบัญชี `orgAdmin` และ `superAdmin` สามารถสร้าง API key ได้:
    - บัญชี `orgAdmin`: ไปที่ **Organization > Create API Key** สำหรับ user ที่ต้องการสร้าง key ให้
    - บัญชี `superAdmin`: ไปที่ **Users > Create API Key** สำหรับ user ที่ต้องการสร้าง key ให้
    - ดูรายละเอียดเพิ่มเติมได้ที่ [API Authentication](https://docs.strangebee.com/cortex/api/api-guide/?h=api+key#authentication){:target=_blank .external-link}
- **URL**: URL ของ TheHive server ของคุณ
- **Ignore SSL Issues**: ถ้าเปิดใช้งาน n8n จะเชื่อมต่อแม้ SSL certificate validation จะล้มเหลว


