---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Motorhead credentials
description: Documentation for the Motorhead credentials. Use these credentials to authenticate Motorhead in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Motorhead credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

* [Motorhead](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md)

## Supported authentication methods

- API key

## Related resources

อ้างอิง [Motorhead's API documentation](https://docs.getmetal.io/rest-api/introduction){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [Motorhead](https://www.metal.ai/){:target=_blank .external-link} และ:

- **Host** URL ของคุณ
- **API Key**
- **Client ID**

วิธีตั้งค่า คุณจะต้องสร้าง API key:

1. หากคุณ self-host Motorhead ให้อัปเดต **Host** URL ให้ตรงกับ Motorhead URL ของคุณ
2. ใน Motorhead ไปที่ [**Settings > Organization**](https://app.getmetal.io/settings/organization){:target=_blank .external-link}
3. ในส่วน **API Keys** เลือก **Create**
4. ป้อน **Name** สำหรับ API Key ของคุณ เช่น `n8n integration`
5. เลือก **Generate**
6. คัดลอก **apiKey** และป้อนลงใน credential ของ n8n
7. กลับไปที่รายการ API key
8. คัดลอก **clientID** สำหรับ key และป้อนเป็น **Client ID** ใน credential ของ n8n

อ้างอิง [Generate an API key](https://docs.getmetal.io/guides/misc-get-keys){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
