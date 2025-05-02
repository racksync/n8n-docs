---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Ollama Chat Model node documentation
description: Learn how to use the Ollama Chat Model node in n8n. Follow technical documentation to integrate Ollama Chat Model node into your workflows.
contentType: [integration, reference]
priority: high
---

# Ollama Chat Model node

Ollama Chat Model node ช่วยให้คุณใช้โมเดล Llama 2 บนเครื่อง local กับ [agents](/glossary.md#ai-agent) แบบสนทนาได้

ในหน้านี้ คุณจะพบ node parameters สำหรับ Ollama Chat Model node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูล authentication สำหรับโหนดนี้ได้ [ที่นี่](/integrations/builtin/credentials/ollama.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

*   **Model**: เลือกโมเดลที่จะใช้สร้าง completion เลือกจาก:
    *   **Llama2**
    *   **Llama2 13B**
    *   **Llama2 70B**
    *   **Llama2 Uncensored**

อ้างอิง [Models Library documentation](https://ollama.com/library){:target=_blank .external-link} ของ Ollama สำหรับข้อมูลเพิ่มเติมเกี่ยวกับโมเดลที่มีให้ใช้งาน

## Node options

*   **Sampling Temperature**: ใช้ตัวเลือกนี้เพื่อควบคุมความสุ่มของการสุ่มตัวอย่าง (sampling process) ค่า temperature ที่สูงขึ้นจะสร้างการสุ่มตัวอย่างที่หลากหลายมากขึ้น แต่เพิ่มความเสี่ยงที่จะเกิดภาพหลอน (hallucinations)
*   **Top K**: ป้อนจำนวนตัวเลือก token ที่โมเดลใช้ในการสร้าง token ถัดไป
*   **Top P**: ใช้ตัวเลือกนี้เพื่อกำหนดค่าความน่าจะเป็น (probability) ที่ completion ควรใช้ ใช้ค่าที่ต่ำลงเพื่อละเว้นตัวเลือกที่มีความน่าจะเป็นน้อยกว่า

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'ollama-chat-model') ]]

## Related resources

อ้างอิง [LangChain's Ollama Chat Model documentation](https://js.langchain.com/docs/integrations/chat/ollama/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Common issues

สำหรับคำถามหรือปัญหาที่พบบ่อยและแนวทางแก้ไข โปรดดูที่ [Common issues](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues.md)

--8<-- "_glossary/ai-glossary.md"

--8<-- "_snippets/self-hosting/starter-kits/self-hosted-ai-starter-kit.md"
