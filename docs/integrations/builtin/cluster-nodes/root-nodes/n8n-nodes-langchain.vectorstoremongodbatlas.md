---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ MongoDB Atlas Vector Store node
description: วิธีใช้งาน MongoDB Atlas Vector Store node ใน n8n สำหรับเชื่อมต่อและค้นหา embeddings ใน MongoDB Atlas
contentType: [integration, reference]
priority: medium
---

# MongoDB Atlas Vector Store node

MongoDB Atlas Vector Search เป็นฟีเจอร์ของ MongoDB Atlas ที่ช่วยให้ผู้ใช้สามารถจัดเก็บและ query vector embeddings ได้ ใช้ node นี้เพื่อโต้ตอบกับ Vector Search indexes ใน MongoDB Atlas collections ของคุณ คุณสามารถ insert documents, retrieve documents และใช้ vector store ใน chains หรือเป็น tool สำหรับ agents

ในหน้านี้ คุณจะพบ node parameters สำหรับ MongoDB Atlas Vector Store node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูล authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/mongodb.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Prerequisites

ก่อนใช้ node นี้ ให้สร้าง [Vector Search index](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-type/) ใน MongoDB Atlas collection ของคุณ ทำตามขั้นตอนเหล่านี้เพื่อสร้าง:

1.  เข้าสู่ระบบ [MongoDB Atlas dashboard](https://cloud.mongodb.com/)

3.  เลือก organization และ project ของคุณ
4.  ค้นหาส่วน "Search & Vector Search"
5.  เลือก cluster ของคุณและคลิก "Go to search"
7.  คลิก "Create Search Index"
8.  เลือกโหมด "Vector Search" และใช้ visual หรือ JSON editors ตัวอย่างเช่น:
    ```json
    {
      "fields": [
        {
          "type": "vector",
          "path": "<field-name>",
          "numDimensions": 1536, // any other value
          "similarity": "<similarity-function>"
        }
      ]
    }
    ```

9.  ปรับค่า "dimensions" ตาม embedding model ของคุณ (ตัวอย่างเช่น `1536` สำหรับ `text-embedding-small-3` ของ OpenAI)
10. ตั้งชื่อ index ของคุณและสร้าง

ตรวจสอบให้แน่ใจว่าได้จดค่าต่อไปนี้ซึ่งจำเป็นเมื่อกำหนดค่า node:

-   Collection name
-   Vector index name
-   Field names สำหรับ embeddings และ metadata

## Node usage patterns

คุณสามารถใช้ MongoDB Atlas Vector Store node ในรูปแบบต่อไปนี้:

### Use as a regular node to insert and retrieve documents

คุณสามารถใช้ MongoDB Atlas Vector Store เป็น node ปกติเพื่อ insert หรือ get documents รูปแบบนี้จะวาง MongoDB Atlas Vector Store ไว้ใน flow การเชื่อมต่อปกติโดยไม่ต้องใช้ agent

คุณสามารถดูตัวอย่างได้ใน scenario 1 ของ [template นี้](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/) (template ใช้ Supabase Vector Store แต่รูปแบบเหมือนกัน)

### Connect directly to an AI agent as a tool

คุณสามารถเชื่อมต่อ MongoDB Atlas Vector Store node โดยตรงกับ tool connector ของ [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) เพื่อใช้ vector store เป็น resource เมื่อตอบคำถาม

ในกรณีนี้ การเชื่อมต่อจะเป็น: AI agent (tools connector) -> MongoDB Atlas Vector Store node

### Use a retriever to fetch documents

คุณสามารถใช้ [Vector Store Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node ร่วมกับ MongoDB Atlas Vector Store node เพื่อดึง documents จาก MongoDB Atlas Vector Store node ซึ่งมักใช้กับ [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md) node เพื่อดึง documents จาก vector store ที่ตรงกับ input ของ chat ที่กำหนด

[ตัวอย่างของ flow การเชื่อมต่อ](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/) (ตัวอย่างที่ลิงก์ใช้ Pinecone แต่รูปแบบเหมือนกัน) จะเป็น: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> MongoDB Atlas Vector Store

### Use the Vector Store Question Answer Tool to answer questions

อีกรูปแบบหนึ่งคือการใช้ [Vector Store Question Answer Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md) เพื่อสรุปผลลัพธ์และตอบคำถามจาก MongoDB Atlas Vector Store node แทนที่จะเชื่อมต่อ MongoDB Atlas Vector Store โดยตรงในฐานะ tool รูปแบบนี้จะใช้ tool ที่ออกแบบมาโดยเฉพาะเพื่อสรุปข้อมูลใน vector store

[flow การเชื่อมต่อ](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/) (ตัวอย่างที่ลิงก์ใช้ In-Memory Vector Store แต่รูปแบบเหมือนกัน) ในกรณีนี้จะมีลักษณะดังนี้: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> In-Memory Vector store

## Node parameters

--8<-- "_snippets/integrations/builtin/cluster-nodes/vector-store-mode.md"

<!-- vale off -->
### Get Many parameters
<!-- vale on -->

-   **Mongo Collection**: ป้อนชื่อ MongoDB collection ที่จะใช้
-   **Vector Index Name**: ป้อนชื่อ Vector Search index ใน MongoDB Atlas collection ของคุณ
-   **Embedding Field**: ป้อนชื่อ field ใน documents ของคุณที่มี vector embeddings
-   **Metadata Field**: ป้อนชื่อ field ใน documents ของคุณที่มี text metadata

### Insert Documents parameters

-   **Mongo Collection**: ป้อนชื่อ MongoDB collection ที่จะใช้
-   **Vector Index Name**: ป้อนชื่อ Vector Search index ใน MongoDB Atlas collection ของคุณ
-   **Embedding Field**: ป้อนชื่อ field ใน documents ของคุณที่มี vector embeddings
-   **Metadata Field**: ป้อนชื่อ field ใน documents ของคุณที่มี text metadata

### Retrieve Documents parameters (As Vector Store for Chain/Tool)

-   **Mongo Collection**: ป้อนชื่อ MongoDB collection ที่จะใช้
-   **Vector Index Name**: ป้อนชื่อ Vector Search index ใน MongoDB Atlas collection ของคุณ
-   **Embedding Field**: ป้อนชื่อ field ใน documents ของคุณที่มี vector embeddings
-   **Metadata Field**: ป้อนชื่อ field ใน documents ของคุณที่มี text metadata

### Retrieve Documents (As Tool for AI Agent) parameters

-   **Name**: ชื่อของ vector store
-   **Description**: อธิบายให้ LLM ทราบว่า tool นี้ทำอะไร คำอธิบายที่ดีและเฉพาะเจาะจงช่วยให้ LLM สร้างผลลัพธ์ที่คาดหวังได้บ่อยขึ้น
-   **Mongo Collection**: ป้อนชื่อ MongoDB collection ที่จะใช้
-   **Vector Index Name**: ป้อนชื่อ Vector Search index ใน MongoDB Atlas collection ของคุณ
-   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

## Node options

### Options

-   **Metadata Filter**: กรองผลลัพธ์ตาม metadata

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'mongodb-atlas-vector-store') ]]

## Related resources

อ้างอิง:

-   [เอกสาร MongoDB Atlas Vector Search ของ LangChain](https://js.langchain.com/docs/integrations/vectorstores/mongodb_atlas){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ
-   [เอกสาร MongoDB Atlas Vector Search](https://www.mongodb.com/docs/atlas/atlas-vector-search/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ MongoDB Atlas Vector Search

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

--8<-- "_snippets/self-hosting/starter-kits/self-hosted-ai-starter-kit.md"
