---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Embeddings Ollama node documentation
description: Learn how to use the Embeddings Ollama node in n8n. Follow technical documentation to integrate Embeddings Ollama node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Embeddings Ollama node

ใช้ Embeddings Ollama node เพื่อสร้าง [embeddings](/glossary.md#ai-embedding) สำหรับข้อความที่กำหนด

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนดสำหรับ Embeddings Ollama node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับโหนดนี้ได้ [ที่นี่](/integrations/builtin/credentials/ollama.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกรุ่น (model) ที่จะใช้สร้าง embedding เลือกจาก:
    * [all-minilm](https://ollama.com/library/all-minilm) (384 Dimensions)
    * [nomic-embed-text](https://ollama.com/library/nomic-embed-text) (768 Dimensions)

เรียนรู้เพิ่มเติมเกี่ยวกับรุ่นที่มีให้ใช้งานใน [เอกสารประกอบ models ของ Ollama](https://ollama.ai/library){:target=_blank .external-link}

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'embeddings-ollama') ]]

## Related resources

อ้างอิง [เอกสารประกอบ Ollama embeddings ของ Langchain](https://js.langchain.com/docs/integrations/text_embedding/ollama/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
