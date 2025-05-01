---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Discourse credentials
description: Documentation for Discourse credentials. Use these credentials to authenticate Discourse in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Discourse credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Discourse](/integrations/builtin/app-nodes/n8n-nodes-base.discourse.md)

## Prerequisites

- Host instance ของ [Discourse](https://discourse.org/)
- สร้างบัญชีบน instance ที่ host ของคุณ และตรวจสอบให้แน่ใจว่าคุณเป็น admin

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Discourse's API documentation](https://docs.discourse.org/){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **URL** ของ Discourse instance ของคุณ เช่น `https://community.n8n.io`
- **API Key**: สร้าง API key ผ่าน Discourse admin panel ดูคำแนะนำในการสร้าง API key และระบุ username ได้ที่ [Discourse create and configure an API key documentation](https://meta.discourse.org/t/create-and-configure-an-api-key/230124){:target=_blank .external-link}
- **Username**: ใช้ชื่อของคุณเอง `system` หรือ user อื่น

ดูตัวอย่างได้ในส่วน Authentication ของ [Discourse API documentation](https://docs.discourse.org/){:target=_blank .external-link}


