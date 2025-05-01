---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Gemini(PaLM) credentials
description: Documentation for the Google Gemini(PaLM) credentials. Use these credentials to authenticate Google Gemini and Google PaLM AI nodes in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: high
---

# Google Gemini(PaLM) credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

* [Embeddings Google Gemini](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini.md)
* [Google Gemini Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini.md)
* [Embeddings Google PaLM](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm.md)

## Prerequisites

* สร้างบัญชี [Google Cloud](https://cloud.google.com/){:target=_blank .external-link}
* สร้าง [Google Cloud Platform project](https://developers.google.com/workspace/marketplace/create-gcp-project){:target=_blank .external-link}

## Supported authentication methods

- Gemini(PaLM) API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Google's Gemini API documentation](https://ai.google.dev/gemini-api/docs){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using Gemini(PaLM) API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- API **Host** URL: ทั้ง PaLM และ Gemini ใช้ค่าเริ่มต้น `https://generativelanguage.googleapis.com`
- **API Key**: สร้าง key ใน [Google AI Studio](https://makersuite.google.com/app/apikey){:target=_blank .external-link}

/// warning | Custom hosts not supported
node ที่เกี่ยวข้องยังไม่รองรับ custom hosts หรือ proxies สำหรับ API host และต้องใช้ 'https://generativelanguage.googleapis.com'
///

วิธีสร้าง API key:

1. ไปที่หน้า API Key ใน Google AI Studio: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey){:target=_blank .external-link}
2. เลือก **Create API Key**
3. คุณสามารถเลือกได้ว่าจะ **Create API key in new project** หรือค้นหา Google Cloud project ที่มีอยู่เพื่อ **Create API key in existing project**
4. คัดลอก API key ที่สร้างขึ้นและเพิ่มลงใน credential ของ n8n
