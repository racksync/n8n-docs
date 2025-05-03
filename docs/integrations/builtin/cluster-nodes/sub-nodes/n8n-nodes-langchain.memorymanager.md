---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือการใช้งาน Chat Memory Manager node
description: วิธีใช้ Chat Memory Manager node ใน n8n สำหรับจัดการ memory ข้อความแชท
contentType: [integration, reference]
priority: medium
---

# Chat Memory Manager node

Chat Memory Manager node เอาไว้จัดการ message ที่เป็น [memory](/glossary.md#ai-memory) สำหรับแชทใน workflow ของคุณ ใช้ node นี้เพื่อโหลด, แทรก, และลบข้อความแชทใน [vector store](/glossary.md#ai-vector-store) ที่อยู่ในหน่วยความจำ (in-memory)

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-sub-nodes/chat-memory-manager-purpose.md"

ในหน้านี้จะมีรายการ operations ที่ Chat Memory Manager node รองรับ พร้อมลิงก์ไปยัง resource อื่นๆ ที่เกี่ยวข้อง

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

* **Operation Mode**: เลือกว่าจะใช้โหมด **Get Many Messages**, **Insert Messages** หรือ **Delete Messages**
* **Insert Mode**: ใช้ได้ในโหมด **Insert Messages** เลือกได้ระหว่าง:
    * **Insert Messages**: แทรกข้อความใหม่เข้าไปพร้อมกับข้อความเดิม
    * **Override All Messages**: แทนที่ข้อความทั้งหมดใน memory
* **Delete Mode**: ใช้ได้ในโหมด **Delete Messages** เลือกได้ระหว่าง:
    * **Last N**: ลบข้อความล่าสุด N ข้อความ
    * **All Messages**: ลบข้อความทั้งหมดใน memory
* **Chat Messages**: ใช้ได้ในโหมด **Insert Messages** กำหนดข้อความแชทที่จะใส่เข้าไปใน memory โดยมี:
	* **Type Name or ID**: กำหนดประเภทของข้อความ เลือกได้ระหว่าง:
		* **AI**: สำหรับข้อความที่มาจาก AI
		* **System**: สำหรับข้อความที่เป็นคำสั่งหรือ instruction ให้ AI
		* **User**: สำหรับข้อความที่มาจากผู้ใช้ (บางทีเรียกว่า 'human' ในเครื่องมือ AI อื่นๆ)
	* **Message**: ใส่เนื้อหาข้อความ
	* **Hide Message in Chat**: เลือกว่าจะให้ n8n แสดงข้อความนี้ใน chat UI ให้ user เห็นหรือไม่ (ถ้าเปิดจะไม่แสดง)
* **Messages Count**: ใช้ได้ในโหมด **Delete Messages** เมื่อเลือก **Last N** ใส่จำนวนข้อความล่าสุดที่จะลบ
* **Simplify Output**: ใช้ได้ในโหมด **Get Many Messages** ถ้าเปิดจะให้ output เฉพาะ sender (AI, user, หรือ system) และข้อความ

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'chat-memory-manager') ]]

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [LangChain's Memory documentation](https://langchain-ai.github.io/langgraphjs/concepts/memory/){:target=_blank .external-link}

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

--8<-- "_glossary/ai-glossary.md"
