---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Simple Memory node
description: วิธีใช้ Simple Memory node ใน n8n พร้อมขั้นตอนการตั้งค่าและเชื่อมต่อ workflow
contentType: [integration, reference]
priority: high
---

# Simple Memory node

ใช้ Simple Memory node เพื่อ [persist](/glossary.md#ai-memory) ประวัติการแชทใน workflow ของคุณ

ในหน้านี้ คุณจะพบรายการ operations ที่ Simple Memory node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// warning | Don't use this node if running n8n in queue mode
หาก n8n instance ของคุณใช้ [queue mode](/hosting/scaling/queue-mode.md) node นี้จะไม่ทำงานใน production workflow ที่ใช้งานอยู่ เนื่องจาก n8n ไม่สามารถรับประกันได้ว่าทุกการเรียก Simple Memory จะไปที่ worker เดียวกัน
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

## Node parameters

ตั้งค่า parameters เหล่านี้เพื่อกำหนดค่า node:

* **Session Key**: ป้อน key ที่จะใช้เก็บ memory ในข้อมูล workflow
* **Context Window Length**: ป้อนจำนวน interactions ก่อนหน้าที่จะพิจารณาสำหรับ context

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'window-buffer-memory') ]]

## Related resources

อ้างอิง [LangChain's Buffer Window Memory documentation](https://v03.api.js.langchain.com/classes/langchain.memory.BufferWindowMemory.html){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ service

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Common issues

สำหรับคำถามหรือปัญหาทั่วไปและแนวทางแก้ไขที่แนะนำ โปรดดูที่ [Common issues](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues.md)

--8<-- "_glossary/ai-glossary.md"
