---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Contentful credentials
description: Documentation for Contentful credentials. Use these credentials to authenticate Contentful in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Contentful credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Contentful](/integrations/builtin/app-nodes/n8n-nodes-base.contentful.md)

## Prerequisites

- สมัคร [Contentful](https://www.contentful.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน
- สร้าง [Contentful space](https://www.contentful.com/help/contentful-101/#step-2-create-a-space){:target=_blank .external-link}

## Supported authentication methods

- API access token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Contentful's API documentation](https://www.contentful.com/developers/docs/references/){:target=_blank .external-link}

## Using API access token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- Contentful **Space ID** ของคุณ: Space ID จะแสดงขึ้นเมื่อคุณสร้าง tokens; คุณยังสามารถดู Space ID ได้ที่ [Contentful Find space ID documentation](https://www.contentful.com/help/find-space-id/){:target=_blank .external-link}
- **Content Delivery API Access Token**: จำเป็นหากคุณต้องการใช้ [Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/){:target=_blank .external-link} เว้นว่างไว้หากคุณไม่ได้ตั้งใจจะใช้ API นี้
- **Content Preview API Access Token**: จำเป็นหากคุณต้องการใช้ [Content Preview API](https://www.contentful.com/developers/docs/references/content-preview-api/){:target=_blank .external-link} เว้นว่างไว้หากคุณไม่ได้ตั้งใจจะใช้ API นี้

ดูและสร้าง access tokens ใน Contentful ได้ที่ **Settings > API keys** Contentful สร้าง tokens สำหรับทั้ง Content Delivery API และ Content Preview API เป็นส่วนหนึ่งของ key เดียว ดูคำแนะนำโดยละเอียดได้ที่ [Contentful Creating and managing API keys](https://training.contentful.com/student/activity/1050378-creating-and-managing-api-keys){:target=_blank .external-link}

