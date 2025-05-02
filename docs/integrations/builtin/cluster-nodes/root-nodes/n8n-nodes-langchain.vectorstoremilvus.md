---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Milvus Vector Store node documentation
description: Learn how to use the Milvus Vector Store node in n8n. Follow technical documentation to integrate Milvus Vector Store node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Milvus Vector Store node

ใช้ Milvus node เพื่อโต้ตอบกับ Milvus database ของคุณในฐานะ [vector store](/glossary.md#ai-vector-store) คุณสามารถใส่ documents เข้าไปใน vector database, ดึง documents จาก vector database, เรียกดู documents เพื่อส่งต่อไปยัง retriever ที่เชื่อมต่อกับ [chain](/glossary.md#ai-chain) หรือเชื่อมต่อโดยตรงกับ [agent](/glossary.md#ai-agent) ในฐานะ [tool](/glossary.md#ai-tool)

ในหน้านี้ คุณจะพบ node parameters สำหรับ Milvus node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูล authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/milvus.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node usage patterns

คุณสามารถใช้ Milvus Vector Store node ในรูปแบบต่อไปนี้

### Use as a regular node to insert and retrieve documents

คุณสามารถใช้ Milvus Vector Store เป็น node ปกติเพื่อ insert หรือ get documents รูปแบบนี้จะวาง Milvus Vector Store ไว้ใน flow การเชื่อมต่อปกติโดยไม่ต้องใช้ agent

คุณสามารถดูตัวอย่างได้ใน scenario 1 ของ [template นี้](https://n8n.io/workflows/2165-chat-with-pdf-docs-using-ai-quoting-sources/) โดยแทนที่ Pinecone Vector store node ด้วย Milvus Vector Store node

### Connect directly to an AI agent as a tool

คุณสามารถเชื่อมต่อ Milvus Vector Store node โดยตรงกับ tool connector ของ [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) เพื่อใช้ vector store เป็น resource เมื่อตอบคำถาม

ในกรณีนี้ การเชื่อมต่อจะเป็น: AI agent (tools connector) -> Milvus Vector Store node

### Use a retriever to fetch documents

คุณสามารถใช้ [Vector Store Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node ร่วมกับ Milvus Vector Store node เพื่อดึง documents จาก Milvus Vector Store node ซึ่งมักใช้กับ [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md) node เพื่อดึง documents จาก vector store ที่ตรงกับ input ของ chat ที่กำหนด

[ตัวอย่างของ flow การเชื่อมต่อ](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/) จะเป็น: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Milvus Vector Store ในตัวอย่างนี้ ควรแทนที่ Pinecone Vector Store node ด้วย Milvus Vector Store node

### Use the Vector Store Question Answer Tool to answer questions

อีกรูปแบบหนึ่งคือการใช้ [Vector Store Question Answer Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md) เพื่อสรุปผลลัพธ์และตอบคำถามจาก Milvus Vector Store node แทนที่จะเชื่อมต่อ Milvus Vector Store โดยตรงในฐานะ tool รูปแบบนี้จะใช้ tool ที่ออกแบบมาโดยเฉพาะเพื่อสรุปข้อมูลใน vector store

[flow การเชื่อมต่อ](https://n8n.io/workflows/2705-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-and-openai/) ในกรณีนี้จะมีลักษณะดังนี้: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Milvus Vector store ในตัวอย่างนี้ ควรแทนที่ Pinecone Vector Store node ด้วย Milvus Vector Store node

## Node parameters

--8<-- "_snippets/integrations/builtin/cluster-nodes/vector-store-mode.md"

<!-- vale from-write-good.Weasel = NO -->
### Get Many parameters
<!-- vale from-write-good.Weasel = YES -->

*   **Milvus Collection**: เลือกหรือป้อน Milvus Collection ที่จะใช้
*   **Prompt**: ป้อนคำค้นหา (search query) ของคุณ
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

### Insert Documents parameters

*   **Milvus Collection**: เลือกหรือป้อน Milvus Collection ที่จะใช้
*   **Clear Collection**: ระบุว่าจะล้าง collection ก่อนที่จะใส่ documents ใหม่หรือไม่

### Retrieve Documents (As Vector Store for Chain/Tool) parameters

*   **Milvus collection**: เลือกหรือป้อน Milvus Collection ที่จะใช้

### Retrieve Documents (As Tool for AI Agent) parameters

*   **Name**: ชื่อของ vector store
*   **Description**: อธิบายให้ LLM ทราบว่า tool นี้ทำอะไร คำอธิบายที่ดีและเฉพาะเจาะจงช่วยให้ LLM สร้างผลลัพธ์ที่คาดหวังได้บ่อยขึ้น
*   **Milvus Collection**: เลือกหรือป้อน Milvus Collection ที่จะใช้
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

## Node options

### Metadata Filter

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/vector-store-metadata-filter.md"

### Clear Collection

มีให้ใช้งานในโหมด **Insert Documents** ลบข้อมูลทั้งหมดออกจาก collection ก่อนที่จะใส่ข้อมูลใหม่

## Related resources

อ้างอิง [เอกสาร Milvus ของ LangChain](https://js.langchain.com/docs/integrations/vectorstores/milvus/) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

