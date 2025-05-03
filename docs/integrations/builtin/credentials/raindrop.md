---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Raindrop
description: เอกสารสำหรับข้อมูลยืนยันตัวตน Raindrop ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Raindrop ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# Raindrop credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Raindrop](/integrations/builtin/app-nodes/n8n-nodes-base.raindrop.md)

## Prerequisites

สร้าง [Raindrop](https://raindrop.io/){:target=_blank .external-link} account

## Supported authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Raindrop's API documentation](https://developer.raindrop.io/){:target=_blank .external-link}

## Using OAuth

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Client ID**
- **Client Secret**

สร้างทั้งสองอย่างโดยการสร้าง Raindrop app

หากต้องการสร้าง app ให้ไปที่ **Settings >** [**Integrations**](https://app.raindrop.io/settings/integrations){:target=_blank .external-link} และเลือก **+ Create new app** ในส่วน **For Developers**

ใช้การตั้งค่าเหล่านี้สำหรับ app ของคุณ:

- คัดลอก **OAuth Redirect URL** จาก n8n และเพิ่มเป็น **Redirect URI** ใน app ของคุณ
- คัดลอก **Client ID** และ **Client Secret** จาก Raindrop app และกรอกลงใน n8n credential ของคุณ

