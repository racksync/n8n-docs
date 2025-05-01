---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Telegram credentials
description: Documentation for Telegram credentials. Use these credentials to authenticate Telegram in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: critical
---

# Telegram credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Telegram](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/index.md)
- [Telegram Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md)

## Prerequisites

สร้างบัญชี [Telegram](https://telegram.org/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API bot access token

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Telegram's Bot API documentation](https://core.telegram.org/bots/api){:target=_blank .external-link}

ดูข้อมูลเกี่ยวกับการสร้างและใช้งาน bot ได้ที่ [Telegram Bot Features](https://core.telegram.org/bots/features){:target=_blank .external-link}

## Using API bot access token

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Access Token** ของ bot

วิธีสร้าง access token:

1. เริ่มแชทกับ [BotFather](https://telegram.me/BotFather){:target=_blank .external-link}
2. พิมพ์คำสั่ง `/newbot` เพื่อสร้าง bot ใหม่
3. BotFather จะถามชื่อและ username ของ bot ใหม่:
    * **name** คือชื่อที่จะแสดงใน contact และที่อื่น ๆ สามารถเปลี่ยนชื่อ bot ได้ภายหลัง
    * **username** คือชื่อสั้น ๆ ที่ใช้ใน search, mention และ t.me link โดยมีข้อกำหนดดังนี้:
        * ต้องมีความยาว 5-32 ตัวอักษร
        * ไม่สนใจตัวพิมพ์ใหญ่/เล็ก
        * ใช้ได้เฉพาะตัวอักษรภาษาอังกฤษ ตัวเลข และขีดล่าง (_)
        * ต้องลงท้ายด้วย `bot` เช่น `tetris_bot` หรือ `TetrisBot`
        * ไม่สามารถเปลี่ยน username ได้ภายหลัง
3. คัดลอก **token** ที่ BotFather สร้างให้ แล้วนำไปใส่ใน n8n เป็น **Access Token**

ดูรายละเอียดเพิ่มเติมได้ที่ [BotFather Create a new bot documentation](https://core.telegram.org/bots/features#creating-a-new-bot)
