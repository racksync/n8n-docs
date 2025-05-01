---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Webex by Cisco credentials
description: Documentation for Webex by Cisco credentials. Use these credentials to authenticate Webex by Cisco in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Webex by Cisco credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Webex by Cisco](/integrations/builtin/app-nodes/n8n-nodes-base.ciscowebex.md)
- [Webex by Cisco Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.ciscowebextrigger.md)

## Prerequisites

สมัคร [Webex by Cisco](https://www.webex.com/) (ซึ่งควรจะให้ [developer account access](https://developer.webex.com){:target=_blank .external-link} โดยอัตโนมัติ)

## Supported authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Webex's API documentation](https://developer.webex.com/docs/getting-started){:target=_blank .external-link}

## Using OAuth2

/// note | Note for n8n Cloud users
คุณจะต้องป้อน Credentials Name และเลือกปุ่ม **Connect my account** ใน OAuth credential เพื่อเชื่อมต่อบัญชี Webex by Cisco ของคุณกับ n8n เท่านั้น
///

หากคุณต้องการตั้งค่า OAuth2 ด้วยตัวเอง คุณจะต้องสร้าง integration เพื่อใช้ credential นี้ โปรดดูคำแนะนำใน [Webex Registering your Integration documentation](https://developer.webex.com/docs/integrations#registering-your-integration){:target=_blank .external-link} เพื่อเริ่มต้น

n8n แนะนำให้ใช้ **Scopes** ต่อไปนี้สำหรับ integration ของคุณ:

* `spark:rooms_read`
* `spark:messages_write`
* `spark:messages_read`
* `spark:memberships_read`
* `spark:memberships_write`
* `meeting:recordings_write`
* `meeting:recordings_read`
* `meeting:preferences_read`
* `meeting:schedules_write`
* `meeting:schedules_read`
