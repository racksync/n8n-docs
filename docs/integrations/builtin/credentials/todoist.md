---
title: คู่มือ Todoist credentials
description: คู่มือการตั้งค่า Todoist credentials สำหรับเชื่อมต่อ Todoist กับ n8n
contentType: [integration, reference]
priority: medium
---

# Todoist credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Todoist](/integrations/builtin/app-nodes/n8n-nodes-base.todoist.md)

## Supported authentication methods

- API key
- OAuth2

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Todoist's REST API documentation](https://developer.todoist.com/rest/v2/#overview){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credentials นี้ คุณจะต้องมีบัญชี [Todoist](https://todoist.com/){:target=_blank .external-link} และ:

- **API Key**

วิธีขอ **API Key**:

1. ใน Todoist ให้เปิด [**Integration settings**](https://todoist.com/prefs/integrations){:target=_blank .external-link}
2. เลือกแท็บ **Developer**
3. คัดลอก **API token** แล้วนำไปใส่ใน n8n credential เป็น **API Key**

ดูรายละเอียดเพิ่มเติมได้ที่ [Find your API token](https://todoist.com/help/articles/find-your-api-token-Jpzx9IIlB){:target=_blank .external-link}

## Using OAuth2

--8<-- "_snippets/integrations/builtin/credentials/cloud-oauth-button.md"

ถ้าคุณ [self-hosting](/hosting/index.md) n8n คุณจะต้องมีบัญชี [Todoist](https://todoist.com/){:target=_blank .external-link} และ:

- **Client ID**
- **Client Secret**

ขอทั้งสองอย่างนี้ได้โดยการสร้างแอปพลิเคชัน:

1. เปิด [App Management Console](https://developer.todoist.com/appconsole.html){:target=_blank .external-link} ของ Todoist
2. เลือก **Create a new app**
3. กรอก **App name** เช่น `n8n integration`
4. เลือก **Create app**
5. คัดลอก **OAuth Redirect URL** ของ n8n ไปใส่ใน Todoist เป็น **OAuth redirect URL**
6. คัดลอก **Client ID** จาก Todoist ไปใส่ใน n8n credential
7. คัดลอก **Client Secret** จาก Todoist ไปใส่ใน n8n credential
8. ตั้งค่าแอป Todoist ที่เหลือตามที่เหมาะสมกับการใช้งานของคุณ

ดูรายละเอียดเพิ่มเติมได้ที่ [Authorization Guide](https://developer.todoist.com/guides/#authorization){:target=_blank .external-link}
