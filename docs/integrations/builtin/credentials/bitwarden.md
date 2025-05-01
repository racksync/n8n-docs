---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Bitwarden credentials
description: Documentation for Bitwarden credentials. Use these credentials to authenticate Bitwarden in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Bitwarden credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node ต่อไปนี้:

- [Bitwarden](/integrations/builtin/app-nodes/n8n-nodes-base.bitwarden.md)

## Prerequisites

สมัคร [Bitwarden](https://vault.bitwarden.com/#/register?org=teams){:target=_blank .external-link} Teams organization หรือ Enterprise organization account (Bitwarden เปิดให้ใช้ Bitwarden Public API เฉพาะสำหรับแผน [organization](https://bitwarden.com/help/about-organizations/){:target=_blank .external-link} เหล่านี้เท่านั้น)

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Bitwarden's Public API documentation](https://bitwarden.com/help/public-api/){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Client ID**: ให้มาเมื่อคุณสร้าง API key
- **Client Secret**: ให้มาเมื่อคุณสร้าง API key
- **Environment**:
    - เลือก **Cloud-hosted** หากคุณไม่ได้ self-host Bitwarden ไม่ต้องกำหนดค่าเพิ่มเติม
    - เลือก **Self-hosted** หากคุณ host Bitwarden บน server ของคุณเอง ป้อน **Self-hosted domain** ของคุณในฟิลด์ที่เหมาะสม

Client ID และ Client Secret ต้องเป็นของ **Organization API Key** ไม่ใช่ Personal API Key ดูคำแนะนำในการสร้าง Organization API Key ได้ที่ [Bitwarden Public API Authentication documentation](https://bitwarden.com/help/public-api/#authentication){:target=_blank .external-link}

