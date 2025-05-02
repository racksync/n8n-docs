---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Gmail node Thread Operations documentation
description: Learn how to use the Thread Operations of the Gmail node in n8n. Follow technical documentation to integrate Thread Operations into your workflows.
contentType: [integration, reference]
priority: high
---

# Gmail node Thread Operations

ใช้ Thread operations เพื่อลบ, ตอบกลับ, ย้ายไปถังขยะ, นำออกจากถังขยะ, เพิ่ม/ลบ label, ดึงข้อมูลหนึ่งรายการ หรือแสดงรายการ thread ทั้งหมด อ้างอิง [Gmail node](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ Gmail node

## Add Label to a thread

ใช้ operation นี้เพื่อเพิ่ม label ให้กับ thread

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Thread**
*   **Operation**: เลือก **Add Label**
*   **Thread ID**: ป้อน ID ของ thread ที่คุณต้องการเพิ่ม label
*   **Label Names or IDs**: เลือกชื่อ Label ที่คุณต้องการใช้ หรือป้อน expression เพื่อระบุ ID รายการใน dropdown จะขึ้นอยู่กับ **Credential** ที่คุณเลือก

<!-- vale off -->
อ้างอิงเอกสาร [Gmail API Method: users.threads.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/modify){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
<!-- vale on -->

## Delete a thread

ใช้ operation นี้เพื่อลบ thread และข้อความทั้งหมดในนั้นทันทีและถาวร

/// note | การลบถาวร
Operation นี้ไม่สามารถยกเลิกได้ หากต้องการลบแบบกู้คืนได้ ให้ใช้ [Trash operation](#trash-a-thread) แทน
///

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Thread**
*   **Operation**: เลือก **Delete**
*   **Thread ID**: ป้อน ID ของ thread ที่คุณต้องการลบ

อ้างอิงเอกสาร [Gmail API Method: users.threads.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/delete){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Get a thread

ใช้ operation นี้เพื่อดึงข้อมูล thread เดียว

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Thread**
*   **Operation**: เลือก **Get**
*   **Thread ID**: ป้อน ID ของ thread ที่คุณต้องการดึงข้อมูล
*   **Simplify**: เลือกว่าจะให้แสดงผลลัพธ์แบบง่าย (เปิด) หรือข้อมูลดิบ (ปิด) ค่าเริ่มต้นคือเปิด
    *   ซึ่งเหมือนกับการตั้งค่า `format` สำหรับ API call เป็น `metadata` ซึ่งจะคืนค่า ID ของข้อความอีเมล, label และ header ของอีเมล รวมถึง: From, To, CC, BCC และ Subject

### Get thread options

ใช้ options เหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม:

*   **Return Only Messages**: เลือกว่าจะให้คืนค่าเฉพาะข้อความใน thread (เปิด) หรือไม่

อ้างอิงเอกสาร [Gmail API Method: users.threads.get](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/get){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

<!-- vale off -->
## Get Many threads
<!-- vale on -->

ใช้ operation นี้เพื่อดึงข้อมูลตั้งแต่สอง thread ขึ้นไป

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Thread**
*   **Operation**: เลือก **Get Many**
*   **Return All**: เลือกว่าจะให้ node คืนค่า thread ทั้งหมด (เปิด) หรือจำกัดจำนวน (ปิด)
*   **Limit**: ป้อนจำนวน thread สูงสุดที่จะคืนค่า ใช้เฉพาะเมื่อคุณปิด **Return All**

<!-- vale off -->
### Get Many threads filters
<!-- vale on -->

ใช้ filters เหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม:

*   **Include Spam and Trash**: เลือกว่าจะให้ node ดึง thread ในโฟลเดอร์ Spam และ Trash (เปิด) หรือไม่ (ปิด)
*   **Label Names or IDs**: คืนค่าเฉพาะ thread ที่มี label ที่เลือกเพิ่มอยู่เท่านั้น เลือกชื่อ Label ที่คุณต้องการใช้ หรือป้อน expression เพื่อระบุ ID รายการใน dropdown จะขึ้นอยู่กับ **Credential** ที่คุณเลือก
*   **Search**: ป้อน filter การค้นหาของ Gmail เช่น `from:` เพื่อกรอง thread ที่จะคืนค่า อ้างอิง [Refine searches in Gmail](https://support.google.com/mail/answer/7190?hl=en){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
*   **Read Status**: เลือกว่าจะรับ **Unread and read emails**, **Unread emails only** (ค่าเริ่มต้น), หรือ **Read emails only**
*   **Received After**: คืนค่าเฉพาะอีเมลที่ได้รับหลังจากวันที่และเวลาที่ระบุ ใช้ตัวเลือกวันที่เพื่อเลือกวันและเวลา หรือป้อน expression เพื่อตั้งค่าวันที่เป็น string ในรูปแบบ ISO หรือ timestamp ในหน่วยมิลลิวินาที อ้างอิง [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับรูปแบบ string
*   **Received Before**: คืนค่าเฉพาะอีเมลที่ได้รับก่อนวันที่และเวลาที่ระบุ ใช้ตัวเลือกวันที่เพื่อเลือกวันและเวลา หรือป้อน expression เพื่อตั้งค่าวันที่เป็น string ในรูปแบบ ISO หรือ timestamp ในหน่วยมิลลิวินาที อ้างอิง [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับรูปแบบ string

อ้างอิงเอกสาร [Gmail API Method: users.threads.list](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/list){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Remove label from a thread

ใช้ operation นี้เพื่อลบ label ออกจาก thread

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Thread**
*   **Operation**: เลือก **Remove Label**
*   **Thread ID**: ป้อน ID ของ thread ที่คุณต้องการลบ label ออก
*   **Label Names or IDs**: เลือกชื่อ Label ที่คุณต้องการลบ หรือป้อน expression เพื่อระบุ ID รายการใน dropdown จะขึ้นอยู่กับ **Credential** ที่คุณเลือก

<!-- vale off -->
อ้างอิงเอกสาร [Gmail API Method: users.threads.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/modify){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
<!-- vale on -->

## Reply to a message

ใช้ operation นี้เพื่อตอบกลับข้อความ

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Thread**
*   **Operation**: เลือก **Reply**
*   **Thread ID**: ป้อน ID ของ thread ที่คุณต้องการตอบกลับ
*   **Message Snippet or ID**: เลือกข้อความที่คุณต้องการตอบกลับ หรือป้อน expression เพื่อระบุ ID รายการใน dropdown จะขึ้นอยู่กับ **Credential** ที่คุณเลือก
*   เลือก **Email Type** เลือกจาก **Text** หรือ **HTML**
*   **Message**: ป้อนเนื้อหาของอีเมล

### Reply options

ใช้ options เหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม:

*   **Attachments**: เลือก **Add Attachment** เพื่อเพิ่มไฟล์แนบ ป้อน **Attachment Field Name (in Input)** เพื่อระบุว่า field ใดจาก input node ที่มีไฟล์แนบ
    *   สำหรับหลาย properties ให้ป้อนรายการที่คั่นด้วยจุลภาค
*   **BCC**: ป้อนที่อยู่อีเมลอย่างน้อยหนึ่งรายการสำหรับผู้รับสำเนาลับ แยกหลายที่อยู่อีเมลด้วยจุลภาค เช่น `jay@gatsby.com, jon@smith.com`
*   **CC**: ป้อนที่อยู่อีเมลอย่างน้อยหนึ่งรายการสำหรับผู้รับสำเนา แยกหลายที่อยู่อีเมลด้วยจุลภาค เช่น `jay@gatsby.com, jon@smith.com`
*   **Sender Name**: ป้อนชื่อที่คุณต้องการให้แสดงในอีเมลของผู้รับว่าเป็นผู้ส่ง
*   **Reply to Sender Only**: เลือกว่าจะตอบกลับทุกคน (ปิด) หรือตอบกลับเฉพาะผู้ส่ง (เปิด)

อ้างอิงเอกสาร [Gmail API Method: users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Trash a thread

ใช้ operation นี้เพื่อย้าย thread และข้อความทั้งหมดในนั้นไปยังถังขยะ

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Thread**
*   **Operation**: เลือก **Trash**
*   **Thread ID**: ป้อน ID ของ thread ที่คุณต้องการย้ายไปยังถังขยะ

อ้างอิงเอกสาร [Gmail API Method: users.threads.trash](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/trash){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Untrash a thread

ใช้ operation นี้เพื่อกู้คืน thread และข้อความทั้งหมดในนั้นจากถังขยะ

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Thread**
*   **Operation**: เลือก **Untrash**
*   **Thread ID**: ป้อน ID ของ thread ที่คุณต้องการนำออกจากถังขยะ

อ้างอิงเอกสาร [Gmail API Method: users.threads.untrash](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/untrash){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Common issues

สำหรับข้อผิดพลาดหรือปัญหาทั่วไปและขั้นตอนการแก้ไขที่แนะนำ โปรดอ้างอิง [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md)
