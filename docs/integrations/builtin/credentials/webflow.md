---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Webflow credentials
description: Documentation for Webflow credentials. Use these credentials to authenticate Webflow in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Webflow credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Webflow](/integrations/builtin/app-nodes/n8n-nodes-base.webflow.md)
- [Webflow Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.webflowtrigger.md)

## Prerequisites

- สร้างบัญชี [Webflow](https://webflow.com/){:target=_blank .external-link}
- [Create a site](https://developers.webflow.com/data/reference/structure-1#sites){:target=_blank .external-link}: จำเป็นสำหรับการยืนยันตัวตนด้วย API access token เท่านั้น

## Supported authentication methods

- API access token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Webflow's API documentation](https://developers.webflow.com/data/reference/rest-introduction){:target=_blank .external-link}

## Using API access token

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Access Token** ของ Site: Access token จะเป็นแบบเฉพาะ site ไปที่ **Site Settings > Apps & integrations > API access** แล้วเลือก **Generate API token** ดูรายละเอียดเพิ่มเติมได้ที่ [Get a Site Token](https://developers.webflow.com/data/docs/get-a-site-token){:target=_blank .external-link}

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

ถ้าคุณต้องการตั้งค่า OAuth2 ใหม่ทั้งหมด ให้ [register an application](https://developers.webflow.com/data/docs/register-an-app){:target=_blank .external-link} ใน workspace ของคุณ

ใช้ค่าต่อไปนี้สำหรับ application ของคุณ:

- คัดลอก **OAuth callback URL** จาก n8n แล้วนำไปใส่เป็น **Redirect URI** ใน application ของคุณ
- เมื่อสร้าง application เสร็จแล้ว ให้คัดลอก **Client ID** และ **Client Secret** ไปใส่ใน credential ของ n8n
- ถ้าคุณใช้ Webflow Data API V1 (deprecated) ให้เปิด toggle **Legacy** ถ้าไม่ใช้ให้ปล่อยว่างไว้

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ OAuth ได้ที่ [OAuth](https://developers.webflow.com/data/reference/oauth-app){:target=_blank .external-link}
