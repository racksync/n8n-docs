---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Chargebee
description: เอกสารข้อมูลรับรอง Chargebee ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Chargebee ใน n8n
contentType: [integration, reference]
---

# Chargebee credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Chargebee](/integrations/builtin/app-nodes/n8n-nodes-base.chargebee.md)
- [Chargebee Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.chargebeetrigger.md)

## Prerequisites

สมัคร [Chargebee](https://www.chargebee.com/) ให้เรียบร้อยก่อน

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Chargebee's API documentation](https://apidocs.chargebee.com/docs/api/){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Account Name**: นี่คือ Chargebee Site Name หรือ subdomain ของคุณ ตัวอย่างเช่น ถ้า `https://n8n.chargebee.com` คือชื่อ site เต็ม Account Name คือ `n8n`
- **API Key**: ดูขั้นตอนเกี่ยวกับวิธีสร้าง API key ได้ที่ [Chargebee Creating an API key documentation](https://www.chargebee.com/docs/api_keys.html#creating-an-api-key){:target=_blank .external-link}

ดูคำชี้แจงเพิ่มเติมได้ที่ [API authentication documentation](https://apidocs.chargebee.com/docs/api/auth?lang=curl){:target=_blank .external-link} ทั่วไปของพวกเขา

