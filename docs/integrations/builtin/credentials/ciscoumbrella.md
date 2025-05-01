---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Cisco Umbrella credentials
description: Documentation for the Cisco Umbrella credentials. Use these credentials to authenticate Cisco Umbrella in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Cisco Umbrella credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

- สมัคร [Cisco DevNet developer account](https://developer.cisco.com){:target=_blank .external-link} ให้เรียบร้อยก่อน
- บัญชีผู้ใช้ [Cisco Umbrella](https://umbrella.cisco.com/){:target=_blank .external-link} ที่มี role **Full Admin**

## Authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Cisco Umbrella's API documentation](https://developer.cisco.com/docs/cloud-security/){:target=_blank .external-link}

นี่คือ credential-only node ดูรายละเอียดเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/cisco-umbrella/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **API Key**
- **Secret**: ให้มาเมื่อคุณสร้าง API key

ดูคำแนะนำในการสร้าง Umbrella API key ได้ที่ [Cisco Umbrella Manage API Keys documentation](https://developer.cisco.com/docs/cloud-security/authentication/#manage-api-keys){:target=_blank .external-link}
