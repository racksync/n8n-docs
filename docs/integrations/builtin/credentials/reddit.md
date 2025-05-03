---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Reddit
description: เอกสารสำหรับข้อมูลยืนยันตัวตน Reddit ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Reddit ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# Reddit credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Reddit](/integrations/builtin/app-nodes/n8n-nodes-base.reddit.md)

## Prerequisites

สร้าง [Reddit](https://reddit.com/){:target=_blank .external-link} account

## Supported authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Reddit's developer documentation](https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data){:target=_blank .external-link}

## Using OAuth2

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Client ID**
- **Client Secret**

/// note | Developer program
โปรแกรม developer ของ Reddit อยู่ในช่วง closed beta คำแนะนำด้านล่างนี้สำหรับผู้ใช้ Reddit ทั่วไป ไม่ใช่สมาชิกของ developer platform
///

สร้างทั้งสองอย่างโดยการสร้าง [third-party app](https://www.reddit.com/prefs/apps){:target=_blank .external-link} ไปที่ลิงก์ก่อนหน้า หรือไปที่ **profile > Settings > Safety & Privacy > Manage third-party app authorization > are you a developer? create an app**

ใช้การตั้งค่าเหล่านี้สำหรับ app ของคุณ:

- คัดลอก **OAuth Callback URL** จาก n8n และใช้เป็น **redirect uri** ของ app ของคุณ
- client ID ของ app จะแสดงอยู่ใต้ชื่อ app ของคุณ คัดลอกและเพิ่มเป็น **Client ID** ใน n8n ของคุณ
- คัดลอก **secret** ของ app และเพิ่มเป็น **Client Secret** ใน n8n ของคุณ

