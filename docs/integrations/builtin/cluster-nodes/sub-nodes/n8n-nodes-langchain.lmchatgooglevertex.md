---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Google Vertex Chat Model node documentation
description: Learn how to use the Google Vertex Chat Model node in n8n. Follow technical documentation to integrate Google Vertex Chat Model node into your workflows.
contentType: [integration, reference]
---

# Google Vertex Chat Model node

ใช้ Google Vertex AI Chat Model node เพื่อใช้งานโมเดลแชทของ Google Vertex AI กับ conversational [agents](/glossary.md#ai-agent)

ในหน้านี้จะมีพารามิเตอร์ของ node Google Vertex AI Chat Model และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/google/service-account.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Project ID**: เลือก Project ID จาก Google Cloud ของคุณ n8n จะโหลดโปรเจกต์จากบัญชี Google Cloud ของคุณแบบอัตโนมัติ หรือจะกรอกเองก็ได้
* **Model Name**: เลือกชื่อโมเดลที่ต้องการให้สร้างข้อความตอบกลับ เช่น `gemini-1.5-flash-001`, `gemini-1.5-pro-001` เป็นต้น ดูรายชื่อโมเดลได้ที่ [Google models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models){:target=_blank .external-link}

## Node options

* **Maximum Number of Tokens**: กำหนดจำนวน tokens สูงสุดที่ใช้ ซึ่งจะเป็นการกำหนดความยาวของข้อความที่โมเดลจะตอบกลับ
* **Sampling Temperature**: ปรับความสุ่มของการสร้างข้อความ ค่า temperature สูงจะทำให้โมเดลตอบหลากหลายมากขึ้น แต่ก็เสี่ยงต่อการตอบแบบหลุดประเด็น
* **Top K**: กำหนดจำนวนตัวเลือก token ที่โมเดลจะใช้ในการสร้าง token ถัดไป
* **Top P**: กำหนดความน่าจะเป็นรวมที่โมเดลจะใช้ในการเลือก token ถัดไป ค่า Top P ต่ำจะตัดตัวเลือกที่มีความน่าจะเป็นน้อยออก
* **Safety Settings**: Gemini รองรับการตั้งค่าความปลอดภัย สามารถดูรายละเอียดได้ที่ [Gemini API safety settings](https://ai.google.dev/docs/safety_setting_gemini){:target=_blank .external-link}

## Templates and examples

[[ templatesWidget(page.title, 'google-vertex-chat-model') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's Google Vertex AI documentation](https://js.langchain.com/docs/integrations/chat/google_vertex_ai/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
