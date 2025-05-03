---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: เอกสารการทำงานกับ Label ของ Gmail node
description: เรียนรู้วิธีใช้ Label Operations ของ Gmail node ใน n8n ทำตามเอกสารทางเทคนิคเพื่อผสาน Label Operations เข้ากับ workflows ของคุณ
contentType: [integration, reference]
priority: high
---

# Gmail node Label Operations

ใช้ Label operations เพื่อสร้าง, ลบ, หรือดึงข้อมูล label เดียว หรือแสดงรายการ label ใน Gmail อ้างอิง [Gmail node](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ Gmail node

## Create a label

ใช้ operation นี้เพื่อสร้าง label ใหม่

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Label**
*   **Operation**: เลือก **Create**
*   **Name**: ป้อนชื่อที่แสดงสำหรับ label

### Create label options

ใช้ options เหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม:

*   **Label List Visibility**: ตั้งค่าการมองเห็นของ label ในรายการ label ในหน้าเว็บ Gmail เลือกจาก:
    *   **Hide**: ไม่แสดง label ในรายการ label
    *   **Show** (ค่าเริ่มต้น): แสดง label ในรายการ label
    *   **Show if Unread**: แสดง label หากมีข้อความที่ยังไม่ได้อ่านที่มี label นั้น
*   **Message List Visibility**: ตั้งค่าการมองเห็นของข้อความที่มี label นี้ในรายการข้อความในหน้าเว็บ Gmail เลือกว่าจะ **Show** หรือ **Hide** ข้อความที่มี label นี้

อ้างอิงเอกสาร [Gmail API Method: users.labels.create](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/create){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Delete a label

ใช้ operation นี้เพื่อลบ label ที่มีอยู่

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Label**
*   **Operation**: เลือก **Delete**
*   **Label ID**: ป้อน ID ของ label ที่คุณต้องการลบ

อ้างอิงเอกสาร [Gmail API Method: users.labels.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/delete){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Get a label

ใช้ operation นี้เพื่อดึงข้อมูล label ที่มีอยู่

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Label**
*   **Operation**: เลือก **Get**
*   **Label ID**: ป้อน ID ของ label ที่คุณต้องการดึงข้อมูล

อ้างอิงเอกสาร [Gmail API Method: users.labels.get](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/get){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

<!-- vale off -->
## Get Many labels
<!-- vale on -->

ใช้ operation นี้เพื่อดึงข้อมูลตั้งแต่สอง label ขึ้นไป

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Label**
*   **Operation**: เลือก **Get Many**
*   **Return All**: เลือกว่าจะให้ node คืนค่า label ทั้งหมด (เปิด) หรือจำกัดจำนวน (ปิด)
*   **Limit**: ป้อนจำนวน label สูงสุดที่จะคืนค่า ใช้เฉพาะเมื่อคุณปิด **Return All**

อ้างอิงเอกสาร [Gmail API Method: users.labels.list](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/list){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Common issues

สำหรับข้อผิดพลาดหรือปัญหาทั่วไปและขั้นตอนการแก้ไขที่แนะนำ โปรดอ้างอิง [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md)
