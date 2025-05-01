---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: OpenAI credentials
description: Documentation for OpenAI credentials. Use these credentials to authenticate OpenAI in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: critical
---

# OpenAI credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [OpenAI](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md)
- [Chat OpenAI](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/index.md)
- [Embeddings OpenAI](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md)
- [LM OpenAI](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/index.md)

## Prerequisites

สร้างบัญชี [OpenAI](https://platform.openai.com/signup/){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

อ้างอิง [OpenAI's API documentation](https://platform.openai.com/docs/introduction){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**
- **Organization ID**: จำเป็นหากคุณอยู่ในหลายองค์กร มิฉะนั้น ให้เว้นว่างไว้

วิธีสร้าง API Key ของคุณ:

1. เข้าสู่ระบบบัญชี OpenAI ของคุณ หรือ [สร้าง](https://platform.openai.com/signup/){:target=_blank .external-link} บัญชี
2. เปิดหน้า [API keys](https://platform.openai.com/api-keys){:target=_blank .external-link} ของคุณ
3. เลือก **Create new secret key** เพื่อสร้าง API key โดยสามารถตั้งชื่อ key ได้ (ไม่บังคับ)
4. คัดลอก key ของคุณและเพิ่มเป็น **API Key** ใน n8n

อ้างอิงเอกสาร [API Quickstart Account Setup documentation](https://platform.openai.com/docs/quickstart/account-setup){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

วิธีค้นหา Organization ID ของคุณ:

1. ไปที่หน้า [Organization Settings](https://platform.openai.com/account/organization){:target=_blank .external-link} ของคุณ
2. คัดลอก Organization ID ของคุณและเพิ่มเป็น **Organization ID** ใน n8n

อ้างอิง [Setting up your organization](https://platform.openai.com/docs/guides/production-best-practices/setting-up-your-organization){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม โปรดทราบว่าคำขอ API ที่ทำโดยใช้ Organization ID จะนับรวมอยู่ในโควต้าการสมัครสมาชิกขององค์กร

