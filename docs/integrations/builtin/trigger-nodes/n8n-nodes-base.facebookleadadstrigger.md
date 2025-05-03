---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Facebook Lead Ads Trigger node
description: วิธีใช้ Facebook Lead Ads Trigger node ใน n8n พร้อมตัวอย่าง workflow
contentType: [integration, reference]
priority: medium
---

# Facebook Lead Ads Trigger node

ใช้ Facebook Lead Ads Trigger node เพื่อตอบสนองต่อ event ต่างๆ ใน [Facebook Lead Ads](https://www.facebook.com/business/ads/lead-ads/){:target=_blank .external-link} และเชื่อมต่อ Facebook Lead Ads กับแอปอื่นๆ ได้โดยตรง n8n รองรับการแจ้งเตือนเมื่อมี lead ใหม่เข้ามา

ในหน้านี้ คุณจะพบรายการ event ที่ Facebook Lead Ads Trigger node สามารถตอบสนองได้ และลิงก์ไปยังแหล่งข้อมูลเพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลการเชื่อมต่อสำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/facebookleadads.md)
///

/// note | Examples and templates
สำหรับตัวอย่างการใช้งานและ template เพื่อช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [Facebook Lead Ads Trigger integrations ของ n8n](https://n8n.io/integrations/facebook-lead-ads-trigger/){:target=_blank .external-link}
///

## Events

* New lead: แจ้งเตือนเมื่อมี lead ใหม่เข้ามา

## Related resources

ดู [ตัวอย่าง workflow และเนื้อหาที่เกี่ยวข้อง](https://n8n.io/integrations/facebook-lead-ads-trigger/){:target=_blank .external-link} บนเว็บไซต์ n8n

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ API ได้ที่ [Facebook Lead Ads' documentation](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/){:target=_blank .external-link}

## Common issues

นี่คือตัวอย่างปัญหาที่พบบ่อยกับ Facebook Lead Ads Trigger node และวิธีแก้ไขหรือแนวทางการตรวจสอบ

### Workflow only works in testing or production

Facebook Lead Ads อนุญาตให้ลงทะเบียน webhook ได้เพียงอันเดียวต่อแอปเท่านั้น หมายความว่าทุกครั้งที่คุณสลับจาก URL สำหรับทดสอบไปยัง URL สำหรับ production (หรือกลับกัน) Facebook Lead Ads จะเขียนทับ webhook URL ที่ลงทะเบียนไว้

คุณอาจเจอปัญหานี้ถ้าคุณพยายามทดสอบ workflow ที่เปิดใช้งานอยู่ใน production ด้วย Facebook Lead Ads จะส่ง event ไปยัง webhook URL เพียงอันเดียวเท่านั้น อีกอันจะไม่ได้รับการแจ้งเตือน

วิธีแก้ไขเบื้องต้นคือให้ปิด workflow ของคุณขณะทดสอบ:

/// warning | Halts production traffic
วิธีนี้จะหยุดการรับ traffic จริงใน production ชั่วคราว Workflow ของคุณจะไม่ได้รับ event จาก production ขณะปิดอยู่
///

1. ไปที่หน้า workflow ของคุณ
2. ปิดสวิตช์ **Active** ด้านบนเพื่อปิดใช้งาน workflow ชั่วคราว
3. ทดสอบ workflow ของคุณโดยใช้ test webhook URL
4. เมื่อทดสอบเสร็จแล้ว เปิดสวิตช์ **Inactive** เพื่อเปิดใช้งาน workflow อีกครั้ง Production webhook URL จะกลับมาใช้งานได้ตามปกติ
