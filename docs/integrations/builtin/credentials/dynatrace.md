---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Dynatrace credentials
description: Documentation for the Dynatrace credentials. Use these credentials to authenticate Dynatrace in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Dynatrace credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สมัคร [Dynatrace](https://www.dynatrace.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Authentication methods

- API token

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Dynatrace's API documentation](https://www.dynatrace.com/support/help/dynatrace-api){:target=_blank .external-link}

นี่คือ credential-only node ดูรายละเอียดเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/dynatrace/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using API token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Environment ID**: ดูได้จาก URL ของ Dynatrace environment ของคุณ
- **API Token**: สร้าง API token ผ่าน Dynatrace ดูคำแนะนำได้ที่ [Dynatrace API Tokens documentation](https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication#generate-api-token){:target=_blank .external-link}
