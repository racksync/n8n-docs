---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Airtable
description: เอกสารข้อมูลรับรอง Airtable ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Airtable ใน n8n
contentType: [integration, reference]
priority: high
---

# Airtable credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Airtable](/integrations/builtin/app-nodes/n8n-nodes-base.airtable/index.md)
- [Airtable Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger.md)

## Prerequisites

สมัคร [Airtable](https://airtable.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Supported authentication methods

- Personal Access Token (PAT)
- OAuth2

/// note | API Key deprecation
n8n เคยมีวิธีการยืนยันตัวตนด้วย API key กับ Airtable Airtable [ยกเลิกการใช้งาน keys เหล่านี้อย่างสมบูรณ์](https://support.airtable.com/v1/docs/airtable-api-deprecation-guidelines){:target=_blank .external-link} ณ เดือนกุมภาพันธ์ 2024 หากคุณเคยใช้ Airtable API credential ให้แทนที่ด้วย Airtable Personal Access Token หรือ Airtable OAuth2 credential n8n แนะนำให้ใช้ Personal Access Token แทน
///

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Airtable's API documentation](https://airtable.com/developers/web/api/authentication){:target=_blank .external-link}

## Using personal access token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- Personal **Access Token** (PAT)

วิธีสร้าง PAT ของคุณ:

1. ไปที่หน้า Airtable Builder Hub [Personal access tokens](https://airtable.com/create/tokens){:target=_blank .external-link}
1. เลือก **+ Create new token** Airtable จะเปิดหน้า **Create personal access token**
1. ป้อน **Name** สำหรับ token ของคุณ เช่น `n8n credential`
1. เพิ่ม **Scopes** ให้กับ token ของคุณ ดูข้อมูลเพิ่มเติมได้ที่คู่มือ [Scopes](https://airtable.com/developers/web/api/scopes){:target=_blank .external-link} ของ Airtable n8n แนะนำให้ใช้ scopes เหล่านี้:
    - `data.records:read`
    - `data.records:write`
    - `schema.bases:read`
1. เลือก **Access** สำหรับ token ของคุณ เลือกจาก base เดียว, หลาย bases (แม้กระทั่ง bases จาก workspaces ที่แตกต่างกัน), bases ทั้งหมดในปัจจุบันและอนาคตใน workspace ที่คุณเป็นเจ้าของ หรือ bases ทั้งหมดจาก workspace ใดๆ ที่คุณเป็นเจ้าของ รวมถึง bases/workspace ที่เพิ่มเข้ามาในอนาคต
1. เลือก **Create token**
1. Airtable จะเปิด modal พร้อม token ของคุณที่แสดงอยู่ คัดลอก token นี้และป้อนลงใน n8n credential ของคุณเป็น **Access Token**

ดูข้อมูลเพิ่มเติมได้ที่ [Find/create PATs documentation](https://support.airtable.com/v1/docs/creating-personal-access-tokens){:target=_blank .external-link} ของ Airtable

## Using OAuth2

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **OAuth Redirect URL**
- **Client ID**
- **Client Secret**

หากต้องการสร้างข้อมูลทั้งหมดนี้ ให้ลงทะเบียน Airtable integration ใหม่:

1. เปิดหน้า Airtable Builder Hub [**OAuth integrations**](https://airtable.com/create/oauth){:target=_blank .external-link} ของคุณ
2. เลือกปุ่ม **Register new OAuth integration**
3. ป้อนชื่อสำหรับ OAuth integration ของคุณ
4. คัดลอก **OAuth Redirect URL** จาก n8n credential ของคุณ
5. วาง redirect URL นั้นใน Airtable เป็น **OAuth redirect URL**
6. เลือก **Register integration**
7. ในหน้าถัดไป คัดลอก **Client ID** จาก Airtable และวางลงใน **Client ID** ใน n8n credential ของคุณ
8. ใน Airtable เลือก **Generate client secret**
9. คัดลอก client secret และวางลงใน **Client Secret** ใน n8n credential ของคุณ
10. เลือก scopes ต่อไปนี้ใน Airtable:
    - `data.records:read`
    - `data.records:write`
    - `schema.bases:read`
11. เลือก **Save changes** ใน Airtable
12. ใน n8n credential ของคุณ เลือก **Connect my account** modal **Grant access** จะเปิดขึ้น
13. ทำตามคำแนะนำและเลือก base ที่คุณต้องการทำงาน (หรือ bases ทั้งหมด)
14. เลือก **Grant access** เพื่อทำการเชื่อมต่อให้เสร็จสิ้น

ดูขั้นตอนเกี่ยวกับการลงทะเบียน Oauth integration ใหม่ได้ที่ [Airtable Register a new integration documentation](https://airtable.com/developers/web/guides/oauth-integrations){:target=_blank .external-link}
