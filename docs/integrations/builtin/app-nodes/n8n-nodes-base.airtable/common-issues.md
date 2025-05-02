---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Airtable node common issues 
description: Documentation for common issues and questions in the Airtable node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: high
---

# Airtable node common issues

นี่คือข้อผิดพลาดหรือปัญหาทั่วไปที่เจอกับ [Airtable node](/integrations/builtin/app-nodes/n8n-nodes-base.airtable/index.md) พร้อมแนวทางแก้ไขหรือวิธีตรวจสอบปัญหา

## Forbidden - perhaps check your credentials

ข้อผิดพลาดนี้จะขึ้นเมื่อคุณพยายามทำบางอย่างที่สิทธิ์ของคุณไม่อนุญาต ข้อความเต็มๆ จะประมาณนี้:

```
There was a problem loading the parameter options from server: "Forbidden - perhaps check your credentials?"
```

ปัญหานี้มักเกิดจาก credential ที่ใช้ไม่มี scopes ที่จำเป็นสำหรับ resources ที่คุณจะจัดการ

ดู [Airtable credentials](/integrations/builtin/credentials/airtable.md) และ [Airtables scopes documentation](https://airtable.com/developers/web/api/scopes) สำหรับข้อมูลเพิ่มเติม

## Service is receiving too many requests from you

Airtable มีข้อจำกัด API ที่เข้มงวดสำหรับจำนวน requests ที่สร้างด้วย personal access tokens

ถ้าคุณส่ง requests เกิน 5 ครั้งต่อวินาทีต่อ base จะเจอ error 429 ซึ่งหมายถึงส่ง requests มากเกินไป ต้องรอ 30 วินาทีก่อนจะส่งได้อีก ข้อจำกัดนี้ใช้กับการส่ง requests เกิน 50 ครั้งในทุก base ต่อ access token ด้วย

ดูข้อมูลเพิ่มเติมได้ที่ [Airtable's rate limits documentation](https://airtable.com/developers/web/api/rate-limits) ถ้าคุณเจอปัญหา rate limits กับ Airtable node ลองดูคำแนะนำในหน้า [handling rate limits](/integrations/builtin/rate-limits.md)
