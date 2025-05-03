---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: ข้อมูลเข้าสู่ระบบ UptimeRobot
description: คู่มือการตั้งค่า credentials สำหรับเชื่อมต่อ UptimeRobot กับ n8n เพื่อใช้งาน workflow automation
contentType: [integration, reference]
---

# UptimeRobot credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [UptimeRobot](/integrations/builtin/app-nodes/n8n-nodes-base.uptimerobot.md)

## Prerequisites

สร้างบัญชี [UptimeRobot](https://uptimerobot.com/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [UptimeRobot's API documentation](https://uptimerobot.com/api/){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credential นี้ คุณจะต้องมี:

- **API Key**: ไปที่ **My Settings > API Settings** เพื่อรับ API Key ของคุณ สร้าง **Main API Key** แล้วนำ key นี้ไปใส่ใน n8n credential ของคุณ

### API key types

UptimeRobot รองรับ API key 3 ประเภท:

- **Account-specific** (หรือเรียกว่า **main**): ใช้ดึงข้อมูลสำหรับ monitor หลายตัว
- **Monitor-specific**: ใช้ดึงข้อมูลสำหรับ monitor ตัวเดียว
- **Read-only**: ใช้ได้เฉพาะ API ที่เป็น `GET` เท่านั้น

ถ้าต้องการใช้งานทุกฟีเจอร์ใน UptimeRobot node ให้ใช้ **Main** หรือ **Account-specific** API key ดูรายละเอียดเพิ่มเติมได้ที่ [API authentication](https://uptimerobot.com/api/#auth){:target=_blank .external-link}
