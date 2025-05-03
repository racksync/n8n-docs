---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ดึงข้อมูลจากไฟล์ (Extract From File)
description: คู่มือ Extract From File node สำหรับแปลงไฟล์เป็นข้อมูลใน n8n
contentType: [integration, reference]
priority: high
---

# Extract From File

workflow ใน n8n มักจะรับไฟล์เข้ามา ไม่ว่าจะจาก [HTTP Request node][] (สำหรับไฟล์ที่ดึงจากเว็บ), [Webhook Node][] (สำหรับไฟล์ที่ส่งมาจากที่อื่น) หรือจาก local source ข้อมูลที่ได้มามักเป็น binary format เช่น spreadsheet หรือ PDF

Extract From File node จะ extract ข้อมูลจากไฟล์ binary format แล้วแปลงเป็น JSON เพื่อให้ workflow จัดการต่อได้ง่าย ถ้าอยากแปลง JSON กลับเป็น binary file ดูที่ [Convert to File](/integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md) node

## Operations

เลือก **Operations** เพื่อระบุ format ของไฟล์ต้นทางที่จะ extract ข้อมูล

- **Extract From CSV**: ไฟล์ Comma Separated Values ใช้สำหรับข้อมูลตาราง
- **Extract From HTML**: extract field จากไฟล์ HTML
- **Extract From JSON**: extract JSON data จาก binary file
- **Extract From ICS**: extract field จากไฟล์ iCalendar
- **Extract From ODS**: extract field จากไฟล์ ODS spreadsheet
- **Extract From PDF**: extract field จากไฟล์ PDF
- **Extract From RTF**: extract field จากไฟล์ Rich Text Format
- **Extract From Text File**: extract field จากไฟล์ text ธรรมดา
- **Extract From XLS**: extract field จากไฟล์ Excel (format เก่า)
- **Extract From XLSX**: extract field จากไฟล์ Excel
- **Move File to Base64 String**: แปลง binary data เป็น [base64][] string

## Example workflow

ตัวอย่างนี้ใช้ Webhook node เป็น trigger เมื่อมีไฟล์ CSV ส่งมาที่ webhook address ข้อมูลไฟล์จะถูกส่งต่อให้ Extract From File node

[[ workflowDemo("file:///integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile/webhook-example.json") ]]

ตั้งค่าเป็น 'Extract from CSV' node จะ output ข้อมูลเป็น JSON 'row' object:

```
{
  "row": {
  "0": "apple",
  "1": "1",
  "2": "2",
  "3": "3"
  }
  ...
```

/// tip | Receiving files with a webhook
เลือก **Add Options** ของ Webhook Node แล้วเปิด **Raw body** เพื่อให้ node ส่ง output เป็น binary file ที่ node ถัดไปต้องการ
///

## Node parameters

### Input Binary Field

ใส่ชื่อ field ใน input data ที่เก็บไฟล์ binary ค่า default คือ 'data'

### Destination Output Field

ใส่ชื่อ field ใน output ที่จะเก็บข้อมูลที่ extract ได้

parameter นี้ใช้ได้เฉพาะกับ operation เหล่านี้:

- Extract From JSON
- Extract From ICS
- Extract From Text File
- Move File to Base64 String

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'extract-from-file') ]]

[HTTP Request Node]: /integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md
[Webhook Node]: /integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md
[base64]: https://datatracker.ietf.org/doc/html/rfc4648#section-4
