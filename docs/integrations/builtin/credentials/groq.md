---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Groq credentials
description: Documentation for the Groq credentials. Use these credentials to authenticate Groq in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Groq credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

* [Groq Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq.md)

## Prerequisites

สร้างบัญชี [Groq](https://groq.com/){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Groq's documentation](https://console.groq.com/docs/quickstart){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**

วิธีรับ API key ของคุณ:

1. ไปที่หน้า [API Keys](https://console.groq.com/keys) ใน Groq console ของคุณ
2. เลือก **Create API Key**
3. ป้อน **display name** สำหรับ key เช่น `n8n integration` แล้วเลือก **Submit**
4. คัดลอก key แล้ววางลงใน credential ของ n8n

ดูข้อมูลเพิ่มเติมได้ที่ [Groq's API Keys documentation](https://console.groq.com/docs/quickstart){:target=_blank .external-link}

/// note | Groq API keys
Groq ผูก API keys กับ organization ไม่ใช่ user
///
