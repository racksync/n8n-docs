---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Embeddings HuggingFace Inference node
description: วิธีใช้ Embeddings HuggingFace Inference node ใน n8n สำหรับสร้าง embedding ข้อความ
contentType: [integration, reference]
priority: medium
---

# Embeddings HuggingFace Inference node

ใช้ Embeddings HuggingFace Inference node เพื่อสร้าง [embeddings](/glossary.md#ai-embedding) สำหรับข้อความที่กำหนด

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนดสำหรับ Embeddings HuggingFace Inference และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับโหนดนี้ได้ [ที่นี่](/integrations/builtin/credentials/huggingface.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกรุ่น (model) ที่จะใช้สร้าง embedding

อ้างอิง [เอกสารประกอบ Hugging Face models](https://huggingface.co/models?other=embeddings){:target=_blank .external-link} สำหรับรุ่นที่มีให้ใช้งาน

## Node options

* **Custom Inference Endpoint**: ป้อน URL ของโมเดลที่คุณ deploy ซึ่งโฮสต์โดย HuggingFace หากคุณตั้งค่านี้ n8n จะไม่สนใจ **Model Name**

อ้างอิง [คู่มือ inference ของ HuggingFace](https://huggingface.co/inference-endpoints){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'embeddings-hugging-face-inference') ]]

## Related resources

อ้างอิง [เอกสารประกอบ HuggingFace Inference embeddings ของ Langchain](https://js.langchain.com/docs/integrations/text_embedding/hugging_face_inference/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
