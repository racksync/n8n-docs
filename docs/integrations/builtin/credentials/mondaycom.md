---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: monday.com credentials
description: Documentation for monday.com credentials. Use these credentials to authenticate monday.com in n8n, a workflow automation platform.
contentType: [integration, reference]
priority: medium
---

# monday.com credentials

คุณสามารถใช้ credentials เหล่านี้เพื่อยืนยันตัวตนใน nodes ต่อไปนี้:

- [monday.com](/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom.md)

/// info | Minimum required version
node monday.com ต้องการ n8n เวอร์ชัน 1.22.6 หรือสูงกว่า
///

## Supported authentication methods

- API token
- OAuth2

## Related resources

อ้างอิง [monday.com's API documentation](https://developer.monday.com/api-reference/docs/basics){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการยืนยันตัวตนกับบริการ

## Using API token

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [monday.com](https://monday.com/){:target=_blank .external-link} และ:

- **Token V2** ของ API

วิธีรับ token ของคุณ:

1. ในบัญชี monday.com ของคุณ เลือกรูปโปรไฟล์ของคุณที่มุมขวาบน
2. เลือก **Developers** Developer Center จะเปิดขึ้นในแท็บใหม่
3. ใน Developer Center เลือก **My Access Tokens > Show**
4. คัดลอก personal token ของคุณและป้อนลงใน credential ของ n8n เป็น **Token V2**

อ้างอิง [monday.com API Authentication](https://developer.monday.com/api-reference/docs/authentication){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Using OAuth2

ในการกำหนดค่า credential นี้ คุณจะต้องมีบัญชี [monday.com](https://monday.com/){:target=_blank .external-link} และ:

- **Client ID**
- **Client Secret**

วิธีสร้างฟิลด์ทั้งสองนี้ ให้ลงทะเบียนแอปพลิเคชัน monday.com ใหม่:

1. ในบัญชี monday.com ของคุณ เลือกรูปโปรไฟล์ของคุณที่มุมขวาบน
2. เลือก **Developers** Developer Center จะเปิดขึ้นในแท็บใหม่
3. ใน Developer Center เลือก **Build app** รายละเอียดแอปจะเปิดขึ้น
4. ป้อน **Name** สำหรับแอปของคุณ เช่น `n8n integration`
5. คัดลอก **Client ID** และป้อนลงใน credential ของ n8n
6. **Show** **Client Secret** คัดลอก และป้อนลงใน credential ของ n8n
7. ในเมนูด้านซ้าย เลือก **OAuth**
8. สำหรับ **Scopes** เลือก `boards:write` และ `boards:read`
9. เลือก **Save Scopes**
10. เลือกแท็บ **Redirect URLs**
11. คัดลอก **OAuth Redirect URL** จาก n8n และป้อนเป็น **Redirect URL**
12. **Save** การเปลี่ยนแปลงของคุณใน monday.com
13. ใน n8n เลือก **Connect my account** เพื่อสิ้นสุดการตั้งค่า

 อ้างอิง [Create an app](https://developer.monday.com/apps/docs/create-an-app){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการสร้างแอป
 
 อ้างอิง [OAuth and permissions](https://developer.monday.com/apps/docs/oauth){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ scopes ที่มีอยู่และการตั้งค่า Redirect URL
