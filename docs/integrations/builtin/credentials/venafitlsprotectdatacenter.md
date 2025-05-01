---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Venafi TLS Protect Datacenter credentials
description: Documentation for Venafi TLS Protect Datacenter credentials. Use these credentials to authenticate Venafi TLS Protect Datacenter in n8n, a workflow automation platform.
contentType: [integration, reference]
---
<!-- vale off -->
# Venafi TLS Protect Datacenter credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

* [Venafi TLS Protect Datacenter node](/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectdatacenter.md)

## Prerequisites

- สมัครบัญชี Venafi [TLS Protect Datacenter](https://venafi.com/){:target=_blank .external-link}
- ตั้งค่า expiration และ refresh time สำหรับ token ดูรายละเอียดที่ [Setting up token authentication](https://docs.venafi.com/Docs/current/TopNav/Content/SDK/AuthSDK/t-SDKa-Setup-OAuth.php){:target=_blank .external-link}
- สร้าง [API integration](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/c-APIAppIntegrations-about.php){:target=_blank .external-link} ที่ **API > Integrations** ดูวิธีการที่ [Integrating other systems with Venafi products](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/t-APIAppIntegrations-creating.php){:target=_blank .external-link}
    - จด Client ID สำหรับ integration ของคุณไว้
    - เลือก scope ที่ต้องการใช้งานใน n8n ดูตาราง scope ได้ที่ [Integrating other systems with Venafi products](https://docs.venafi.com/Docs/current/TopNav/Content/API-ApplicationIntegration/t-APIAppIntegrations-creating.php){:target=_blank .external-link}

## Supported authentication methods

- API integration

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Venafi's API integration documentation](https://docs.venafi.com/Docs/currentSDK/TopNav/Content/SDK/WebSDK/c-sdk-AboutThisGuide.php){:target=_blank .external-link}

## Using API integration

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Domain**: ใส่ domain ของ Venafi TLS Protect Datacenter ของคุณ
- **Client ID**: ใส่ Client ID จาก API integration ดูรายละเอียดใน [Prerequisites](#prerequisites)
- **Username**: ใส่ username ของคุณ
- **Password**: ใส่ password ของคุณ
- **Allow Self-Signed Certificates**: ถ้าเปิดใช้งาน credential จะยอมรับ self-signed certificates ได้

<!-- vale on -->