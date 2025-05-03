---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Facebook Trigger Certificate Transparency object
description: เรียนรู้วิธีใช้ Facebook Trigger node กับ Certificate Transparency object ใน n8n และวิธีเชื่อมต่อกับ workflow ของคุณ
contentType: [integration, reference]
priority: medium
---

# Facebook Trigger Certificate Transparency object

ใช้ object นี้เพื่อรับการแจ้งเตือนเกี่ยวกับ certificate ที่ออกใหม่สำหรับโดเมนที่คุณ subscribe ไว้สำหรับ certificate alerts หรือ phishing alerts ดูข้อมูลเพิ่มเติมเกี่ยวกับ trigger ได้ที่ [Facebook Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/index.md)

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
1. เลือก **Certificate Transparency** ในช่อง **Object**
1. **Field Names or IDs**: โดยปกติ node จะ trigger กับทุก event โดยใช้ wildcard `*` ถ้าต้องการจำกัด event ให้กด X เพื่อลบดาว แล้วเลือกจาก dropdown หรือใช้ expression เพื่อเลือกเฉพาะ event ที่ต้องการ ตัวเลือกเช่น:
    * **Certificate**: แจ้งเตือนเมื่อมีการออก certificate ใหม่สำหรับโดเมนที่คุณ subscribe ไว้ ต้อง subscribe domain สำหรับ certificate alerts ก่อน
    * **Phishing**: แจ้งเตือนเมื่อมีการออก certificate ใหม่ที่อาจเป็น phishing สำหรับโดเมนที่คุณ subscribe ไว้
1. ใน **Options** ให้เปิด toggle **Include Values** (object นี้จะ error ถ้าไม่เปิด option นี้)

สำหรับการแจ้งเตือนเหล่านี้ คุณต้อง subscribe domain ของคุณให้กับ alerts ที่เกี่ยวข้อง:

* ดูวิธี subscribe สำหรับ Certificate Alerts ได้ที่ [Certificate Alerts](https://developers.facebook.com/docs/certificate-transparency-api#certificate-alerts-subscribing){:target=_blank .external-link}
* ดูวิธี subscribe สำหรับ Phishing Alerts ได้ที่ [Phishing Alerts](https://developers.facebook.com/docs/certificate-transparency-api#phishing-alerts-subscribing){:target=_blank .external-link}

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [Webhooks for Certificate Transparency](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-certificate-transparency){:target=_blank .external-link} และ [Certificate Transparency](https://developers.facebook.com/docs/graph-api/webhooks/reference/certificate-transparency/){:target=_blank .external-link} ในเอกสารของ Meta
