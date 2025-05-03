---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลเข้าสู่ระบบ Venafi TLS Protect Cloud
description: คู่มือการตั้งค่า credentials สำหรับเชื่อมต่อ Venafi TLS Protect Cloud กับ n8n เพื่อใช้งาน workflow automation
contentType: [integration, reference]
---

# Venafi TLS Protect Cloud credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

* [Venafi TLS Protect Cloud node](/integrations/builtin/app-nodes/n8n-nodes-base.venafitlsprotectcloud.md)
* [Venafi TLS Protect Cloud Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.venafitlsprotectcloudtrigger.md)

## Prerequisites

สมัครบัญชี Venafi [TLS Protect Cloud](https://venafi.com/tls-protect/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Venafi TLS Protect Cloud's API documentation](https://docs.venafi.cloud/api/vaas-rest-api/){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Region**: เลือก region ที่ตรงกับความต้องการของธุรกิจคุณ ถ้าอยู่ใน EU ให้เลือก **EU** ถ้าไม่ใช่ให้เลือก **US**
- **API Key**: ไปที่ **avatar > Preferences > API Keys** เพื่อรับ API key ของคุณ หรือจะใช้ VCert เพื่อรับ API key ก็ได้ ดูรายละเอียดเพิ่มเติมที่ [Obtaining an API Key](https://docs.venafi.cloud/api/obtaining-api-key/){:target=_blank .external-link}
