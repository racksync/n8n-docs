---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Cisco Secure Endpoint credentials
description: Documentation for the Cisco Secure Endpoint credentials. Use these credentials to authenticate Cisco Secure Endpoint in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Cisco Secure Endpoint credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

- สมัคร [Cisco DevNet developer account](https://developer.cisco.com){:target=_blank .external-link} ให้เรียบร้อยก่อน
- เข้าถึง [Cisco Secure Endpoint license](https://www.cisco.com/site/us/en/products/security/endpoint-security/secure-endpoint/index.html){:target=_blank .external-link}

## Authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Cisco Secure Endpoint's documentation](https://developer.cisco.com/docs/secure-endpoint/introduction/){:target=_blank .external-link}

นี่คือ credential-only node ดูรายละเอียดเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/cisco-secure-endpoint/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using OAuth2

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Region** สำหรับ Cisco Secure Endpoint ของคุณ ตัวเลือกคือ:
    - Asia Pacific, Japan, and China
    - Europe
    - North America
- **Client ID**: ให้มาเมื่อคุณลงทะเบียน SecureX API Client
- **Client Secret**: ให้มาเมื่อคุณลงทะเบียน SecureX API Client

หากต้องการรับ Client ID และ Client Secret คุณจะต้องลงทะเบียน SecureX API Client ดูคำแนะนำโดยละเอียดได้ที่ [Cisco Secure Endpoint's authentication documentation](https://developer.cisco.com/docs/secure-endpoint/authentication/#authentication){:target=_blank .external-link} ใช้ SecureX **Client Password** เป็น **Client Secret** ภายใน n8n credential

