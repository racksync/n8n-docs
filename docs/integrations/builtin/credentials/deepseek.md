---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลรับรอง DeepSeek
description: เอกสารข้อมูลรับรอง DeepSeek ใช้ข้อมูลนี้เพื่อยืนยันตัวตน Deepseek ใน n8n
contentType: [integration, reference]
priority: critical
---

# DeepSeek credentials

คุณสามารถใช้ credentials นี้เพื่อเชื่อมต่อกับ node เหล่านี้:

- [Chat DeepSeek](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek.md)

## Prerequisites

สมัคร [DeepSeek](https://platform.deepseek.com/sign_up) ให้เรียบร้อยก่อน

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับการใช้งาน API ได้ที่ [DeepSeek's API documentation](https://api-docs.deepseek.com/api/deepseek-api)

## Using API key

ถ้าจะตั้งค่า credentials นี้ คุณต้องมี:

- **API Key**

วิธีสร้าง API Key ของคุณ:

1. ล็อกอินเข้าบัญชี DeepSeek ของคุณ หรือ [สร้าง](https://platform.deepseek.com/sign_up) บัญชี
2. เปิดหน้า [API keys](https://platform.deepseek.com/api_keys) ของคุณ
3. เลือก **Create new secret key** เพื่อสร้าง API key โดยสามารถตั้งชื่อ key ได้ (ไม่บังคับ)
4. คัดลอก key ของคุณและเพิ่มเป็น **API Key** ใน n8n

ดูข้อมูลเพิ่มเติมได้ที่หน้า [Your First API Call](https://api-docs.deepseek.com/)
