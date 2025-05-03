---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Supabase Vector Store node
description: วิธีใช้งาน Supabase Vector Store node ใน n8n สำหรับเชื่อมต่อและจัดการ Supabase vector database
contentType: [integration, reference]
priority: medium
---

# Supabase Vector Store node

ใช้ Supabase Vector Store เพื่อโต้ตอบกับ Supabase database ของคุณในฐานะ [vector store](/glossary.md#ai-vector-store) คุณสามารถใส่ documents เข้าไปใน vector database, ดึง documents จาก vector database, เรียกดู documents เพื่อส่งต่อไปยัง retriever ที่เชื่อมต่อกับ [chain](/glossary.md#ai-chain) หรือเชื่อมต่อโดยตรงกับ [agent](/glossary.md#ai-agent) เพื่อใช้เป็น [tool](/glossary.md#ai-tool)

ในหน้านี้ คุณจะพบ node parameters สำหรับ Supabase node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูล authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/supabase.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

Supabase มี [quickstart สำหรับการตั้งค่า vector store ของคุณ](https://supabase.com/docs/guides/ai/langchain?database-method=sql){:target=_blank .external-link} หากคุณใช้การตั้งค่าอื่นนอกเหนือจากค่าเริ่มต้นใน quickstart อาจส่งผลต่อการตั้งค่า parameter ใน n8n โปรดตรวจสอบให้แน่ใจว่าคุณเข้าใจสิ่งที่คุณกำลังทำ

## Node usage patterns

คุณสามารถใช้ Supabase Vector Store node ในรูปแบบต่อไปนี้

### Use as a regular node to insert, update, and retrieve documents

คุณสามารถใช้ Supabase Vector Store เป็น node ปกติเพื่อ insert, update หรือ get documents รูปแบบนี้จะวาง Supabase Vector Store ไว้ใน flow การเชื่อมต่อปกติโดยไม่ต้องใช้ agent

คุณสามารถดูตัวอย่างได้ใน scenario 1 ของ [template นี้](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)

### Connect directly to an AI agent as a tool

คุณสามารถเชื่อมต่อ Supabase Vector Store node โดยตรงกับ tool connector ของ [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) เพื่อใช้ vector store เป็น resource เมื่อตอบคำถาม

ในกรณีนี้ การเชื่อมต่อจะเป็น: AI agent (tools connector) -> Supabase Vector Store node

### Use a retriever to fetch documents

คุณสามารถใช้ [Vector Store Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node ร่วมกับ Supabase Vector Store node เพื่อดึง documents จาก Supabase Vector Store node ซึ่งมักใช้กับ [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md) node เพื่อดึง documents จาก vector store ที่ตรงกับ input ของ chat ที่กำหนด

[ตัวอย่างของ flow การเชื่อมต่อ](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/) (ตัวอย่างใช้ Pinecone แต่รูปแบบเหมือนกัน) จะเป็น: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Supabase Vector Store

### Use the Vector Store Question Answer Tool to answer questions

อีกรูปแบบหนึ่งคือการใช้ [Vector Store Question Answer Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md) เพื่อสรุปผลลัพธ์และตอบคำถามจาก Supabase Vector Store node แทนที่จะเชื่อมต่อ Supabase Vector Store โดยตรงในฐานะ tool รูปแบบนี้จะใช้ tool ที่ออกแบบมาโดยเฉพาะเพื่อสรุปข้อมูลใน vector store

[flow การเชื่อมต่อ](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/) ในกรณีนี้จะมีลักษณะดังนี้: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Supabase Vector store

## Node parameters

--8<-- "_snippets/integrations/builtin/cluster-nodes/vector-store-mode-with-update.md"

<!-- vale from-write-good.Weasel = NO -->
### Get Many parameters
<!-- vale from-write-good.Weasel = YES -->

*   **Table Name**: ป้อนตาราง Supabase ที่จะใช้
*   **Prompt**: ป้อนคำค้นหา (search query)
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

### Insert Documents parameters

*   **Table Name**: ป้อนตาราง Supabase ที่จะใช้

### Retrieve Documents (As Vector Store for Chain/Tool) parameters

*   **Table Name**: ป้อนตาราง Supabase ที่จะใช้

### Retrieve Documents (As Tool for AI Agent) parameters

*   **Name**: ชื่อของ vector store
*   **Description**: อธิบายให้ LLM ทราบว่า tool นี้ทำอะไร คำอธิบายที่ดีและเฉพาะเจาะจงช่วยให้ LLM สร้างผลลัพธ์ที่คาดหวังได้บ่อยขึ้น
*   **Table Name**: ป้อนตาราง Supabase ที่จะใช้
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

### Update Documents

*   **Table Name**: ป้อนตาราง Supabase ที่จะใช้
*   **ID**: ID ของรายการ embedding

## Node options

### Query Name

ชื่อของ matching function ที่คุณตั้งค่าใน Supabase หากคุณทำตาม [Supabase quickstart](https://supabase.com/docs/guides/ai/langchain?database-method=sql){:target=_blank .external-link} ชื่อนี้จะเป็น `match_documents`

### Metadata Filter

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/vector-store-metadata-filter.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'supabase-vector-store') ]]

## Related resources

อ้างอิง [เอกสาร Supabase ของ LangChain](https://js.langchain.com/docs/integrations/vectorstores/supabase/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
