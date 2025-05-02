---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Gmail node common issues
description: Documentation for common issues and questions in the Gmail node in n8n, a workflow automation platform. Includes details of the issue and suggested solutions.
contentType: [integration, reference]
priority: critical
---

# Gmail node common issues

นี่คือข้อผิดพลาดและปัญหาทั่วไปบางประการเกี่ยวกับ [Gmail node](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md) และขั้นตอนในการแก้ไขหรือแก้ไขปัญหา

## Remove the n8n attribution from sent messages

หากคุณใช้ node เพื่อ [send a message](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#send-a-message) หรือ [reply to a message](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#reply-to-a-message) node จะเพิ่มข้อความนี้ต่อท้ายอีเมล:

> This email was sent automatically with n8n

หากต้องการลบข้อความระบุแหล่งที่มานี้:

1.  ในส่วน **Options** ของ node เลือก **Add option**
2.  เลือก **Append n8n attribution**
3.  ปิด toggle

อ้างอิง [Send options](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#send-options) และ [Reply options](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#reply-options) สำหรับข้อมูลเพิ่มเติม

## Forbidden - perhaps check your credentials

ข้อผิดพลาดนี้จะแสดงถัดจาก dropdown บางรายการใน node เช่น dropdown **Label Names or IDs** ข้อความเต็มๆ จะมีลักษณะประมาณนี้:

```
There was a problem loading the parameter options from server: "Forbidden - perhaps check your credentials?"
```

ข้อผิดพลาดนี้มักจะแสดงเมื่อคุณใช้ Google Service Account เป็น credential และ credential นั้นไม่ได้เปิดใช้งาน **Impersonate a User**

อ้างอิง [Google Service Account: Finish your n8n credential](/integrations/builtin/credentials/google/service-account.md#finish-your-n8n-credential) สำหรับข้อมูลเพิ่มเติม

## 401 unauthorized error

ข้อความเต็มๆ ของข้อผิดพลาดมีลักษณะดังนี้:
<!--vale off-->
```
401 - {"error":"unauthorized_client","error_description":"Client is unauthorized to retrieve access tokens using this method, or client not authorized for any of the scopes requested."}
```
<!--vale on-->

ข้อผิดพลาดนี้เกิดขึ้นเมื่อมีปัญหากับ credential ที่คุณใช้อยู่และ scopes หรือ permissions ของมัน

วิธีแก้ไข:

1.  สำหรับ [OAuth2](/integrations/builtin/credentials/google/oauth-single-service.md) credentials ตรวจสอบให้แน่ใจว่าคุณได้เปิดใช้งาน Gmail API ใน **APIs & Services > Library** อ้างอิง [Google OAuth2 Single Service - Enable APIs](/integrations/builtin/credentials/google/oauth-single-service.md#enable-apis) สำหรับข้อมูลเพิ่มเติม
2.  สำหรับ [Service Account](/integrations/builtin/credentials/google/service-account.md) credentials:
    1.  [Enable domain-wide delegation](/integrations/builtin/credentials/google/service-account.md#enable-domain-wide-delegation)
    2.  ตรวจสอบให้แน่ใจว่าคุณได้เพิ่ม Gmail API เป็นส่วนหนึ่งของการกำหนดค่า domain-wide delegation

## Bad request - please check your parameters

ข้อผิดพลาดนี้มักเกิดขึ้นหากคุณป้อน Message ID, Thread ID หรือ Label ID ที่ไม่มีอยู่จริง

ลองใช้ **Get** operation กับ ID นั้นเพื่อยืนยันว่ามีอยู่จริง
