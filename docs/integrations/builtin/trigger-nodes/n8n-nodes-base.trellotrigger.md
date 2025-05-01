---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Trello Trigger node documentation
description: Learn how to use the Trello Trigger node in n8n. Follow technical documentation to integrate Trello Trigger node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Trello Trigger node

[Trello](https://trello.com/){:target=_blank .external-link} คือแอป Kanban ออนไลน์สำหรับจัดการงาน ที่เป็นบริษัทลูกของ Atlassian ผู้ใช้สามารถสร้างบอร์ดงานที่มีหลายคอลัมน์ และย้าย task ระหว่างคอลัมน์ได้

/// note | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/trello.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่ช่วยให้เริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [Trello Trigger integrations](https://n8n.io/integrations/trello-trigger/){:target=_blank .external-link} ของ n8n
///

## Find the Model ID

Model ID คือรหัสของ model ใด ๆ ใน Trello แล้วแต่ use-case เช่น อาจเป็น User ID, List ID ฯลฯ

สำหรับตัวอย่างนี้ List ID จะเป็น Model ID:

1. เปิด Trello board ที่มี list ที่ต้องการ
2. ถ้า list นั้นยังไม่มี card ให้เพิ่ม card เข้าไปก่อน
3. เปิด card แล้วเติม `.json` ต่อท้าย URL จากนั้นกด enter
4. ในไฟล์ JSON จะมี field ชื่อ `idList`
5. คัดลอก `idList` แล้วนำไปวางในช่อง **Model ID** ใน n8n

