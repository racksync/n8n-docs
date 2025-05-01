---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: SIGNL4 credentials
description: Documentation for SIGNL4 credentials. Use these credentials to authenticate SIGNL4 in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# SIGNL4 credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [SIGNL4](/integrations/builtin/app-nodes/n8n-nodes-base.signl4.md)

## Prerequisites

สมัคร [SIGNL4](https://www.signl4.com/){:target=_blank .external-link} account ก่อนใช้งาน

## Supported authentication methods

- Webhook secret

## Related resources

ดูรายละเอียดเพิ่มเติมได้ที่ [SIGNL4's Inbound Webhook documentation](https://connect.signl4.com/webhook/docs/index.html){:target=_blank .external-link}

## Using webhook secret

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **Team Secret**: SIGNL4 จะส่ง secret นี้ในอีเมล "✅ Sign up complete" เป็นส่วนท้ายของ webhook URL เช่น ถ้า URL คือ `https://connect.signl4.com/webhook/helloworld` team secret คือ `helloworld`

