---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Pipedrive credentials
description: Documentation for Pipedrive credentials. Use these credentials to authenticate Pipedrive in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Pipedrive credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Pipedrive](/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive.md)
- [Pipedrive Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.pipedrivetrigger.md)

## Supported authentication methods

- API token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Pipedrive's developer documentation](https://pipedrive.readme.io/docs/getting-started){:target=_blank .external-link}

## Using API token

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี [Pipedrive](https://pipedrive.com/){:target=_blank .external-link} account และ:

- **API Token**

วิธีรับ API token ของคุณ:

1. เปิด [**API Personal Preferences**](https://app.pipedrive.com/settings/api){:target=_blank .external-link} ของคุณ
2. คัดลอก **Your personal API token** และกรอกลงใน n8n credential ของคุณ

หากคุณมีหลายบริษัท คุณจะต้องเลือกบริษัทที่ถูกต้องก่อน:

1. เลือกชื่อ account ของคุณและตรวจสอบให้แน่ใจว่าคุณกำลังดูบริษัทที่ถูกต้อง
2. จากนั้นเลือก **Company Settings**
2. เลือก **Personal Preferences**
3. เลือกแท็บ **API**
4. คัดลอก **Your personal API token** และกรอกลงใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมที่ [How to find the API token](https://pipedrive.readme.io/docs/how-to-find-the-api-token){:target=_blank .external-link}

## Using OAuth2

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี [Pipedrive developer sandbox account](https://developers.pipedrive.com/){:target=_blank .external-link} และ:

- **Client ID**
- **Client Secret**

หากต้องการรับทั้งสองอย่าง คุณจะต้องลงทะเบียน app ใหม่:

1. เลือกชื่อโปรไฟล์ของคุณที่มุมบนขวา
2. ค้นหาชื่อบริษัทของ sandbox account ของคุณและเลือก **Developer Hub**

    /// note | No Developer Hub
    หากคุณไม่เห็น **Developer Hub** ใน dropdown ของ account ของคุณ ให้ลงทะเบียน [developer sandbox account](https://developers.pipedrive.com/){:target=_blank .external-link}
    ///

3. เลือก **Create an app**
4. เลือก **Create public app** แท็บ **Basic info** ของ app จะเปิดขึ้น
5. กรอก **App name** สำหรับ app ของคุณ เช่น `n8n integration`
6. คัดลอก **OAuth Redirect URL** จาก n8n และเพิ่มเป็น **Callback URL** ของ app
7. เลือก **Save** แท็บ **OAuth & access scopes** ของ app จะเปิดขึ้น
8. เปิดใช้งาน **Scopes** ที่เหมาะสมสำหรับ app ของคุณ ดูคำแนะนำเพิ่มเติมที่ [Pipedrive node scopes](#pipedrive-node-scopes) และ [Pipedrive Trigger node scopes](#pipedrive-trigger-node-scopes) ด้านล่าง
8. คัดลอก **Client ID** และกรอกลงใน n8n credential ของคุณ
9. คัดลอก **Client Secret** และกรอกลงใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมที่ [Registering a public app](https://pipedrive.readme.io/docs/marketplace-registering-the-app){:target=_blank .external-link}

### Pipedrive node scopes

scopes ที่คุณเพิ่มลงใน app ของคุณขึ้นอยู่กับว่าคุณต้องการใช้ node ใดใน n8n และต้องการดำเนินการใดกับ node เหล่านั้น

Scopes ที่คุณอาจต้องการสำหรับ [Pipedrive](/integrations/builtin/app-nodes/n8n-nodes-base.pipedrive.md) node:

| **Object** | **Node action** | **UI scope** | **Actual scope** |
| --- | --- | --- | --- |
| Activity | Get data of an activity <br> Get data of all activities | **Activities: Read only** หรือ <br> **Activities: Full Access** | `activities:read` หรือ <br> `activities:full` |
| Activity | Create <br> Delete <br> Update | **Activities: Full Access** | `activities:full` |
| Deal | Get data of a deal <br> Get data of all deals <br> Search a deal | **Deals: Read only** หรือ <br> **Deals: Full Access** | `deals:read` หรือ <br> `deals:full` |
| Deal | Create <br> Delete <br> Duplicate <br> Update | **Deals: Full Access** | `deals:full` |
| Deal Activity | Get all activities of a deal | **Activities: Read only** หรือ <br> **Activities: Full Access** | `activities:read` หรือ <br> `activities:full` |
| Deal Product | Get all products in a deal |  **Products: Read Only** หรือ <br> **Products: Full Access** | `products:read` หรือ <br> `products:full` |
| File | Download <br> Get data of a file | ดูหมายเหตุด้านล่าง | ดูหมายเหตุด้านล่าง |
| File | Create <br> Delete | ดูหมายเหตุด้านล่าง | ดูหมายเหตุด้านล่าง |
| Lead | Get data of a lead <br> Get data of all leads | **Leads: Read only** หรือ <br> **Leads: Full access** | `leads:read` หรือ <br> `leads:full` |
| Lead | Create <br> Delete <br> Update | **Leads: Full access** | `leads:full` |
| Note | Get data of a note <br> Get data of all notes | ดูหมายเหตุด้านล่าง | ดูหมายเหตุด้านล่าง |
| Note | Create <br> Delete <br> Update | ดูหมายเหตุด้านล่าง | ดูหมายเหตุด้านล่าง |
| Organization | Get data of an organization <br> Get data of all organizations <br> Search | **Contacts: Read Only** หรือ <br> **Contacts: Full Access** | `contacts:read` หรือ <br> `contacts:full` |
| Organization | Create <br> Delete <br> Update | **Contacts: Full Access** | `contacts:full` |
| Person | Get data of a person <br> Get data of all persons <br> Search | **Contacts: Read Only** หรือ <br> **Contacts: Full Access** | `contacts:read` หรือ <br> `contacts:full` |
| Person | Create <br> Delete <br> Update | **Contacts: Full Access** | `contacts:full` |
| Product | Get data of all products | **Products: Read Only** | `products:read` |

/// note | Files and Notes
scopes สำหรับ Files และ Notes ขึ้นอยู่กับ object ที่เกี่ยวข้อง:

- Files เกี่ยวข้องกับ Deals, Activities หรือ Contacts
- Notes เกี่ยวข้องกับ Deals หรือ Contacts

โปรดดู scopes ของ object เหล่านั้น
///

Pipedrive node ยังรองรับ Custom API calls เพิ่ม scopes ที่เกี่ยวข้องสำหรับ custom API calls ใดๆ ที่คุณตั้งใจจะทำ

ดูข้อมูลเพิ่มเติมที่ [Scopes and permissions explanations](https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations){:target=_blank .external-link}

### Pipedrive Trigger node scopes

[Pipedrive Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.pipedrivetrigger.md) node ต้องการ scope **Webhooks: Full access** (`webhooks:full`)
