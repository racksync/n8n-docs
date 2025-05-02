---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Azure OpenAI Chat Model node documentation
description: Learn how to use the Azure OpenAI Chat Model node in n8n. Follow technical documentation to integrate Azure OpenAI Chat Model node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Azure OpenAI Chat Model node

ใช้ Azure OpenAI Chat Model node เพื่อใช้งานโมเดลแชทของ OpenAI ผ่าน Azure สำหรับงานกับ [agents](/glossary.md#ai-agent)

ในหน้านี้จะมีพารามิเตอร์ของ node Azure OpenAI Chat Model และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/azureopenai.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกโมเดลที่ต้องการให้สร้างข้อความตอบกลับ

## Node options

* **Frequency Penalty**: ปรับโอกาสที่โมเดลจะตอบซ้ำๆ ค่าเยอะจะลดการตอบซ้ำ
* **Maximum Number of Tokens**: กำหนดจำนวน tokens สูงสุดที่ใช้ ซึ่งจะเป็นการกำหนดความยาวของข้อความที่โมเดลจะตอบกลับ
* **Response Format**: เลือก **Text** หรือ **JSON** ถ้าเลือก JSON โมเดลจะตอบกลับเป็น JSON ที่ถูกต้องเสมอ
* **Presence Penalty**: ปรับโอกาสที่โมเดลจะพูดถึงหัวข้อใหม่ๆ ค่าเยอะจะเพิ่มโอกาสพูดเรื่องใหม่
* **Sampling Temperature**: ปรับความสุ่มของการสร้างข้อความ ค่า temperature สูงจะทำให้โมเดลตอบหลากหลายมากขึ้น แต่ก็เสี่ยงต่อการตอบแบบหลุดประเด็น
* **Timeout**: กำหนดเวลาสูงสุด (ms) ที่จะรอผลลัพธ์
* **Max Retries**: กำหนดจำนวนครั้งสูงสุดที่ระบบจะลองส่ง request ใหม่
* **Top P**: กำหนดความน่าจะเป็นรวมที่โมเดลจะใช้ในการเลือก token ถัดไป ค่า Top P ต่ำจะตัดตัวเลือกที่มีความน่าจะเป็นน้อยออก

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'azure-openai-chat-model') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChains's Azure OpenAI documentation](https://js.langchain.com/docs/integrations/chat/azure){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
