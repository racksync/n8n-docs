---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: HubSpot credentials
description: Documentation for HubSpot credentials. Use these credentials to authenticate HubSpot in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# HubSpot credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [HubSpot](/integrations/builtin/app-nodes/n8n-nodes-base.hubspot.md)
- [HubSpot Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger.md)

## Supported authentication methods

- App token: ใช้กับ node [HubSpot](/integrations/builtin/app-nodes/n8n-nodes-base.hubspot.md)
- Developer API key: ใช้กับ node [HubSpot Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger.md)
- OAuth2: ใช้กับ node [HubSpot](/integrations/builtin/app-nodes/n8n-nodes-base.hubspot.md)

/// warning | API key deprecated
HubSpot ได้ยกเลิกวิธีการยืนยันตัวตนด้วย **API Key** แบบปกติแล้ว ตัวเลือกนี้ยังคงปรากฏใน n8n แต่คุณควรใช้วิธีการยืนยันตัวตนที่ระบุไว้ข้างต้นแทน หากคุณมีการรวมระบบที่มีอยู่ซึ่งใช้วิธี API key นี้ โปรดดูคู่มือ [Migrate an API key integration to a private app](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app){:target=_blank .external-link} ของ HubSpot และตั้งค่า app token
///

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [HubSpot's API documentation](https://developers.hubspot.com/docs/api/overview){:target=_blank .external-link} node [HubSpot Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger.md) ใช้ Webhooks API; ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนั้นได้ที่ [HubSpot's Webhooks API documentation](https://developers.hubspot.com/docs/api/webhooks){:target=_blank .external-link}

## Using App token

ในการตั้งค่า credential นี้ คุณจะต้องมีบัญชี [HubSpot](https://www.hubspot.com/){:target=_blank .external-link} หรือบัญชีนักพัฒนา [HubSpot developer](https://developers.hubspot.com/){:target=_blank .external-link} และ:

- **App Token**

ในการสร้าง app token ให้สร้าง private app ใน HubSpot:

1.  ในบัญชี HubSpot ของคุณ เลือก **settings icon** ในแถบนำทางหลัก
2.  ในเมนูแถบด้านข้างซ้าย ไปที่ **Integrations > Private Apps**
3.  เลือก **Create private app**
4.  บนแท็บ **Basic Info** ป้อน **Name** ของแอปของคุณ
5.  วางเมาส์เหนือ **placeholder logo** และเลือกไอคอนอัปโหลดเพื่ออัปโหลดภาพสี่เหลี่ยมจัตุรัสที่จะใช้เป็นโลโก้สำหรับแอปของคุณ
6.  ป้อน **Description** สำหรับแอปของคุณ
7.  เปิดแท็บ **Scopes** และเพิ่ม scopes ที่เหมาะสม ดูรายการ scopes ทั้งหมดที่คุณควรเพิ่มได้ที่ [Required scopes for HubSpot node](#required-scopes-for-hubspot-node)
8.  เลือก **Create app** เพื่อสิ้นสุดกระบวนการ
9.  ใน modal ตรวจสอบข้อมูลเกี่ยวกับ access token ของแอปของคุณ จากนั้นเลือก **Continue creating**
10. เมื่อแอปของคุณสร้างเสร็จแล้ว ให้เปิด **Access token card** และเลือก **Show token** เพื่อแสดง token
11. คัดลอก token นี้และป้อนลงใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมได้ที่ [HubSpot Private Apps documentation](https://developers.hubspot.com/docs/api/private-apps){:target=_blank .external-link}

## Using Developer API key

ในการตั้งค่า credential นี้ คุณจะต้องมีบัญชีนักพัฒนา [HubSpot developer](https://developers.hubspot.com/){:target=_blank .external-link} และ:

- **Client ID**: สร้างขึ้นเมื่อคุณสร้าง public app
- **Client Secret**: สร้างขึ้นเมื่อคุณสร้าง public app
- **Developer API Key**: สร้างจาก dashboard Developer Apps ของคุณ
- **App ID**: สร้างขึ้นเมื่อคุณสร้าง public app

วิธีสร้าง public app และตั้งค่า credential:

1.  เข้าสู่ระบบบัญชีนักพัฒนาแอป [HubSpot app developer account](https://developers.hubspot.com/){:target=_blank .external-link} ของคุณ
2.  เลือก **Apps** จากแถบนำทางหลัก
3.  เลือก **Get HubSpot API key** คุณอาจต้องเลือกตัวเลือก **Show key**
4.  คัดลอก key และป้อนลงใน n8n เป็น **Developer API Key**
5.  ยังคงอยู่ในหน้า HubSpot **Apps** เลือก **Create app**
6.  บนแท็บ **App Info** เพิ่ม **App name**, **Description**, **Logo** และข้อมูลติดต่อฝ่ายสนับสนุนที่คุณต้องการให้ ใครก็ตามที่พบแอปจะเห็นข้อมูลเหล่านี้
7.  เปิดแท็บ **Auth**
8.  คัดลอก **App ID** และป้อนลงใน n8n
9.  คัดลอก **Client ID** และป้อนลงใน n8n
10. คัดลอก **Client Secret** และป้อนลงใน n8n
11. ในส่วน **Scopes** เลือก **Add new scope**
12. เพิ่ม scopes ทั้งหมดที่ระบุใน [Required scopes for HubSpot Trigger node](#required-scopes-for-hubspot-trigger-node) ลงในแอปของคุณ
13. เลือก **Update**
14. คัดลอก **OAuth Redirect URL** ของ n8n และป้อนเป็น **Redirect URL** ในแอป HubSpot ของคุณ
15. เลือก **Create app** เพื่อสิ้นสุดการสร้างแอป HubSpot

 ดูคำแนะนำโดยละเอียดเพิ่มเติมได้ที่ [HubSpot Public Apps documentation](https://developers.hubspot.com/docs/api/creating-an-app){:target=_blank .external-link}

### Required scopes for HubSpot Trigger node

หากคุณกำลังสร้างแอปเพื่อใช้กับ node [HubSpot Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger.md) n8n แนะนำให้เริ่มต้นด้วย scopes เหล่านี้:

| **Element** | **Object** | **Permission** | **Scope name** |
| --- | --- | --- | --- |
| n/a | n/a | n/a | `oauth` |
| CRM | Companies | Read | `crm.objects.companies.read` |
| CRM | Companies schemas | Read | `crm.schemas.companies.read` |
| CRM | Contacts | Read | `crm.objects.contacts.read` |
| CRM | Contacts schemas | Read | `crm.schemas.contacts.read` |
| CRM | Deals | Read | `crm.objects.deals.read` |
| CRM | Deals schemas| Read | `crm.schemas.deals.read` |

/// warning | HubSpot old accounts
บัญชี HubSpot บางบัญชีไม่สามารถเข้าถึง scopes ทั้งหมดได้ HubSpot กำลังทยอยย้ายบัญชี หากคุณไม่พบ scopes ทั้งหมดในบัญชีนักพัฒนา HubSpot ปัจจุบันของคุณ ลองสร้างบัญชีนักพัฒนาใหม่
///

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณ [self-hosting](/hosting/index.md) n8n คุณจะต้องตั้งค่า OAuth2 ตั้งแต่ต้นโดยสร้าง public app ใหม่:

1.  เข้าสู่ระบบบัญชีนักพัฒนาแอป [HubSpot app developer account](https://developers.hubspot.com/){:target=_blank .external-link} ของคุณ
2.  เลือก **Apps** จากแถบนำทางหลัก
3.  เลือก **Create app**
4.  บนแท็บ **App Info** เพิ่ม **App name**, **Description**, **Logo** และข้อมูลติดต่อฝ่ายสนับสนุนที่คุณต้องการให้ ใครก็ตามที่พบแอปจะเห็นข้อมูลเหล่านี้
5.  เปิดแท็บ **Auth**
6.  คัดลอก **App ID** และป้อนลงใน n8n
7.  คัดลอก **Client ID** และป้อนลงใน n8n
8.  คัดลอก **Client Secret** และป้อนลงใน n8n
9.  ในส่วน **Scopes** เลือก **Add new scope**
10. เพิ่ม scopes ทั้งหมดที่ระบุใน [Required scopes for HubSpot node](#required-scopes-for-hubspot-node) ลงในแอปของคุณ
11. เลือก **Update**
12. คัดลอก **OAuth Redirect URL** ของ n8n และป้อนเป็น **Redirect URL** ในแอป HubSpot ของคุณ
13. เลือก **Create app** เพื่อสิ้นสุดการสร้างแอป HubSpot

ดูคำแนะนำโดยละเอียดเพิ่มเติมได้ที่ [HubSpot Public Apps documentation](https://developers.hubspot.com/docs/api/creating-an-app){:target=_blank .external-link} หากคุณต้องการรายละเอียดเพิ่มเติมเกี่ยวกับสิ่งที่เกิดขึ้นใน OAuth web flow โปรดดู [HubSpot Working with OAuth documentation](https://developers.hubspot.com/docs/api/working-with-oauth){:target=_blank .external-link}

## Required scopes for HubSpot node

หากคุณกำลังสร้างแอปเพื่อใช้กับ node [HubSpot](/integrations/builtin/app-nodes/n8n-nodes-base.hubspot.md) n8n แนะนำให้เริ่มต้นด้วย scopes เหล่านี้:

| **Element** | **Object** | **Permission** | **Scope name(s)** |
| --- | --- | --- | --- |
| n/a | n/a | n/a |  `oauth` |
| n/a | n/a | n/a |  `forms` |
| n/a | n/a | n/a |  `tickets` |
| CRM | Companies | Read <br> Write | `crm.objects.companies.read` <br> `crm.objects.companies.write`|
| CRM | Companies schemas | Read | `crm.schemas.companies.read` |
| CRM | Contacts schemas | Read | `crm.schemas.contacts.read` |
| CRM | Contacts | Read <br> Write | `crm.objects.contacts.read` <br> `crm.objects.contacts.write`|
| CRM | Deals | Read <br> Write | `crm.objects.deals.read` <br> `crm.objects.deals.write`|
| CRM | Deals schemas | Read | `crm.schemas.deals.read` |
| CRM | Owners | Read | `crm.objects.owners.read` |
| CRM | Lists | Write | `crm.lists.write` |

/// warning | HubSpot old accounts
บัญชี HubSpot บางบัญชีไม่สามารถเข้าถึง scopes ทั้งหมดได้ HubSpot กำลังทยอยย้ายบัญชี หากคุณไม่พบ scopes ทั้งหมดในบัญชีนักพัฒนา HubSpot ปัจจุบันของคุณ ลองสร้างบัญชีนักพัฒนาใหม่
///
