---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: HighLevel credentials
description: Documentation for HighLevel credentials. Use these credentials to authenticate HighLevel in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# HighLevel credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

* [HighLevel node](/integrations/builtin/app-nodes/n8n-nodes-base.highlevel.md)

## Prerequisites

สร้างบัญชีนักพัฒนา [HighLevel developer](https://marketplace.gohighlevel.com/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API key: ใช้กับ API v1
- OAuth2: ใช้กับ API v2

/// note | API 1.0 deprecation
HighLevel เลิกใช้ API v1.0 แล้วและไม่ได้ดูแลอีกต่อไป แนะนำให้ใช้ OAuth2 สำหรับการตั้งค่า credentials ใหม่
///

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [HighLevel's API 2.0 documentation](https://highlevel.stoplight.io/docs/integrations/0443d7d1a4bd0-overview){:target=_blank .external-link}

สำหรับการเชื่อมต่อกับ API v1.0 ที่มีอยู่แล้ว ดูที่ [HighLevel's API 1.0 documentation](https://public-api.gohighlevel.com/){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials แบบนี้ คุณต้องมี:

- **API Key**: ดูวิธีการขอ API key ได้ที่ [HighLevel API 1.0 Welcome documentation](https://public-api.gohighlevel.com/){:target=_blank .external-link}

## Using OAuth2

ถ้าจะตั้งค่า credentials แบบนี้ คุณต้องมี:

- **Client ID**
- **Client Secret**

วิธีสร้างทั้งสองอย่างนี้ ให้สร้างแอปใน **My Apps > Create App** แล้วตั้งค่าตามนี้:

1.  เลือก **Distribution Type** เป็น **Sub-Account**
2.  เพิ่ม **Scopes** เหล่านี้:
    - `locations.readonly`
    - `contacts.readonly`
    - `contacts.write`
    - `opportunities.readonly`
    - `opportunities.write`
    - `users.readonly`
3.  คัดลอก **OAuth Redirect URL** จาก n8n แล้วเพิ่มเป็น **Redirect URL** ในแอป HighLevel ของคุณ
4.  คัดลอก **Client ID** และ **Client Secret** จาก HighLevel แล้วใส่ใน credentials ของ n8n
5.  เพิ่ม scopes เดิมที่ระบุข้างบนใน credentials ของ n8n โดยใช้เว้นวรรคคั่น เช่น

    ```locations.readonly contacts.readonly contacts.write opportunities.readonly opportunities.write users.readonly```

ดูรายละเอียดเพิ่มเติมได้ที่ [HighLevel's API Authorization documentation](https://highlevel.stoplight.io/docs/integrations/a04191c0fabf9-authorization){:target=_blank .external-link} และ [HighLevel's API Scopes documentation](https://highlevel.stoplight.io/docs/integrations/vcctp9t1w8hja-scopes){:target=_blank .external-link}

