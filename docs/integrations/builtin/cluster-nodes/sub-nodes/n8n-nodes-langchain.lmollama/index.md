---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Ollama Model node documentation
description: Learn how to use the Ollama Model node in n8n. Follow technical documentation to integrate Ollama Model node into your workflows.
contentType: [integration, reference]
priority: high
---

# Ollama Model node

Ollama Model node ช่วยให้คุณสามารถใช้โมเดล Llama 2 แบบ local ได้

ในหน้านี้ คุณจะพบพารามิเตอร์ของ node สำหรับ Ollama Model node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/ollama.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกโมเดลที่จะใช้สร้าง completion เลือกจาก:
	* **Llama2**
	* **Llama2 13B**
	* **Llama2 70B**
	* **Llama2 Uncensored**

อ้างอิงถึงเอกสาร [Models Library documentation](https://ollama.com/library){:target=_blank .external-link} ของ Ollama สำหรับข้อมูลเพิ่มเติมเกี่ยวกับโมเดลที่มีให้ใช้งาน

## Node options

* **Sampling Temperature**: ใช้ตัวเลือกนี้เพื่อควบคุมความสุ่มของกระบวนการ sampling ค่า temperature ที่สูงขึ้นจะสร้างการ sampling ที่หลากหลายมากขึ้น แต่เพิ่มความเสี่ยงของ hallucination
* **Top K**: ป้อนจำนวน token ที่โมเดลจะใช้ในการสร้าง token ถัดไป
* **Top P**: ใช้ตัวเลือกนี้เพื่อกำหนดค่าความน่าจะเป็นที่ completion ควรใช้ ใช้ค่าที่ต่ำลงเพื่อละเว้นตัวเลือกที่มีความน่าจะเป็นน้อย

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'ollama-model') ]]

## Related resources

อ้างอิงถึง [LangChains's Ollama documentation](https://js.langchain.com/docs/integrations/llms/ollama/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Common issues

สำหรับคำถามหรือปัญหาที่พบบ่อยและแนวทางแก้ไขที่แนะนำ โปรดดูที่ [Common issues](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/common-issues.md)

--8<-- "_glossary/ai-glossary.md"

--8<-- "_snippets/self-hosting/starter-kits/self-hosted-ai-starter-kit.md"
