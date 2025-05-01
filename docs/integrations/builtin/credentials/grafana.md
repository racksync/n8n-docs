---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Grafana credentials
description: Documentation for Grafana credentials. Use these credentials to authenticate Grafana in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Grafana credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [Grafana](/integrations/builtin/app-nodes/n8n-nodes-base.grafana.md)

## Prerequisites

- สร้างบัญชี [Grafana](https://grafana.com/){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับการยืนยันตัวตนกับบริการนี้ได้ที่ [Grafana's API documentation](https://grafana.com/docs/grafana/latest/developers/http_api/){:target=_blank .external-link}

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**: ดูคำแนะนำโดยละเอียดเกี่ยวกับการสร้าง API key ได้ที่ [Create an API key documentation](https://grafana.com/docs/grafana/latest/administration/api-keys/#create-an-api-key){:target=_blank .external-link}
- **Base URL** สำหรับ instance ของ Grafana ของคุณ ตัวอย่างเช่น: `https://n8n.grafana.net`

