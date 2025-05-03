---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Zep Vector Store node
description: วิธีใช้งาน Zep Vector Store node ใน n8n สำหรับเชื่อมต่อและจัดการ Zep vector database
contentType: [integration, reference]
---

# Zep Vector Store node

ใช้ Zep Vector Store node เพื่อโต้ตอบกับ Zep vector databases คุณสามารถใส่ documents เข้าไปใน vector database, ดึง documents จาก vector database, เรียกดู documents เพื่อส่งต่อไปยัง retriever ที่เชื่อมต่อกับ [chain](/glossary.md#ai-chain) หรือเชื่อมต่อโดยตรงกับ [agent](/glossary.md#ai-agent) เพื่อใช้เป็น [tool](/glossary.md#ai-tool)

ในหน้านี้ คุณจะพบ node parameters สำหรับ Zep Vector Store node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูล authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/zep.md)
///

/// note | Examples and templates
สำหรับตัวอย่างการใช้งานและ templates เพื่อช่วยให้คุณเริ่มต้น โปรดดูที่หน้า [Zep Vector Store integrations](https://n8n.io/integrations/zep-vector-store/){:target=_blank .external-link} ของ n8n
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node usage patterns

คุณสามารถใช้ Zep Vector Store node ในรูปแบบต่อไปนี้

### Use as a regular node to insert, update, and retrieve documents

คุณสามารถใช้ Zep Vector Store เป็น node ปกติเพื่อ insert หรือ get documents รูปแบบนี้จะวาง Zep Vector Store ไว้ใน flow การเชื่อมต่อปกติโดยไม่ต้องใช้ agent

คุณสามารถดูตัวอย่างได้ใน scenario 1 ของ [template นี้](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/) (ตัวอย่างใช้ Supabase แต่รูปแบบเหมือนกัน)

### Connect directly to an AI agent as a tool

คุณสามารถเชื่อมต่อ Zep Vector Store node โดยตรงกับ tool connector ของ [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) เพื่อใช้ vector store เป็น resource เมื่อตอบคำถาม

ในกรณีนี้ การเชื่อมต่อจะเป็น: AI agent (tools connector) -> Zep Vector Store node

### Use a retriever to fetch documents

คุณสามารถใช้ [Vector Store Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node ร่วมกับ Zep Vector Store node เพื่อดึง documents จาก Zep Vector Store node ซึ่งมักใช้กับ [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md) node เพื่อดึง documents จาก vector store ที่ตรงกับ input ของ chat ที่กำหนด

[ตัวอย่างของ flow การเชื่อมต่อ](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/) (ตัวอย่างใช้ Pinecone แต่รูปแบบเหมือนกัน) จะเป็น: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Zep Vector Store

### Use the Vector Store Question Answer Tool to answer questions

อีกรูปแบบหนึ่งคือการใช้ [Vector Store Question Answer Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md) เพื่อสรุปผลลัพธ์และตอบคำถามจาก Zep Vector Store node แทนที่จะเชื่อมต่อ Zep Vector Store โดยตรงในฐานะ tool รูปแบบนี้จะใช้ tool ที่ออกแบบมาโดยเฉพาะเพื่อสรุปข้อมูลใน vector store

[flow การเชื่อมต่อ](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/) (ตัวอย่างนี้ใช้ Supabase แต่รูปแบบเหมือนกัน) ในกรณีนี้จะมีลักษณะดังนี้: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Zep Vector store

## Node parameters

--8<-- "_snippets/integrations/builtin/cluster-nodes/vector-store-mode.md"

### Insert Documents parameters

*   **Collection Name**: ป้อนชื่อ collection ที่จะจัดเก็บข้อมูล

<!-- vale from-write-good.Weasel = NO -->
### Get Many parameters
<!-- vale from-write-good.Weasel = YES -->

*   **Collection Name**: ป้อนชื่อ collection ที่จะดึงข้อมูล
*   **Prompt**: ป้อนคำค้นหา (search query)
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

### Retrieve Documents (As Vector Store for Chain/Tool) parameters

*   **Collection Name**: ป้อนชื่อ collection ที่จะดึงข้อมูล

### Retrieve Documents (As Tool for AI Agent) parameters

*   **Name**: ชื่อของ vector store
*   **Description**: อธิบายให้ LLM ทราบว่า tool นี้ทำอะไร คำอธิบายที่ดีและเฉพาะเจาะจงช่วยให้ LLM สร้างผลลัพธ์ที่คาดหวังได้บ่อยขึ้น
*   **Collection Name**: ป้อนชื่อ collection ที่จะดึงข้อมูล
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

## Node options

### Embedding Dimensions

ต้องเหมือนกันทั้งตอนทำ embedding ข้อมูลและตอน query ข้อมูล

สิ่งนี้กำหนดขนาดของ array ของ floats ที่ใช้แทนความหมายเชิง semantic ของเอกสารข้อความ

อ่านเพิ่มเติมเกี่ยวกับ Zep embeddings ใน [เอกสาร embeddings ของ Zep](https://docs.getzep.com/deployment/embeddings/){:target=_blank .external-link}

### Is Auto Embedded

มีให้ใช้งานใน **Insert Documents** Operation Mode เปิดใช้งานโดยค่าเริ่มต้น

ปิดใช้งานตัวเลือกนี้เพื่อกำหนดค่า embeddings ของคุณใน Zep แทนที่จะเป็นใน n8n

### Metadata Filter

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/vector-store-metadata-filter.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'zep-vector-store') ]]

## Related resources

อ้างอิง [เอกสาร Zep ของ LangChain](https://js.langchain.com/docs/integrations/vectorstores/zep/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
