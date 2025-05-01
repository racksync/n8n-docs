---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Facebook Trigger WhatsApp Business Account object documentation
description: Learn how to use the WhatsApp Business Account object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's WhatsApp Business Account object into your workflows.
contentType: [integration, reference]
priority: medium
---

# Facebook Trigger WhatsApp Business Account object

ใช้ object นี้เพื่อรับการแจ้งเตือนเมื่อ WhatsApp Business Account (WABA) ของคุณมีการเปลี่ยนแปลง ดูข้อมูลเพิ่มเติมเกี่ยวกับ trigger ได้ที่ [Facebook Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/index.md)

/// warning | Use WhatsApp trigger
n8n แนะนำให้ใช้ [WhatsApp Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md) คู่กับ [WhatsApp credentials](/integrations/builtin/credentials/whatsapp.md) แทน Facebook Trigger node เพราะ node นี้มี event ให้ subscribe ได้มากกว่า 2 เท่า
///

/// note | Credentials
คุณสามารถดูข้อมูลเกี่ยวกับการตั้งค่า credentials สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/facebookapp.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่จะช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [Facebook Trigger integrations](https://n8n.io/integrations/facebook-trigger/){:target=_blank .external-link} ของ n8n
///

## Prerequisites

Object นี้ต้องมีการตั้งค่าบางอย่างในแอปและบัญชี WhatsApp ของคุณก่อนใช้งาน trigger:

1. ต้อง subscribe แอปของคุณภายใต้ WhatsApp business account ของคุณเอง ต้องเป็นแอปที่ business ของคุณเป็นเจ้าของ (แอปที่แชร์กับ business อื่นจะไม่ได้รับ webhook)
1. ถ้าคุณเป็น Solution Partner ต้องให้แอปผ่าน App Review และขอ permission `whatsapp_business_management`

## Trigger configuration

วิธีตั้งค่า trigger ด้วย Object นี้:

1. เลือก **Credential to connect with** เลือกหรือสร้าง [Facebook App credential](/integrations/builtin/credentials/facebookapp.md) ใหม่
1. กรอก **APP ID** ของแอปที่เชื่อมกับ credential ของคุณ ดูรายละเอียดเพิ่มเติมได้ที่ [Facebook App credential](/integrations/builtin/credentials/facebookapp.md)
1. เลือก **WhatsApp Business Account** ในช่อง **Object**
1. **Field Names or IDs**: โดยปกติ node จะ trigger กับทุก event โดยใช้ wildcard `*` ถ้าต้องการจำกัด event ให้กด X เพื่อลบดาว แล้วเลือกจาก dropdown หรือใช้ expression เพื่อเลือกเฉพาะ event ที่ต้องการ ตัวเลือกเช่น:
    * **Message Template Status Update**
    * **Phone Number Name Update**
    * **Phone Number Quality Update**
    * **Account Review Update**
    * **Account Update**
1. ใน **Options** ให้เปิด toggle **Include Values** (object นี้จะ error ถ้าไม่เปิด option นี้)

ดูข้อมูลเพิ่มเติมได้ที่ [Webhooks for WhatsApp Business Accounts](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-whatsapp){:target=_blank .external-link} และ [WhatsApp Business Account](https://developers.facebook.com/docs/graph-api/webhooks/reference/whatsapp-business-account/){:target=_blank .external-link} ในเอกสารของ Meta
