---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการใช้งาน Mistral Cloud Chat Model node
description: วิธีใช้ Mistral Cloud Chat Model node ใน n8n เพื่อเชื่อมต่อโมเดลแชท Mistral Cloud
contentType: [integration, reference]
priority: medium
---

# Mistral Cloud Chat Model node

ใช้ Mistral Cloud Chat Model node เพื่อใช้งานโมเดลแชทของ Mistral Cloud กับ conversational [agents](/glossary.md#ai-agent)

ในหน้านี้จะมีพารามิเตอร์ของ node Mistral Cloud Chat Model และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/mistral.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกโมเดลที่ต้องการให้สร้างข้อความตอบกลับ n8n จะโหลดโมเดลจาก Mistral Cloud แบบ dynamic คุณจะเห็นเฉพาะโมเดลที่บัญชีของคุณเข้าถึงได้

## Node options

* **Maximum Number of Tokens**: กำหนดจำนวน tokens สูงสุดที่ใช้ ซึ่งจะเป็นการกำหนดความยาวของข้อความที่โมเดลจะตอบกลับ
* **Sampling Temperature**: ปรับความสุ่มของการสร้างข้อความ ค่า temperature สูงจะทำให้โมเดลตอบหลากหลายมากขึ้น แต่ก็เสี่ยงต่อการตอบแบบหลุดประเด็น
* **Timeout**: กำหนดเวลาสูงสุด (ms) ที่จะรอผลลัพธ์
* **Max Retries**: กำหนดจำนวนครั้งสูงสุดที่ระบบจะลองส่ง request ใหม่
* **Top P**: กำหนดความน่าจะเป็นรวมที่โมเดลจะใช้ในการเลือก token ถัดไป ค่า Top P ต่ำจะตัดตัวเลือกที่มีความน่าจะเป็นน้อยออก
* **Enable Safe Mode**: เปิด Safe Mode เพื่อเพิ่มข้อความความปลอดภัยในตอนต้นของการตอบกลับ ช่วยลดโอกาสที่โมเดลจะตอบเนื้อหาที่ไม่เหมาะสม
* **Random Seed**: กำหนด seed สำหรับการสุ่ม ถ้าตั้งค่าไว้ การเรียกแต่ละครั้งจะได้ผลลัพธ์ที่เหมือนกัน

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'mistral-cloud-chat-model') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChains's Mistral documentation](https://js.langchain.com/docs/integrations/chat/mistral){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
