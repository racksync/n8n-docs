---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Trello credentials
description: เอกสารสำหรับ Trello credentials ใช้ credentials นี้เพื่อยืนยันตัวตน Trello ใน n8n ซึ่งเป็นแพลตฟอร์มสำหรับการทำงานอัตโนมัติ
contentType: [integration, reference]
priority: medium
---

# Trello credentials

คุณสามารถใช้ credentials นี้เพื่อยืนยันตัวตนกับ node ต่อไปนี้ได้:

- [Trello](/integrations/builtin/app-nodes/n8n-nodes-base.trello.md)
- [Trello Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.trellotrigger.md)

## Supported authentication methods

- API key

## Related resources

ดูข้อมูลเพิ่มเติมเกี่ยวกับบริการนี้ได้ที่ [Trello's API documentation](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/){:target=_blank .external-link}

## Using API key

ในการตั้งค่า credentials นี้ คุณจะต้องมีบัญชี [Trello](https://trello.com/){:target=_blank .external-link} และ:

- **API Key**
- **API Token**

วิธีสร้าง API Key และ API Token ให้สร้าง Trello Power-Up:

1. เปิด [Power-Up Admin Portal](https://trello.com/power-ups/admin){:target=_blank .external-link} ของ Trello
2. เลือก **New**
3. กรอก **Name** สำหรับ Power-Up เช่น `n8n integration`
4. เลือก **Workspace** ที่ Power-Up นี้จะเข้าถึง
5. ช่อง **iframe connector URL** ปล่อยว่างไว้
6. กรอกข้อมูลติดต่อที่จำเป็น
7. เลือก **Create**
8. ระบบจะเปิดหน้า **API Key** (ถ้าไม่เปิดให้ไปที่หน้านั้นเอง)
9. เลือก **Generate a new API Key**
10. คัดลอก **API key** จาก Trello แล้วนำไปใส่ใน n8n credential
11. ในหน้า API key ของ Trello ให้กรอก n8n base URL เป็น **Allowed origin**
12. ใน **Capabilities** ให้เลือก options ที่จำเป็น
13. เลือก **Token** ข้าง **API Key** ของ Trello
14. เมื่อระบบถาม ให้เลือก **Allow** เพื่ออนุญาต permission ทั้งหมด
15. คัดลอก **Token** ของ Trello แล้วนำไปใส่ใน n8n credential เป็น **API Token**

ดูรายละเอียดเพิ่มเติมเกี่ยวกับ API key และ token ได้ที่ [API Introduction](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#api-introduction){:target=_blank .external-link} และดูข้อมูลเกี่ยวกับ Power-Up ได้ที่ [Power-Up Admin Portal](https://developer.atlassian.com/cloud/trello/guides/power-ups/managing-power-ups/#power-up-admin-portal){:target=_blank .external-link}
