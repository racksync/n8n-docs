---
title: คู่มือ Trellix ePO credentials
description: คู่มือการตั้งค่า Trellix ePO credentials สำหรับเชื่อมต่อ Trellix ePO กับ n8n
contentType: [integration, reference]
priority: medium
---

# Trellix ePO credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สร้างบัญชี [Trellix ePolicy Orchestrator](https://www.trellix.com/products/epo/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- Basic auth

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Trellix ePO's documentation](https://docs.trellix.com/bundle/epolicy-orchestrator-web-api-reference-guide/page/GUID-D87A6839-AED2-47B0-BE93-5BF83F710278.html){:target=_blank .external-link}

นี่คือ node สำหรับ credential เท่านั้น ดูข้อมูลเพิ่มเติมได้ที่ [Custom API operations](/integrations/custom-operations.md) และดู [example workflows and related content](https://n8n.io/integrations/trellix-epo/){:target=_blank .external-link} บนเว็บไซต์ n8n

## Using basic auth

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Username** ที่จะใช้เชื่อมต่อ
- **Password** ของบัญชีผู้ใช้นั้น

n8n จะใช้ field เหล่านี้ในการสร้าง parameter `-u` ในรูปแบบ `-u username:pw` ดูรายละเอียดเพิ่มเติมได้ที่ [Web API basics](https://docs.trellix.com/bundle/epolicy-orchestrator-web-api-reference-guide/page/GUID-2503B69D-2BCE-4491-9969-041838B39C1F.html){:target=_blank .external-link}