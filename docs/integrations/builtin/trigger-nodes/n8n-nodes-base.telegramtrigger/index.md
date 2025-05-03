---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: คู่มือ Telegram Trigger node
description: เรียนรู้วิธีใช้ Telegram Trigger node ใน n8n พร้อมวิธีเชื่อมต่อ Telegram กับ workflow ของคุณ
contentType: [integration, reference]
priority: critical
---

# Telegram Trigger node

[Telegram](https://telegram.org/){:target=_blank .external-link} คือบริการแชทและโทรศัพท์ผ่านอินเทอร์เน็ตแบบ cloud-based ผู้ใช้สามารถส่งข้อความ รูป วิดีโอ สติกเกอร์ เสียง และไฟล์ทุกประเภทได้ ในหน้านี้จะมีรายการ event ที่ Telegram Trigger node ตอบสนองได้ และลิงก์ไปยัง resource เพิ่มเติม

/// note | Credentials
คุณสามารถดูข้อมูลเกี่ยวกับการตั้งค่า credentials สำหรับ node นี้ได้ [ที่นี่](/integrations/builtin/credentials/telegram.md)
///

///  note  | Examples and templates
สำหรับตัวอย่างการใช้งานและ template ที่จะช่วยให้คุณเริ่มต้นได้ง่ายขึ้น ดูได้ที่หน้า [Telegram Trigger integrations](https://n8n.io/integrations/telegram-trigger/){:target=_blank .external-link} ของ n8n
///

## Events

- **`*`**: ทุก update ยกเว้น "Chat Member", "Message Reaction", และ "Message Reaction Count" (เป็น default ของ Telegram API เพราะ event เหล่านี้จะเรียกบ่อยมาก)
- **Business Connection**: trigger เมื่อ bot เชื่อมต่อหรือถูกตัดกับ business account หรือผู้ใช้แก้ไขการเชื่อมต่อกับ bot
- **Business Message**: trigger เมื่อมีข้อความใหม่จาก business account ที่เชื่อมต่อ
- **Callback Query**: trigger เมื่อมี callback query ใหม่เข้ามา
- **Channel Post**: trigger เมื่อมี channel post ใหม่เข้ามา (ทุกประเภท เช่น ข้อความ รูป สติกเกอร์ ฯลฯ)
- **Chat Boost**: trigger เมื่อมีการเพิ่มหรือเปลี่ยนแปลง chat boost bot ต้องเป็น admin ใน chat ถึงจะรับ event นี้ได้
- **Chat Join Request**: trigger เมื่อมี request ขอเข้าร่วม chat bot ต้องมีสิทธิ์ `can_invite_users` ใน chat
- **Chat Member**: trigger เมื่อสถานะสมาชิกใน chat เปลี่ยนแปลง bot ต้องเป็น admin ใน chat
- **Chosen Inline Result**: trigger เมื่อมีการเลือกผลลัพธ์ inline query ดูวิธีเปิด event นี้ใน [feedback collection](https://core.telegram.org/bots/inline#collecting-feedback) ของ Telegram
- **Deleted Business Messages**: trigger เมื่อข้อความถูกลบจาก business account ที่เชื่อมต่อ
- **Edited Business Message**: trigger เมื่อมีข้อความใหม่จาก business account ที่เชื่อมต่อ
- **Edited Channel Post**: trigger เมื่อ channel post ที่ bot รู้จักถูกแก้ไข
- **Edited Message**: trigger เมื่อ channel post ที่ bot รู้จักถูกแก้ไข
- **Inline Query**: trigger เมื่อมี inline query ใหม่เข้ามา
- **Message**: trigger เมื่อมีข้อความใหม่เข้ามา (ทุกประเภท เช่น ข้อความ รูป สติกเกอร์ ฯลฯ)
- **Message Reaction**: trigger เมื่อมีการเปลี่ยนแปลง reaction ใน message โดย user bot ต้องเป็น admin ใน chat (ไม่รับ update จาก reaction ที่ bot เป็นคน set)
- **Message Reaction Count**: trigger เมื่อ reaction ของ message ที่เป็น anonymous เปลี่ยนแปลง bot ต้องเป็น admin ใน chat (update นี้จะ grouped และอาจ delay ได้ถึงไม่กี่นาที)
- **My Chat Member**: trigger เมื่อสถานะสมาชิกของ bot ใน chat เปลี่ยนแปลง สำหรับ private chat จะรับ update เฉพาะตอนถูก block/unblock
- **Poll**: trigger เมื่อ poll เปลี่ยนสถานะ bot จะรับเฉพาะ poll ที่ bot เป็นคนส่งหรือ poll ที่หยุดแล้ว
- **Poll Answer**: trigger เมื่อ user เปลี่ยนคำตอบใน poll ที่ไม่ anonymous bot จะรับเฉพาะ vote ใหม่ใน poll ที่ bot เป็นคนส่ง
- **Pre-Checkout Query**: trigger เมื่อมี pre-checkout query ใหม่เข้ามา (ข้อมูล checkout เต็ม)
- **Purchased Paid Media**: trigger เมื่อ user ซื้อ paid media ที่มี payload จาก bot ใน non-channel chat
- **Removed Chat Boost**: trigger เมื่อ boost ถูกลบออกจาก chat bot ต้องเป็น admin ใน chat
- **Shipping Query**: trigger เมื่อมี shipping query ใหม่เข้ามา (เฉพาะ invoice ที่ flexible price)

**บาง event ต้องใช้ permission เพิ่มเติม** ดูรายละเอียดที่ [Telegram's API documentation](https://core.telegram.org/bots/api#getting-updates)

## Related resources

n8n มี app node สำหรับ Telegram ด้วย ดูเอกสาร node ได้ [ที่นี่](/integrations/builtin/credentials/telegram.md)

ดู [ตัวอย่าง workflow และเนื้อหาที่เกี่ยวข้อง](https://n8n.io/integrations/telegram-trigger/){:target=_blank .external-link} บนเว็บไซต์ n8n

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ API ได้ที่ [Telegram's API documentation](https://core.telegram.org/bots/api){:target=_blank .external-link}

## Common issues

สำหรับคำถามหรือปัญหาที่พบบ่อยและวิธีแก้ไข ดูได้ที่ [Common issues](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/common-issues.md)
