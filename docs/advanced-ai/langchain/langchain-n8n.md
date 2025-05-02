---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
contentType: explanation
title: LangChain concepts in n8n
description: How LangChain concepts map to n8n, and which n8n nodes to use.
---

# LangChain concepts in n8n

หน้านี้อธิบายว่า LangChain concepts และ features แมปกับ n8n nodes อย่างไร

หน้านี้รวมรายการของ LangChain-focused nodes ใน n8n คุณสามารถใช้ n8n node ใดก็ได้ใน workflow ที่คุณโต้ตอบกับ LangChain เพื่อเชื่อมโยง LangChain กับ services อื่นๆ ฟีเจอร์ LangChain ใช้ [Cluster nodes](/integrations/builtin/cluster-nodes/index.md) ของ n8n

/// note | n8n implements LangChain JS
ฟีเจอร์นี้เป็นการนำ [LangChain's JavaScript framework](https://js.langchain.com/docs/get_started/introduction){:target=_blank .external-link} มาใช้ใน n8n
///
## Trigger nodes

[Chat Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md)

## Cluster nodes

--8<-- "_snippets/integrations/builtin/cluster-nodes/cluster-nodes-summary.md"

### Root nodes

แต่ละ cluster เริ่มต้นด้วย [root node](/glossary.md#root-node-n8n) หนึ่งตัว

#### Chains

[chain](/glossary.md#ai-chain) คือชุดของ LLMs และ tools ที่เกี่ยวข้อง ซึ่งเชื่อมโยงเข้าด้วยกันเพื่อรองรับฟังก์ชันที่ LLM เดี่ยวๆ ทำไม่ได้

Available nodes:

* [Basic LLM Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md)
* [Retrieval Q&A Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md)
* [Summarization Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization.md)
* [Sentiment Analysis](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis.md)
* [Text Classifier](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier.md)

ดูเพิ่มเติมเกี่ยวกับ [chaining in LangChain](https://js.langchain.com/docs/concepts/lcel){:target=_blank .external-link}

#### Agents

> [agent](/glossary.md#ai-agent){ data-preview} สามารถเข้าถึงชุด tools และเลือกใช้ตาม user input Agents สามารถใช้หลาย tools และนำ output ของ tool หนึ่งไปเป็น input ของ tool ถัดไป [Source](https://github.com/langchain-ai/langchainjs/blob/def3a26c054575e1ed40b9062087e8c0a8899633/docs/core_docs/docs/modules/agents/index.mdx){:target=_blank .external-link}

Available nodes:

* [Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md)

ดูเพิ่มเติมเกี่ยวกับ [Agents in LangChain](https://js.langchain.com/docs/concepts/agents){:target=_blank .external-link}

#### Vector stores

[Vector stores](/glossary.md#ai-vector-store) ใช้เก็บ embedded data และค้นหา vector บนข้อมูลนั้น

* [Simple Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory.md)
* [PGVector Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector.md)
* [Pinecone Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md)
* [Qdrant Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant.md)
* [Supabase Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoresupabase.md)
* [Zep Vector Store](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep.md)

ดูเพิ่มเติมเกี่ยวกับ [Vector stores in LangChain](https://js.langchain.com/docs/concepts/vectorstores/){:target=_blank .external-link}

#### Miscellaneous

Utility nodes

[LangChain Code](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code.md): import LangChain หมายความว่าถ้ามีฟังก์ชันที่คุณต้องการแต่ n8n ยังไม่มี node ให้ คุณก็ยังใช้งานได้

### Sub-nodes

แต่ละ root node สามารถมี [sub-nodes](/glossary.md#sub-node-n8n) ได้หนึ่งตัวหรือมากกว่า

#### Document loaders

Document loaders เพิ่มข้อมูลเข้า chain ของคุณในรูปแบบ documents แหล่งข้อมูลอาจเป็นไฟล์หรือ web service

Available nodes:

* [Default Document Loader](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md)
* [GitHub Document Loader](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md)

ดูเพิ่มเติมเกี่ยวกับ [Document loaders in LangChain](https://js.langchain.com/docs/concepts/document_loaders){:target=_blank .external-link}

#### Language models

[LLMs (large language models)](/glossary.md#large-language-model-llm) คือโปรแกรมที่วิเคราะห์ datasets เป็นหัวใจของการทำงานกับ AI

Available nodes:

* [Anthropic Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md)
* [AWS Bedrock Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md)
* [Cohere Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere.md)
* [Hugging Face Inference Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference.md)
* [Mistral Cloud Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md)
* [Ollama Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/index.md)
* [Ollama Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/index.md)
* [OpenAI Chat Model](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/index.md)

ดูเพิ่มเติมเกี่ยวกับ [Language models in LangChain](https://js.langchain.com/docs/concepts/chat_models){:target=_blank .external-link}

#### Memory

[Memory](/glossary.md#ai-memory) เก็บข้อมูลเกี่ยวกับ queries ก่อนหน้าในชุด queries เช่น เมื่อผู้ใช้คุยกับ chat model จะดีถ้าแอปของคุณจำและเรียกใช้ conversation ทั้งหมดได้ ไม่ใช่แค่ query ล่าสุด

Available nodes:

* [Motorhead](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md)
* [Redis Chat Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md)
* [Postgres Chat Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md) 
* [Simple Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/index.md)
* [Xata](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata.md)
* [Zep](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep.md)

ดูเพิ่มเติมเกี่ยวกับ [Memory in LangChain](https://langchain-ai.github.io/langgraphjs/concepts/memory/){:target=_blank .external-link}

#### Output parsers

Output parsers รับข้อความที่ LLM สร้าง แล้วจัดรูปแบบให้ตรงกับโครงสร้างที่ต้องการ

Available nodes:

* [Auto-fixing Output Parser](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing.md)
* [Item List Output Parser](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist.md)
* [Structured Output Parser](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/index.md)

ดูเพิ่มเติมเกี่ยวกับ [Output parsers in LangChain](https://js.langchain.com/docs/concepts/output_parsers/){:target=_blank .external-link}

#### Retrievers

* [Contextual Compression Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression.md)
* [MultiQuery Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievermultiquery.md)
* [Vector Store Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievervectorstore.md)
* [Workflow Retriever](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow.md)

#### Text splitters

Text splitters แบ่งข้อมูล (documents) ออกเป็นส่วนย่อย ทำให้ LLM ประมวลผลและคืนผลลัพธ์ได้แม่นยำขึ้น

Available nodes:

* [Character Text Splitter](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittercharactertextsplitter.md)
* [Recursive Character Text Splitter](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md)
* [Token Splitter](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter.md)

n8n's text splitter nodes นำบางส่วนของ [LangChain's text_splitter API](https://js.langchain.com/docs/concepts/text_splitters/){:target=_blank .external-link} มาใช้

#### Tools

Utility [tools](/glossary.md#ai-tool)

* [Calculator](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcalculator.md)
* [Code Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode.md)
* [SerpAPI](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md)
* [Think Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink.md)
* [Vector Store Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md)
* [Wikipedia](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia.md)
* [Wolfram|Alpha](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha.md)
* [Workflow Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md)

#### Embeddings

> [Embeddings](/glossary.md#ai-embedding) คือการจับ "ความเกี่ยวข้อง" ของข้อความ รูปภาพ วิดีโอ หรือข้อมูลประเภทอื่นๆ ([source](https://supabase.com/docs/guides/ai/concepts){:target=_blank .external-link})

Available nodes:

* [Embeddings AWS Bedrock](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md)
* [Embeddings Cohere](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere.md)
* [Embeddings Google PaLM](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm.md)
* [Embeddings Hugging Face Inference](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingshuggingfaceinference.md)
* [Embeddings Mistral Cloud](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud.md)
* [Embeddings Ollama](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama.md)
* [Embeddings OpenAI](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md)

ดูเพิ่มเติมเกี่ยวกับ [Text embeddings in LangChain](https://js.langchain.com/docs/concepts/embedding_models/){:target=_blank .external-link}

#### Miscellaneous

* [Chat Memory Manager](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager.md)



