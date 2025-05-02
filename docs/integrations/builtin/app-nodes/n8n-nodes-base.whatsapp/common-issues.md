---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: WhatsApp Business Cloud node common issues
description: Documentation for common issues and questions in the WhatsApp Business Cloud node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: high
---

# WhatsApp Business Cloud node common issues

Here are some common errors and issues with the [WhatsApp Business Cloud node](/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/index.md) and steps to resolve or troubleshoot them.
พวกนี้คือข้อผิดพลาดและปัญหาที่พบได้บ่อยใน [WhatsApp Business Cloud node](/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/index.md) พร้อมกับขั้นตอนแนะนำการแก้ไขหรือวิเคราะห์ปัญหา.

## Bad request - please check your parameters

This error occurs when WhatsApp Business Cloud rejects your request because of a problem with its parameters. It's common to see this when using the **Send Template** operation if the data you send doesn't match the format of your template.
ข้อผิดพลาดนี้เกิดขึ้นเมื่อ WhatsApp Business Cloud ปฏิเสธคำขอของคุณ เนื่องจากพารามิเตอร์ที่ส่งไปมีปัญหา เห็นได้บ่อยเมื่อใช้ฟังก์ชัน **Send Template** หากข้อมูลที่ส่งไปไม่ตรงกับรูปแบบที่กำหนดใน template

To resolve this issue, review the parameters in your [message template](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343). Pay attention to each parameter's data type and the order they're defined in the template.
ในการแก้ปัญหานี้ ให้ตรวจสอบพารามิเตอร์ใน [message template](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343) โดยใส่ใจในประเภทข้อมูลและลำดับที่แต่ละพารามิเตอร์ถูกกำหนดไว้ใน template

Check the data that n8n is mapping to the template parameters. If you're using expressions to set parameter values, check the input data to make sure each item resolves to a valid value. You may want to use the [Edit Fields (Set) node](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) or [set a fallback value](/code/cookbook/expressions/check-incoming-data.md) to ensure you send a value with the correct format.
ตรวจสอบข้อมูลที่ n8n กำหนดให้กับพารามิเตอร์ของ template หากคุณใช้ expressions เพื่อกำหนดค่าพารามิเตอร์ ตรวจสอบข้อมูลที่รับเข้ามาให้แน่ใจว่าแต่ละค่าถูกแปลงเป็นค่าที่ถูกต้อง คุณอาจต้องใช้ [Edit Fields (Set) node](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) หรือ [set a fallback value](/code/cookbook/expressions/check-incoming-data.md) เพื่อให้แน่ใจว่าค่าที่ส่งไปตรงตามรูปแบบที่ต้องการ

## Working with non-text media

The WhatsApp Business Cloud node can work with non-text messages and media like images, audio, documents, and more.
WhatsApp Business Cloud node สามารถจัดการกับข้อความที่ไม่ใช่ตัวอักษรและสื่ออื่นๆ เช่น รูปภาพ, เสียง, เอกสาร เป็นต้น

If your operation includes a **Input Data Field Name** or **Property Name** parameter, set this to the field name itself rather than referencing the data in an expression.
หากการทำงานของคุณต้องรวมพารามิเตอร์ **Input Data Field Name** หรือ **Property Name** ให้กำหนดเป็นชื่อฟิลด์โดยตรง แทนที่จะอ้างอิงข้อมูลผ่าน expression

For example, if you are trying to send a message with an "Image" **MessageType** and **Take Image From** set to "n8n", set **Input Data Field Name** to a field name like `data` instead of an expression like `{{ $json.input.data }}`.
ตัวอย่างเช่น หากคุณพยายามส่งข้อความในรูปแบบ "Image" โดยมี **MessageType** เป็น "Image" และ **Take Image From** ตั้งเป็น "n8n" ให้ตั้งค่า **Input Data Field Name** เป็นชื่อฟิลด์ เช่น `data` แทนที่จะใช้ expression อย่าง `{{ $json.input.data }}`
