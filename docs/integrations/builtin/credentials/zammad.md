---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการตั้งค่า Zammad credentials
description: วิธีตั้งค่า Zammad credentials เพื่อเชื่อมต่อและยืนยันตัวตนกับ Zammad ใน n8n
contentType: [integration, reference]
---

# Zammad credentials

คุณสามารถใช้ credentials นี้เพื่อ authenticate กับ node เหล่านี้:

- [Zammad](/integrations/builtin/app-nodes/n8n-nodes-base.zammad.md)

## Prerequisites

- สมัคร [Zammad](https://zammad.com/){:target=_blank .external-link} แบบ hosted หรือ setup instance ของคุณเอง
- ถ้าจะใช้ token authentication ให้เปิด **API Token Access** ที่ **Settings > System > API** ดูรายละเอียดที่ [Setting up a Zammad](https://admin-docs.zammad.org/en/latest/system/integrations/zabbix.html?#setting-up-a-zammad){:target=_blank .external-link}

## Supported authentication methods

- Basic auth
- Token auth: Zammad แนะนำให้ใช้วิธีนี้

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการ authenticate ได้ที่ [Zammad's API Authentication documentation](https://docs.zammad.org/en/latest/api/intro.html?#authentication){:target=_blank .external-link}

## Using basic auth

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Base URL**: ใส่ URL ของ Zammad instance ของคุณ
- **Email**: ใส่อีเมลที่ใช้ login Zammad
- **Password**: ใส่รหัสผ่าน Zammad ของคุณ
- **Ignore SSL Issues**: ถ้าเปิดอันนี้ n8n จะเชื่อมต่อแม้ SSL certificate validation จะล้มเหลว

## Using token auth

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Base URL**: ใส่ URL ของ Zammad instance ของคุณ
- **Access Token**: หลังจากเปิด **API Token Access** แล้ว user ที่มี permission `user_preferences.access_token` สามารถสร้าง **Access Token** ได้ที่ **avatar > Profile > Token Access** แล้วกด **Create** เพื่อสร้าง token ใหม่
    - permission ของ access token ขึ้นอยู่กับ action ที่ต้องการใช้กับ credential นี้ ถ้าต้องการใช้ทุกฟีเจอร์ใน [Zammad](/integrations/builtin/app-nodes/n8n-nodes-base.zammad.md) node ให้เลือก:
        - `admin.group`
        - `admin.organization`
        - `admin.user`
        - `ticket.agent`
        - `ticket.customer`
- **Ignore SSL Issues**: ถ้าเปิดอันนี้ n8n จะเชื่อมต่อแม้ SSL certificate validation จะล้มเหลว

