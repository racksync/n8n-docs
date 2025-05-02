---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Embeddings Google PaLM node documentation
description: Learn how to use the Embeddings Google PaLM node in n8n. Follow technical documentation to integrate Embeddings Google PaLM node into your workflows.
contentType: [integration, reference]
---

# Embeddings Google PaLM node

ใช้ Embeddings Google PaLM node เพื่อสร้าง [embeddings](/glossary.md#ai-embedding) สำหรับข้อความที่กำหนด

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนดสำหรับ Embeddings Google PaLM node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับโหนดนี้ได้ [ที่นี่](/integrations/builtin/credentials/googleai.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกรุ่น (model) ที่จะใช้สร้าง embedding

n8n โหลดโมเดลจาก Google PaLM API แบบไดนามิก และคุณจะเห็นเฉพาะโมเดลที่พร้อมใช้งานสำหรับบัญชีของคุณเท่านั้น

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'embeddings-google-palm') ]]

## Related resources

อ้างอิง [เอกสารประกอบ Google PaLM embeddings ของ Langchain](https://js.langchain.com/v0.2/docs/integrations/text_embedding/google_palm/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
