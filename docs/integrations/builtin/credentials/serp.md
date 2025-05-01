---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Serp credentials
description: Documentation for the Serp credentials. Use these credentials to authenticate Serp in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: high
---

# Serp credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

* [Serp](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md)

## Prerequisites

สมัคร [SerpApi](https://serpapi.com/){:target=_blank .external-link} ก่อนใช้งาน

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมได้ที่ [Serp's API documentation](https://serpapi.com/search-api){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **API Key**

วิธีรับ API key:

1. ไปที่ **Your Account >** [**API Key**](https://serpapi.com/manage-api-key){:target=_blank .external-link}
2. คัดลอก **Your Private API Key** แล้วนำไปใส่ในช่อง **API Key** ของ n8n credential
