---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ WhatsApp Trigger node
description: วิธีใช้ WhatsApp Trigger node ใน n8n เพื่อเชื่อมต่อ WhatsApp กับ workflow ของคุณ
contentType: [integration, reference]
priority: high
---

# WhatsApp Trigger node

ใช้ WhatsApp Trigger node เพื่อตอบสนองต่อ event ต่างๆ ใน WhatsApp และเชื่อมต่อ WhatsApp กับแอปอื่นๆ ได้ n8n รองรับ event ของ WhatsApp หลากหลาย เช่น account, message และ phone number events

ในหน้านี้ คุณจะเห็นรายการ event ที่ WhatsApp Trigger node สามารถตอบสนองได้ พร้อมลิงก์ไปยัง resource อื่นๆ

///  note  | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/whatsapp.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่ช่วยให้เริ่มต้นได้ง่ายขึ้น ดูได้ที่ [WhatsApp integrations ของ n8n](https://n8n.io/integrations/whatsapp-trigger/){:target=_blank .external-link}
///

## Events

* Account Review Update
* Account Update
* Business Capability Update
* Message Template Quality Update
* Message Template Status Update
* Messages
* Phone Number Name Update
* Phone Number Quality Update
* Security
* Template Category Update

## Related resources

n8n มี app node สำหรับ WhatsApp ด้วย ดูเอกสาร node ได้ [ที่นี่](/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/index.md)

ดู [example workflows และเนื้อหาอื่นๆ ที่เกี่ยวข้อง](https://n8n.io/integrations/whatsapp-trigger/){:target=_blank .external-link} บนเว็บไซต์ n8n

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ API ของ WhatsApp ได้ที่ [WhatsApp's documentation](https://developers.facebook.com/docs/whatsapp/cloud-api){:target=_blank .external-link}

## Common issues

นี่คือตัวอย่างปัญหาที่พบบ่อยกับ WhatsApp Trigger node และวิธีแก้ไขหรือแนวทางการตรวจสอบ

### Workflow only works in testing or production

WhatsApp อนุญาตให้ลงทะเบียน webhook ได้แค่หนึ่งอันต่อแอปเท่านั้น หมายความว่า ทุกครั้งที่คุณสลับจากการใช้ testing URL ไป production URL (หรือกลับกัน) WhatsApp จะเขียนทับ webhook URL ที่ลงทะเบียนไว้

คุณอาจเจอปัญหานี้ถ้าพยายามทดสอบ workflow ที่เปิดใช้งานใน production อยู่ WhatsApp จะส่ง event ไปแค่ webhook URL เดียว อีกอันจะไม่ได้รับ event

วิธี workaround คือปิด workflow ของคุณชั่วคราวตอนทดสอบ:

/// warning | Halts production traffic
วิธีนี้จะปิด workflow production ชั่วคราวระหว่างทดสอบ ทำให้ workflow ไม่ได้รับ traffic production ขณะปิดอยู่
///

1. ไปที่หน้า workflow ของคุณ
2. กดปุ่ม **Active** ด้านบนเพื่อปิด workflow ชั่วคราว
3. ทดสอบ workflow โดยใช้ test webhook URL
4. เมื่อทดสอบเสร็จแล้ว กดปุ่ม **Inactive** เพื่อเปิด workflow อีกครั้ง production webhook URL จะกลับมาใช้งานได้ตามปกติ
