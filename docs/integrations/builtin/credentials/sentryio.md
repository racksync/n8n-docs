---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Sentry.io credentials
description: Documentation for Sentry.io credentials. Use these credentials to authenticate Sentry.io in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Sentry.io credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Sentry.io](/integrations/builtin/app-nodes/n8n-nodes-base.sentryio.md)

## Prerequisites

สร้าง [Sentry.io](https://sentry.io/){:target=_blank .external-link} account

## Supported authentication methods

- API token
- OAuth2
- Server API token: ใช้สำหรับ [self-hosted Sentry](https://develop.sentry.dev/self-hosted/){:target=_blank .external-link}

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Sentry.io's API documentation](https://docs.sentry.io/api/){:target=_blank .external-link}

## Using API token

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Token**: สร้าง [**User Auth Token**](https://sentry.io/settings/account/api/auth-tokens/){:target=_blank .external-link} ที่ **Account > Settings > User Auth Tokens** ดูรายละเอียดเพิ่มเติมที่ [User Auth Tokens](https://docs.sentry.io/account/auth-tokens/#user-auth-tokens){:target=_blank .external-link}

## Using OAuth

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

ถ้าคุณต้องการตั้งค่า OAuth2 เอง [create an integration](https://docs.sentry.io/organization/integrations/integration-platform/#creating-an-integration){:target=_blank .external-link} โดยใช้ค่าต่อไปนี้:

- คัดลอก **OAuth Callback URL** ของ n8n ไปใส่ใน **Authorized Redirect URI**
- คัดลอก **Client ID** และ **Client Secret** ไปใส่ใน n8n credential

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการสร้าง integration ได้ที่ [Public integrations](https://docs.sentry.io/organization/integrations/integration-platform/public-integration/){:target=_blank .external-link}

## Using Server API token

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Token**: สร้าง [**User Auth Token**](https://sentry.io/settings/account/api/auth-tokens/){:target=_blank .external-link} ที่ **Account > Settings > User Auth Tokens** ดูรายละเอียดเพิ่มเติมที่ [User Auth Tokens](https://docs.sentry.io/account/auth-tokens/#user-auth-tokens){:target=_blank .external-link}
- **URL**: URL ของ self-hosted Sentry instance ของคุณ
