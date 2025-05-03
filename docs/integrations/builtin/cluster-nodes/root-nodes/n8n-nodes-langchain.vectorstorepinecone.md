---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Pinecone Vector Store node
description: วิธีใช้งาน Pinecone Vector Store node ใน n8n สำหรับเชื่อมต่อและจัดการ Pinecone vector database
contentType: [integration, reference]
priority: medium
---

# Pinecone Vector Store node

ใช้ Pinecone node เพื่อโต้ตอบกับ Pinecone database ของคุณในฐานะ [vector store](/glossary.md#ai-vector-store) คุณสามารถใส่ documents เข้าไปใน vector database, ดึง documents จาก vector database, เรียกดู documents เพื่อส่งต่อไปยัง retriever ที่เชื่อมต่อกับ [chain](/glossary.md#ai-chain) หรือเชื่อมต่อโดยตรงกับ [agent](/glossary.md#ai-agent) ในฐานะ [tool](/glossary.md#ai-tool)

ในหน้านี้ คุณจะพบ node parameters สำหรับ Pinecone node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูล authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/pinecone.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node usage patterns

คุณสามารถใช้ Pinecone Vector Store node ในรูปแบบต่อไปนี้

### Use as a regular node to insert, update, and retrieve documents

คุณสามารถใช้ Pinecone Vector Store เป็น node ปกติเพื่อ insert, update หรือ get documents รูปแบบนี้จะวาง Pinecone Vector Store ไว้ใน flow การเชื่อมต่อปกติโดยไม่ต้องใช้ agent

คุณสามารถดูตัวอย่างได้ใน scenario 1 ของ [template นี้](https://n8n.io/workflows/2165-chat-with-pdf-docs-using-ai-quoting-sources/)

### Connect directly to an AI agent as a tool

คุณสามารถเชื่อมต่อ Pinecone Vector Store node โดยตรงกับ tool connector ของ [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) เพื่อใช้ vector store เป็น resource เมื่อตอบคำถาม

ในกรณีนี้ การเชื่อมต่อจะเป็น: AI agent (tools connector) -> Pinecone Vector Store node

### Use a retriever to fetch documents

คุณสามารถใช้ [Vector Store Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node ร่วมกับ Pinecone Vector Store node เพื่อดึง documents จาก Pinecone Vector Store node ซึ่งมักใช้กับ [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md) node เพื่อดึง documents จาก vector store ที่ตรงกับ input ของ chat ที่กำหนด

[ตัวอย่างของ flow การเชื่อมต่อ](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/) จะเป็น: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Pinecone Vector Store

### Use the Vector Store Question Answer Tool to answer questions

อีกรูปแบบหนึ่งคือการใช้ [Vector Store Question Answer Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md) เพื่อสรุปผลลัพธ์และตอบคำถามจาก Pinecone Vector Store node แทนที่จะเชื่อมต่อ Pinecone Vector Store โดยตรงในฐานะ tool รูปแบบนี้จะใช้ tool ที่ออกแบบมาโดยเฉพาะเพื่อสรุปข้อมูลใน vector store

[flow การเชื่อมต่อ](https://n8n.io/workflows/2705-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-and-openai/) ในกรณีนี้จะมีลักษณะดังนี้: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Pinecone Vector store

## Node parameters

--8<-- "_snippets/integrations/builtin/cluster-nodes/vector-store-mode-with-update.md"

<!-- vale from-write-good.Weasel = NO -->
### Get Many parameters
<!-- vale from-write-good.Weasel = YES -->

*   **Pinecone Index**: เลือกหรือป้อน Pinecone Index ที่จะใช้
*   **Prompt**: ป้อนคำค้นหา (search query) ของคุณ
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

### Insert Documents parameters

*   **Pinecone Index**: เลือกหรือป้อน Pinecone Index ที่จะใช้

### Retrieve Documents (As Vector Store for Chain/Tool) parameters

*   **Pinecone Index**: เลือกหรือป้อน Pinecone Index ที่จะใช้

### Retrieve Documents (As Tool for AI Agent) parameters

*   **Name**: ชื่อของ vector store
*   **Description**: อธิบายให้ LLM ทราบว่า tool นี้ทำอะไร คำอธิบายที่ดีและเฉพาะเจาะจงช่วยให้ LLM สร้างผลลัพธ์ที่คาดหวังได้บ่อยขึ้น
*   **Pinecone Index**: เลือกหรือป้อน Pinecone Index ที่จะใช้
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

## Node options

### Pinecone Namespace

ตัวเลือกการแบ่งแยกข้อมูลอีกวิธีหนึ่งสำหรับวิธีการจัดเก็บข้อมูลของคุณภายใน index

### Metadata Filter

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/vector-store-metadata-filter.md"

### Clear Namespace

มีให้ใช้งานในโหมด **Insert Documents** ลบข้อมูลทั้งหมดออกจาก namespace ก่อนที่จะใส่ข้อมูลใหม่

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'pinecone-vector-store') ]]

## Related resources

อ้างอิง [เอกสาร Pinecone ของ LangChain](https://js.langchain.com/docs/integrations/vectorstores/pinecone/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

### Find your Pinecone index and namespace

Pinecone index และ namespace ของคุณมีอยู่ในบัญชี Pinecone ของคุณ

![Screenshot of a Pinecone account, with the Pinecone index labelled](/_images/integrations/builtin/cluster-nodes/vectorstorepinecone/pinecone-index-namespace.png)
--8<-- "_glossary/ai-glossary.md"
