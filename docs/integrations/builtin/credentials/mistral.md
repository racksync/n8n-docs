---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน Mistral Cloud
description: เอกสารสำหรับ Mistral Cloud credentials ใช้เพื่อยืนยันตัวตน Mistral Cloud ใน n8n
contentType: [integration, reference]
priority: medium
---

# Mistral Cloud credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

* [Mistral Cloud](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md)
* [Embeddings Mistral Cloud](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud.md)

## Prerequisites

<!-- vale off -->
- สร้างบัญชี [Mistral](https://mistral.ai/){:target=_blank .external-link} La Plateforme
- คุณต้องเพิ่มข้อมูลการชำระเงินใน **Workspace >** [**Billing**](https://admin.mistral.ai/organization/billing){:target=_blank .external-link} และเปิดใช้งานการชำระเงินเพื่อเปิดใช้งาน API keys อ้างอิง [Account setup](https://docs.mistral.ai/getting-started/quickstart/#account-setup){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
<!-- vale on -->

## Supported authentication methods

- API key

## Related resources

อ้างอิง [Mistral's API documentation](https://docs.mistral.ai/api/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ APIs

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**

เมื่อคุณเพิ่มข้อมูลการชำระเงินในบัญชี Mistral Cloud ของคุณแล้ว:

1. ลงชื่อเข้าใช้บัญชี [Mistral account](https://console.mistral.ai/home){:target=_blank .external-link} ของคุณ
2. ไปที่หน้า **API Keys**
3. เลือก **Create new key**
4. คัดลอก API key และป้อนลงใน credential ของ n8n

อ้างอิง [Account setup](https://docs.mistral.ai/getting-started/quickstart/#account-setup){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

/// note | Paid account required
Mistral ต้องการให้คุณเพิ่มข้อมูลการชำระเงินและเปิดใช้งานการชำระเงินเพื่อใช้ API keys อ้างอิงส่วน [Prerequisites](#prerequisites) ด้านบนสำหรับข้อมูลเพิ่มเติม
///
