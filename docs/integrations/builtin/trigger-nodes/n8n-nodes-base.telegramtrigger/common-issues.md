---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ปัญหาที่พบบ่อยของ Telegram Trigger node
description: รวมปัญหาและคำถามที่พบบ่อยสำหรับ Telegram Trigger node ใน n8n พร้อมแนวทางแก้ไข
contentType: [integration, reference]
priority: critical
---

# Telegram Trigger node common issues

รวม error และปัญหาที่พบบ่อยกับ [Telegram Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md) พร้อมวิธีแก้ไขหรือแนวทางตรวจสอบ

## Stuck waiting for trigger event

เวลาทดสอบ Telegram Trigger node ด้วยปุ่ม **Test step** หรือ **Test workflow** อาจเจอ workflow ค้างและหยุดฟัง event ไม่ได้ ถ้าเกิดแบบนี้ให้ลองออกจาก workflow แล้วเข้าใหม่เพื่อ reset canvas

ปัญหานี้มักเกิดจาก network configuration ภายนอก n8n โดยเฉพาะถ้าคุณ run n8n หลัง reverse proxy ที่ไม่ได้ตั้งค่า websocket proxying

วิธีแก้ไข ให้เช็ค config reverse proxy (Nginx, Caddy, Apache HTTP Server, Traefik ฯลฯ) ให้รองรับ websocket

<!-- vale off -->
## Bad request: bad webhook: An HTTPS URL must be provided for webhook
<!-- vale on -->

error นี้เกิดเมื่อคุณ run n8n หลัง reverse proxy แล้ว webhook URL มีปัญหา

ถ้า run n8n หลัง reverse proxy ต้อง [ตั้งค่า environment variable `WEBHOOK_URL`](/hosting/configuration/configuration-examples/webhook-url.md) ให้เป็น public URL ที่ instance ของคุณใช้งาน สำหรับ Telegram URL นี้ต้องเป็น HTTPS

วิธีแก้ไข ให้ตั้งค่า TLS/SSL termination ใน reverse proxy แล้วอัปเดต `WEBHOOK_URL` ให้เป็น HTTPS

## Workflow only works in testing or production

Telegram อนุญาตให้ register webhook ได้แค่ 1 อันต่อ app ทุกครั้งที่สลับจาก testing URL ไป production URL (หรือกลับกัน) Telegram จะ overwrite webhook URL เดิม

ถ้าคุณทดสอบ workflow ที่เปิดใช้งานใน production อยู่ อาจเจอปัญหา Telegram bot ส่ง event ไปแค่ 1 URL อีกอันจะไม่ได้รับ event

วิธี workaround คือปิด workflow ตอนทดสอบ หรือสร้าง Telegram bot แยกสำหรับ test กับ production

ถ้าจะสร้าง Telegram bot สำหรับ test ให้ทำเหมือนตอนสร้าง bot แรก ดูวิธีที่ [Telegram's bot documentation](https://core.telegram.org/bots) และ [Telegram bot API reference](https://core.telegram.org/bots/api)

ถ้าจะปิด workflow ตอนทดสอบ ให้ทำตามนี้:

/// warning | Halts production traffic
workaround นี้จะปิด workflow production ชั่วคราวระหว่างทดสอบ workflow จะไม่ได้รับ traffic production ขณะ inactive
///

1. ไปที่หน้า workflow ของคุณ
2. ปิด **Active** toggle ด้านบนเพื่อปิด workflow ชั่วคราว
3. ทดสอบ workflow ด้วย test webhook URL
4. ทดสอบเสร็จแล้วเปิด toggle **Inactive** เพื่อเปิด workflow อีกครั้ง production webhook URL จะกลับมาใช้งานได้
