---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Matrix credentials
description: Documentation for Matrix credentials. Use these credentials to authenticate Matrix in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Matrix credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Matrix](/integrations/builtin/app-nodes/n8n-nodes-base.matrix.md)

## Prerequisites

สร้างบัญชีบนเซิร์ฟเวอร์ [Matrix](https://matrix.org/){:target=_blank .external-link} อ้างอิง [Creating an account](https://matrix.org/docs/chat_basics/matrix-for-im/#creating-a-matrix-account){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Supported authentication methods

- API access token

## Related resources

อ้างอิง [Matrix Specification](https://spec.matrix.org/latest/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

อ้างอิงเอกสารสำหรับ client เฉพาะที่คุณใช้เพื่อเข้าถึงเซิร์ฟเวอร์ Matrix

## Using API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Access Token**: token นี้ผูกกับบัญชีที่คุณใช้เข้าสู่ระบบ Matrix
- **Homeserver URL**: นี่คือ URL ของ [homeserver](https://matrix.org/docs/matrix-concepts/elements-of-matrix/#homeserver){:target=_blank .external-link} ที่คุณป้อนเมื่อสร้างบัญชีของคุณ n8n เติมข้อมูลนี้ล่วงหน้าด้วยเซิร์ฟเวอร์ของ matrix.org เอง ปรับเปลี่ยนค่านี้หากคุณใช้เซิร์ฟเวอร์ที่โฮสต์ที่อื่น

คำแนะนำในการรับรายละเอียดเหล่านี้แตกต่างกันไปขึ้นอยู่กับ client ที่คุณใช้เพื่อเข้าถึงเซิร์ฟเวอร์ ทั้ง **Access Token** และ **Homeserver URL** ส่วนใหญ่มักพบได้ใน **Settings > Help & About > Advanced** แต่อ้างอิงเอกสารของ client ของคุณสำหรับรายละเอียดเพิ่มเติม

