---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลเข้าสู่ระบบ VirusTotal
description: คู่มือการตั้งค่า credentials สำหรับเชื่อมต่อ VirusTotal กับ n8n เพื่อใช้งาน workflow automation
contentType: [integration, reference]
priority: medium
---

# VirusTotal credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สร้างบัญชี [VirusTotal](https://www.virustotal.com){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [VirusTotal's documentation](https://docs.virustotal.com/reference/overview){:target=_blank .external-link}

นี่เป็น node สำหรับ credential เท่านั้น ดูรายละเอียดเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) และดู [example workflows and related content](https://n8n.io/integrations/virustotal/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using API key

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **API Token**: ไปที่ **user account menu > API key** เพื่อรับ API key ของคุณ แล้วนำไปใส่ใน n8n เป็น **API Token** ดูรายละเอียดเพิ่มเติมได้ที่ [API authentication](https://docs.virustotal.com/reference/authentication){:target=_blank .external-link}
