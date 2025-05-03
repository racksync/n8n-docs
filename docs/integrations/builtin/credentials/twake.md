---
title: คู่มือ Twake credentials
description: คู่มือการตั้งค่า Twake credentials สำหรับเชื่อมต่อ Twake กับ n8n
contentType: [integration, reference]
---

# Twake credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Twake](/integrations/builtin/app-nodes/n8n-nodes-base.twake.md)

## Prerequisites

สร้างบัญชี [Twake](https://twake.app/){:target=_blank .external-link} ก่อน

## Supported authentication methods

- Cloud API key
- Server API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Twake's documentation](https://doc.twake.app/developers-api/api-reference){:target=_blank .external-link}

## Using Cloud API key

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Workspace Key**: ได้จากการติดตั้งแอป **n8n** ใน Twake Cloud environment แล้วเลือก **Configure** ดูรายละเอียดเพิ่มเติมได้ที่ [How to connect n8n to Twake](https://help.twake.app/en/latest/applications/connectors/index.html#how-to-connect-n8n-to-twake){:target=_blank .external-link}

## Using Server API key

ในการตั้งค่า credentials นี้ คุณจะต้องมี:

- **Host URL**: URL ของ Twake self-hosted instance ของคุณ
- **Public ID**: ได้จากการสร้างแอป
- **Private API Key**: ได้จากการสร้างแอป

วิธีสร้าง **Public ID** และ **Private API Key** ให้ [สร้าง Twake application](https://doc.twake.app/developers-api/get-started/create-your-first-application){:target=_blank .external-link}:

1. ไปที่ **Workspace Settings > Applications and connectors > Access your applications and connectors > Create an application**
2. กรอกข้อมูลที่จำเป็น
3. เมื่อสร้างแอปแล้ว ให้ดูที่ **API Details**
4. คัดลอก **Public identifier** แล้วนำไปใส่ใน n8n เป็น **Public ID**
5. คัดลอก **Private key** แล้วนำไปใส่ใน n8n เป็น **Private API Key**

ดูรายละเอียดเพิ่มเติมได้ที่ [API settings](https://doc.twake.app/developers-api/get-started/create-your-first-application#id-3.-api-settings){:target=_blank .external-link}