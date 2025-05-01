---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ActiveCampaign credentials
description: Documentation for ActiveCampaign credentials. Use these credentials to authenticate ActiveCampaign in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# ActiveCampaign credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [ActiveCampaign](/integrations/builtin/app-nodes/n8n-nodes-base.activecampaign.md)
- [Active Campaign Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.activecampaigntrigger.md)

## Supported authentication methods

* API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับการทำงานกับบริการได้ที่ [ActiveCampaign's API documentation](https://help.activecampaign.com/hc/en-us/sections/360005740979-ActiveCampaign-API-Resources){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมีบัญชี [ActiveCampaign](https://www.activecampaign.com/){:target=_blank .external-link} และ:

- **API URL**
- **API Key**

วิธีรับทั้งสองอย่างและตั้งค่า credential:

1. ใน ActiveCampaign เลือก **Settings** (ไอคอนรูปเฟือง) จากเมนูด้านซ้าย
2. เลือก **Developer**
3. คัดลอก **API URL** และป้อนลงใน n8n credential ของคุณ
4. คัดลอก **API Key** และป้อนลงใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมหรือคำแนะนำในการรีเซ็ต API key ของคุณได้ที่ [How to obtain your ActiveCampaign API URL and Key](https://help.activecampaign.com/hc/en-us/articles/207317590-Getting-started-with-the-API#h_01HJ6REM2YQW19KYPB189726ST){:target=_blank .external-link}
