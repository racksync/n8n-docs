---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการตั้งค่า Zep credentials
description: วิธีตั้งค่า Zep credentials เพื่อเชื่อมต่อและยืนยันตัวตนกับ Zep ใน n8n
contentType: [integration, reference]
priority: medium
---

# Zep credentials

คุณสามารถใช้ credentials นี้เพื่อ authenticate กับ node เหล่านี้:

* [Zep](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep.md)
* [Zep Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep.md)

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน SDK ได้ที่ [Zep's Cloud SDK documentation](https://help.getzep.com/sdks){:target=_blank .external-link} และ [Open Source SDK documentation](https://docs.getzep.com/sdk/){:target=_blank .external-link} สำหรับ REST API ดูที่ [Zep's REST API documentation](https://getzep.github.io/zep/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี [Zep server](https://www.getzep.com/){:target=_blank .external-link} ที่มี project อย่างน้อย 1 อัน และ:

- **API URL**
- **API Key**

วิธี setup ขึ้นอยู่กับว่าคุณใช้ Zep Cloud หรือ self-hosted Zep Open Source

### Zep Cloud setup

ถ้าใช้ [Zep Cloud](https://app.getzep.com){:target=_blank .external-link} ให้ทำตามนี้:

1. ใน Zep ให้เข้า [**Project Settings**](https://app.getzep.com/projects){:target=_blank .external-link}
2. ที่ **Project Keys** เลือก **Add Key**
3. ตั้งชื่อ key เช่น `n8n integration`
4. กด **Create**
5. คัดลอก key ไปใส่ใน n8n integration เป็น **API Key**
6. เปิด **Cloud** toggle

### Self-hosted Zep Open Source setup

ถ้าใช้ [Zep Open Source](https://docs.getzep.com/deployment/quickstart/){:target=_blank .external-link} แบบ self-host ให้ทำตามนี้:

1. ใส่ JWT token ของ Zep server เป็น **API Key** ใน n8n
    - ถ้ายังไม่เคยสร้าง JWT token ดูวิธีที่ [Configuring Authentication](https://docs.getzep.com/deployment/auth/){:target=_blank .external-link}
2. ปิด **Cloud** toggle
3. ใส่ URL ของ Zep server เป็น **API URL**
