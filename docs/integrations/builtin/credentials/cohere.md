---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง Cohere
description: เอกสารข้อมูลรับรอง Cohere ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Cohere ใน n8n
contentType: [integration, reference]
---

# Cohere credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

* [Cohere](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere.md)
* [Embeddings Cohere](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere.md)

## Prerequisites

สมัคร [Cohere account](https://cohere.com/){:target=_blank .external-link} ให้เรียบร้อยก่อน

คุณจะต้องมีบัญชีที่มีสิทธิ์การเข้าถึงดังต่อไปนี้:

- สำหรับ Trial API คุณต้องมีสิทธิ์ User หรือ Owner
- สำหรับ Production API คุณต้องมีสิทธิ์ Owner

ดูข้อมูลเพิ่มเติมได้ที่ [Cohere Teams and Roles documentation](https://docs.cohere.com/reference/teams-and-roles){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการได้ที่ [Cohere's documentation](https://docs.cohere.com/reference/about){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **API Key**: หากต้องการสร้าง Cohere API key ให้ไปที่ส่วน [API Keys ของ Cohere dashboard ของคุณ](https://dashboard.cohere.com/api-keys){:target=_blank .external-link}
