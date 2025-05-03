---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Embeddings AWS Bedrock node
description: วิธีใช้ Embeddings AWS Bedrock node ใน n8n สำหรับสร้าง embedding ข้อความ
contentType: [integration, reference]
---

# Embeddings AWS Bedrock node

ใช้ Embeddings AWS Bedrock node เพื่อสร้าง [embeddings](/glossary.md#ai-embedding) สำหรับข้อความที่กำหนด

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนดสำหรับ Embeddings AWS Bedrock node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับโหนดนี้ได้ [ที่นี่](/integrations/builtin/credentials/aws.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Model**: เลือกรุ่น (model) ที่จะใช้สร้าง embedding

เรียนรู้เพิ่มเติมเกี่ยวกับรุ่นที่มีให้ใช้งานใน [เอกสารประกอบ Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html){:target=_blank .external-link}

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'embeddings-aws-bedrock') ]]

## Related resources

อ้างอิง [เอกสารประกอบ AWS Bedrock embeddings ของ LangChain](https://js.langchain.com/docs/integrations/platforms/aws/#text-embedding-models){:target=_blank .external-link} และ [เอกสารประกอบ AWS Bedrock](https://docs.aws.amazon.com/bedrock/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ AWS Bedrock

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
