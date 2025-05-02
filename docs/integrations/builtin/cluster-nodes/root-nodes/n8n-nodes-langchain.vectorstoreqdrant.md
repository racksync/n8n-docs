---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Qdrant Vector Store node documentation
description: Learn how to use the Qdrant Vector Store node in n8n. Follow technical documentation to integrate Qdrant Vector Store node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Qdrant Vector Store node

ใช้ Qdrant node เพื่อโต้ตอบกับ Qdrant collection ของคุณในฐานะ [vector store](/glossary.md#ai-vector-store) คุณสามารถใส่ documents เข้าไปใน vector database, ดึง documents จาก vector database, เรียกดู documents เพื่อส่งต่อไปยัง retriever ที่เชื่อมต่อกับ [chain](/glossary.md#ai-chain) หรือเชื่อมต่อโดยตรงกับ [agent](/glossary.md#ai-agent) เพื่อใช้เป็น [tool](/glossary.md#ai-tool)

ในหน้านี้ คุณจะพบ node parameters สำหรับ Qdrant node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูล authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/qdrant.md)
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node usage patterns

คุณสามารถใช้ Qdrant Vector Store node ในรูปแบบต่อไปนี้

### Use as a regular node to insert and retrieve documents

คุณสามารถใช้ Qdrant Vector Store เป็น node ปกติเพื่อ insert หรือ get documents รูปแบบนี้จะวาง Qdrant Vector Store ไว้ใน flow การเชื่อมต่อปกติโดยไม่ต้องใช้ agent

คุณสามารถดูตัวอย่างได้ในส่วนแรกของ [template นี้](https://n8n.io/workflows/2440-building-rag-chatbot-for-movie-recommendations-with-qdrant-and-open-ai/)

### Connect directly to an AI agent as a tool

คุณสามารถเชื่อมต่อ Qdrant Vector Store node โดยตรงกับ tool connector ของ [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) เพื่อใช้ vector store เป็น resource เมื่อตอบคำถาม

ในกรณีนี้ การเชื่อมต่อจะเป็น: AI agent (tools connector) -> Qdrant Vector Store node

### Use a retriever to fetch documents

คุณสามารถใช้ [Vector Store Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node ร่วมกับ Qdrant Vector Store node เพื่อดึง documents จาก Qdrant Vector Store node ซึ่งมักใช้กับ [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md) node เพื่อดึง documents จาก vector store ที่ตรงกับ input ของ chat ที่กำหนด

[ตัวอย่างของ flow การเชื่อมต่อ](https://n8n.io/workflows/2183-ai-crew-to-automate-fundamental-stock-analysis-qanda-workflow/) จะเป็น: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Qdrant Vector Store

### Use the Vector Store Question Answer Tool to answer questions

อีกรูปแบบหนึ่งคือการใช้ [Vector Store Question Answer Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md) เพื่อสรุปผลลัพธ์และตอบคำถามจาก Qdrant Vector Store node แทนที่จะเชื่อมต่อ Qdrant Vector Store โดยตรงในฐานะ tool รูปแบบนี้จะใช้ tool ที่ออกแบบมาโดยเฉพาะเพื่อสรุปข้อมูลใน vector store

[flow การเชื่อมต่อ](https://n8n.io/workflows/2464-scale-deal-flow-with-a-pitch-deck-ai-vision-chatbot-and-qdrant-vector-store/) ในกรณีนี้จะมีลักษณะดังนี้: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Qdrant Vector store

## Node parameters

--8<-- "_snippets/integrations/builtin/cluster-nodes/vector-store-mode.md"

<!-- vale from-write-good.Weasel = NO -->
### Get Many parameters
<!-- vale from-write-good.Weasel = YES -->

*   **Qdrant collection name**: ป้อนชื่อของ Qdrant collection ที่จะใช้
*   **Prompt**: ป้อนคำค้นหา (search query)
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

Operation Mode นี้มี **Node option** หนึ่งตัวคือ [Metadata Filter](#metadata-filter)

### Insert Documents parameters

*   **Qdrant collection name**: ป้อนชื่อของ Qdrant collection ที่จะใช้

Operation Mode นี้มี **Node option** หนึ่งตัว:

*   **Collection Config**: ป้อน JSON options สำหรับการสร้าง configuration การสร้าง Qdrant collection อ้างอิงเอกสาร [Collections](https://qdrant.tech/documentation/concepts/collections/){:target=_blank .external-link} ของ Qdrant สำหรับข้อมูลเพิ่มเติม

### Retrieve Documents (As Vector Store for Chain/Tool) parameters

*   **Qdrant Collection**: ป้อนชื่อของ Qdrant collection ที่จะใช้

Operation Mode นี้มี **Node option** หนึ่งตัวคือ [Metadata Filter](#metadata-filter)

### Retrieve Documents (As Tool for AI Agent) parameters

*   **Name**: ชื่อของ vector store
*   **Description**: อธิบายให้ LLM ทราบว่า tool นี้ทำอะไร คำอธิบายที่ดีและเฉพาะเจาะจงช่วยให้ LLM สร้างผลลัพธ์ที่คาดหวังได้บ่อยขึ้น
*   **Qdrant Collection**: ป้อนชื่อของ Qdrant collection ที่จะใช้
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

## Node options

### Metadata Filter

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/vector-store-metadata-filter.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'qdrant-vector-store') ]]

## Related resources

อ้างอิง [เอกสาร Qdrant ของ LangChain](https://js.langchain.com/docs/integrations/vectorstores/qdrant){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

--8<-- "_snippets/self-hosting/starter-kits/self-hosted-ai-starter-kit.md"
