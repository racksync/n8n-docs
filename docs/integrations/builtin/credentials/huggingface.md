---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Hugging Face credentials
description: Documentation for the Hugging Face credentials. Use these credentials to authenticate Hugging Face in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Hugging Face credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

* [Hugging Face Inference](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference.md)
* [Embeddings Hugging Face Inference](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference.md)

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Hugging Face's documentation](https://huggingface.co/docs/api-inference/quicktour){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

ในการตั้งค่า credential นี้ คุณจะต้องมีบัญชี [Hugging Face](https://huggingface.co/){:target=_blank .external-link} และ:

- **API Key**: Hugging Face เรียกสิ่งเหล่านี้ว่า API tokens

วิธีรับ API token ของคุณ:

1.  เปิดโปรไฟล์ Hugging Face ของคุณและไปที่ส่วน [**Tokens**](https://huggingface.co/settings/tokens){:target=_blank .external-link}
2.  คัดลอก token ที่แสดงอยู่ที่นั่น ควรขึ้นต้นด้วย `hf_`
3.  ป้อน API token นี้เป็น **API Key** ของ n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมได้ที่ [Get your API token](https://huggingface.co/docs/api-inference/quicktour#get-your-api-token){:target=_blank .external-link}
