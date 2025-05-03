---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Rocket.Chat
description: เอกสารสำหรับข้อมูลยืนยันตัวตน Rocket.Chat ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Rocket.Chat ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# Rocket.Chat credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Rocket.Chat](/integrations/builtin/app-nodes/n8n-nodes-base.rocketchat.md)

## Prerequisites

- สร้าง [Rocket.Chat](https://rocket.chat/){:target=_blank .external-link} account
- account ของคุณต้องมี permission `create-personal-access-tokens` เพื่อสร้าง personal access tokens

## Supported authentication methods

- API access token

## Related resources

<!--vale off-->
ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Rocket.Chat's API documentation](https://developer.rocket.chat/reference/api/rest-api){:target=_blank .external-link}
<!--vale on-->

## Using API access token

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **User ID** ของคุณ: แสดงเมื่อคุณสร้าง access token
- **Auth Key**: personal access token ของคุณ หากต้องการสร้าง access token ให้ไปที่ **avatar > Account > Personal Access Tokens** คัดลอก token และเพิ่มเป็น **Auth Key** ใน n8n
- **Domain** ของ Rocket.Chat ของคุณ: หรือที่เรียกว่า default URL หรือ workspace URL

ดูข้อมูลเพิ่มเติมที่ [Personal Access Tokens](https://docs.rocket.chat/docs/manage-your-account-settings#personal-access-tokens){:target=_blank .external-link}

