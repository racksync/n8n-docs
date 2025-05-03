---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการตั้งค่า Zoho credentials
description: วิธีตั้งค่า Zoho credentials เพื่อเชื่อมต่อและยืนยันตัวตนกับ Zoho ใน n8n
contentType: [integration, reference]
---

# Zoho credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Zoho CRM](/integrations/builtin/app-nodes/n8n-nodes-base.zohocrm.md)

## Prerequisites

สมัคร [Zoho](https://www.zoho.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Supported authentication methods

- OAuth2

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Zoho's CRM API documentation](https://www.zoho.com/crm/developer/docs/api/v3/){:target=_blank .external-link}

## Using OAuth2

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Access Token URL**: Zoho มี Access Token URL แยกตาม region ให้เลือก region ที่ตรงกับ data center ของคุณ:
    - **AU**: สำหรับ Australia data center
    - **CN**: สำหรับ Canada data center
    - **EU**: สำหรับ European Union data center
    - **IN**: สำหรับ India data center
    - **US**: สำหรับ United States data center

ดูรายละเอียดเพิ่มเติมที่ [Multi DC](https://www.zoho.com/crm/developer/docs/api/v3/multi-dc.html){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

ถ้าต้องการตั้งค่า OAuth2 เอง ให้ [register an application](https://www.zoho.com/accounts/protocol/oauth-setup.html){:target=_blank .external-link} กับ Zoho

ใช้ค่าต่อไปนี้ในการตั้งค่า application:

- เลือก **Server-based Applications** เป็น **Client Type**
- คัดลอก **OAuth Callback URL** จาก n8n ไปใส่ใน Zoho **Authorized Redirect URIs**
- คัดลอก **Client ID** และ **Client Secret** จาก application ไปใส่ใน n8n credential

