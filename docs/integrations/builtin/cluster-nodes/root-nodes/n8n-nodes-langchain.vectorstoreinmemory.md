---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Simple Vector Store node documentation
description: Learn how to use the Simple Vector Store node in n8n. Follow technical documentation to integrate Simple Vector Store node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Simple Vector Store node

ใช้ Simple Vector Store node เพื่อจัดเก็บและเรียกดู [embeddings](/glossary.md#ai-embedding) ในหน่วยความจำภายในแอป (in-app memory) ของ n8n

ในหน้านี้ คุณจะพบ node parameters สำหรับ Simple Vector Store node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

/// note | This node is different from AI memory nodes
Simple vector storage ที่อธิบายในที่นี้แตกต่างจาก AI memory nodes เช่น [Simple Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/index.md)

Node นี้สร้าง [vector database](/glossary.md#ai-vector-store) ในหน่วยความจำของแอป
///

/// warning | For development use only
Node นี้จัดเก็บข้อมูลในหน่วยความจำเท่านั้นและไม่แนะนำให้ใช้ใน production ข้อมูลทั้งหมดจะหายไปเมื่อ n8n รีสตาร์ท และอาจถูกล้างออกไปในสภาวะที่หน่วยความจำเหลือน้อย
///

## Node usage patterns

คุณสามารถใช้ Simple Vector Store node ในรูปแบบต่อไปนี้

### Use as a regular node to insert and retrieve documents

คุณสามารถใช้ Simple Vector Store เป็น node ปกติเพื่อ insert หรือ get documents รูปแบบนี้จะวาง Simple Vector Store ไว้ใน flow การเชื่อมต่อปกติโดยไม่ต้องใช้ agent

คุณสามารถดูตัวอย่างได้ในขั้นตอนที่ 2 ของ [template นี้](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)

### Connect directly to an AI agent as a tool

คุณสามารถเชื่อมต่อ Simple Vector Store node โดยตรงกับ [tool](/glossary.md#ai-tool) connector ของ [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) เพื่อใช้ vector store เป็น resource เมื่อตอบคำถาม

ในกรณีนี้ การเชื่อมต่อจะเป็น: AI agent (tools connector) -> Simple Vector Store node

### Use a retriever to fetch documents

คุณสามารถใช้ [Vector Store Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node ร่วมกับ Simple Vector Store node เพื่อดึง documents จาก Simple Vector Store node ซึ่งมักใช้กับ [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md) node เพื่อดึง documents จาก vector store ที่ตรงกับ input ของ chat ที่กำหนด

[ตัวอย่างของ flow การเชื่อมต่อ](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/) (ตัวอย่างที่ลิงก์ใช้ Pinecone แต่รูปแบบเหมือนกัน) จะเป็น: Question and Answer Chain (Retriever connector) -> Vector Store Retriever (Vector Store connector) -> Simple Vector Store

### Use the Vector Store Question Answer Tool to answer questions

อีกรูปแบบหนึ่งคือการใช้ [Vector Store Question Answer Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md) เพื่อสรุปผลลัพธ์และตอบคำถามจาก Simple Vector Store node แทนที่จะเชื่อมต่อ Simple Vector Store โดยตรงในฐานะ tool รูปแบบนี้จะใช้ tool ที่ออกแบบมาโดยเฉพาะเพื่อสรุปข้อมูลใน vector store

[flow การเชื่อมต่อ](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/) ในกรณีนี้จะมีลักษณะดังนี้: AI agent (tools connector) -> Vector Store Question Answer Tool (Vector Store connector) -> Simple Vector store

## Memory Management

Simple Vector Store ใช้การจัดการหน่วยความจำเพื่อป้องกันการใช้หน่วยความจำมากเกินไป:

-   ล้าง vector stores เก่าโดยอัตโนมัติเมื่อแรงกดดันด้านหน่วยความจำเพิ่มขึ้น
-   ลบ stores ที่ไม่ได้ใช้งานซึ่งไม่มีการเข้าถึงเป็นระยะเวลาที่กำหนดได้
-   แต่ละ workflow จะได้รับพื้นที่จัดเก็บแยกต่างหากซึ่งระบุโดย workflow ID และ memory key

### Configuration Options

คุณสามารถควบคุมการใช้หน่วยความจำด้วย environment variables เหล่านี้:

 | Variable                      | Type   | Default | Description                                                                         |
 |-------------------------------|--------|---------|-------------------------------------------------------------------------------------|
 | `N8N_VECTOR_STORE_MAX_MEMORY` | Number | -1      | หน่วยความจำสูงสุด (MB) ที่อนุญาตสำหรับ vector stores ทั้งหมดรวมกัน (-1 เพื่อปิดการจำกัด) |
 | `N8N_VECTOR_STORE_TTL_HOURS`  | Number | -1      | จำนวนชั่วโมงที่ไม่มีการใช้งาน หลังจากนั้น store จะถูกลบ (-1 เพื่อปิด TTL)           |

บน n8n Cloud ค่าเหล่านี้ถูกตั้งค่าไว้ล่วงหน้าที่ 100MB (ประมาณ 8,000 documents ขึ้นอยู่กับขนาด document และ metadata) และ 7 วันตามลำดับ สำหรับ self-hosted instances ทั้งสองค่ามีค่าเริ่มต้นเป็น -1 (ไม่มีการจำกัดหน่วยความจำหรือการล้างตามเวลา)

## Node parameters

--8<-- "_snippets/integrations/builtin/cluster-nodes/vector-store-mode.md"

<!-- vale from-write-good.Weasel = NO -->
### Get Many parameters
<!-- vale from-write-good.Weasel = YES -->

*   **Memory Key**: ป้อน key ที่จะใช้เพื่อจัดเก็บ vector memory ในข้อมูล workflow n8n จะเติม workflow ID ไว้ข้างหน้า key เพื่อหลีกเลี่ยงการชนกัน
*   **Prompt**: ป้อนคำค้นหา (search query)
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

### Insert Documents parameters

*   **Memory Key**: ป้อน key ที่จะใช้เพื่อจัดเก็บ vector memory ในข้อมูล workflow n8n จะเติม workflow ID ไว้ข้างหน้า key เพื่อหลีกเลี่ยงการชนกัน
*   **Clear Store**: ใช้ parameter นี้เพื่อควบคุมว่าจะล้าง vector store สำหรับ memory key ที่กำหนดสำหรับ workflow นี้ก่อนที่จะใส่ข้อมูลหรือไม่ (เปิด)

### Retrieve Documents (As Vector Store for Chain/Tool) parameters

*   **Memory Key**: ป้อน key ที่จะใช้เพื่อจัดเก็บ vector memory ในข้อมูล workflow n8n จะเติม workflow ID ไว้ข้างหน้า key เพื่อหลีกเลี่ยงการชนกัน

### Retrieve Documents (As Tool for AI Agent) parameters

*   **Name**: ชื่อของ vector store
*   **Description**: อธิบายให้ LLM ทราบว่า tool นี้ทำอะไร คำอธิบายที่ดีและเฉพาะเจาะจงช่วยให้ LLM สร้างผลลัพธ์ที่คาดหวังได้บ่อยขึ้น
*   **Memory Key**: ป้อน key ที่จะใช้เพื่อจัดเก็บ vector memory ในข้อมูล workflow n8n จะเติม workflow ID ไว้ข้างหน้า key เพื่อหลีกเลี่ยงการชนกัน
*   **Limit**: ป้อนจำนวนผลลัพธ์ที่ต้องการดึงจาก vector store ตัวอย่างเช่น ตั้งค่าเป็น `10` เพื่อรับผลลัพธ์ที่ดีที่สุดสิบรายการ

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'in-memory-vector-store') ]]

## Related resources

อ้างอิง [เอกสาร Memory Vector Store ของ LangChain](https://js.langchain.com/docs/integrations/vectorstores/memory/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
