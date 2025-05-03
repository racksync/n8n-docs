---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการใช้งาน Cohere Model node
description: วิธีใช้ Cohere Model node ใน n8n เพื่อเชื่อมต่อโมเดล Cohere กับ workflow
contentType: [integration, reference]
---

# Cohere Model node

ใช้ Cohere Model node เพื่อใช้งานโมเดลของ Cohere

ในหน้านี้จะมีพารามิเตอร์ของ node Cohere Model และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/cohere.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node Options

* **Maximum Number of Tokens**: กำหนดจำนวน tokens สูงสุดที่ใช้ ซึ่งจะเป็นการกำหนดความยาวของข้อความที่โมเดลจะตอบกลับ
* **Sampling Temperature**: ปรับความสุ่มของการสร้างข้อความ ค่า temperature สูงจะทำให้โมเดลตอบหลากหลายมากขึ้น แต่ก็เสี่ยงต่อการตอบแบบหลุดประเด็น

## Templates and examples

[[ templatesWidget(page.title, 'cohere-model') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChains's Cohere documentation](https://js.langchain.com/docs/integrations/llms/cohere/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
