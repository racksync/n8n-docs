---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Chain ใน AI คืออะไร
description: ทำความเข้าใจ chains ในบริบท AI เรียนรู้เกี่ยวกับ chains ใน n8n
contentType: explanation
---

# What's a chain in AI?

[Chains](/glossary.md#ai-chain) คือการนำ component ต่างๆ ของ AI มาต่อกันเป็นระบบเดียวกัน โดยจะกำหนดลำดับการเรียกใช้งานระหว่าง component เหล่านั้น ซึ่ง component ที่ใช้ใน chain อาจเป็น model หรือ [memory](/glossary.md#ai-memory) (แต่ใน n8n chain จะไม่สามารถใช้ memory ได้)

## Chains in n8n

n8n มี node สำหรับ chain อยู่ 3 แบบ:

* [Basic LLM Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md): ใช้สำหรับคุยกับ LLM โดยตรงโดยไม่มี component อื่นเสริม
* [Question and Answer Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md): สามารถเชื่อมต่อกับ [vector store](/glossary.md#ai-vector-store) ผ่าน retriever หรือเชื่อมกับ workflow ของ n8n ผ่าน Workflow Retriever node เหมาะสำหรับ workflow ที่ต้องการถาม-ตอบกับเอกสารเฉพาะ
* [Summarization Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization.md): รับ input แล้วสรุปเนื้อหาให้

ข้อแตกต่างสำคัญระหว่าง chain ใน n8n กับเครื่องมืออื่น เช่น LangChain คือ chain ใน n8n จะไม่รองรับ memory เลย หมายความว่า chain จะไม่สามารถจดจำคำถามก่อนหน้าได้ ถ้าคุณใช้ LangChain ในการเขียนแอป AI เอง คุณสามารถใส่ memory ได้ แต่ใน n8n ถ้าต้องการให้ workflow จำประวัติการคุย ให้ใช้ agent แทน ซึ่งจำเป็นมากถ้าต้องการให้ผู้ใช้คุยกับแอปแบบ ongoing conversation
