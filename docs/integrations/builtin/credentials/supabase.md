---
title: ข้อมูลเข้าสู่ระบบ Supabase
description: คู่มือการตั้งค่า Supabase credentials สำหรับเชื่อมต่อ Supabase กับ n8n
contentType: [integration, reference]
priority: high
---

# Supabase credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Supabase](/integrations/builtin/app-nodes/n8n-nodes-base.supabase/index.md)
- [Supabase Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase.md)

## Prerequisites

สร้างบัญชี [Supabase](https://supabase.com/dashboard/sign-up){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Supabase's API documentation](https://supabase.com/docs/guides/api){:target=_blank .external-link}

## Using access token

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Host**
- **Service Role Secret**

วิธีสร้าง API Key:

<!-- vale off -->

1. ในบัญชี Supabase ของคุณ ไปที่ **Dashboard** แล้วสร้างหรือเลือกโปรเจกต์ที่ต้องการสร้าง API key
2. ไปที่ [**Project Settings > API**](https://supabase.com/dashboard/project/_/settings/api){:target=_blank .external-link} เพื่อดู API Settings ของโปรเจกต์
3. คัดลอก **URL** จากส่วน **Project URL** แล้วนำไปใส่ใน n8n เป็น **Host** ดูรายละเอียดได้ที่ [API URL and keys](https://supabase.com/docs/guides/api#api-url-and-keys){:target=_blank .external-link}
4. กด Reveal แล้วคัดลอก **Project API key** สำหรับ `service_role` แล้วนำไปใส่ใน n8n เป็น **Service Role Secret** ดูข้อมูลเพิ่มเติมเกี่ยวกับสิทธิ์ของ `service_role` ได้ที่ [Understanding API Keys](https://supabase.com/docs/guides/api/api-keys){:target=_blank .external-link}
<!-- vale on -->

