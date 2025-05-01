---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Datadog credentials
description: Documentation for the Datadog credentials. Use these credentials to authenticate Datadog in n8n, a workflow automation platform.
contentType: [integration, reference]
---
# Datadog credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สมัคร [Datadog](https://app.datadoghq.eu/signup){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการยืนยันตัวตนกับบริการได้ที่ [Datadog's API documentation](https://docs.datadoghq.com/api/latest/){:target=_blank .external-link}

นี่คือ credential-only node ดูรายละเอียดเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/datadog/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using API Key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Host** ของ Datadog instance ของคุณ
- **API Key**
- **App Key**
	
ดูข้อมูลเพิ่มเติมได้ที่ [Authentication](https://docs.datadoghq.com/api/latest/authentication/){:target=_blank .external-link} บนเว็บไซต์ Datadog
