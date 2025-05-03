---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง crowd.dev
description: เอกสารข้อมูลรับรอง crowd.dev ใช้ข้อมูลนี้เพื่อยืนยันตัวตน crowd.dev ใน n8n
contentType: [integration, reference]
---

# crowd.dev credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

* [crowd.dev](/integrations/builtin/app-nodes/n8n-nodes-base.crowddev.md)
* [crowd.dev Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.crowddevtrigger.md)

## Prerequisites

สร้าง instance ที่ใช้งานได้ของ [crowd.dev](https://www.crowd.dev/){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [crowd.dev's documentation](https://docs.crowd.dev/docs){:target=_blank .external-link} และ [API documentation](https://api.crowd.dev/api-reference){:target=_blank .external-link} สำหรับการทำงานกับ API

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **URL**:
    - หาก crowd.dev instance ของคุณ host อยู่บน crowd.dev ให้คงค่าเริ่มต้นเป็น `https://app.crowd.dev`
    - หาก crowd.dev instance ของคุณเป็น [self-hosted](https://docs.crowd.dev/docs/technical-docs/self-hosting){:target=_blank .external-link} ให้ใช้ URL ที่คุณใช้เข้าถึง crowd.dev instance ของคุณ
- crowd.dev **Tenant ID** ของคุณ: แสดงในส่วน **Settings** ของ crowd.dev app
- API **Token**: แสดงในส่วน **Settings** ของ crowd.dev app

ดูคำแนะนำโดยละเอียดเพิ่มเติมได้ที่ [crowd.dev API documentation](https://api.crowd.dev/api-reference){:target=_blank .external-link}
