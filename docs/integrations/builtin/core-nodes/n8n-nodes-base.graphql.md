---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: GraphQL
description: Documentation for the GraphQL node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
priority: medium
---

# GraphQL

[GraphQL](https://graphql.org/){:target=_blank .external-link} เป็นภาษา query และ runtime สำหรับ API แบบ open-source ใช้สำหรับดึงและแก้ไขข้อมูลจาก endpoint ที่รองรับ GraphQL ใช้ GraphQL node เพื่อ query endpoint แบบ GraphQL

## Node parameters

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

### Authentication

เลือกประเภท authentication ที่ต้องการใช้

ถ้าเลือกอย่างอื่นที่ไม่ใช่ **None** จะมี parameter **Credential for <selected-auth-type>** ให้เลือกหรือสร้าง credential สำหรับ authentication นั้น

### HTTP Request Method

เลือก HTTP Request method ที่ node จะใช้ มีให้เลือก:

* **GET**
* **POST**: ถ้าเลือก POST ต้องเลือก **Request Format** สำหรับ query payload มีให้เลือก:
    * **GraphQL (Raw)**
    * **JSON**

### Endpoint

กรอก GraphQL Endpoint ที่ต้องการเชื่อมต่อ

### Ignore SSL Issues

ถ้าเปิด option นี้ n8n จะไม่ตรวจสอบ SSL certificate

### Query

กรอก GraphQL query ที่ต้องการรัน

ดูข้อมูลการเขียน query เพิ่มเติมได้ที่ [Related Resources](#related-resources)

### Response Format

เลือก format ที่ต้องการรับผลลัพธ์ query มีให้เลือก:

* **JSON**
* **String**: ถ้าเลือกแบบนี้ ให้กรอก **Response Data Property Name** เพื่อกำหนด property ที่จะเก็บ string

## Headers

กรอก **Headers** ที่ต้องการส่งไปกับ query เป็นคู่ **Name** / **Value**

## Templates and examples

[[ templatesWidget(page.title, 'graphql') ]]

## Related resources

ถ้าจะใช้ GraphQL node ควรเข้าใจภาษา query ของ GraphQL ดู tutorial ได้ที่ [Introduction to GraphQL](https://graphql.org/learn/){:target=_blank .external-link}

