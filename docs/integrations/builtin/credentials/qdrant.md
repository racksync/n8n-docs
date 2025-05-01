---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Qdrant credentials
description: Documentation for the Qdrant credentials. Use these credentials to authenticate Qdrant in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Qdrant credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

* [Qdrant Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant.md)

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมที่ [Qdrant's documentation](https://qdrant.tech/documentation/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

สำหรับการตั้งค่า credentials นี้ คุณจะต้องมี [Qdrant cluster](https://qdrant.tech/documentation/cloud/create-cluster/){:target=_blank .external-link} และ:

- **API Key**
- **Qdrant URL** ของคุณ

ขั้นตอนการตั้งค่า:

1. ไปที่ [Cloud Dashboard](https://qdrant.to/cloud){:target=_blank .external-link}
2. เลือก **Access Management** เพื่อแสดง API keys ที่มีอยู่ (หรือไปที่ส่วน **API Keys** ของหน้า **Cluster detail**)
3. เลือก **Create**
4. เลือก cluster ที่คุณต้องการให้ key มีสิทธิ์เข้าถึงใน dropdown
5. เลือก **OK**
6. คัดลอก API Key และกรอกลงใน n8n credential ของคุณ
7. กรอก URL สำหรับ Qdrant cluster ของคุณใน **Qdrant URL** ดูข้อมูลเพิ่มเติมที่ [Qdrant Web UI](https://qdrant.tech/documentation/interfaces/web-ui/){:target=_blank .external-link}

ดูข้อมูลเพิ่มเติมเกี่ยวกับการสร้างและใช้ API keys ได้ที่ [Qdrant's authentication documentation](https://qdrant.tech/documentation/cloud/authentication/){:target=_blank .external-link}
