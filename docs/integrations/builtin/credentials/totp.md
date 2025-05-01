---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: TOTP credentials
description: Documentation for TOTP credentials. Use these credentials to authenticate TOTP in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# TOTP credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [TOTP](/integrations/builtin/core-nodes/n8n-nodes-base.totp.md)

## Prerequisites

สร้าง **Secret** และ **Label** สำหรับ TOTP

## Supported authentication methods

- Secret and label

## Related resources

TOTP (Time-based One-time Password) คืออัลกอริทึมที่ใช้เวลาปัจจุบันในการสร้างรหัสผ่านแบบใช้ครั้งเดียว (OTP) ดูรายละเอียดเพิ่มเติมได้ที่ [Google Authenticator | Key URI format](https://github.com/google/google-authenticator/wiki/Key-Uri-Format){:target=_blank .external-link}

## Using secret and label

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Secret**: คีย์ลับที่ได้จาก QR code ตอนตั้งค่า authenticator เป็นคีย์ที่เข้ารหัสแบบ Base32 เช่น `BVDRSBXQB2ZEL5HE` ดูรายละเอียดได้ที่ [Google Authenticator Secret](https://github.com/google/google-authenticator/wiki/Key-Uri-Format#secret){:target=_blank .external-link}
- **Label**: ตัวระบุสำหรับบัญชี โดยเป็นชื่อบัญชีในรูปแบบ URI-encoded string สามารถใส่ prefix เพื่อระบุ provider หรือ service ที่ดูแลบัญชีนี้ได้ ถ้าใช้ prefix ให้คั่นด้วย colon หรือ url-encoded colon เช่น `GitHub:john-doe` ดูรายละเอียดได้ที่ [Google Authenticator Label](https://github.com/google/google-authenticator/wiki/Key-Uri-Format#label){:target=_blank .external-link}
