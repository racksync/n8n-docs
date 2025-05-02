---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Chat Trigger node common issues 
description: Documentation for common issues and questions in the Chat Trigger node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: high
---

# Chat Trigger node common issues

นี่คือปัญหาและ error ที่พบบ่อยสำหรับ [Chat Trigger node](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md) พร้อมแนวทางแก้ไขหรือวิเคราะห์ปัญหา

## Pass data from a website to an embedded Chat Trigger node

เวลาคุณ [embed](https://www.npmjs.com/package/@n8n/chat) Chat Trigger node ลงในเว็บไซต์ อาจอยากส่งข้อมูลเพิ่มเติมไปที่ Chat Trigger เช่น ส่ง user ID ที่เก็บใน cookie ของเว็บ

ให้ใช้ field `metadata` ใน object JSON ที่ส่งเข้า `createChat` function ใน chat window ฝั่ง embed:

```javascript
createChat({
	webhookUrl: 'YOUR_PRODUCTION_WEBHOOK_URL',
	metadata: {
		'YOUR_KEY': 'YOUR_DATA'
	};
});
```

field `metadata` นี้จะเก็บข้อมูลอะไรก็ได้ และจะไปโผล่ใน output ของ Chat Trigger พร้อมกับข้อมูลอื่นๆ จากนั้นสามารถนำไปใช้ใน node ถัดไปใน workflow ได้ตามปกติด้วย [data processing features](/data/index.md) ของ n8n

## Chat Trigger node doesn't fetch previous messages

ถ้าตั้งค่า Chat Trigger node แล้วเจอปัญหาโหลดข้อความเก่าไม่ได้ หรือขึ้น error `workflow could not be started!` อาจเกิดจากการตั้งค่า session loading ไม่ถูกต้อง

ใน Chat Trigger, option **Load Previous Session** จะดึงข้อความเก่าด้วย `sessionID` ถ้าตั้งเป็น **From memory** แนะนำให้ [เชื่อมต่อ memory node เดียวกัน](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md#load-previous-session) ให้ทั้ง Chat Trigger และ Agent ใน workflow:

1. ใน **Chat Trigger** node ให้ตั้ง **Load Previous Session** เป็น **From Memory** (จะเห็น option นี้ถ้าเปิด chat สาธารณะ)
2. เชื่อม **Simple Memory** node เข้ากับ **Memory** connector
3. เชื่อม **Simple Memory** node เดียวกันเข้ากับ **Memory** connector ของ **Agent**
4. ใน **Simple Memory** node ตั้ง **Session ID** เป็น **Connected Chat Trigger Node**

กรณีที่อาจอยากใช้ memory node แยกกันระหว่าง Chat Trigger กับ Agent คือถ้าต้องการตั้ง **Session ID** ใน memory node เป็น **Define below**

ถ้าดึง session ID จาก expression ต้องแน่ใจว่า expression นั้นใช้ได้กับทุก node ที่เชื่อมต่อกับ memory node นั้น ถ้า expression ใช้ไม่ได้กับบาง node อาจต้องใช้ memory node แยกกันเพื่อจะได้ตั้ง expression session ID ให้เหมาะกับแต่ละ node
