---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Embeddings Mistral Cloud node
description: วิธีใช้ Embeddings Mistral Cloud node ใน n8n สำหรับสร้าง embedding ข้อความ
contentType: [integration, reference]
---

# Embeddings Mistral Cloud node

ใช้ Embeddings Mistral Cloud node เพื่อสร้าง [embeddings](/glossary.md#ai-embedding) สำหรับข้อความที่กำหนด

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนดสำหรับ Embeddings Mistral Cloud node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับโหนดนี้ได้ [ที่นี่](/integrations/builtin/credentials/mistral.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกรุ่น (model) ที่จะใช้สร้าง embedding

เรียนรู้เพิ่มเติมเกี่ยวกับรุ่นที่มีให้ใช้งานใน [เอกสารประกอบ models ของ Mistral](https://docs.mistral.ai/platform/pricing/){:target=_blank .external-link}

## Node options

* **Batch Size**: ป้อนจำนวนเอกสารสูงสุดที่จะส่งในแต่ละคำขอ
* **Strip New Lines**: เลือกว่าจะลบอักขระขึ้นบรรทัดใหม่ (new line characters) ออกจากข้อความอินพุต (เปิด) หรือไม่ (ปิด) n8n เปิดใช้งานตัวเลือกนี้เป็นค่าเริ่มต้น

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'embeddings-mistral-cloud') ]]

## Related resources

อ้างอิง [เอกสารประกอบ Mistral embeddings ของ Langchain](https://js.langchain.com/docs/integrations/text_embedding/mistralai){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
