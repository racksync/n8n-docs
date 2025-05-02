---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: What's memory in AI?
description: Understand memory in the context of AI. Learn what's special about memory in n8n.
contentType: explanation
---

# What's memory in AI?

Memory เป็นส่วนสำคัญของบริการ AI chat [memory](/glossary.md#ai-memory) จะเก็บประวัติข้อความก่อนหน้า ทำให้สามารถคุยกับ AI แบบต่อเนื่องได้ ไม่ต้องเริ่มใหม่ทุกครั้ง

## AI memory in n8n

ถ้าต้องการเพิ่ม memory ให้ workflow AI ของคุณใน n8n มี 2 ทางเลือก:

* [Simple Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/index.md): เก็บประวัติ chat ตามจำนวนที่กำหนดสำหรับ session ปัจจุบัน ใช้งานง่ายสุด
* ใช้ memory service ที่ n8n มี node ให้ เช่น:
	* [Motorhead](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md)
	* [Redis Chat Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat.md)
	* [Postgres Chat Memory](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat.md) 
	* [Xata](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata.md)
	* [Zep](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep.md)

ถ้าต้องการจัดการ memory ของ AI แบบ advance ใน workflow ให้ใช้ [Chat Memory Manager](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager.md) node

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-sub-nodes/chat-memory-manager-purpose.md"
