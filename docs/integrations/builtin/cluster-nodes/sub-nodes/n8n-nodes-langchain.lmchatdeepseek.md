---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการใช้งาน DeepSeek Chat Model node
description: วิธีใช้ DeepSeek Chat Model node ใน n8n เพื่อเชื่อมต่อโมเดลแชท DeepSeek กับ workflow
contentType: [integration, reference]
priority: high
---

# DeepSeek Chat Model node

ใช้ DeepSeek Chat Model node เพื่อใช้งานโมเดลแชทของ DeepSeek กับ conversational [agents](/glossary.md#ai-agent)

ในหน้านี้จะมีพารามิเตอร์ของ node DeepSeek Chat Model และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/deepseek.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

### Model

เลือกโมเดลที่ต้องการให้สร้างข้อความตอบกลับ

n8n จะโหลดโมเดลจาก DeepSeek แบบ dynamic คุณจะเห็นเฉพาะโมเดลที่บัญชีของคุณเข้าถึงได้

## Node options

ตัวเลือกเหล่านี้จะช่วยให้คุณปรับแต่งการทำงานของ node ได้มากขึ้น

### Base URL

ใส่ URL เพื่อ override ค่า default ของ API

### Frequency Penalty

ปรับโอกาสที่โมเดลจะตอบซ้ำๆ ค่าเยอะจะลดการตอบซ้ำ

### Maximum Number of Tokens

กำหนดจำนวน tokens สูงสุดที่ใช้ ซึ่งจะเป็นการกำหนดความยาวของข้อความที่โมเดลจะตอบกลับ

### Response Format

เลือก **Text** หรือ **JSON** ถ้าเลือก JSON โมเดลจะตอบกลับเป็น JSON ที่ถูกต้องเสมอ

### Presence Penalty

ปรับโอกาสที่โมเดลจะพูดถึงหัวข้อใหม่ๆ ค่าเยอะจะเพิ่มโอกาสพูดเรื่องใหม่

### Sampling Temperature

ปรับความสุ่มของการสร้างข้อความ ค่า temperature สูงจะทำให้โมเดลตอบหลากหลายมากขึ้น แต่ก็เสี่ยงต่อการตอบแบบหลุดประเด็น

### Timeout

กำหนดเวลาสูงสุด (ms) ที่จะรอผลลัพธ์

### Max Retries

กำหนดจำนวนครั้งสูงสุดที่ระบบจะลองส่ง request ใหม่

### Top P

กำหนดความน่าจะเป็นรวมที่โมเดลจะใช้ในการเลือก token ถัดไป ค่า Top P ต่ำจะตัดตัวเลือกที่มีความน่าจะเป็นน้อยออก

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'deepseek-chat-model') ]]

## Related resources

DeepSeek ใช้ API แบบเดียวกับ OpenAI สามารถดูข้อมูลเพิ่มเติมได้ที่ [LangChains's OpenAI documentation](https://js.langchain.com/docs/integrations/chat/openai/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

--8<-- "_glossary/ai-glossary.md"
