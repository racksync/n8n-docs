---
title: ข้อมูลเข้าสู่ระบบ Serp
description: คู่มือการตั้งค่า Serp credentials สำหรับเชื่อมต่อ Serp กับ n8n
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
