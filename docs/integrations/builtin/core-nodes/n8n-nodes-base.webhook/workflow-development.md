---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Webhook node workflow development documentation
description: Learn how to build, test, and use the Webhook node in your workflows in n8n.
priority: critical
contentType: howto
---

# Workflow development

[Webhook node](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md) จะทำงานแตกต่างจาก core node อื่นๆ เล็กน้อย n8n แนะนำให้ทำตามขั้นตอนนี้สำหรับการสร้าง ทดสอบ และใช้งาน Webhook node ใน production

n8n จะสร้าง **Webhook URLs** ให้แต่ละ Webhook node สองแบบ: **Test URL** และ **Production URL**

## Build and test workflows

ตอนสร้างหรือทดสอบ workflow ให้ใช้ **Test** webhook URL

การใช้ test webhook จะช่วยให้คุณดูข้อมูลที่เข้ามาใน editor UI ได้ เหมาะสำหรับ debug ให้เลือก **Listen for test event** เพื่อ register webhook ก่อนส่งข้อมูลไปยัง test webhook โดย test webhook จะ active อยู่ 120 วินาที

ถ้าใช้ Webhook node บน localhost ใน [self-hosted](/hosting/index.md) n8n instance ให้รัน n8n ใน tunnel mode:

* [npm with tunnel](/hosting/installation/npm.md#n8n-with-tunnel)
* [Docker with tunnel](/hosting/installation/docker.md#n8n-with-tunnel)

<video src="/_video/integrations/builtin/core-nodes/webhook/webhook-node-intro.mp4" controls width="100%"></video>

## Production workflows

เมื่อ workflow พร้อมใช้งานแล้ว ให้เปลี่ยนไปใช้ **Production** webhook URL จากนั้น activate workflow ได้เลย n8n จะรัน workflow อัตโนมัติเมื่อมี external service เรียก webhook URL นี้

ถ้าใช้ Production webhook ต้องแน่ใจว่าได้ save และ activate workflow แล้ว ข้อมูลที่ผ่าน webhook จะไม่แสดงใน editor UI เมื่อใช้ production webhook

ดูรายละเอียดเพิ่มเติมที่ [Create a workflow](/workflows/create.md) สำหรับการ activate workflow
