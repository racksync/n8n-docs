---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Facebook Trigger Page object documentation
description: Learn how to use the Page object of the Facebook Trigger node in n8n. Follow technical documentation to integrate the Facebook Trigger node's Page object into your workflows.
contentType: [integration, reference]
priority: medium
---

# Facebook Trigger Page object

ใช้ object นี้เพื่อรับการแจ้งเตือนเมื่อมีการอัปเดต field หรือ setting ของ page หรือมีคน mention page ของคุณ ดูข้อมูลเพิ่มเติมเกี่ยวกับ trigger ได้ที่ [Facebook Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/index.md)

/// note | Credentials
คุณสามารถดูข้อมูลเกี่ยวกับการตั้งค่า credentials สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/facebookapp.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่จะช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [Facebook Trigger integrations](https://n8n.io/integrations/facebook-trigger/){:target=_blank .external-link} ของ n8n
///

## Prerequisites

Object นี้ต้องมีการตั้งค่าบางอย่างในแอปและเพจก่อนใช้งาน trigger:

1. ต้องมี admin ของ page อย่างน้อย 1 คนที่ให้ permission `manage_pages` กับแอปของคุณ
1. admin ของ page ต้องมีสิทธิ์อย่างน้อยเป็น moderator ถ้าไม่เช่นนั้นจะไม่ได้รับเนื้อหาทั้งหมด
1. ต้องเพิ่มแอปเข้าไปใน page และอาจต้องเข้า [Graph API explorer](https://developers.facebook.com/tools/explorer/){:target=_blank .external-link} แล้วรันคำสั่งนี้ด้วย app token:

    ```
    {page-id}/subscribed_apps?subscribed_fields=feed
    ```

## Trigger configuration

วิธีตั้งค่า trigger ด้วย Object นี้:

1. เลือก **Credential to connect with** เลือกหรือสร้าง [Facebook App credential](/integrations/builtin/credentials/facebookapp.md) ใหม่
1. กรอก **APP ID** ของแอปที่เชื่อมกับ credential ของคุณ ดูรายละเอียดเพิ่มเติมได้ที่ [Facebook App credential](/integrations/builtin/credentials/facebookapp.md)
1. เลือก **Page** ในช่อง **Object**
1. **Field Names or IDs**: โดยปกติ node จะ trigger กับทุก event โดยใช้ wildcard `*` ถ้าต้องการจำกัด event ให้กด X เพื่อลบดาว แล้วเลือกจาก dropdown หรือใช้ expression เพื่อเลือกเฉพาะ event ที่ต้องการ ตัวเลือกเช่น field ของ profile และ:
    * **Feed**: แจ้งเตือนการเปลี่ยนแปลงใน feed ของ page เช่น โพสต์ ไลค์ แชร์ ฯลฯ
    * **Leadgen**: แจ้งเตือนเมื่อมีการเปลี่ยนแปลง lead generation settings ของ page
    * **Live Videos**: แจ้งเตือนเมื่อสถานะ live video ของ page เปลี่ยนแปลง
    * **Mention**: แจ้งเตือนเมื่อมีการ mention ใหม่ใน page, comment ฯลฯ
    * **Merchant Review**: แจ้งเตือนเมื่อมีการเปลี่ยนแปลง merchant review settings ของ page
    * **Page Change Proposal**: แจ้งเตือนเมื่อ Facebook เสนอการเปลี่ยนแปลงให้กับ page ของคุณ
    * **Page Upcoming Change**: แจ้งเตือนเกี่ยวกับการเปลี่ยนแปลงที่จะเกิดขึ้นใน page ของคุณ ซึ่ง Facebook เสนอและอาจมี deadline ให้ยอมรับหรือปฏิเสธ
    * **Product Review**: แจ้งเตือนเมื่อมีการเปลี่ยนแปลง product review settings ของ page
    * **Ratings**: แจ้งเตือนเมื่อมีการเปลี่ยนแปลง ratings ของ page เช่น มี rating ใหม่ หรือมีคน comment/react กับ rating
    * **Videos**: แจ้งเตือนเมื่อ encoding status ของวิดีโอบน page เปลี่ยนแปลง
1. ใน **Options** ให้เปิด toggle **Include Values** (object นี้จะ error ถ้าไม่เปิด option นี้)

## Related resources

ดูข้อมูลเพิ่มเติมได้ที่ [Webhooks for Pages](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-pages){:target=_blank .external-link} และ [Page](https://developers.facebook.com/docs/graph-api/webhooks/reference/page/){:target=_blank .external-link} ในเอกสารของ Meta
