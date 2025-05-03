---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ OpenAI Chat Model node
description: วิธีใช้ OpenAI Chat Model node ใน n8n พร้อมขั้นตอนการตั้งค่าและเชื่อมต่อ workflow
contentType: [integration, reference]
priority: high
---

# OpenAI Chat Model node

ใช้ OpenAI Chat Model node เพื่อใช้งาน Chat Model ของ OpenAI ร่วมกับ [agents](/glossary.md#ai-agent) ที่ใช้ในการสนทนา

ในหน้านี้ คุณจะพบกับพารามิเตอร์ของ OpenAI Chat Model node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/openai.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

### Model

เลือก Model ที่จะใช้ในการสร้างข้อความ completion

n8n จะโหลด Model จาก OpenAI แบบไดนามิก และคุณจะเห็นเฉพาะ Model ที่มีให้สำหรับบัญชีของคุณเท่านั้น

## Node options

ใช้ตัวเลือกเหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม

### Base URL

ป้อน URL ที่นี่เพื่อแทนที่ URL เริ่มต้นสำหรับ API

### Frequency Penalty

ใช้ตัวเลือกนี้เพื่อควบคุมโอกาสที่ Model จะสร้างข้อความซ้ำ ค่าที่สูงขึ้นจะลดโอกาสที่ Model จะสร้างข้อความซ้ำ

### Maximum Number of Tokens

ป้อนจำนวน Token สูงสุดที่จะใช้ ซึ่งจะเป็นการกำหนดความยาวของข้อความ completion

### Response Format

เลือก **Text** หรือ **JSON** การเลือก **JSON** จะทำให้มั่นใจได้ว่า Model จะส่งคืนค่าเป็น JSON ที่ถูกต้อง

### Presence Penalty

ใช้ตัวเลือกนี้เพื่อควบคุมโอกาสที่ Model จะพูดคุยเกี่ยวกับหัวข้อใหม่ๆ ค่าที่สูงขึ้นจะเพิ่มโอกาสที่ Model จะพูดคุยเกี่ยวกับหัวข้อใหม่ๆ

### Sampling Temperature

ใช้ตัวเลือกนี้เพื่อควบคุมความสุ่มของการสุ่มตัวอย่าง (sampling process) ค่า temperature ที่สูงขึ้นจะสร้างการสุ่มตัวอย่างที่หลากหลายมากขึ้น แต่ก็เพิ่มความเสี่ยงที่จะเกิดภาพหลอน (hallucinations)

### Timeout

ป้อนเวลาร้องขอสูงสุดในหน่วยมิลลิวินาที

### Max Retries

ป้อนจำนวนครั้งสูงสุดที่จะลองส่งคำขอใหม่

### Top P

ใช้ตัวเลือกนี้เพื่อกำหนดความน่าจะเป็นที่ completion ควรใช้ ใช้ค่าที่ต่ำลงเพื่อละเว้นตัวเลือกที่มีความน่าจะเป็นน้อยกว่า

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'openai-chat-model') ]]

## Related resources

อ้างอิง [เอกสาร OpenAI ของ LangChain](https://js.langchain.com/docs/integrations/chat/openai/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Common issues

สำหรับคำถามหรือปัญหาที่พบบ่อยและแนวทางแก้ไข โปรดดูที่ [Common issues](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues.md)

--8<-- "_glossary/ai-glossary.md"
