---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ PGVector Vector Store node
description: วิธีใช้งาน PGVector Vector Store node ใน n8n สำหรับจัดการ vector table บน Postgresql
priority: medium
---

# PGVector Vector Store node

PGVector เป็น extension ของ Postgresql ใช้ node นี้เพื่อโต้ตอบกับตาราง PGVector ใน Postgresql database ของคุณ คุณสามารถใส่ documents เข้าไปใน vector table, ดึง documents จาก vector table, เรียกดู documents เพื่อส่งต่อไปยัง retriever ที่เชื่อมต่อกับ [chain](/glossary.md#ai-chain) หรือเชื่อมต่อโดยตรงกับ [agent](/glossary.md#ai-agent) ในฐานะ [tool](/glossary.md#ai-tool)

ในหน้านี้ คุณจะพบ node parameters สำหรับ PGVector node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูล authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/postgres.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node usage patterns

คุณสามารถใช้ PGVector Vector Store node ในรูปแบบต่อไปนี้

### Use as a regular node to insert and retrieve documents

คุณสามารถใช้ PGVector Vector Store เป็น node ปกติเพื่อ insert หรือ get documents รูปแบบนี้จะวาง PGVector Vector Store ไว้ใน flow การเชื่อมต่อปกติโดยไม่ต้องใช้ agent

คุณสามารถดูตัวอย่างได้ใน scenario 1 ของ [template นี้](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/) (template ใช้ Supabase Vector Store แต่รูปแบบเหมือนกัน)

### Connect directly to an AI agent as a tool

คุณสามารถเชื่อมต่อ PGVector Vector Store node โดยตรงกับ tool connector ของ [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) เพื่อใช้ vector store เป็น resource เมื่อตอบคำถาม

ในกรณีนี้ การเชื่อมต่อจะเป็น: AI agent (tools connector) -> PGVector Vector Store node

### Use a retriever to fetch documents

คุณสามารถใช้ [Vector Store Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node ร่วมกับ PGVector Vector Store node เพื่อดึง documents จาก PGVector Vector Store node ซึ่งมักใช้กับ [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md) node เพื่อดึง documents จาก vector store ที่ตรงกับ input ของ chat ที่กำหนด

[ตัวอย่างของ flow การเชื่อมต่อ](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/) (ตัวอย่างที่ลิงก์ใช้ Pinecone แต่รูปแบบเหมือนกัน) จะเป็น: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> PGVector Vector Store

### Use the Vector Store Question Answer Tool to answer questions

อีกรูปแบบหนึ่งคือการใช้ [Vector Store Question Answer Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md) เพื่อสรุปผลลัพธ์และตอบคำถามจาก PGVector Vector Store node แทนที่จะเชื่อมต่อ PGVector Vector Store โดยตรงในฐานะ tool รูปแบบนี้จะใช้ tool ที่ออกแบบมาโดยเฉพาะเพื่อสรุปข้อมูลใน vector store

[flow การเชื่อมต่อ](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/) (ตัวอย่างที่ลิงก์ใช้ Simple Vector Store แต่รูปแบบเหมือนกัน) ในกรณีนี้จะมีลักษณะดังนี้: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Simple Vector store

## Node parameters

--8<-- "_snippets/integrations/builtin/cluster-nodes/vector-store-mode.md"

<!-- vale off -->
### Get Many parameters
<!-- vale on -->

*   **Table name**: ป้อนชื่อตารางที่คุณต้องการ query
*   **Prompt**: ป้อนคำค้นหา (search query) ของคุณ
*   **Limit**: ป้อนตัวเลขเพื่อกำหนดจำนวนผลลัพธ์ที่จะดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

### Insert Documents parameters

*   **Table name**: ป้อนชื่อตารางที่คุณต้องการ query

### Retrieve Documents parameters (As Vector Store for Chain/Tool)

*   **Table name**: ป้อนชื่อตารางที่คุณต้องการ query

### Retrieve Documents (As Tool for AI Agent) parameters

*   **Name**: ชื่อของ vector store
*   **Description**: อธิบายให้ LLM ทราบว่า tool นี้ทำอะไร คำอธิบายที่ดีและเฉพาะเจาะจงช่วยให้ LLM สร้างผลลัพธ์ที่คาดหวังได้บ่อยขึ้น
*   **Table Name**: ป้อนตาราง PGVector ที่จะใช้
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

## Node options

### Collection

วิธีแยก datasets ใน PGVector สิ่งนี้จะสร้างตารางและคอลัมน์แยกต่างหากเพื่อติดตามว่า vector ใดอยู่ใน collection ใด

*   **Use Collection**: เลือกว่าจะใช้ collection (เปิด) หรือไม่ (ปิด)
*   **Collection Name**: ป้อนชื่อ collection ที่คุณต้องการใช้
*   **Collection Table Name**: ป้อนชื่อตารางที่จะจัดเก็บข้อมูล collection

### Column Names

ตัวเลือกต่อไปนี้ระบุชื่อคอลัมน์ที่จะจัดเก็บ vectors และข้อมูลที่เกี่ยวข้อง:

*   **ID Column Name**
*   **Vector Column Name**
*   **Content Column Name**
*   **Metadata Column Name**

### Metadata Filter

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/vector-store-metadata-filter.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'postgres-pgvector-store') ]]

## Related resources

อ้างอิง [เอกสาร PGVector ของ LangChain](https://js.langchain.com/docs/integrations/vectorstores/pgvector){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

--8<-- "_snippets/self-hosting/starter-kits/self-hosted-ai-starter-kit.md"
