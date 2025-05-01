---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Miro credentials
description: Documentation for the Miro credentials. Use these credentials to authenticate Miro in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Miro credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สร้างบัญชี [Miro](https://miro.com/)

## Supported authentication methods

* OAuth2

## Related resources

อ้างอิง [Miro's API documentation](https://developers.miro.com/reference/overview) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

นี่คือ node สำหรับ credential เท่านั้น อ้างอิง [Custom API operations](/integrations/custom-operations.md) เพื่อเรียนรู้เพิ่มเติม ดู [example workflows and related content](https://n8n.io/integrations/miro/) บนเว็บไซต์ของ n8n

## Using OAuth2

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชีและแอป [Miro](https://miro.com/login/) รวมถึง:

- **Client ID**: สร้างขึ้นเมื่อคุณสร้างแอปพลิเคชัน OAuth2 ใหม่
- **Client Secret**: สร้างขึ้นเมื่อคุณสร้างแอปพลิเคชัน OAuth2 ใหม่

อ้างอิง [Miro's API documentation](https://developers.miro.com/reference/overview) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการยืนยันตัวตนกับบริการ

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณ [self-hosting](/hosting/index.md) n8n คุณจะต้อง [สร้างแอป](https://developers.miro.com/docs/rest-api-build-your-first-hello-world-app) เพื่อกำหนดค่า OAuth2 อ้างอิง [Miro's OAuth documentation](https://developers.miro.com/docs/getting-started-with-oauth){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการตั้งค่า OAuth2
