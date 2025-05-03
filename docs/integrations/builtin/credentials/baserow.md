---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Baserow
description: เอกสารข้อมูลรับรอง Baserow ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Baserow ใน n8n
contentType: [integration, reference]
priority: high
---

# Baserow credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node ต่อไปนี้:

- [Baserow](/integrations/builtin/app-nodes/n8n-nodes-base.baserow.md)

## Prerequisites

สมัคร [Baserow](https://baserow.io/){:target=_blank .external-link} บน Baserow instance ที่ host ใดก็ได้ หรือ self-hosted instance

## Supported authentication methods

- Basic auth

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Baserow's documentation](https://baserow.io/docs/index){:target=_blank .external-link}

ดูข้อมูลเพิ่มเติมเกี่ยวกับ API โดยเฉพาะได้ที่ [Baserow's auto-generated API documentation](https://baserow.io/api-docs){:target=_blank .external-link}

## Using basic auth

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Host** ของ Baserow ของคุณ
- **Username** และ **Password** เพื่อล็อกอิน

ทำตามขั้นตอนเหล่านี้:

1. ป้อน **Host** สำหรับ Baserow instance:
    - สำหรับ Baserow-hosted instance: คงไว้เป็น `https://api.baserow.io`
    - สำหรับ self-hosted instance: ตั้งค่าเป็น self-hosted instance API URL ของคุณ
2. ป้อน **Username** สำหรับบัญชีผู้ใช้ที่ n8n ควรใช้
3. ป้อน **Password** สำหรับบัญชีผู้ใช้นั้น

ดูข้อมูลเกี่ยวกับการสร้างบัญชีผู้ใช้ได้ที่ [Baserow's API Authentication documentation](https://baserow.io/docs/apis/rest-api#authentication)

