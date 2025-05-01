---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Auth0 Management credentials
description: Documentation for the Auth0 Management credentials. Use these credentials to authenticate Auth0 Management in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Auth0 Management credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สมัคร [Auth0](https://auth0.com){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Supported authentication methods

- API client secret

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Auth0 Management's documentation](https://auth0.com/docs/api/management/v2){:target=_blank .external-link}

นี่คือ credential-only node ดูรายละเอียดเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/auth0-management-api/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using API client secret

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- Auth0 **Domain**
- **Client ID**
- **Client Secret**

ดูคำแนะนำในการรับ Client ID และ Client Secret จากแท็บ **Settings** ของ application ได้ที่ [Auth0 Management API Get Access Tokens documentation](https://auth0.com/docs/secure/tokens/access-tokens/get-access-tokens){:target=_blank .external-link}