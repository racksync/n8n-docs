---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Azure OpenAI
description: เอกสารข้อมูลรับรอง Azure OpenAI ใช้ข้อมูลนี้เพื่อยืนยันตัวตน OpenAI ใน n8n
contentType: [integration, reference]
priority: medium
---

# Azure OpenAI credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Chat Azure OpenAI](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai.md)
- [Embeddings Azure OpenAI](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai.md)

## Prerequisites

- สมัคร [Azure](https://azure.microsoft.com){:target=_blank .external-link} subscription
- เข้าถึง Azure OpenAI ภายใน subscription นั้น คุณอาจต้อง [ขอสิทธิ์เข้าถึง](https://aka.ms/oai/access){:target=_blank .external-link} หากองค์กรของคุณยังไม่มี

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Azure OpenAI's API documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Resource Name**: **Name** ที่คุณตั้งให้กับ resource
- **API key**: **Key 1** ใช้งานได้ดี สามารถเข้าถึงได้ก่อน deployment ใน **Keys and Endpoint**
- **API Version** ที่ credentials ควรใช้ ดูข้อมูลเพิ่มเติมเกี่ยวกับ API versioning ใน Azure OpenAI ได้ที่ [Azure OpenAI API preview lifecycle documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation){:target=_blank .external-link}

หากต้องการข้อมูลข้างต้น ให้ [สร้างและ deploy Azure OpenAI Service resource](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource){:target=_blank .external-link}

/// note | Model name for Azure OpenAI nodes
เมื่อคุณ deploy resource แล้ว ให้ใช้ **Deployment name** เป็น model name สำหรับ Azure OpenAI nodes ที่คุณใช้ credential นี้
///
