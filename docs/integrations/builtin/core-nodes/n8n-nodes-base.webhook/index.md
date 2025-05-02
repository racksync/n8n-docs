---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Webhook node documentation 
description: Learn how to use the Webhook node in n8n. Follow technical documentation to integrate Webhook node into your workflows.
priority: critical
contentType: [integration, reference]
tags:
  - "webhook set route parameters"
  - "get webhook URL"
  - "call workflow externally"
hide:
  - tags
---

# Webhook node

ใช้ Webhook node เพื่อสร้าง [webhooks](https://en.wikipedia.org/wiki/Webhook){:target=_blank .external-link} ที่สามารถรับข้อมูลจากแอปหรือบริการต่างๆ เมื่อเกิด event ขึ้น Webhook node เป็น trigger node หมายความว่าสามารถใช้เริ่ม workflow ใน n8n ได้เลย ช่วยให้บริการต่างๆ เชื่อมต่อกับ n8n และรัน workflow ได้ทันที

คุณสามารถใช้ Webhook node เป็น trigger ให้ workflow เมื่ออยากรับข้อมูลและรัน workflow ตามข้อมูลที่ได้รับ Webhook node ยังรองรับการส่งข้อมูลที่ workflow ประมวลผลเสร็จแล้วกลับไปด้วย เหมาะสำหรับสร้าง workflow ที่รับข้อมูล ประมวลผล แล้วส่งผลลัพธ์กลับ เหมือน API endpoint

Webhook นี้ช่วยให้ trigger workflow จากบริการที่ไม่มี node trigger เฉพาะใน n8n ได้

## Workflow development process

n8n มี **Webhook URL** แยกสำหรับทดสอบและ production URL สำหรับทดสอบจะมีตัวเลือก **Listen for test event** ดูรายละเอียดเพิ่มเติมที่ [Workflow development](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development.md) สำหรับวิธีสร้าง ทดสอบ และเปลี่ยน Webhook node ไป production

## Node parameters

ใช้ parameter เหล่านี้เพื่อ config node ของคุณ

### Webhook URLs

Webhook node จะมี **Webhook URLs** สองแบบ: test และ production โดย n8n จะแสดง URL เหล่านี้ที่ด้านบนของ panel node

เลือก **Test URL** หรือ **Production URL** เพื่อสลับดู URL ที่ต้องการ

<figure markdown="span">
![Sample Webhook URLs in the Webhook node's Parameters tab display a Test URL and Production URL](/_images/integrations/builtin/core-nodes/webhook/webhook-urls.png)
<figcaption>ตัวอย่าง Webhook URLs ใน Parameters tab ของ Webhook node</figcaption>
</figure>

* **Test**: n8n จะ register test webhook เมื่อเลือก **Listen for Test Event** หรือ **Test workflow** ถ้า workflow ยังไม่ active เมื่อเรียก webhook URL นี้ n8n จะแสดงข้อมูลใน workflow
* **Production**: n8n จะ register production webhook เมื่อคุณ activate workflow เมื่อใช้ production URL n8n จะไม่แสดงข้อมูลใน workflow แต่ยังดูข้อมูล workflow ได้ใน production execution โดยไปที่ **Executions** tab แล้วเลือก execution ที่ต้องการดู

### HTTP Method

Webhook node รองรับ [HTTP Request Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods){:target=_blank .external-link} มาตรฐาน:

* DELETE
* GET
* HEAD
* PATCH
* POST
* PUT

    /// note | Webhook max payload
	ขนาด payload สูงสุดของ webhook คือ 16MB
    ถ้า self-host n8n สามารถเปลี่ยนได้โดยใช้ [endpoint environment variable](/hosting/configuration/environment-variables/endpoints.md) `N8N_PAYLOAD_SIZE_MAX`
	///	

### Path

โดยปกติ field นี้จะมี path ของ webhook URL ที่สุ่มมาให้ เพื่อป้องกันชนกับ webhook node อื่น

คุณสามารถกำหนด path เองได้ รวมถึงใส่ route parameters เช่น ถ้าใช้ n8n สร้าง prototype API แล้วอยากได้ endpoint URL ที่แน่นอน

**Path** field รองรับรูปแบบเหล่านี้:

- `/:variable`
- `/path/:variable`
- `/:variable/path`
- `/:variable1/path/:variable2`
- `/:variable1/:variable2`

### Supported authentication methods

คุณสามารถบังคับให้ service ที่เรียก webhook URL ต้อง auth ก่อน โดยเลือกวิธี auth ได้ดังนี้:

- Basic auth
- Header auth
- JWT auth
- None

ดูรายละเอียดการตั้งค่าแต่ละ credential ได้ที่ [Webhook credentials](/integrations/builtin/credentials/webhook.md)

### Respond

* **Immediately**: Webhook node จะส่ง response code และข้อความ **Workflow got started**
* **When Last Node Finishes**: Webhook node จะส่ง response code และข้อมูล output จาก node สุดท้ายที่รันใน workflow
* **Using 'Respond to Webhook' Node**: Webhook node จะตอบกลับตามที่กำหนดใน [Respond to Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md) node

### Response Code

ปรับแต่ง [HTTP response code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status){:target=_blank .external-link} ที่ Webhook node จะส่งกลับเมื่อรันสำเร็จ เลือกจาก code ที่ใช้บ่อยหรือกำหนดเองก็ได้

### Response Data

เลือกข้อมูลที่จะใส่ใน response body:

* **All Entries**: Webhook จะส่งข้อมูลทั้งหมดของ node สุดท้ายใน array
* **First Entry JSON**: Webhook จะส่งข้อมูล JSON ของ entry แรกของ node สุดท้ายในรูปแบบ JSON object
* **First Entry Binary**: Webhook จะส่งข้อมูล binary ของ entry แรกของ node สุดท้ายเป็นไฟล์ binary
* **No Response Body**: Webhook จะส่ง response โดยไม่มี body

ใช้ได้เฉพาะกับ **Respond > When Last Node Finishes**

## Node options

เลือก **Add Option** เพื่อดูตัวเลือก config เพิ่มเติม ตัวเลือกที่มีจะแตกต่างกันตาม parameter ที่ตั้งไว้ ดูตารางด้านล่างสำหรับ option ที่ใช้ได้

* **Allowed Origins (CORS)**: กำหนด domain ที่อนุญาต cross-origin ได้ ใส่ URL คั่นด้วย comma หรือใช้ `*` (default) เพื่ออนุญาตทุก origin
* **Binary Property**: เปิด option นี้เพื่อให้ Webhook node รับ binary data เช่น รูปภาพหรือไฟล์เสียง ใส่ชื่อ binary property ที่จะเก็บไฟล์
* **Ignore Bots**: ไม่รับ request จาก bot เช่น link previewer หรือ web crawler
* **IP(s) Whitelist**: จำกัดเฉพาะ IP ที่อนุญาตให้เรียก Webhook trigger URL ได้ ใส่ IP คั่นด้วย comma ถ้าเว้นว่างจะอนุญาตทุก IP
* **No Response Body**: เปิด option นี้เพื่อไม่ให้ n8n ส่ง body กลับใน response
* **Raw Body**: ระบุว่า Webhook node จะรับข้อมูลแบบ raw เช่น JSON หรือ XML
* **Response Content-Type**: เลือก format สำหรับ webhook body
* **Response Data**: ส่งข้อมูล custom ใน response
* **Response Headers**: ส่ง header เพิ่มใน Webhook response ดูรายละเอียด [MDN Web Docs | Response header](https://developer.mozilla.org/en-US/docs/Glossary/Response_header){:target=_blank .external-link}
* **Property Name**: โดยปกติ n8n จะส่งข้อมูลทั้งหมด สามารถเลือกส่งเฉพาะ key ใน JSON ได้

| Option | Required node configuration |
| ------ | --------------------------- | 
| Allowed Origins (CORS) | Any |
| Binary Property | Either: <br />HTTP Method > POST <br /> HTTP Method > PATCH <br /> HTTP Method > PUT |
| Ignore Bots | Any |
| IP(s) Whitelist | Any |
| Property Name | Both: <br /> Respond > When Last Node Finishes <br /> Response Data > First Entry JSON |
| No Response Body | Respond > Immediately |
| Raw Body | Any |
| Response Code | Any except Respond > Using 'Respond to Webhook' Node |
| Response Content-Type | Both: <br /> Respond > When Last Node Finishes <br /> Response Data > First Entry JSON |
| Response Data | Respond > Immediately |
| Response Headers | Any |

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'webhook') ]]

## Common issues

สำหรับคำถามหรือปัญหาที่พบบ่อยและวิธีแก้ไข ดูที่ [Common issues](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues.md)
