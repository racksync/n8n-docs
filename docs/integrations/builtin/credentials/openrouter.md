---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน OpenRouter
description: เอกสารสำหรับข้อมูลยืนยันตัวตน OpenRouter ใช้ข้อมูลนี้เพื่อยืนยันตัวตน OpenRouter ใน n8n แพลตฟอร์ม workflow automation
contentType: [integration, reference]
priority: critical
---

# OpenRouter credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [Chat OpenRouter](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenrouter.md)

## Prerequisites

สร้างบัญชี [OpenRouter](https://openrouter.ai/)

## Supported authentication methods

- API key

## Related resources

อ้างอิง [OpenRouter's API documentation](https://openrouter.ai/docs/quick-start) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**

วิธีสร้าง API Key ของคุณ:

1. เข้าสู่ระบบบัญชี OpenRouter ของคุณ หรือ [สร้าง](https://openrouter.ai/) บัญชี
2. เปิดหน้า [API keys](https://openrouter.ai/keys) ของคุณ
3. เลือก **Create new secret key** เพื่อสร้าง API key โดยสามารถตั้งชื่อ key ได้ (ไม่บังคับ)
4. คัดลอก key ของคุณและเพิ่มเป็น **API Key** ใน n8n

อ้างอิงหน้า [OpenRouter Quick Start](https://openrouter.ai/docs/quick-start) สำหรับข้อมูลเพิ่มเติม
