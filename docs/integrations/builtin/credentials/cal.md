---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Cal.com credentials
description: Documentation for Cal.com credentials. Use these credentials to authenticate Cal.com in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Cal.com credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Cal.com Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.caltrigger.md)

## Prerequisites

สมัคร [Cal.com](https://www.cal.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Cal.com's API documentation](https://cal.com/docs/enterprise-features/api#api-server-specifications){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **API Key**: ดูข้อมูลเกี่ยวกับวิธีสร้าง API key ใหม่ได้ที่ [Cal API Quick Start documentation](https://cal.com/docs/enterprise-features/api/quick-start){:target=_blank .external-link}
- **Host**: หากคุณใช้ Cal.com เวอร์ชัน cloud ให้คง Host เป็น `https://api.cal.com` หากคุณ self-hosting Cal.com ให้ป้อน **Host** สำหรับ Cal.com instance ของคุณ

