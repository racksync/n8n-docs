---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Webhook credentials
description: Documentation for Webhook credentials. Use these credentials to authenticate Webhook in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: critical
---

# Webhook credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md)

## Prerequisites

คุณต้องใช้วิธีการยืนยันตัวตนที่แอปหรือบริการที่คุณต้องการเชื่อมต่อกำหนดไว้

## Supported authentication methods

- Basic auth
- Header auth
- JWT auth
- None

--8<-- "_snippets/integrations/builtin/credentials/generic-auth/basic-auth.md"

--8<-- "_snippets/integrations/builtin/credentials/generic-auth/header-auth.md"

## Using JWT auth

[**JWT Auth**](https://jwt.io/introduction/){:target=_blank .external-link} เป็นวิธีการยืนยันตัวตนที่ใช้ JSON Web Tokens (JWT) ในการเซ็นข้อมูลแบบดิจิทัล วิธีนี้จะใช้ **JWT credential** และสามารถใช้ได้ทั้ง **Passphrase** หรือ **PEM Key** เป็น key type ดูรายละเอียดเพิ่มเติมได้ที่ [JWT credential](/integrations/builtin/credentials/jwt.md)
