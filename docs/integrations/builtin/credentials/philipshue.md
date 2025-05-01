---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Philips Hue credentials
description: Documentation for Philips Hue credentials. Use these credentials to authenticate Philips Hue in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Philips Hue credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Philips Hue](/integrations/builtin/app-nodes/n8n-nodes-base.philipshue.md)

## Prerequisites

สร้าง [Philips Hue](https://www.philips-hue.com/en-us){:target=_blank .external-link} account

## Supported authentication methods

- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Philips Hue's CLIP API documentation](https://developers.meethue.com/develop/hue-api-v2/api-reference/){:target=_blank .external-link}

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณใช้การเชื่อมต่อ OAuth ในตัว คุณไม่จำเป็นต้องกรอก **APP ID**

หากคุณต้องการกำหนดค่า OAuth2 ตั้งแต่ต้น คุณจะต้องมี [Philips Hue developer](https://developers.meethue.com/){:target=_blank .external-link} account

สร้าง remote app ใหม่บนหน้า [Add new Hue Remote API app](https://developers.meethue.com/add-new-hue-remote-api-app/)

ใช้การตั้งค่าเหล่านี้สำหรับ app ของคุณ:

- คัดลอก **OAuth Callback URL** จาก n8n และเพิ่มเป็น **Callback URL**
- คัดลอก **AppId**, **ClientId** และ **ClientSecret** และกรอกลงในฟิลด์ที่เกี่ยวข้องใน n8n
