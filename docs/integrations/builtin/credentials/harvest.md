---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Harvest credentials
description: Documentation for Harvest credentials. Use these credentials to authenticate Harvest in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Harvest credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Harvest](/integrations/builtin/app-nodes/n8n-nodes-base.harvest.md)

## Prerequisites

สร้างบัญชี [Harvest](https://www.getharvest.com/)

## Supported authentication methods

- API access token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Harvest's API documentation](https://help.getharvest.com/api-v2/){:target=_blank .external-link}

## Using API Access Token

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- Personal **Access Token**: ดูคำแนะนำในการสร้าง personal access token ได้ที่ [Harvest Personal Access Token Authentication documentation](https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/#personal-access-tokens){:target=_blank .external-link}


## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณต้องการตั้งค่า OAuth2 ตั้งแต่ต้น หรือต้องการรายละเอียดเพิ่มเติมเกี่ยวกับสิ่งที่เกิดขึ้นใน OAuth web flow โปรดดูคำแนะนำใน [Harvest OAuth2 documentation](https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/#oauth2-application){:target=_blank .external-link} เพื่อตั้งค่า OAuth

