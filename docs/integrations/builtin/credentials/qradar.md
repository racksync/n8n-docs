---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน QRadar
description: เอกสารสำหรับข้อมูลยืนยันตัวตน QRadar ใช้ข้อมูลนี้เพื่อยืนยันตัวตน QRadar ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
---

# QRadar credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สร้าง [Qradar](https://www.ibm.com/qradar){:target=_blank .external-link} account

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [QRadar's documentation](https://ibmsecuritydocs.github.io/qradar_api_overview/){:target=_blank .external-link}

นี่คือ credential-only node ดูข้อมูลเพิ่มเติมที่ [Custom API operations](/integrations/custom-operations.md) ดู [example workflows and related content](https://n8n.io/integrations/qradar/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using API key

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี:

- **API Key**: หรือที่เรียกว่า authorized service token ใช้หน้าต่าง **Manage Authorized Services** บนแท็บ **Admin** เพื่อสร้าง authentication token ดูข้อมูลเพิ่มเติมที่ [Creating an authentication token](https://www.ibm.com/docs/en/qradar-common?topic=forwarding-creating-authentication-token){:target=_blank .external-link}
