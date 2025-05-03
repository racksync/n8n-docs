---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Beeminder
description: เอกสารข้อมูลรับรอง Beeminder ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Beeminder ใน n8n
contentType: [integration, reference]
---

# Beeminder credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node นี้:

- [Beeminder](/integrations/builtin/app-nodes/n8n-nodes-base.beeminder.md)

## Prerequisites

สมัคร [Beeminder](https://www.beeminder.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Supported authentication methods

- API user token

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Beeminder's API documentation](https://api.beeminder.com/#beeminder-api-reference){:target=_blank .external-link}

## Using API user token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **User** name: ต้องตรงกับ user ที่สร้าง Auth Token
- **Auth Token** ส่วนตัวของ user นั้น สร้างได้ 2 วิธี:
    - ใน GUI: ไปที่ [Apps & API](https://help.beeminder.com/article/110-apps-and-api#API-token){:target=_blank .external-link} ใน **Account Settings**
    - ใน API: ใช้ [`auth_token` API endpoint](https://api.beeminder.com/#auth){:target=_blank .external-link}

