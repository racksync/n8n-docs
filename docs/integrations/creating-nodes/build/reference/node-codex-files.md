---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ไฟล์ Codex ของ Node
description: เอกสารอ้างอิงสำหรับไฟล์ codex ของ node
contentType: reference
---

# Node codex files

ไฟล์ codex จะเก็บ metadata เกี่ยวกับ node ของคุณ ไฟล์นี้จะเป็นไฟล์ JSON ที่อยู่ใน root ของ node ตัวอย่างเช่น [`HttpBin.node.json`](https://github.com/n8n-io/n8n-nodes-starter/blob/master/nodes/HttpBin/HttpBin.node.json){:target=_blank .external-class} ใน n8n starter

ชื่อไฟล์ codex ต้องตรงกับชื่อไฟล์ base ของ node เช่น ถ้าไฟล์ base ของ node ชื่อ `MyNode.node.ts` ไฟล์ codex ก็ต้องชื่อ `MyNode.node.json`

| Parameter | Description |
| -------- | ----------- |
| `node`    | ใส่ชื่อ node โดยต้องขึ้นต้นด้วย `n8n-nodes-base.` เช่น `n8n-nodes-base.openweatherapi` | 
| `nodeVersion` | เวอร์ชันของ node ค่านี้ควรตรงกับ parameter `version` ในไฟล์ node หลักของคุณ เช่น `"1.0"` |
| `codexVersion` | เวอร์ชันของไฟล์ codex ปัจจุบันคือ `"1.0"` |
| `categories` | การตั้งค่าใน array `categories` จะกำหนดว่า n8n จะเพิ่ม node ของคุณไว้ในหมวดหมู่ไหนใน GUI ดูข้อมูลเพิ่มเติมที่ [Node categories](#node-categories) |
| `resources` | object `resources` จะเก็บลิงก์ไปยังเอกสารของ node ของคุณ n8n จะเพิ่มลิงก์ช่วยเหลือให้กับ credentials และ nodes ใน GUI ให้อัตโนมัติ |

## Node categories

คุณสามารถกำหนดหมวดหมู่ (category) ได้มากกว่าหนึ่งหมวดใน configuration JSON ของ node เพื่อช่วยให้ n8n จัด node ของคุณไว้ในหมวดหมู่ที่ถูกต้องใน panel ของ nodes

เลือกจากหมวดหมู่เหล่านี้:

* Data & Storage
* Finance & Accounting
* Marketing & Content
* Productivity
* Miscellaneous
* Sales
* Development
* Analytics
* Communication
* Utility

ต้องใช้ชื่อหมวดหมู่ให้ตรงตามนี้ เช่น `Data & Storage` ไม่ใช่ `data and storage`
