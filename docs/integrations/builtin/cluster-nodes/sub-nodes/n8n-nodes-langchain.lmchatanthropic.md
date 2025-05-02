---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Anthropic Chat Model node documentation
description: เรียนรู้วิธีการใช้งาน Anthropic Chat Model node ใน n8n พร้อมคำแนะนำทางเทคนิคเพื่อรวม Anthropic Chat Model node เข้ากับเวิร์กโฟลว์ของคุณ
contentType: [integration, reference]
priority: medium
---

# Anthropic Chat Model node

ใช้ Anthropic Chat Model node เพื่อใช้งานโมเดล Claude ของ Anthropic สำหรับงานแชทกับ [agents](/glossary.md#ai-agent) ได้เลย

ในหน้านี้จะมีพารามิเตอร์ของ node Anthropic Chat Model และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/anthropic.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกโมเดลที่ต้องการให้สร้างข้อความตอบกลับ เลือกได้จาก:
	* **Claude**
	* **Claude Instant**

ดูรายละเอียดเพิ่มเติมได้ที่ [Anthropic model documentation](https://docs.anthropic.com/claude/reference/selecting-a-model){:target=_blank .external-link}

## Node options

* **Maximum Number of Tokens**: กำหนดจำนวน tokens สูงสุดที่ใช้ ซึ่งจะเป็นการกำหนดความยาวของข้อความที่โมเดลจะตอบกลับ
* **Sampling Temperature**: ปรับความสุ่มของการสร้างข้อความ ค่า temperature สูงจะทำให้โมเดลตอบหลากหลายมากขึ้น แต่ก็เสี่ยงต่อการตอบแบบหลุดประเด็น
* **Top K**: กำหนดจำนวนตัวเลือก token ที่โมเดลจะใช้ในการสร้าง token ถัดไป
* **Top P**: กำหนดความน่าจะเป็นรวมที่โมเดลจะใช้ในการเลือก token ถัดไป ค่า Top P ต่ำจะตัดตัวเลือกที่มีความน่าจะเป็นน้อยออก

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'anthropic-chat-model') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChains's Anthropic documentation](https://js.langchain.com/docs/integrations/chat/anthropic/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

--8<-- "_glossary/ai-glossary.md"
