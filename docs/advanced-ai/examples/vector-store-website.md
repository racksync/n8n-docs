---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: howto
title: Populate a Pinecone vector database from a website
description: Scrape a website, load the data into Pinecone, then query it using a chat workflow.
---

# Populate a Pinecone vector database from a website

ใช้ n8n เพื่อ scrape ข้อมูลจากเว็บไซต์ โหลดข้อมูลเข้า Pinecone แล้ว query ด้วย chat workflow workflow นี้ใช้ [HTTP node](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) เพื่อดึงข้อมูลเว็บไซต์, ใช้ [HTML node](/integrations/builtin/core-nodes/n8n-nodes-base.html.md) เพื่อ extract เนื้อหาหลัก แล้วใช้ [Pinecone Vector Store node](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md) เพื่อส่งข้อมูลเข้า Pinecone

[[ workflowDemo("file:///advanced-ai/examples/populate_a_pinecone_vector_database_from_a_website.json") ]]

## Key features

workflow นี้ใช้:

* [HTTP node](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md): ดึงข้อมูลเว็บไซต์
* [HTML node](/integrations/builtin/core-nodes/n8n-nodes-base.html.md): extract เนื้อหาหลักจากหน้าเว็บ
* [Pinecone Vector Store node](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md) และ [Embeddings OpenAI](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md): แปลงข้อมูลเป็นเวกเตอร์แล้วเก็บใน Pinecone
* [Chat Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md) และ [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md) สำหรับ query vector database

## Using the example

--8<-- "_snippets/examples-color-key.md"
