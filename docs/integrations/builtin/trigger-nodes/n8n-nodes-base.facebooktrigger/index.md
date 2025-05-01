---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Facebook Trigger
description: Learn how to use the Facebook Trigger node in n8n. Follow technical documentation to integrate Facebook Trigger node into your workflows.
contentType: [integration, reference]
priority: medium
---

# Facebook Trigger node

[Facebook](https://www.facebook.com/){:target=_blank .external-link} เป็น social network ที่ให้คุณเชื่อมต่อและแชร์กับครอบครัวและเพื่อนๆ ออนไลน์

ใช้ Facebook Trigger node เพื่อ trigger workflow ของคุณเมื่อมี event ต่างๆ เกิดขึ้นใน Facebook

/// note | Credentials
คุณสามารถดูข้อมูลเกี่ยวกับการตั้งค่า credentials สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/facebookapp.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่จะช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [Facebook Trigger integrations](https://n8n.io/integrations/facebook-trigger/){:target=_blank .external-link} ของ n8n
///

## Objects

- [**Ad Account**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/ad-account.md): รับการแจ้งเตือนเมื่อมีการเปลี่ยนแปลงโฆษณาบางอย่าง
- [**Application**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/application.md): รับการแจ้งเตือนที่ถูกส่งไปยังแอปของคุณ
- [**Certificate Transparency**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency.md): รับการแจ้งเตือนเมื่อมีการสร้าง security certificate ใหม่สำหรับโดเมนที่ subscribe รวมถึง certificate ใหม่และความเสี่ยง phishing
- กิจกรรมและ event ใน [**Group**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/group.md)
- [**Instagram**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/instagram.md): รับการแจ้งเตือนเมื่อมีคน comment ใน Media ของผู้ใช้แอป, @mention ผู้ใช้แอป หรือ story หมดอายุ
- [**Link**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link.md): รับการแจ้งเตือนเกี่ยวกับลิงก์สำหรับ rich preview จาก provider ภายนอก
- [**Page**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/page.md) อัปเดตต่างๆ ของเพจ
- [**Permissions**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/permissions.md): แจ้งเตือนเมื่อมีการให้หรือเพิกถอน permissions
- [**User**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/user.md) อัปเดตโปรไฟล์ผู้ใช้
- [**WhatsApp Business Account**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/whatsapp.md)
    
    /// note | Use WhatsApp Trigger
    n8n แนะนำให้ใช้ [WhatsApp Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md) คู่กับ [WhatsApp credentials](/integrations/builtin/credentials/whatsapp.md) แทน Facebook Trigger node สำหรับ event เหล่านี้ เพราะ WhatsApp Trigger node มี event ให้เลือกมากกว่า
    ///

- [**Workplace Security**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/workplace-security.md)

สำหรับแต่ละ **Object** ให้ใช้ dropdown **Field Names or IDs** เพื่อเลือกข้อมูลที่ต้องการรับเพิ่มเติม ดูรายละเอียดแต่ละ object ได้ที่ลิงก์ด้านบน

## Related resources

ดู [ตัวอย่าง workflow และเนื้อหาที่เกี่ยวข้อง](https://n8n.io/integrations/facebook-trigger/){:target=_blank .external-link} บนเว็บไซต์ n8n

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ API ได้ที่ [Graph API documentation](https://developers.facebook.com/docs/graph-api/webhooks/reference){:target=_blank .external-link} ของ Meta
