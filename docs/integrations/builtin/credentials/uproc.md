---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลเข้าสู่ระบบ uProc
description: คู่มือการตั้งค่า credentials สำหรับเชื่อมต่อ uProc กับ n8n เพื่อใช้งาน workflow automation
contentType: [integration, reference]
---

# uProc credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [uProc](/integrations/builtin/app-nodes/n8n-nodes-base.uproc.md)

## Prerequisites

สมัครบัญชี [uProc](https://uproc.io){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [uProc's API documentation](https://docs.uproc.io/api/){:target=_blank .external-link}

## Using API Key

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Email**: ใส่อีเมลที่คุณใช้ล็อกอิน uProc ซึ่งจะแสดงใน **Settings > Integrations > API Credentials** ด้วย
- **API Key**: ไปที่ **Settings > Integrations > API Credentials** แล้วคัดลอก **API Key (real)** จากส่วน **API Credentials** มาใส่ใน n8n credential ของคุณ


