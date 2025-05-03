---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการใช้งาน Groq Chat Model node
description: วิธีใช้ Groq Chat Model node ใน n8n เพื่อเชื่อมต่อโมเดลภาษา Groq กับ workflow
contentType: [integration, reference]
priority: medium
---

# Groq Chat Model node

ใช้ Groq Chat Model node เพื่อเข้าถึงโมเดลภาษา (LLM) ของ Groq สำหรับงาน AI แชทและการสร้างข้อความ

ในหน้านี้จะมีพารามิเตอร์ของ node Groq Chat Model และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials 
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/groq.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกโมเดลที่ต้องการให้สร้างข้อความตอบกลับ n8n จะโหลดโมเดลที่มีอยู่จาก Groq API อัตโนมัติ ดูรายละเอียดเพิ่มเติมได้ที่ [Groq model documentation](https://console.groq.com/docs/models){:target=_blank .external-link}

## Node options

* **Maximum Number of Tokens**: กำหนดจำนวน tokens สูงสุดที่ใช้ ซึ่งจะเป็นการกำหนดความยาวของข้อความที่โมเดลจะตอบกลับ
* **Sampling Temperature**: ปรับความสุ่มของการสร้างข้อความ ค่า temperature สูงจะทำให้โมเดลตอบหลากหลายมากขึ้น แต่ก็เสี่ยงต่อการตอบแบบหลุดประเด็น

## Templates and examples

[[ templatesWidget(page.title, 'groq-chat-model') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [Groq's API documentation](https://console.groq.com/docs/quickstart){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
