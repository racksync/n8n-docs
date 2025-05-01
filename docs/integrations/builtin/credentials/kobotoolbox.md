---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: KoboToolbox credentials
description: Documentation for KoboToolbox credentials. Use these credentials to authenticate KoboToolbox in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# KoboToolbox credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

* [KoboToolbox trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.kobotoolboxtrigger.md)
* [KoboToolbox](/integrations/builtin/app-nodes/n8n-nodes-base.kobotoolbox.md)

## Prerequisites

สร้างบัญชี [KoboToolbox](https://www.kobotoolbox.org/){:target=_blank .external-link}

## Supported authentication methods

- API token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [KoboToolbox's API documentation](https://support.kobotoolbox.org/api.html){:target=_blank .external-link}

## Using API token

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **API Root URL**: ป้อน URL ของ KoboToolbox server ที่คุณสร้างบัญชี สำหรับ Global KoboToolbox Server ใช้ `https://kf.kobotoolbox.org` สำหรับ European Union KoboToolbox Server ใช้ `https://eu.kobotoolbox.org`
- **API Token**: แสดงใน **Account Settings** ของคุณ ดูข้อมูลเพิ่มเติมได้ที่ [Getting your API token](https://support.kobotoolbox.org/api.html#getting-your-api-token){:target=_blank .external-link}
