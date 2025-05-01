---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: NocoDB credentials
description: Documentation for NocoDB credentials. Use these credentials to authenticate NocoDB in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# NocoDB credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [NocoDB](/integrations/builtin/app-nodes/n8n-nodes-base.nocodb.md)

## Supported authentication methods

- API token (แนะนำ)
- User auth token

    /// note | User auth token deprecation
    NocoDB เลิกใช้ user auth tokens ในเวอร์ชัน v0.205.1 ให้ใช้ [API tokens](#using-api-token) แทน
    ///

## Related resources

อ้างอิง [NocoDB's API documentation](https://data-apis-v2.nocodb.com/){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้

## Using API token

ในการกำหนดค่า credential นี้ คุณจะต้องมี instance ของ [NocoDB](https://www.nocodb.com/){:target=_blank .external-link} และ:

- **API Token**
- **Host** ของฐานข้อมูลของคุณ

วิธีสร้าง API token:

1. เข้าสู่ระบบ NocoDB และเลือก **User menu** ที่แถบด้านข้างซ้ายล่าง
2. เลือก **Account Settings**
3. เปิดแท็บ **Tokens**
4. เลือก **Add new API token**
5. ป้อน **Name** สำหรับ token ของคุณ เช่น `n8n integration`
6. เลือก **Save**
7. คัดลอก **API Token** และป้อนลงใน credential ของ n8n
8. ป้อน **Host** ของ instance NocoDB ของคุณใน credential ของ n8n เช่น `http://localhost:8080`

อ้างอิงเอกสาร NocoDB [API Tokens documentation](https://docs.nocodb.com/account-settings/api-tokens/){:target=_blank .external-link} สำหรับคำแนะนำโดยละเอียดเพิ่มเติม

## Using user auth token

ก่อนที่ NocoDB จะเลิกใช้ user auth token เป็น token ชั่วคราวที่ออกแบบมาสำหรับการทดลอง API อย่างรวดเร็ว ซึ่งใช้ได้สำหรับ session จนกว่าผู้ใช้จะออกจากระบบ หรือเป็นเวลา 10 ชั่วโมง

/// note | User auth token deprecation
NocoDB เลิกใช้ user auth tokens ในเวอร์ชัน v0.205.1 ให้ใช้ [API tokens](#using-api-token) แทน
///

ในการกำหนดค่า credential นี้ คุณจะต้องมี instance ของ [NocoDB](https://www.nocodb.com/){:target=_blank .external-link} และ:

- **User Token**
- **Host** ของฐานข้อมูลของคุณ

วิธีสร้าง user auth token:

1. เข้าสู่ระบบ NocoDB และเลือก **User menu** ที่แถบด้านข้างซ้ายล่าง
2. เลือก **Copy Auth token**
3. ป้อน auth token นั้นเป็น **User Token** ใน n8n
4. ป้อน **Host** ของ instance NocoDB ของคุณ เช่น `http://localhost:8080`

อ้างอิงเอกสาร NocoDB [Auth Tokens documentation](https://docs.nocodb.com/account-settings/api-tokens/#auth-tokens){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
