---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Airtop node documentation
description: Learn how to use the Airtop node in n8n. Follow technical documentation to integrate Airtop node into your workflows.
contentType: [integration, reference]
---

# Airtop node

ใช้ Airtop node เพื่อทำงานอัตโนมัติใน Airtop และผสานรวม Airtop กับแอปพลิเคชันอื่นๆ n8n มีการรองรับฟีเจอร์หลากหลายของ Airtop ในตัว ช่วยให้คุณสามารถควบคุม web browser บนคลาวด์สำหรับงานต่างๆ เช่น การ query, การ scrape, และการโต้ตอบกับหน้าเว็บ

ในหน้านี้ คุณจะพบรายการ operations ที่ Airtop node รองรับ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

///  note  | Credentials
อ้างอิง [Airtop credentials](/integrations/builtin/credentials/airtop.md) สำหรับคำแนะนำในการตั้งค่าการยืนยันตัวตน
///


## Operations

* Session
    * Create session
    * Save profile on termination
    * Terminate session
* Window
    * Create a new browser window
    * Load URL
    * Take screenshot
    * Close window
* Extraction
    * Query page
    * Query page with pagination
    * Smart scrape page
* Interaction
    * Click an element
    * Hover on an element
    * Type


## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'airtop') ]]


## Related resources

อ้างอิง [เอกสารของ Airtop](https://docs.airtop.ai/api-reference/airtop-api) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

ติดต่อ [ฝ่ายสนับสนุนของ Airtop](https://docs.airtop.ai/guides/misc/support) เพื่อขอความช่วยเหลือหรือสร้างคำขอฟีเจอร์

## Node reference

### Create a session and window

สร้าง Airtop browser session เพื่อรับ **Session ID** จากนั้นใช้ ID นี้เพื่อสร้างหน้าต่างเบราว์เซอร์ใหม่ หลังจากนี้ คุณสามารถใช้ operation การดึงข้อมูล (extraction) หรือการโต้ตอบ (interaction) ใดๆ ก็ได้

### Extract content

ดึงเนื้อหาจาก web browser โดยใช้ operations เหล่านี้:

- **Query page**: ดึงข้อมูลจากหน้าต่างปัจจุบัน
- **Query page with pagination**: ดึงข้อมูลจากหน้าที่มี pagination หรือ infinite scrolling
- **Smart scrape page**: รับเนื้อหาของหน้าต่างเป็น markdown

รับการตอบกลับเป็น JSON โดยใช้พารามิเตอร์ **JSON Output Schema** ใน query operations

### Interacting with pages

คลิก, วางเมาส์เหนือ (hover), หรือพิมพ์บน elements โดยอธิบาย element ที่คุณต้องการโต้ตอบด้วย

### Terminate a session

สิ้นสุด session ของคุณเพื่อประหยัดทรัพยากร Sessions จะถูกยุติโดยอัตโนมัติตาม **Idle Timeout** ที่ตั้งค่าไว้ใน operation **Create Session** หรือสามารถยุติด้วยตนเองโดยใช้ operation **Terminate Session**
