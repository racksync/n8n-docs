---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Drive Trigger node common issues
description: Documentation for common issues and questions in the Google Drive Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: medium
---

# Google Drive Trigger node common issues

รวม error และปัญหาที่พบบ่อยกับ [Google Drive Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/index.md) พร้อมวิธีแก้ไขหรือแนวทางตรวจสอบ

## 401 unauthorized error

ข้อความ error เต็มจะประมาณนี้:
<!--vale off-->
```
401 - {"error":"unauthorized_client","error_description":"Client is unauthorized to retrieve access tokens using this method, or client not authorized for any of the scopes requested."}
```
<!--vale on-->

error นี้เกิดจาก credential ที่ใช้มีปัญหาเรื่อง scope หรือ permission

วิธีแก้ไข:

1. ถ้าใช้ [OAuth2](/integrations/builtin/credentials/google/oauth-single-service.md) credential ให้แน่ใจว่าได้เปิด Google Drive API ใน **APIs & Services > Library** แล้ว ดูวิธีเปิดได้ที่ [Google OAuth2 Single Service - Enable APIs](/integrations/builtin/credentials/google/oauth-single-service.md#enable-apis)
2. ถ้าใช้ [Service Account](/integrations/builtin/credentials/google/service-account.md) credential:
    1. [Enable domain-wide delegation](/integrations/builtin/credentials/google/service-account.md#enable-domain-wide-delegation)
    2. ตรวจสอบว่าได้เพิ่ม Google Drive API ใน domain-wide delegation configuration แล้ว

## Handling more than one file change

Google Drive Trigger node จะ poll Google Drive เพื่อเช็คการเปลี่ยนแปลงตามช่วงเวลาที่ตั้งไว้ (default คือทุก 1 นาที)

ถ้ามีการเปลี่ยนแปลงหลายไฟล์ที่ตรงกับ **Watch For** criteria ในช่วง polling เดียว จะเกิด event เดียวที่รวมการเปลี่ยนแปลงทั้งหมดเป็น items ดังนั้น workflow ของคุณต้องรองรับกรณีที่ข้อมูลมีมากกว่า 1 item

คุณสามารถใช้ [if node](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) หรือ [switch node](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md) เพื่อเปลี่ยนพฤติกรรม workflow ตามจำนวน item ที่ได้จาก Google Drive Trigger node
