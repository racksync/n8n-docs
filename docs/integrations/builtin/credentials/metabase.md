---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Metabase
description: เอกสารสำหรับ Metabase credentials ใช้เพื่อเชื่อมต่อ Metabase ใน n8n
contentType: [integration, reference]
---

# Metabase credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Metabase node](/integrations/builtin/app-nodes/n8n-nodes-base.metabase.md)

## Prerequisites

สร้างบัญชี [Metabase](https://www.metabase.com/){:target=_blank .external-link} ที่มีสิทธิ์เข้าถึง instance ของ Metabase

## Supported authentication methods

- Basic auth

## Related resources

อ้างอิง [Metabase's API documentation](https://www.metabase.com/docs/latest/api-documentation){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using basic auth

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **URL**: ป้อน base URL ของ instance Metabase ของคุณ หากคุณใช้ custom domain ให้ใช้ URL นั้น
- **Username**: ป้อนชื่อผู้ใช้ Metabase ของคุณ
- **Password**: ป้อนรหัสผ่าน Metabase ของคุณ
