---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Cockpit
description: เอกสารข้อมูลรับรอง Cockpit ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Cockpit ใน n8n
contentType: [integration, reference]
---

# Cockpit credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Cockpit](/integrations/builtin/app-nodes/n8n-nodes-base.cockpit.md)

## Prerequisites

- สมัคร [Cockpit](https://getcockpit.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน
- ตั้งค่า [self-hosted instance ของ Cockpit](https://getcockpit.com/documentation/core/quickstart/installation){:target=_blank .external-link}

## Supported authentication methods

- API access token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Cockpit's API documentation](https://getcockpit.com/documentation/core/api/introduction){:target=_blank .external-link}

## Using API access token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Cockpit URL** ของคุณ: URL ที่คุณใช้เข้าถึง Cockpit instance ของคุณ
- **Access Token**: ดูคำแนะนำในการสร้าง API token ได้ที่ [Cockpit Managing tokens documentation](https://getcockpit.com/documentation/core/api/authentication/#managing-tokens){:target=_blank .external-link} ใช้ **API token** เป็น **Access Token** ของ n8n

