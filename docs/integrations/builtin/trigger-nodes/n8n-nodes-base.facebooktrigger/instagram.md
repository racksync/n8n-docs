---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Facebook Trigger Instagram object documentation
description: Learn how to use the Instagram object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Instagram object into your workflows.
contentType: [integration, reference]
priority: medium
---

# Facebook Trigger Instagram object

ใช้ object นี้เพื่อรับการแจ้งเตือนเมื่อมีคน comment ใน Media ของผู้ใช้แอป, @mention ผู้ใช้แอป หรือ story ของผู้ใช้แอปหมดอายุ ดูข้อมูลเพิ่มเติมเกี่ยวกับ trigger ได้ที่ [Facebook Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/index.md)

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
1. เลือก **Instagram** ในช่อง **Object**
1. **Field Names or IDs**: โดยปกติ node จะ trigger กับทุก event โดยใช้ wildcard `*` ถ้าต้องการจำกัด event ให้กด X เพื่อลบดาว แล้วเลือกจาก dropdown หรือใช้ expression เพื่อเลือกเฉพาะ event ที่ต้องการ ตัวเลือกเช่น:
    * **Comments**: แจ้งเตือนเมื่อมีคน comment ใน IG Media ของผู้ใช้ Instagram ที่เชื่อมกับแอปของคุณ
    * **Messaging Handover**
    * **Mentions**: แจ้งเตือนเมื่อมีคน @mention Instagram Business หรือ Creator Account ใน comment หรือ caption
    * **Messages**: แจ้งเตือนเมื่อมีคนส่งข้อความถึงผู้ใช้ Instagram ของแอปคุณ
    * **Messaging Seen**: แจ้งเตือนเมื่อมีคนเห็นข้อความที่ผู้ใช้ Instagram ของแอปคุณส่งไป
    * **Standby**
    * **Story Insights**: แจ้งเตือนหลัง story หมดอายุ 1 ชั่วโมง พร้อม metric การมีส่วนร่วมกับ story นั้น
1. ใน **Options** ให้เปิด toggle **Include Values** (object นี้จะ error ถ้าไม่เปิด option นี้)

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [Webhooks for Instagram](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-instagram){:target=_blank .external-link} และ [Instagram](https://developers.facebook.com/docs/graph-api/webhooks/reference/instagram/){:target=_blank .external-link} ในเอกสารของ Meta
