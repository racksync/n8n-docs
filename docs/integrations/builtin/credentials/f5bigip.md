---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: F5 Big-IP credentials
description: Documentation for the F5 Big-IP credentials. Use these credentials to authenticate F5 Big-IP in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# F5 Big-IP credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สร้างบัญชี [F5 Big-IP](https://www.f5.com/products/big-ip-services){:target=_blank .external-link}

## Authentication methods

- Account login

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [F5 Big-IP's API documentation](https://clouddocs.f5.com/products/big-iq/mgmt-api/v0.0/){:target=_blank .external-link}

นี่คือ node แบบ credential-only ดูข้อมูลเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/f5-big-ip/){:target=_blank .external-link} บนเว็บไซต์ของ n8n

## Using account login

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **Username**: ใช้ username ที่คุณใช้เข้าสู่ระบบ F5 Big-IP
- **Password**: ใช้ password ของผู้ใช้ที่คุณใช้เข้าสู่ระบบ F5 Big-IP
