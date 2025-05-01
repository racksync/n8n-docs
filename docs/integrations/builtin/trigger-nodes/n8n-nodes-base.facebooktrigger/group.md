---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Facebook Trigger Group object documentation
description: Learn how to use the Group object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Group object into your workflows.
contentType: [integration, reference]
priority: medium
---

# Facebook Trigger Group object

ใช้ object นี้เพื่อรับการแจ้งเตือนเกี่ยวกับกิจกรรมและ event ต่างๆ ใน group ของคุณ ดูข้อมูลเพิ่มเติมเกี่ยวกับ trigger ได้ที่ [Facebook Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/index.md)

/// note | Credentials
คุณสามารถดูข้อมูลเกี่ยวกับการตั้งค่า credentials สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/facebookapp.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่จะช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [Facebook Trigger integrations](https://n8n.io/integrations/facebook-trigger/){:target=_blank .external-link} ของ n8n
///

## Trigger configuration

วิธีตั้งค่า trigger ด้วย Object นี้:

1. เลือก **Credential to connect with** เลือกหรือสร้าง [Facebook App credential](/integrations/builtin/credentials/facebookapp.md) ใหม่
1. กรอก **APP ID** ของแอปที่เชื่อมกับ credential ของคุณ ดูรายละเอียดเพิ่มเติมได้ที่ [Facebook App credential](/integrations/builtin/credentials/facebookapp.md)
1. เลือก **Group** ในช่อง **Object**
1. **Field Names or IDs**: โดยปกติ node จะ trigger กับทุก event โดยใช้ wildcard `*` ถ้าต้องการจำกัด event ให้กด X เพื่อลบดาว แล้วเลือกจาก dropdown หรือใช้ expression เพื่อเลือกเฉพาะ event ที่ต้องการ
1. ใน **Options** ให้เปิด toggle **Include Values** (object นี้จะ error ถ้าไม่เปิด option นี้)

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [Groups](https://developers.facebook.com/docs/workplace/reference/webhooks/#groups){:target=_blank .external-link} ใน Workplace API ของ Meta
