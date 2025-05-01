---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Fortinet FortiGate credentials
description: Documentation for the Fortinet FortiGate credentials. Use these credentials to authenticate Fortinet FortiGate in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Fortinet FortiGate credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สร้างบัญชี [Fortinet FortiGate](https://www.fortinet.com/){:target=_blank .external-link}

## Supported authentication methods

- API access token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Fortinet FortiGate's API documentation](https://docs.fortinet.com/document/fortigate/7.4.3/administration-guide/940602/using-apis){:target=_blank .external-link}

นี่คือ node แบบ credential-only ดูข้อมูลเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/fortinet-fortigate/){:target=_blank .external-link} บนเว็บไซต์ของ n8n

## Using API access token

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- API **Access Token**: หากต้องการสร้าง access token ให้สร้าง [REST API administrator](https://docs.fortinet.com/document/fortigate/7.4.3/administration-guide/399023/rest-api-administrator){:target=_blank .external-link}

ดูข้อมูลเพิ่มเติมเกี่ยวกับการยืนยันตัวตนแบบ token-based ใน FortiGate ได้ที่ [Fortinet FortiGate Using APIs documentation](https://docs.fortinet.com/document/fortigate/7.4.3/administration-guide/940602/using-apis){:target=_blank .external-link}