---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการใช้งาน Google Gemini Chat Model node
description: วิธีใช้ Google Gemini Chat Model node ใน n8n เพื่อเชื่อมต่อโมเดลแชท Google Gemini
contentType: [integration, reference]
priority: high
---

# Google Gemini Chat Model node

ใช้ Google Gemini Chat Model node เพื่อใช้งานโมเดลแชทของ Google Gemini กับ conversational agents

ในหน้านี้จะมีพารามิเตอร์ของ node Google Gemini Chat Model และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/googleai.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกโมเดลที่ต้องการให้สร้างข้อความตอบกลับ

n8n จะโหลดโมเดลจาก Google Gemini API แบบ dynamic คุณจะเห็นเฉพาะโมเดลที่บัญชีของคุณเข้าถึงได้

## Node options

* **Maximum Number of Tokens**: กำหนดจำนวน tokens สูงสุดที่ใช้ ซึ่งจะเป็นการกำหนดความยาวของข้อความที่โมเดลจะตอบกลับ
* **Sampling Temperature**: ปรับความสุ่มของการสร้างข้อความ ค่า temperature สูงจะทำให้โมเดลตอบหลากหลายมากขึ้น แต่ก็เสี่ยงต่อการตอบแบบหลุดประเด็น
* **Top K**: กำหนดจำนวนตัวเลือก token ที่โมเดลจะใช้ในการสร้าง token ถัดไป
* **Top P**: กำหนดความน่าจะเป็นรวมที่โมเดลจะใช้ในการเลือก token ถัดไป ค่า Top P ต่ำจะตัดตัวเลือกที่มีความน่าจะเป็นน้อยออก
* **Safety Settings**: Gemini รองรับการตั้งค่าความปลอดภัย สามารถดูรายละเอียดได้ที่ [Gemini API safety settings](https://ai.google.dev/docs/safety_setting_gemini){:target=_blank .external-link}

## Templates and examples

[[ templatesWidget(page.title, 'google-gemini-chat-model') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's Google Gemini documentation](https://js.langchain.com/docs/integrations/chat/google_generativeai){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
