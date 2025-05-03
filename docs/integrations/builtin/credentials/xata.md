---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการตั้งค่า Xata credentials
description: วิธีตั้งค่า Xata credentials เพื่อเชื่อมต่อและยืนยันตัวตนกับ Xata ใน n8n
contentType: [integration, reference]
---

# Xata credentials

คุณสามารถใช้ credentials นี้เพื่อ authenticate กับ node เหล่านี้:

* [Xata](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata.md)

## Prerequisites

สมัคร [Xata](https://xata.io/){:target=_blank .external-link} หรือสร้าง database ใหม่ หรือใช้ database ที่มีอยู่แล้ว

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [Xata's documentation](https://xata.io/docs/rest-api/authentication){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **Database Endpoint**: Workspace API ต้องระบุ database ที่ต้องการใช้งานในรูปแบบนี้: `https://{workspace-display-name}-{workspace-id}.{region}.xata.sh/db/{dbname}` ดูรายละเอียดที่ [Workspace API](https://xata.io/docs/rest-api#workspace-api){:target=_blank .external-link}
    - `{workspace-display-name}`: ชื่อ workspace (ใส่หรือไม่ใส่ก็ได้) เพื่อให้ง่ายต่อการแยก workspace ถ้ามีหลาย credentials
    - `{workspace-id}`: รหัส workspace เป็นตัวอักษรและตัวเลข 6 ตัว
    - `{region}`: region ที่ database ถูก deploy อยู่ ต้องตรงกับที่ตั้ง database
    - `{dbname}`: ชื่อ database ที่ต้องการใช้งาน
- **Branch**: ใส่ชื่อ branch ของ GitHub ที่ใช้กับ database ของคุณ
- **API Key**: สร้าง API key ได้ที่ [**Account Settings**](https://app.xata.io/settings){:target=_blank .external-link} แล้วเลือก **+ Add a key** ดูรายละเอียดที่ [Generate an API Key](https://xata.io/docs/rest-api#generate-an-api-key){:target=_blank .external-link}