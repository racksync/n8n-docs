---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ตรวจสอบความปลอดภัย
description: "รันการตรวจสอบความปลอดภัยบน n8n instance ของคุณ"
contentType: howto
---

# Security audit

คุณสามารถรัน security audit บน n8n instance ของคุณ เพื่อเช็คปัญหาด้านความปลอดภัยที่พบบ่อย

## Run an audit

สามารถรัน audit ได้หลายวิธี: ผ่าน CLI, public API หรือใช้ n8n node

### CLI

รันคำสั่ง `n8n audit`

### API

ส่ง `POST` ไปที่ endpoint `/audit` โดยต้อง authenticate เป็น instance owner

### n8n node

เพิ่ม [n8n node](/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md) ใน workflow ของคุณ เลือก **Resource** > **Audit** และ **Operation** > **Generate**

## Report contents

audit จะสร้างรายงานความเสี่ยง 5 ประเภท

### Credentials

รายงานนี้จะแสดง:

* Credentials ที่ไม่ได้ใช้ใน workflow ไหนเลย
* Credentials ที่ไม่ได้ใช้ใน workflow ที่ active
* Credentials ที่ไม่ได้ใช้ใน workflow ที่ active ล่าสุด

### Database

รายงานนี้จะแสดง:

* Expressions ที่ใช้ใน field **Execute Query** ของ SQL nodes
* Expressions ที่ใช้ใน field **Query Parameters** ของ SQL nodes
* Field **Query Parameters** ที่ไม่ได้ใช้ใน SQL nodes

### File system

รายงานนี้จะแสดง nodes ที่มีการเข้าถึง file system

### Nodes

รายงานนี้จะแสดง:

* Official risky nodes คือ nodes ที่ built-in มากับ n8n ซึ่งสามารถใช้รันโค้ดใดๆ บน host system ได้ เสี่ยงต่อการโดนโจมตี ดูรายชื่อได้ที่ [n8n code | Audit constants](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/security-audit/constants.ts#L51){:target=_blank .external-link} ใน `OFFICIAL_RISKY_NODE_TYPES`
* Community nodes
* Custom nodes

### Instance

รายงานนี้จะแสดง:

* Webhooks ที่ไม่ได้ป้องกันใน instance
* Security settings ที่ยังไม่ได้ตั้งค่า
* เช็คว่า instance ของคุณเป็นเวอร์ชันล่าสุดหรือไม่
