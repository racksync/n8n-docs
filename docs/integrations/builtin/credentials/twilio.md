---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Twilio credentials
description: Documentation for Twilio credentials. Use these credentials to authenticate Twilio in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# Twilio credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Twilio](/integrations/builtin/app-nodes/n8n-nodes-base.twilio.md)
- [Twilio trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger.md)

## Supported authentication methods

- **Auth token**: Twilio แนะนำวิธีนี้สำหรับการทดสอบในเครื่องเท่านั้น
- **API key**: Twilio แนะนำวิธีนี้สำหรับ production

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Twilio's API documentation](https://www.twilio.com/docs){:target=_blank .external-link}

## Using Auth Token

ในการตั้งค่า credentials นี้ คุณจะต้องมีบัญชี [Twilio](https://twilio.com/){:target=_blank .external-link} และ:

- **Account SID** ของ Twilio
- **Auth Token** ของ Twilio

วิธีตั้งค่า credentials:

1. ใน n8n เลือก **Auth Token** เป็น **Auth Type**
2. ใน Twilio ไปที่ **Console Dashboard > Account Info**
3. คัดลอก **Account SID** แล้วนำไปใส่ใน n8n credential (ใช้เป็น username)
4. คัดลอก **Auth Token** แล้วนำไปใส่ใน n8n credential (ใช้เป็น password)

ดูรายละเอียดเพิ่มเติมได้ที่ [Auth Tokens and How to Change Them](https://help.twilio.com/articles/223136027-Auth-Tokens-and-How-to-Change-Them){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credentials นี้ คุณจะต้องมีบัญชี [Twilio](https://twilio.com/){:target=_blank .external-link} และ:

- **Account SID** ของ Twilio
- **API Key SID**: ได้จากการสร้าง API key
- **API Key Secret**: ได้จากการสร้าง API key

วิธีตั้งค่า credentials:

1. ใน n8n เลือก **API Key** เป็น **Auth Type**
2. ใน Twilio ไปที่ **Console Dashboard > Account Info**
3. คัดลอก **Account SID** แล้วนำไปใส่ใน n8n credential
4. ใน Twilio ไปที่ [**API keys & tokens**](https://www.twilio.com/console/project/api-keys) ของบัญชีคุณ
5. เลือก **Create API Key**
6. กรอก **Friendly name** สำหรับ API key เช่น `n8n integration`
7. เลือก **Key type** ที่ต้องการ n8n รองรับทั้ง **Main** และ **Standard** ดูรายละเอียดเพิ่มเติมที่ [Selecting an API key type](#selecting-an-api-key-type)
8. เลือก **Create API Key** เพื่อสร้าง key
5. ในหน้า **Copy secret key** คัดลอก **SID** ที่แสดงกับ key แล้วนำไปใส่ใน n8n credential **API Key SID**
6. ในหน้า **Copy secret key** คัดลอก **Secret** ที่แสดงกับ key แล้วนำไปใส่ใน n8n credential **API Key Secret**

ดูรายละเอียดเพิ่มเติมได้ที่ [Create an API key](https://www.twilio.com/docs/iam/api-keys#create-an-api-key){:target=_blank .external-link}

### Selecting an API key type

ตอนสร้าง Twilio API key คุณต้องเลือก key type โดย n8n credential รองรับ **Main** และ **Standard**

รายละเอียดของแต่ละ key type:

* **Main**: ให้สิทธิ์เท่ากับการใช้ Account SID และ Auth Token ใน API request
* **Standard**: ให้สิทธิ์เข้าถึงฟังก์ชันทั้งหมดใน Twilio API ยกเว้น API key resources และ Account resources
* **Restricted**: key type นี้ยังเป็น beta n8n ยังไม่ได้ทดสอบ credential กับ key type นี้ ถ้าคุณลองใช้แล้วพบปัญหาแจ้งเราได้เลย

ดูรายละเอียดเพิ่มเติมได้ที่ [Types of API keys](https://www.twilio.com/docs/iam/api-keys#types-of-api-keys){:target=_blank .external-link}
