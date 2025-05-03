---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Embeddings Cohere node
description: วิธีใช้ Embeddings Cohere node ใน n8n สำหรับสร้าง embedding ข้อความ
contentType: [integration, reference]
---

# Embeddings Cohere node

ใช้ Embeddings Cohere node เพื่อสร้าง [embeddings](/glossary.md#ai-embedding) สำหรับข้อความที่กำหนด

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนดสำหรับ Embeddings Cohere node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับโหนดนี้ได้ [ที่นี่](/integrations/builtin/credentials/cohere.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกรุ่น (model) ที่จะใช้สร้าง embedding เลือกจาก:
    * **Embed-English-v2.0(4096 Dimensions)**
	* **Embed-English-Light-v2.0(1024 Dimensions)**
	* **Embed-Multilingual-v2.0(768 Dimensions)**

เรียนรู้เพิ่มเติมเกี่ยวกับรุ่นที่มีให้ใช้งานใน [เอกสารประกอบ models ของ Cohere](https://docs.cohere.com/docs/models){:target=_blank .external-link}

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'embeddings-cohere') ]]

## Related resources

อ้างอิง [เอกสารประกอบ Cohere embeddings ของ Langchain](https://js.langchain.com/docs/integrations/text_embedding/cohere/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
