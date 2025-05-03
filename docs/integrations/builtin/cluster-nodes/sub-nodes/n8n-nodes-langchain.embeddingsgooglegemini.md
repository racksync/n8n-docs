---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Embeddings Google Gemini node
description: วิธีใช้ Embeddings Google Gemini node ใน n8n สำหรับสร้าง embedding ข้อความ
contentType: [integration, reference]
priority: medium
---

# Embeddings Google Gemini node

ใช้ Embeddings Google Gemini node เพื่อสร้าง [embeddings](/glossary.md#ai-embedding) สำหรับข้อความที่กำหนด

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนดสำหรับ Embeddings Google Gemini node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับโหนดนี้ได้ [ที่นี่](/integrations/builtin/credentials/googleai.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกรุ่น (model) ที่จะใช้สร้าง embedding

เรียนรู้เพิ่มเติมเกี่ยวกับรุ่นที่มีให้ใช้งานใน [เอกสารประกอบ models ของ Google Gemini](https://ai.google.dev/models/gemini){:target=_blank .external-link}

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'embeddings-google-gemini') ]]

## Related resources

อ้างอิง [เอกสารประกอบ Google Generative AI embeddings ของ Langchain](https://js.langchain.com/docs/integrations/text_embedding/google_generativeai){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
