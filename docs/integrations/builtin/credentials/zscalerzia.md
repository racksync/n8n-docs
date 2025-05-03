---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการตั้งค่า Zscaler ZIA credentials
description: วิธีตั้งค่า Zscaler ZIA credentials เพื่อเชื่อมต่อและยืนยันตัวตนกับ Zscaler ZIA ใน n8n
contentType: [integration, reference]
priority: medium
---

# Zscaler ZIA credentials

--8<-- "_snippets/integrations/builtin/credentials/cred-only-statement.md"

## Prerequisites

สร้างบัญชีแอดมินบน [Zscaler Internet Access (ZIA)](https://www.zscaler.com/products/zscaler-internet-access){:target=_blank .external-link} cloud instance

## Supported authentication methods

- Basic auth และ API key combo

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Zscaler ZIA's documentation](https://help.zscaler.com/zia/getting-started-zia-api){:target=_blank .external-link}

This is a credential-only node. ดูวิธีใช้งานเพิ่มเติมที่ [Custom API operations](/integrations/custom-operations.md) และดูตัวอย่าง workflow ได้ที่ [example workflows and related content](https://n8n.io/integrations/zscaler-zia/){:target=_blank .external-link}

## Using basic auth and API key combo

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Base URL**: ใส่ base URL ของ Zscaler ZIA cloud name ของคุณ ดูได้จาก ZIA Admin Portal ที่ **Administration > Cloud Service API Security**
- **Username**: ใส่ username ของแอดมิน ZIA
- **Password**: ใส่ password ของแอดมิน ZIA
- **Api Key**: สร้าง API key ได้ที่ **Administration > Cloud Service API Security > Cloud Service API Key**

ดูรายละเอียดเพิ่มเติมที่ [About Cloud Service API Key](https://help.zscaler.com/zia/about-cloud-service-api-key){:target=_blank .external-link}
