---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Bitly
description: เอกสารข้อมูลรับรอง Bitly ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Bitly ใน n8n
contentType: [integration, reference]
---

# Bitly credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node ต่อไปนี้:

- [Bitly](/integrations/builtin/app-nodes/n8n-nodes-base.bitly.md)

## Prerequisites

สมัคร [Bitly](https://www.bitly.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน

## Supported authentication methods

- API token
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Bitly's API documentation](https://dev.bitly.com/){:target=_blank .external-link}

## Using API token

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Access Token**: เมื่อล็อกอินแล้ว ไปที่ [Settings > Developer Settings > API](https://app.bitly.com/settings/api/){:target=_blank .external-link} เพื่อสร้าง Access Token


## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

หากคุณต้องการตั้งค่า OAuth2 ด้วยตัวเอง หรือต้องการรายละเอียดเพิ่มเติมเกี่ยวกับขั้นตอน OAuth web flow โปรดดูข้อมูลเพิ่มเติมได้ที่ [Bitly API Authentication documentation](https://dev.bitly.com/docs/getting-started/authentication/){:target=_blank .external-link}

