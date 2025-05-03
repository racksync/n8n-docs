---
title: ข้อมูลเข้าสู่ระบบ SyncroMSP
description: คู่มือการตั้งค่า SyncroMSP credentials สำหรับเชื่อมต่อ SyncroMSP กับ n8n
contentType: [integration, reference]
---

# SyncroMSP credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [SyncroMSP](/integrations/builtin/app-nodes/n8n-nodes-base.syncromsp.md)

## Prerequisites

สร้างบัญชี [SyncroMSP](https://syncromsp.com/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [SyncroMSP's API documentation](https://api-docs.syncromsp.com/){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **API Key**: ใน SyncroMSP เรียกว่า **API token** วิธีสร้าง API token ให้ไปที่ **user menu > Profile/Password > API Tokens** แล้วเลือก **Create New Token** จากนั้นเลือก **Custom Permissions** เพื่อกรอกชื่อ token และกำหนด permission ตามที่ต้องการ
- **Subdomain** ของคุณ: กรอก subdomain ของ SyncroMSP ซึ่งจะอยู่ใน URL ระหว่าง `https://` และ `.syncromsp.com` เช่น ถ้า URL คือ `https://n8n-instance.syncromsp.com` ให้กรอก `n8n-instance` เป็น subdomain

ดูข้อมูลเพิ่มเติมเกี่ยวกับการสร้าง token ได้ที่ [API Tokens](https://community.syncromsp.com/t/api-tokens/2297){:target=_blank .external-link}
