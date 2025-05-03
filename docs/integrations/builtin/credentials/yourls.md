---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการตั้งค่า Yourls credentials
description: วิธีตั้งค่า Yourls credentials เพื่อเชื่อมต่อและยืนยันตัวตนกับ Yourls ใน n8n
contentType: [integration, reference]
---

# Yourls credentials

คุณสามารถใช้ credentials นี้เพื่อ authenticate กับ node เหล่านี้:

- [Yourls](/integrations/builtin/app-nodes/n8n-nodes-base.yourls.md)

## Prerequisites

ติดตั้ง [Yourls](https://github.com/YOURLS/YOURLS){:target=_blank .external-link} บน server ของคุณ

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Yourl's documentation](https://yourls.org/docs){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Signature** token: ไปที่ **Tools > Secure passwordless API call** เพื่อรับ **Signature** token ดูรายละเอียดที่ [Yourl's Passworldess API documentation](https://yourls.org/docs/guide/advanced/passwordless-api){:target=_blank .external-link}
- **URL**: ใส่ URL ของ Yourls instance ของคุณ

