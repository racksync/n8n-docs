---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: TOTP
description: Documentation for the TOTP node in n8n, a workflow automation platform. Includes guidance on usage, and links to examples.
contentType: [integration, reference]
---

# TOTP

TOTP node ช่วยให้คุณสามารถสร้างรหัส TOTP (time-based one-time password) ได้ง่ายๆ

/// note | Credentials
ดูวิธีตั้งค่า authentication ได้ที่ [TOTP credentials](/integrations/builtin/credentials/totp.md)
///

## Node parameters

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

ตั้งค่า node นี้ด้วย parameters เหล่านี้

### Credential to connect with

เลือกหรือสร้าง [TOTP credential](/integrations/builtin/credentials/totp.md) ที่จะใช้กับ node นี้

### Operation

**Generate Secret** เป็น operation เดียวที่รองรับในตอนนี้

## Node options

ใช้ **Options** เหล่านี้เพื่อปรับแต่ง node เพิ่มเติม

### Algorithm

เลือก HMAC hashing algorithm ที่ต้องการใช้ ค่า default คือ SHA1

### Digits

ใส่จำนวนหลักของรหัสที่ต้องการให้สร้าง ค่า default คือ `6`

### Period

ใส่จำนวนวินาทีที่รหัส TOTP จะใช้งานได้ ค่า default คือ `30`

## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'totp') ]]
