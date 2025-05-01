---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Microsoft Azure Monitor credentials
description: Documentation for the Microsoft Azure Monitor credentials. Use these credentials to authenticate Microsoft Azure Monitor in n8n, a workflow automation platform.
contentType: [integration, reference]
---
# Microsoft Azure Monitor credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

* สร้างบัญชีหรือสมัครสมาชิก Microsoft Azure
* แอปที่ลงทะเบียนใน Microsoft Entra ID

## Supported authentication methods

* OAuth2

## Related resources

อ้างอิง [Microsoft Azure Monitor's API documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/azure-monitor-rest-api-index){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using OAuth2

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี Microsoft Azure และ:

- **Client ID**
- **Client Secret**
- **Tenant ID**
- **Resource** ที่คุณวางแผนจะเข้าถึง

อ้างอิง [Microsoft Azure Monitor's API documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/api/access-api?tabs=rest#set-up-authentication){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการยืนยันตัวตนกับบริการ
