---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Elasticsearch credentials
description: Documentation for Elasticsearch credentials. Use these credentials to authenticate Elasticsearch in n8n, a workflow automation platform.
contentType: [integration, reference]
---

# Elasticsearch credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Elasticsearch](/integrations/builtin/app-nodes/n8n-nodes-base.elasticsearch.md)

## Prerequisites

- มี instance ของ [Elasticsearch](https://www.elastic.co/elasticsearch/){:target=_blank .external-link} ที่เข้าถึงได้
- สร้างบัญชีผู้ใช้บน instance นั้น

## Supported authentication methods

- API key
- Basic auth

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Elasticsearch's API documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html){:target=_blank .external-link}

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **URL** ของ Elasticsearch instance ของคุณ
- **API Key**: สร้าง API key ผ่าน Elasticsearch ดูคำแนะนำได้ที่ [Elasticsearch API Keys documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html){:target=_blank .external-link}

## Using basic auth

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **URL** ของ Elasticsearch instance ของคุณ
- **Username** สำหรับเข้าสู่ระบบ
- **Password** สำหรับเข้าสู่ระบบ
