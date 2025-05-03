---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Twilio Trigger node
description: วิธีใช้ Twilio Trigger node ใน n8n เพื่อเชื่อมต่อ Twilio กับ workflow ของคุณ
contentType: [integration, reference]
---

# Twilio Trigger node

ใช้ Twilio Trigger node เพื่อตอบสนองต่อ event ต่างๆ ใน [Twilio](https://www.twilio.com){:target=_blank .external-link} และเชื่อมต่อ Twilio กับแอปอื่นๆ ได้ n8n รองรับ event ของ Twilio หลากหลาย เช่น ข้อความ SMS ใหม่ หรือสายโทรเข้าใหม่

ในหน้านี้ คุณจะเห็นรายการ event ที่ Twilio Trigger node สามารถตอบสนองได้ พร้อมลิงก์ไปยัง resource อื่นๆ

///  note  | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/twilio.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่ช่วยให้เริ่มต้นได้ง่ายขึ้น ดูได้ที่ [Twilio integrations ของ n8n](https://n8n.io/integrations/twilio-trigger/){:target=_blank .external-link}
///

## Events

* On New SMS
* On New Call

///  note  | New Call Delay
Twilio อาจใช้เวลาสูงสุด 30 นาทีในการสร้างสรุปสำหรับสายที่เสร็จสมบูรณ์
///

## Related resources

n8n มี app node สำหรับ Twilio ด้วย ดูเอกสาร node ได้ [ที่นี่](/integrations/builtin/app-nodes/n8n-nodes-base.twilio.md)

ดู [example workflows และเนื้อหาอื่นๆ ที่เกี่ยวข้อง](https://n8n.io/integrations/twilio/){:target=_blank .external-link} บนเว็บไซต์ n8n

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ API ของ Twilio ได้ที่ [Twilio's documentation](https://www.twilio.com/docs){:target=_blank .external-link}
