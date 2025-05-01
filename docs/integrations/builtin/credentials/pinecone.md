---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Pinecone credentials
description: Documentation for the Pinecone credentials. Use these credentials to authenticate Pinecone in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Pinecone credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

* [Pinecone Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md)

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Pinecone's documentation](https://docs.pinecone.io/reference/api/introduction){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี [Pinecone](https://www.pinecone.io/){:target=_blank .external-link} account และ:

- **API Key**

วิธีรับ API key:

1. เปิด [Pinecone console](https://app.pinecone.io/organizations/-/projects){:target=_blank .external-link} ของคุณ
2. เลือก project ที่คุณต้องการสร้าง API key หากคุณไม่มี project ที่มีอยู่ ให้สร้าง project ใหม่ ดูข้อมูลเพิ่มเติมที่ [Quickstart](https://docs.pinecone.io/guides/get-started/quickstart){:target=_blank .external-link} ของ Pinecone
3. ไปที่ **API Keys**
4. คัดลอก API Key ที่แสดงและกรอกลงใน n8n credential ของคุณ

ดูข้อมูลเพิ่มเติมที่ [Authentication documentation](https://docs.pinecone.io/guides/get-started/authentication){:target=_blank .external-link} ของ Pinecone API
