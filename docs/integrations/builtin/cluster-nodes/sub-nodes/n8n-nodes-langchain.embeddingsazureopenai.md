---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Embeddings Azure OpenAI node
description: วิธีใช้ Embeddings Azure OpenAI node ใน n8n สำหรับสร้าง embedding ข้อความ
contentType: [integration, reference]
---

# Embeddings Azure OpenAI node

ใช้ Embeddings Azure OpenAI node เพื่อสร้าง [embeddings](/glossary.md#ai-embedding) สำหรับข้อความที่กำหนด

ในหน้านี้ คุณจะพบพารามิเตอร์ของโหนดสำหรับ Embeddings Azure OpenAI node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการยืนยันตัวตนสำหรับโหนดนี้ได้ [ที่นี่](/integrations/builtin/credentials/azureopenai.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"


## Node options

* **Model (Deployment) Name**: เลือกรุ่น (deployment) ที่จะใช้สร้าง embeddings
* **Batch Size**: ป้อนจำนวนเอกสารสูงสุดที่จะส่งในแต่ละคำขอ
* **Strip New Lines**: เลือกว่าจะลบอักขระขึ้นบรรทัดใหม่ (new line characters) ออกจากข้อความอินพุต (เปิด) หรือไม่ (ปิด) n8n เปิดใช้งานตัวเลือกนี้เป็นค่าเริ่มต้น
* **Timeout**: ป้อนระยะเวลาสูงสุดที่คำขอสามารถใช้ได้เป็นวินาที ตั้งค่าเป็น `-1` หากไม่ต้องการกำหนดเวลาหมดอายุ (timeout)

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'embeddings-azure-openai') ]]

## Related resources

อ้างอิง [เอกสารประกอบ OpenAI embeddings ของ LangChain](https://js.langchain.com/docs/integrations/text_embedding/azure_openai/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
