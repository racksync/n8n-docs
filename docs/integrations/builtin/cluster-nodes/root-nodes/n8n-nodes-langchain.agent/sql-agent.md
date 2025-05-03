---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ SQL AI Agent node
description: วิธีใช้งาน SQL Agent ของ AI Agent node ใน n8n สำหรับถาม-ตอบข้อมูลจากฐานข้อมูล SQL
contentType: [integration, reference]
priority: critical
---

# SQL AI Agent node

SQL Agent ใช้ฐานข้อมูล SQL เป็นแหล่งข้อมูล มันสามารถเข้าใจคำถามภาษาธรรมชาติ แปลงเป็น SQL queries ดำเนินการ queries และนำเสนอผลลัพธ์ในรูปแบบที่ใช้งานง่าย Agent นี้มีประโยชน์สำหรับการสร้าง interfaces ภาษาธรรมชาติไปยังฐานข้อมูล

อ้างอิง [AI Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ AI Agent node เอง

## Node parameters

กำหนดค่า SQL Agent โดยใช้ parameters ต่อไปนี้

### Data Source

เลือกฐานข้อมูลที่จะใช้เป็นแหล่งข้อมูลสำหรับ node ตัวเลือก ได้แก่:

* **MySQL**: เลือกตัวเลือกนี้เพื่อใช้ฐานข้อมูล MySQL
    * เลือก **Credential for MySQL** ด้วย
* **SQLite**: เลือกตัวเลือกนี้เพื่อใช้ฐานข้อมูล SQLite
    * คุณต้องเพิ่ม [Read/Write File From Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md) node ก่อน Agent เพื่ออ่านไฟล์ SQLite ของคุณ
    * ป้อนชื่อ **Input Binary Field** ของไฟล์ SQLite ของคุณที่มาจาก Read/Write File From Disk node ด้วย
* **Postgres**: เลือกตัวเลือกนี้เพื่อใช้ฐานข้อมูล Postgres
    * เลือก **Credential for Postgres** ด้วย

/// warning | Postgres and MySQL Agents
หากคุณใช้ [Postgres](/integrations/builtin/credentials/postgres.md) หรือ [MySQL](/integrations/builtin/credentials/mysql.md) agent นี้ไม่รองรับ credential tunnel options
///

### Prompt

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/prompt.md"

## Node options

ปรับแต่งพฤติกรรมของ SQL Agent node โดยใช้ options เหล่านี้:

### Ignored Tables

หากคุณต้องการให้ node ละเว้นตารางใดๆ จากฐานข้อมูล ให้ป้อนรายการตารางที่คั่นด้วยจุลภาคที่คุณต้องการให้ละเว้น

หากปล่อยว่างไว้ agent จะไม่ละเว้นตารางใดๆ

### Include Sample Rows

ป้อนจำนวนแถวตัวอย่างที่จะรวมไว้ใน prompt ที่ส่งไปยัง agent ค่าเริ่มต้นคือ `3`

แถวตัวอย่างช่วยให้ agent เข้าใจ schema ของฐานข้อมูล แต่ก็เพิ่มจำนวน tokens ที่ใช้ด้วย

### Included Tables

หากคุณต้องการรวมเฉพาะตารางที่ระบุจากฐานข้อมูล ให้ป้อนรายการตารางที่คั่นด้วยจุลภาคที่จะรวม

หากปล่อยว่างไว้ agent จะรวมทุกตาราง

### Prefix Prompt

ป้อนข้อความที่คุณต้องการส่งไปยัง agent ก่อนข้อความ **Prompt** ข้อความเริ่มต้นนี้สามารถให้บริบทและคำแนะนำเพิ่มเติมแก่ agent เกี่ยวกับสิ่งที่สามารถทำได้และทำไม่ได้ และวิธีการจัดรูปแบบการตอบกลับ

n8n เติมฟิลด์นี้ด้วยตัวอย่าง

### Suffix Prompt

ป้อนข้อความที่คุณต้องการส่งไปยัง agent หลังจากข้อความ **Prompt**

LangChain expressions ที่มีอยู่:

* `{chatHistory}`: ประวัติข้อความในการสนทนานี้ มีประโยชน์สำหรับการรักษาบริบท
* `{input}`: มี prompt ของผู้ใช้
* `{agent_scratchpad}`: ข้อมูลที่ต้องจำสำหรับการวนซ้ำครั้งต่อไป

n8n เติมฟิลด์นี้ด้วยตัวอย่าง

### Limit

ป้อนจำนวนผลลัพธ์สูงสุดที่จะส่งคืน

ค่าเริ่มต้นคือ `10`

## Templates and examples

อ้างอิงส่วน [Templates and examples](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md#templates-and-examples) ของ AI Agent node หลัก

## Common issues

สำหรับคำถามหรือปัญหาทั่วไปและแนวทางแก้ไขที่แนะนำ โปรดดูที่ [Common issues](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md)

--8<-- "_glossary/ai-glossary.md"
