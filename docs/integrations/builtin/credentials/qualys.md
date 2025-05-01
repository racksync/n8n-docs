---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Qualys credentials
description: Documentation for the Qualys credentials. Use these credentials to authenticate Qualys in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Qualys credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สร้าง [Qualys](https://www.qualys.com/){:target=_blank .external-link} user account ด้วย user role ใดก็ได้ ยกเว้น Contact

## Supported authentication methods

- Basic auth

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Qualys's documentation](https://qualysguard.qg2.apps.qualys.com/qwebhelp/fo_portal/api_doc/index.htm){:target=_blank .external-link}

นี่คือ credential-only node ดูข้อมูลเพิ่มเติมที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/qualys/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using basic auth

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Username**
- **Password**
- สตริง **Requested With**: กรอกคำอธิบาย user เช่น user agent หรือคงค่า default `n8n application` ไว้ สิ่งนี้จะตั้งค่า header `X-Requested-With` ที่จำเป็น