---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Chat Trigger node documentation
description: เรียนรู้วิธีใช้ Chat Trigger node ใน n8n ทำตามเอกสารทางเทคนิคเพื่อรวม Chat Trigger node เข้ากับ workflow ของคุณ
priority: critical
---

# Chat Trigger node

ใช้ Chat Trigger node เวลาสร้าง workflow AI สำหรับ chatbot หรือ chat interface อื่นๆ สามารถตั้งค่าว่าผู้ใช้จะเข้าถึง chat ได้อย่างไร จะใช้ interface ที่ n8n มีให้ หรือจะใช้ของตัวเองก็ได้ สามารถเพิ่ม authentication ได้ด้วย

คุณต้องเชื่อมต่อ agent หรือ chain [root node](/integrations/builtin/cluster-nodes/root-nodes/index.md) อย่างใดอย่างหนึ่ง

/// warning | Workflow execution usage
ทุกข้อความที่ส่งมาที่ Chat Trigger จะเป็นการรัน workflow หนึ่งครั้ง หมายความว่าถ้ามีการสนทนา 1 ครั้ง ผู้ใช้ส่ง 10 ข้อความ จะใช้ execution quota ไป 10 ครั้ง ตรวจสอบแผนการชำระเงินของคุณสำหรับรายละเอียด execution allowance
///

/// note | Manual Chat trigger
node นี้มาแทน Manual Chat Trigger node ตั้งแต่เวอร์ชัน 1.24.0
///

## Node parameters

### Make Chat Publicly Available

ตั้งค่าว่าจะให้ chat นี้เปิดสาธารณะ (เปิด) หรือให้ใช้ได้เฉพาะผ่าน manual chat interface (ปิด)

แนะนำให้ปิดไว้ตอนสร้าง workflow และเปิดเมื่อพร้อมให้ผู้ใช้เข้าถึง chat

### Mode

เลือกวิธีที่ผู้ใช้จะเข้าถึง chat มีตัวเลือกดังนี้:

* **Hosted Chat**: ใช้ interface chat ของ n8n เอง แนะนำสำหรับผู้ใช้ทั่วไป เพราะตั้งค่าได้จาก [node options](#node-options) โดยไม่ต้องตั้งค่าอะไรเพิ่ม
* **Embedded Chat**: ตัวเลือกนี้ต้องสร้าง chat interface เอง สามารถใช้ [chat widget ของ n8n](https://www.npmjs.com/package/@n8n/chat){:target=_blank .external-link} หรือสร้างเองก็ได้ interface ของคุณต้องเรียก webhook URL ที่แสดงใน **Chat URL** ของ node

### Authentication

เลือกว่าจะจำกัดการเข้าถึง chat หรือไม่ มีตัวเลือกดังนี้:

* **None**: ไม่มี authentication ใครก็ใช้ chat ได้
* **Basic Auth**: ใช้ basic authentication
	* เลือกหรือสร้าง **Credential for Basic Auth** พร้อม username และ password ทุกคนต้องใช้ username/password เดียวกัน
* **n8n User Auth**: เฉพาะผู้ใช้ที่ login n8n เท่านั้นที่ใช้ chat ได้

### Initial Message(s)

parameter นี้จะมีเฉพาะถ้าใช้ **Hosted Chat** ใช้ตั้งค่าข้อความที่จะแสดงเมื่อผู้ใช้เข้าหน้า chat

## Node options

option ที่มีให้เลือกขึ้นกับ chat mode

### Hosted chat options

#### Allowed Origin (CORS)

ตั้งค่า origin ที่เข้าถึง chat URL ได้ ใส่ URL ที่อนุญาตแบบ comma-separated

ใช้ `*` (default) เพื่ออนุญาตทุก origin

#### Input Placeholder, Title, and Subtitle

ใส่ข้อความสำหรับแต่ละ element ใน chat interface

??? Details "View screenshot"
	![Customizable text elements](/_images/integrations/builtin/core-nodes/chat-trigger/hosted-text-elements.png)

#### Load Previous Session

เลือกว่าจะโหลดข้อความจาก session ก่อนหน้าหรือไม่

ถ้าเลือก option อื่นที่ไม่ใช่ **Off** ต้องเชื่อมต่อ Chat trigger และ Agent ที่ใช้กับ memory sub-node ตัว memory connector จะโผล่ใน Chat trigger เมื่อเลือก **Load Previous Session** เป็น **From Memory** แนะนำให้เชื่อมต่อ Chat trigger และ Agent กับ memory sub-node เดียวกัน เพื่อให้ข้อมูลตรงกัน

??? Details "View screenshot"
	![Connect nodes to memory](/_images/integrations/builtin/core-nodes/chat-trigger/connect-memory.png)

#### Response Mode

ใช้ option นี้ถ้าสร้าง workflow ที่มี node ต่อท้าย agent หรือ chain ที่รับผิดชอบ chat เลือกได้ว่า:

* **When Last Node Finishes**: Chat Trigger node จะส่ง response code และข้อมูล output จาก node สุดท้ายที่รันใน workflow
* **Using 'Respond to Webhook' Node**: Chat Trigger node จะตอบกลับตามที่กำหนดใน [Respond to Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md) node

#### Require Button Click to Start Chat

ตั้งค่าว่าจะแสดงปุ่ม **New Conversation** ใน chat interface (เปิด) หรือไม่ (ปิด)

??? Details "View screenshot"
	![New Conversation button](/_images/integrations/builtin/core-nodes/chat-trigger/new-conversation-button.png)


### Embedded chat options

#### Allowed Origin (CORS)

ตั้งค่า origin ที่เข้าถึง chat URL ได้ ใส่ URL ที่อนุญาตแบบ comma-separated

ใช้ `*` (default) เพื่ออนุญาตทุก origin

#### Load Previous Session

เลือกว่าจะโหลดข้อความจาก session ก่อนหน้าหรือไม่

ถ้าเลือก option อื่นที่ไม่ใช่ **Off** ต้องเชื่อมต่อ Chat trigger และ Agent ที่ใช้กับ memory sub-node ตัว memory connector จะโผล่ใน Chat trigger เมื่อเลือก **Load Previous Session** เป็น **From Memory** แนะนำให้เชื่อมต่อ Chat trigger และ Agent กับ memory sub-node เดียวกัน เพื่อให้ข้อมูลตรงกัน

??? Details "View screenshot"
	![Connect nodes to memory](/_images/integrations/builtin/core-nodes/chat-trigger/connect-memory.png)

#### Response Mode

ใช้ option นี้ถ้าสร้าง workflow ที่มี node ต่อท้าย agent หรือ chain ที่รับผิดชอบ chat เลือกได้ว่า:

* **When Last Node Finishes**: Chat Trigger node จะส่ง response code และข้อมูล output จาก node สุดท้ายที่รันใน workflow
* **Using 'Respond to Webhook' Node**: Chat Trigger node จะตอบกลับตามที่กำหนดใน [Respond to Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md) node

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'chat-trigger') ]]

## Related resources

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

## Set the chat response manually

คุณต้องตั้งค่า chat response เองในกรณีที่ไม่ต้องการส่ง output ของ Agent หรือ Chain node ตรงๆ ให้ user แต่ต้องการนำ output ไปปรับแต่งหรือทำอย่างอื่นก่อนส่งกลับ

ใน workflow พื้นฐาน Agent และ Chain node จะ output parameter ชื่อ `output` หรือ `text` แล้ว Chat trigger จะส่งค่าของ parameter นี้เป็น chat response

ถ้าต้องการสร้าง response เอง ต้องสร้าง parameter ชื่อ `text` หรือ `output` ถ้าใช้ชื่ออื่น Chat trigger จะส่ง object ทั้งก้อนเป็น response ไม่ใช่แค่ value

## Common issues

สำหรับคำถามหรือปัญหาที่พบบ่อยและวิธีแก้ไข ดูที่ [Common Issues](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues.md)
