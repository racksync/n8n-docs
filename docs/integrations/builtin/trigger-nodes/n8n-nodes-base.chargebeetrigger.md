---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Chargebee Trigger node
description: วิธีใช้ Chargebee Trigger node ใน n8n พร้อมตัวอย่าง workflow
contentType: [integration, reference]
---

# Chargebee Trigger node

[Chargebee](https://www.chargebee.com/){:target=_blank .external-link} เป็นแพลตฟอร์ม billing สำหรับธุรกิจ SaaS และ eCommerce แบบ subscription ช่วยให้คุณ automate การเก็บเงิน recurring, ออก invoice, คำนวณภาษี, ทำบัญชี, ส่งอีเมลแจ้งเตือน, ดู SaaS Metrics และจัดการลูกค้าได้ครบจบในที่เดียว

/// note | Credentials
คุณสามารถดูข้อมูลการตั้งค่า authentication สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/chargebee.md)
///

///  note  | Examples and templates
ถ้าต้องการดูตัวอย่างการใช้งานและ workflow template เพื่อเริ่มต้นใช้งาน ลองดูที่หน้า [Chargebee Trigger integrations](https://n8n.io/integrations/chargebee-trigger/){:target=_blank .external-link} ของ n8n ได้เลย
///

## Add webhook URL in Chargebee

วิธีเพิ่ม Webhook URL ใน Chargebee:

1. เปิด Chargebee dashboard ของคุณ
2. ไปที่ **Settings** > **Configure Chargebee**
4. เลื่อนลงแล้วเลือก **Webhooks**
5. กดปุ่ม **Add Webhook**
6. ใส่ **Webhook Name** และ **Webhook URL**
7. กด **Create**
