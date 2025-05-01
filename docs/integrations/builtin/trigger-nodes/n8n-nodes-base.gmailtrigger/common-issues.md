---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Gmail Trigger node common issues
description: Documentation for common issues and questions in the Gmail Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: _priority-from-main-node_
---

# Gmail Trigger node common issues

รวม error และปัญหาที่พบบ่อยกับ [Gmail Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/index.md) พร้อมวิธีแก้ไขหรือแนวทางตรวจสอบ

## 401 unauthorized error

ข้อความ error เต็มจะประมาณนี้:
<!--vale off-->
```
401 - {"error":"unauthorized_client","error_description":"Client is unauthorized to retrieve access tokens using this method, or client not authorized for any of the scopes requested."}
```
<!--vale on-->

error นี้เกิดจาก credential ที่ใช้มีปัญหาเรื่อง scope หรือ permission

วิธีแก้ไข:

1. ถ้าใช้ [OAuth2](/integrations/builtin/credentials/google/oauth-single-service.md) credential ให้แน่ใจว่าได้เปิด Gmail API ใน **APIs & Services > Library** แล้ว ดูวิธีเปิดได้ที่ [Google OAuth2 Single Service - Enable APIs](/integrations/builtin/credentials/google/oauth-single-service.md#enable-apis)
2. ถ้าใช้ [Service Account](/integrations/builtin/credentials/google/service-account.md) credential:
    1. [Enable domain-wide delegation](/integrations/builtin/credentials/google/service-account.md#enable-domain-wide-delegation)
    2. ตรวจสอบว่าได้เพิ่ม Gmail API ใน domain-wide delegation configuration แล้ว
