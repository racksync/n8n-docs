---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Mautic
description: เอกสารสำหรับ Mautic credentials ใช้เพื่อเชื่อมต่อ Mautic ใน n8n
contentType: [integration, reference]
priority: medium
---

# Mautic credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Mautic](/integrations/builtin/app-nodes/n8n-nodes-base.mautic.md)
- [Mautic Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.mautictrigger.md)

## Supported authentication methods

- Basic auth
- OAuth2

## Related resources

อ้างอิง [Mautic's API documentation](https://developer.mautic.org/#rest-api){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using basic auth

/// note | API enabled
ในการตั้งค่า credential นี้ instance Mautic ของคุณต้องเปิดใช้งาน API อ้างอิง [Enable the API](#enable-the-api) สำหรับคำแนะนำ
///

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชีบน instance ของ [Mautic](https://www.mautic.org/){:target=_blank .external-link} และ:

- **URL** ของคุณ
- **Username**
- **Password**

วิธีตั้งค่า:

1. ใน Mautic ไปที่ **Configuration > API Settings**
2. หาก **Enable HTTP basic auth?** ตั้งค่าเป็น **No** ให้เปลี่ยนเป็น **Yes** และบันทึก อ้างอิงเอกสาร [API Settings documentation](https://docs.mautic.org/en/5.x/configuration/settings.html#api-settings){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
1. ใน n8n ป้อน Base **URL** ของ instance Mautic ของคุณ
2. ป้อน **Username** ของ Mautic ของคุณ
3. ป้อน **Password** ของ Mautic ของคุณ

## Using OAuth2

/// note | API enabled
ในการตั้งค่า credential นี้ instance Mautic ของคุณต้องเปิดใช้งาน API อ้างอิง [Enable the API](#enable-the-api) สำหรับคำแนะนำ
///

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชีบน instance ของ [Mautic](https://www.mautic.org/){:target=_blank .external-link} และ:

- **Client ID**: สร้างขึ้นเมื่อคุณสร้าง API credentials ใหม่
- **Client Secret**: สร้างขึ้นเมื่อคุณสร้าง API credentials ใหม่
- **URL** ของคุณ

วิธีตั้งค่า:

1. ใน Mautic ไปที่ **Configuration > Settings**
2. เลือก **API Credentials**

    /// note | No API Credentials menu
    หากคุณไม่เห็นตัวเลือก **API Credentials** ใต้ **Configuration > Settings** ตรวจสอบให้แน่ใจว่าได้ [Enable the API](#enable-the-api) หากคุณเปิดใช้งาน API แล้วและยังไม่เห็นตัวเลือก ให้ลอง [ล้างแคชด้วยตนเอง](https://forum.mautic.org/t/cant-find-api-credentials-menu/10689){:target=_blank .external-link}
    ///

2. เลือกตัวเลือก **Create new client**
3. เลือก **OAuth 2** เป็น **Authorization Protocol**
4. ป้อน **Name** สำหรับ credential ของคุณ เช่น `n8n integration`
5. ใน n8n คัดลอก **OAuth Callback URL** และป้อนเป็น **Redirect URI** ใน Mautic
6. เลือก **Apply**
7. คัดลอก **Client ID** จาก Mautic และป้อนลงใน credential ของ n8n
8. คัดลอก **Client Secret** จาก Mautic และป้อนลงใน credential ของ n8n
9. ป้อน Base **URL** ของ instance Mautic ของคุณ

อ้างอิง [What is Mautic's API?](https://kb.mautic.org/article/what-is-mautic-039%3bs-api.html#mcetoc_1g7n1bgoo0){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Enable the API

วิธีเปิดใช้งาน API ใน instance Mautic ของคุณ:

1. ไปที่ **Settings > Configuration**
2. เลือก **API Settings**
3. ตั้งค่า **API enabled?** เป็น **Yes**
4. **Save** การเปลี่ยนแปลงของคุณ

อ้างอิง [How to use the Mautic API](https://kb.mautic.org/article/what-is-mautic-039;s-api.html){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
