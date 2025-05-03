---
title: ข้อมูลเข้าสู่ระบบ Storyblok
description: คู่มือการตั้งค่า Storyblok credentials สำหรับเชื่อมต่อ Storyblok กับ n8n
contentType: [integration, reference]
---

# Storyblok credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Storyblok](/integrations/builtin/app-nodes/n8n-nodes-base.storyblok.md)

## Prerequisites

สร้างบัญชี [Storyblok](https://www.storyblok.com/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- Content API key: สำหรับการอ่านข้อมูลเท่านั้น (read-only)
- Management API key: สำหรับการจัดการข้อมูลแบบเต็มรูปแบบ (CRUD)

/// note | Content API support
n8n รองรับ Content API v1 เท่านั้น
///

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Content v1 API documentation](https://www.storyblok.com/docs/api/content-delivery/v1){:target=_blank .external-link} และ [Management API documentation](https://www.storyblok.com/docs/api/management/getting-started/introduction){:target=_blank .external-link}

## Using Content API key

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **API Key** สำหรับ Content: ไปที่ **Settings > Access Tokens** ใน workspace ของ Storyblok เพื่อรับ API key เลือก **Access Level** เป็น **Public** (`version=published`) หรือ **Preview** (`version-published` และ `version=draft`) แล้วนำ access token นี้ไปใส่ในช่อง **API Key** ของ n8n ดูวิธีการได้ที่ [How to retrieve and generate access tokens](https://www.storyblok.com/faq/retrieve-and-generate-access-tokens){:target=_blank .external-link}

ดูข้อมูลเพิ่มเติมเกี่ยวกับการยืนยันตัวตนและ operation ที่รองรับแต่ละ Access Level ได้ที่ [Content v1 API Authentication](https://www.storyblok.com/docs/api/content-delivery/v1#topics/authentication){:target=_blank .external-link}

## Using Management API key

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Personal Access Token**: ไปที่ [**My Account**](https://app.storyblok.com/#!/me/account){:target=_blank .external-link} **> Personal access tokens** เพื่อสร้าง access token ใหม่ แล้วนำ access token นี้ไปใส่ในช่อง **Personal Access Token** ของ n8n

