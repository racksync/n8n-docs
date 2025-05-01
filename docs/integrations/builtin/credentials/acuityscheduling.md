---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Acuity Scheduling credentials
description: Documentation for Acuity Scheduling credentials. Use these credentials to authenticate Acuity Scheduling in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Acuity Scheduling credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Acuity Scheduling Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.acuityschedulingtrigger.md)

## Prerequisites

สมัคร [Acuity Scheduling](https://acuityscheduling.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Supported authentication methods

- API key
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับบริการได้ที่ [Acuity's API documentation](https://developers.acuityscheduling.com/reference/quick-start){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **User ID** ที่เป็นตัวเลข
- **API Key**

ดู [Acuity API Quick Start authentication instructions](https://developers.acuityscheduling.com/reference/quick-start#authentication){:target=_blank .external-link} เพื่อสร้าง API key และดู User ID ของคุณ

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณต้องการตั้งค่านี้ด้วยตัวเอง ให้กรอก [Acuity OAuth2 Account Registration page](https://acuityscheduling.com/oauth2/register){:target=_blank .external-link} ใช้ **Client ID** และ **Client Secret** ที่ให้มาจากการลงทะเบียนนั้น
