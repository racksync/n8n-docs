---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ LangChain Code node
description: วิธีใช้งาน LangChain Code node ใน n8n สำหรับรันโค้ด LangChain แบบกำหนดเอง
contentType: [integration, reference]
priority: medium
---

# LangChain Code node

ใช้ LangChain Code node เพื่อ import LangChain ซึ่งหมายความว่าหากมีฟังก์ชันที่คุณต้องการแต่ n8n ยังไม่ได้สร้าง node ให้ คุณก็ยังสามารถใช้งานได้ โดยการกำหนดค่า LangChain Code node connectors คุณสามารถใช้มันเป็น node ปกติ, root node หรือ sub-node ได้

ในหน้านี้ คุณจะพบ node parameters, คำแนะนำในการกำหนดค่า node และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Not available on Cloud
Node นี้มีให้ใช้งานเฉพาะบน n8n แบบ self-hosted เท่านั้น
///

## Node parameters

### Add Code

เพิ่ม custom code ของคุณ เลือกโหมด **Execute** หรือ **Supply Data** คุณสามารถใช้ได้เพียงโหมดเดียว

ต่างจาก [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md) LangChain Code node ไม่รองรับ Python

*   **Execute**: ใช้ LangChain Code node เหมือนกับ Code node ของ n8n เอง ซึ่งจะรับ input data จาก workflow, ประมวลผล และส่งคืนเป็น node output โหมดนี้ต้องการ main input และ output คุณต้องสร้างการเชื่อมต่อเหล่านี้ใน **Inputs** และ **Outputs**
*   **Supply Data**: ใช้ LangChain Code node เป็น sub-node โดยส่งข้อมูลไปยัง root node ซึ่งจะใช้ output อื่นที่ไม่ใช่ main

โดยค่าเริ่มต้น คุณไม่สามารถโหลด built-in หรือ external modules ใน node นี้ได้ ผู้ใช้ self-hosted สามารถ [เปิดใช้งาน built-in และ external modules](/hosting/configuration/configuration-methods.md) ได้

### Inputs

เลือกประเภท input

Main input คือ connector ปกติที่พบใน n8n workflows ทั้งหมด หากคุณมี main input และ output ที่ตั้งค่าไว้ใน node จำเป็นต้องใช้ code แบบ **Execute**

### Outputs

เลือกประเภท output

Main output คือ connector ปกติที่พบใน n8n workflows ทั้งหมด หากคุณมี main input และ output ที่ตั้งค่าไว้ใน node จำเป็นต้องใช้ code แบบ **Execute**

## Node inputs and outputs configuration

โดยการกำหนดค่า LangChain Code node connectors (inputs และ outputs) คุณสามารถใช้มันเป็น app node, root node หรือ sub-node ได้

![Screenshot of a workflow with four LangChain nodes, configured as different node types](/_images/integrations/builtin/cluster-nodes/langchaincode/create-node-types.png)

| Node type | Inputs | Outputs | Code mode |
| --------- | ------ | ------- | --------- |
| App node คล้ายกับ [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md) | Main | Main | Execute |
| Root node | Main; อย่างน้อยหนึ่งประเภทอื่น | Main | Execute |
| Sub-node | - | ประเภทอื่นที่ไม่ใช่ main ต้องตรงกับประเภท input ที่คุณต้องการเชื่อมต่อ | Supply Data |
| Sub-node พร้อม sub-nodes | ประเภทอื่นที่ไม่ใช่ main | ประเภทอื่นที่ไม่ใช่ main ต้องตรงกับประเภท input ที่คุณต้องการเชื่อมต่อ | Supply Data |

## Built-in methods

n8n มี methods เหล่านี้เพื่อให้ง่ายต่อการทำงานทั่วไปใน LangChain Code node

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/langchaincode/builtin-methods.md"

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'langchain-code') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"
--8<-- "_glossary/ai-glossary.md"
