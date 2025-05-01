---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: PostHog credentials
description: Documentation for PostHog credentials. Use these credentials to authenticate PostHog in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# PostHog credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [PostHog](/integrations/builtin/app-nodes/n8n-nodes-base.posthog.md)

## Prerequisites

สร้าง [PostHog](https://posthog.com/){:target=_blank .external-link} account หรือ host PostHog บน server ของคุณ

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [PostHog's API documentation](https://posthog.com/docs/api){:target=_blank .external-link}


## Using API key

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- API **URL**: กรอก domain ที่ถูกต้องสำหรับ API requests ของคุณ:
    - บน US Cloud ใช้ `https://us.i.posthog.com` สำหรับ public POST-only endpoints หรือ `https://us.posthog.com` สำหรับ private endpoints
    - บน EU Cloud ใช้ `https://eu.i.posthog.com` สำหรับ public POST-only endpoints หรือ `https://eu.posthog.com` สำหรับ private endpoints
    - สำหรับ self-hosted instances ใช้ self-hosted domain ของคุณ
    - ยืนยันของคุณโดยตรวจสอบ PostHog instance URL ของคุณ
- **API Key**: API key ที่คุณใช้ขึ้นอยู่กับว่าคุณกำลังเข้าถึง public หรือ private endpoints:
    - สำหรับ public POST-only endpoints ใช้ [Project API key](https://app.posthog.com/project/settings) จาก **General** Settings ของ project ของคุณ
    - สำหรับ private endpoints ใช้ [Personal API key](https://app.posthog.com/settings/user-api-keys) จาก **Personal API Keys** Settings ของ User account ของคุณ ดูข้อมูลเพิ่มเติมที่ [How to obtain a personal API key](https://posthog.com/docs/api#private-endpoint-authentication){:target=_blank .external-link}
