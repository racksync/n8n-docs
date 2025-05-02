---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Summarization Chain node documentation
description: Learn how to use the Summarize Chain node in n8n. Follow technical documentation to integrate Summarize Chain node into your workflows.
contentType: [integration, reference]
priority: high
---

# Summarization Chain node

ใช้ Summarization Chain node เพื่อสรุปเอกสาร (documents) หลายฉบับ

ในหน้านี้ คุณจะพบ node parameters สำหรับ Summarization Chain node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

## Node parameters

เลือกประเภทข้อมูลที่คุณต้องการสรุปใน **Data to Summarize** ประเภทข้อมูลที่คุณเลือกจะกำหนด node parameters อื่นๆ

*   **Use Node Input (JSON)** และ **Use Node Input (Binary)**: สรุปข้อมูลที่เข้ามาใน node จาก workflow
    *   คุณสามารถกำหนดค่า **Chunking Strategy**: เลือกกลยุทธ์ที่จะใช้ในการกำหนดขนาด chunk ของข้อมูล
        *   หากคุณเลือก **Simple (Define Below)** คุณสามารถตั้งค่า **Characters Per Chunk** และ **Chunk Overlap (Characters)** ได้
        *   เลือก **Advanced** หากคุณต้องการเชื่อมต่อ splitter sub-node ที่มีตัวเลือกการกำหนดค่าเพิ่มเติม
*   **Use Document Loader**: สรุปข้อมูลที่มาจาก document loader sub-node

## Node Options

คุณสามารถกำหนดค่า summarization method และ prompts ได้ เลือก **Add Option** > **Summarization Method and Prompts**

ตัวเลือกใน **Summarization Method**:

*   **Map Reduce**: นี่คือตัวเลือกที่แนะนำ เรียนรู้เพิ่มเติมเกี่ยวกับ [Map Reduce](https://js.langchain.com/v0.1/docs/modules/chains/document/map_reduce/){:target=_blank .external-link} ในเอกสาร LangChain
*   **Refine**: เรียนรู้เพิ่มเติมเกี่ยวกับ [Refine](https://js.langchain.com/v0.1/docs/modules/chains/document/refine/){:target=_blank .external-link} ในเอกสาร LangChain
*   **Stuff**: เรียนรู้เพิ่มเติมเกี่ยวกับ [Stuff](https://js.langchain.com/v0.1/docs/modules/chains/document/stuff/){:target=_blank .external-link} ในเอกสาร LangChain

คุณสามารถปรับแต่ง **Individual Summary Prompts** และ **Final Prompt to Combine** ได้ มีตัวอย่างอยู่ใน node คุณต้องใส่ placeholder `"{text}"`

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'summarization-chain') ]]

## Related resources

อ้างอิง [เอกสารของ LangChain เกี่ยวกับการสรุป](https://js.langchain.com/docs/tutorials/summarization/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการ

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
