---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Postmark
description: เอกสารสำหรับข้อมูลยืนยันตัวตน Postmark ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Postmark ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# Postmark credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Postmark Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.postmarktrigger.md)

## Prerequisites

สร้าง [Postmark](https://postmarkapp.com/){:target=_blank .external-link} account บน Postmark server

## Supported authentication methods

- API token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Postmark's API documentation](https://postmarkapp.com/developer/api/overview){:target=_blank .external-link}

## Using API token

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Server API Token**: Server API token สามารถเข้าถึงได้โดย Account Owners, Account Admins และ users ที่มีสิทธิ์ Server Admin บน server รับของคุณได้จากแท็บ [**API Tokens**](https://account.postmarkapp.com/api_tokens){:target=_blank .external-link} ใต้ Postmark server ของคุณ ดูข้อมูลเพิ่มเติมที่ [API Authentication](https://postmarkapp.com/developer/api/overview#authentication){:target=_blank .external-link}
