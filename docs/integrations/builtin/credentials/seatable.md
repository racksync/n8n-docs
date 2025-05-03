---
title: ข้อมูลเข้าสู่ระบบ SeaTable
description: คู่มือการตั้งค่า SeaTable credentials สำหรับเชื่อมต่อ SeaTable กับ n8n
contentType: [integration, reference]
---

# SeaTable credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้:

- [SeaTable](/integrations/builtin/app-nodes/n8n-nodes-base.seatable.md)
- [SeaTable Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.seatabletrigger.md)

## Prerequisites

สร้าง [SeaTable](https://seatable.io/en/){:target=_blank .external-link} account บน cloud หรือ self-hosted SeaTable server

## Supported authentication methods

- API key

## Related resources

ดูรายละเอียดเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [SeaTable's API documentation](https://api.seatable.io){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Environment**: เลือก environment ที่ตรงกับ SeaTable instance ของคุณ:
    - **Cloud-Hosted**
    - **Self-Hosted**
- **API Token (of a Base)**: สร้าง **Base-Token** ใน SeaTable จาก base options > **Advanced > API Token**
    - ใช้ permission แบบ **Read-Write** สำหรับ token ของคุณ
    - ดูวิธีสร้าง API token ได้ที่ [Creating an API token](https://seatable.io/en/docs/seatable-api/erzeugen-eines-api-tokens/){:target=_blank .external-link}
- **Timezone**: เลือก timezone ของ SeaTable server ของคุณ

