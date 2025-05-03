---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Intercom
description: เอกสารสำหรับ Intercom credentials ใช้เพื่อเชื่อมต่อ Intercom ใน n8n
contentType: [integration, reference]
---

# Intercom credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Intercom](/integrations/builtin/app-nodes/n8n-nodes-base.intercom.md)


## Prerequisites

- สร้างบัญชีนักพัฒนา [Intercom](https://www.intercom.com/)
- [Create an app](https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/){:target=_blank .external-link} ใน developer hub ของคุณ

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Intercom's API documentation](https://developers.intercom.com/docs/references/introduction/){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **API Key**: Intercom จะสร้าง **Access Token** โดยอัตโนมัติเมื่อคุณ [create an app](https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/){:target=_blank .external-link} ใช้ **Access Token** นี้เป็น **API Key** ของ n8n ดูคำแนะนำโดยละเอียดเพิ่มเติมได้ที่ [How to get your Access Token](https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/#how-to-get-your-access-token){:target=_blank .external-link}
