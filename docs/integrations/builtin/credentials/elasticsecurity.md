---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Elastic Security credentials
description: Documentation for the Elastic Security credentials. Use these credentials to authenticate Elastic Security in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Elastic Security credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

- มี instance ของ [Elastic Security](https://www.elastic.co/security){:target=_blank .external-link} ที่เข้าถึงได้
- สร้างบัญชีผู้ใช้บน instance นั้น

## Authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Elastic Security's API documentation](https://www.elastic.co/guide/en/security/current/security-apis.html){:target=_blank .external-link}

นี่คือ credential-only node ดูรายละเอียดเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/elastic-security/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **URL** ของ Elastic Security instance ของคุณ
- **API Key**: สร้าง API key ผ่าน Elastic Security ดูคำแนะนำได้ที่ [Elastic Security API Keys documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html){:target=_blank .external-link}
