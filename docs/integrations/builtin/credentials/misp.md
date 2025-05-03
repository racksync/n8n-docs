---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลยืนยันตัวตน MISP
description: เอกสารสำหรับ MISP credentials ใช้เพื่อยืนยันตัวตน MISP ใน n8n
contentType: [integration, reference]
---

# MISP credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [MISP](/integrations/builtin/app-nodes/n8n-nodes-base.misp.md)

## Prerequisites

ติดตั้งและรัน instance ของ [MISP](https://misp.github.io/MISP/){:target=_blank .external-link}

## Supported authentication methods

- API key

## Related resources

อ้างอิง [MISP's Automation API documentation](https://www.circl.lu/doc/misp/automation){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API key

ในการกำหนดค่า credential นี้ คุณจะต้องมี:

- **API Key**: ใน MISP สิ่งเหล่านี้เรียกว่า Automation keys รับ automation key จาก **Event Actions > Automation** อ้างอิงเอกสาร [MISP's automation keys documentation](https://www.circl.lu/doc/misp/automation/#automation-key){:target=_blank .external-link} สำหรับคำแนะนำในการสร้าง keys เพิ่มเติม
- **Base URL**: URL ของ MISP ของคุณ
- เลือกว่าจะ **Allow Unauthorized Certificates**: หากเปิดใช้งาน credential จะเชื่อมต่อแม้ว่าการตรวจสอบใบรับรอง SSL จะล้มเหลว

