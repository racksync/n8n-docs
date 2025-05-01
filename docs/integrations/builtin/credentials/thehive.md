---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: TheHive credentials
description: Documentation for TheHive credentials. Use these credentials to authenticate TheHive in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# TheHive credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [TheHive](/integrations/builtin/app-nodes/n8n-nodes-base.thehive.md)

/// note | TheHive and TheHive 5
n8n มี node สำหรับ TheHive สองแบบ ใช้ credentials นี้กับ TheHive node สำหรับ TheHive 3 หรือ TheHive 4 ถ้าใช้ TheHive5 node ให้ใช้ [TheHive 5 credentials](/integrations/builtin/credentials/thehive5.md)
///

## Prerequisites

ติดตั้ง [TheHive](https://github.com/TheHive-Project/TheHiveDocs/blob/master/installation/install-guide.md){:target=_blank .external-link} บนเซิร์ฟเวอร์ของคุณ

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [TheHive 3's API documentation](https://docs.thehive-project.org/thehive/legacy/thehive3/api/){:target=_blank .external-link} และ [TheHive 4's API documentation](https://docs.thehive-project.org/thehive/){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **API Key**: สร้าง API key ได้ที่ **Organization > Create API Key** ดูรายละเอียดได้ที่ [API Authentication](https://docs.thehive-project.org/thehive/legacy/thehive3/api/authentication/){:target=_blank .external-link}
- **URL** ของคุณ: URL ของ TheHive server ของคุณ
- **API Version**: เลือกได้ระหว่าง:
    - **TheHive 3 (api v0)**
    - **TheHive 4 (api v1)**
    - ถ้าใช้ TheHive 5 ให้ใช้ [TheHive 5 credentials](/integrations/builtin/credentials/thehive5.md) แทน
- **Ignore SSL Issues**: ถ้าเปิดใช้งาน n8n จะเชื่อมต่อแม้ SSL certificate validation จะล้มเหลว

