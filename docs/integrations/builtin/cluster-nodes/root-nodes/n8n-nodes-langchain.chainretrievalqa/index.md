---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Question and Answer Chain node
description: วิธีใช้งาน Question and Answer Chain node ใน n8n สำหรับถาม-ตอบข้อมูลจาก vector store
contentType: [integration, reference]
priority: high
---

# Question and Answer Chain node

ใช้ Question and Answer Chain node เพื่อใช้ [vector store](/glossary.md#ai-vector-store) เป็น retriever

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนดสำหรับ Question and Answer Chain node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

## Node parameters

### Query

คำถามที่คุณต้องการถาม

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'retrieval-qanda-chain') ]]

## Related resources

อ้างอิง [เอกสารของ LangChain เกี่ยวกับ retrieval chains](https://js.langchain.com/docs/tutorials/rag/){:target=_blank .external-link} สำหรับตัวอย่างวิธีการที่ LangChain สามารถใช้ vector store เป็น retriever

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Common issues

สำหรับข้อผิดพลาดหรือปัญหาทั่วไปและขั้นตอนการแก้ไขที่แนะนำ โปรดดูที่ [Common Issues](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues.md)

--8<-- "_glossary/ai-glossary.md"
