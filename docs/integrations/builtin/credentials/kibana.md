---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Kibana
description: เอกสารสำหรับ Kibana credentials ใช้เพื่อเชื่อมต่อ Kibana ใน n8n
contentType: [integration, reference]
priority: medium
---

# Kibana credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

- สร้างบัญชี [Elasticsearch](https://www.elastic.co/){:target=_blank .external-link}
- หากคุณกำลังสร้างบัญชีใหม่เพื่อทดสอบ ให้โหลดข้อมูลตัวอย่างบางส่วนลงใน Kibana ดูข้อมูลเพิ่มเติมได้ที่ [Kibana quick start](https://www.elastic.co/guide/en/kibana/current/get-started.html){:target=_blank .external-link}

## Supported authentication methods

- Basic auth

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Kibana's API documentation](https://www.elastic.co/guide/en/kibana/current/api.html){:target=_blank .external-link}

นี่คือ node ที่มีเฉพาะ credential เท่านั้น ดูข้อมูลเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/kibana/){:target=_blank .external-link} บนเว็บไซต์ของ n8n

## Using basic auth

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **URL** ที่คุณใช้เข้าถึง Kibana เช่น `http://localhost:5601`
- **Username**: ใช้ username เดียวกับที่คุณใช้เข้าสู่ระบบ Elastic
- **Password**: ใช้ password เดียวกับที่คุณใช้เข้าสู่ระบบ Elastic