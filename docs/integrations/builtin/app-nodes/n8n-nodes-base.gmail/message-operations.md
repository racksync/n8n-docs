---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Gmail node Message Operations documentation
description: Learn how to use the Message Operations of the Gmail node in n8n. Follow technical documentation to integrate Message Operations into your workflows.
contentType: [integration, reference]
priority: high
---

# Gmail node Message Operations

ใช้ Message operations เพื่อส่ง, ตอบกลับ, ลบ, ทำเครื่องหมายว่าอ่านแล้วหรือยังไม่ได้อ่าน, เพิ่ม label, ลบ label, หรือดึงข้อมูลข้อความเดียว หรือดึงรายการข้อความใน Gmail อ้างอิง [Gmail node](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ Gmail node

## Add Label to a message

ใช้ operation นี้เพื่อเพิ่ม label อย่างน้อยหนึ่งรายการให้กับข้อความ

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Message**
*   **Operation**: เลือก **Add Label**
*   **Message ID**: ป้อน ID ของข้อความที่คุณต้องการเพิ่ม label
*   **Label Names or IDs**: เลือกชื่อ Label ที่คุณต้องการเพิ่ม หรือป้อน expression เพื่อระบุ ID รายการใน dropdown จะขึ้นอยู่กับ **Credential** ที่คุณเลือก

<!-- vale off -->
อ้างอิงเอกสาร [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
<!-- vale on -->

## Delete a message

ใช้ operation นี้เพื่อลบข้อความทันทีและถาวร

/// note | การลบถาวร
Operation นี้ไม่สามารถยกเลิกได้ หากต้องการลบแบบกู้คืนได้ ให้ใช้ [Thread Trash operation](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md#trash-a-thread) แทน
///

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Message**
*   **Operation**: เลือก **Delete**
*   **Message ID**: ป้อน ID ของข้อความที่คุณต้องการลบ

อ้างอิงเอกสาร [Gmail API Method: users.messages.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/delete){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Get a message

ใช้ operation นี้เพื่อดึงข้อมูลข้อความเดียว

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Message**
*   **Operation**: เลือก **Get**
*   **Message ID**: ป้อน ID ของข้อความที่คุณต้องการดึงข้อมูล
*   **Simplify**: เลือกว่าจะให้แสดงผลลัพธ์แบบง่าย (เปิด) หรือข้อมูลดิบ (ปิด) ค่าเริ่มต้นคือเปิด
    *   ซึ่งเหมือนกับการตั้งค่า `format` สำหรับ API call เป็น `metadata` ซึ่งจะคืนค่า ID ของข้อความอีเมล, label และ header ของอีเมล รวมถึง: From, To, CC, BCC และ Subject

อ้างอิงเอกสาร [Gmail API Method: users.messages.get](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

<!-- vale off -->
## Get Many messages
<!-- vale on -->

ใช้ operation นี้เพื่อดึงข้อมูลตั้งแต่สองข้อความขึ้นไป

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Message**
*   **Operation**: เลือก **Get Many**
*   **Return All**: เลือกว่าจะให้ node คืนค่าข้อความทั้งหมด (เปิด) หรือจำกัดจำนวน (ปิด)
*   **Limit**: ป้อนจำนวนข้อความสูงสุดที่จะคืนค่า ใช้เฉพาะเมื่อคุณปิด **Return All**
*   **Simplify**: เลือกว่าจะให้แสดงผลลัพธ์แบบง่าย (เปิด) หรือข้อมูลดิบ (ปิด) ค่าเริ่มต้นคือเปิด
    *   ซึ่งเหมือนกับการตั้งค่า `format` สำหรับ API call เป็น `metadata` ซึ่งจะคืนค่า ID ของข้อความอีเมล, label และ header ของอีเมล รวมถึง: From, To, CC, BCC และ Subject

<!-- vale off -->
### Get Many messages filters
<!-- vale on -->

ใช้ filters เหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม:

*   **Include Spam and Trash**: เลือกว่าจะให้ node ดึงข้อความในโฟลเดอร์ Spam และ Trash (เปิด) หรือไม่ (ปิด)
*   **Label Names or IDs**: คืนค่าเฉพาะข้อความที่มี label ที่เลือกเพิ่มอยู่เท่านั้น เลือกชื่อ Label ที่คุณต้องการใช้ หรือป้อน expression เพื่อระบุ ID รายการใน dropdown จะขึ้นอยู่กับ **Credential** ที่คุณเลือก
*   **Search**: ป้อน filter การค้นหาของ Gmail เช่น `from:` เพื่อกรองข้อความที่จะคืนค่า อ้างอิง [Refine searches in Gmail](https://support.google.com/mail/answer/7190?hl=en){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
*   **Read Status**: เลือกว่าจะรับ **Unread and read emails**, **Unread emails only** (ค่าเริ่มต้น), หรือ **Read emails only**
*   **Received After**: คืนค่าเฉพาะอีเมลที่ได้รับหลังจากวันที่และเวลาที่ระบุ ใช้ตัวเลือกวันที่เพื่อเลือกวันและเวลา หรือป้อน expression เพื่อตั้งค่าวันที่เป็น string ในรูปแบบ ISO หรือ timestamp ในหน่วยมิลลิวินาที อ้างอิง [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับรูปแบบ string
*   **Received Before**: คืนค่าเฉพาะอีเมลที่ได้รับก่อนวันที่และเวลาที่ระบุ ใช้ตัวเลือกวันที่เพื่อเลือกวันและเวลา หรือป้อน expression เพื่อตั้งค่าวันที่เป็น string ในรูปแบบ ISO หรือ timestamp ในหน่วยมิลลิวินาที อ้างอิง [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติมเกี่ยวกับรูปแบบ string
*   **Sender**: ป้อนอีเมลหรือส่วนหนึ่งของชื่อผู้ส่งเพื่อคืนค่าข้อความจากผู้ส่งนั้นเท่านั้น

อ้างอิงเอกสาร [Gmail API Method: users.messages.list](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Mark as Read

ใช้ operation นี้เพื่อทำเครื่องหมายข้อความว่าอ่านแล้ว

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Message**
*   **Operation**: เลือก **Mark as Read**
*   **Message ID**: ป้อน ID ของข้อความที่คุณต้องการทำเครื่องหมายว่าอ่านแล้ว

<!-- vale off -->
อ้างอิงเอกสาร [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
<!-- vale on -->

## Mark as Unread

ใช้ operation นี้เพื่อทำเครื่องหมายข้อความว่ายังไม่ได้อ่าน

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Message**
*   **Operation**: เลือก **Mark as Unread**
*   **Message ID**: ป้อน ID ของข้อความที่คุณต้องการทำเครื่องหมายว่ายังไม่ได้อ่าน

<!-- vale off -->
อ้างอิงเอกสาร [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
<!-- vale on -->

## Remove Label from a message

ใช้ operation นี้เพื่อลบ label อย่างน้อยหนึ่งรายการออกจากข้อความ

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Message**
*   **Operation**: เลือก **Remove Label**
*   **Message ID**: ป้อน ID ของข้อความที่คุณต้องการลบ label ออก
*   **Label Names or IDs**: เลือกชื่อ Label ที่คุณต้องการลบ หรือป้อน expression เพื่อระบุ ID รายการใน dropdown จะขึ้นอยู่กับ **Credential** ที่คุณเลือก

<!-- vale off -->
อ้างอิงเอกสาร [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม
<!-- vale on -->

## Reply to a message

ใช้ operation นี้เพื่อส่งข้อความตอบกลับข้อความที่มีอยู่

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Message**
*   **Operation**: เลือก **Reply**
*   **Message ID**: ป้อน ID ของข้อความที่คุณต้องการตอบกลับ
*   เลือก **Email Type** เลือกจาก **Text** หรือ **HTML**
*   **Message**: ป้อนเนื้อหาของอีเมล

### Reply options

ใช้ options เหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม:

*   **Append n8n attribution**: โดยค่าเริ่มต้น node จะเพิ่มข้อความ `This email was sent automatically with n8n` ต่อท้ายอีเมล หากต้องการลบข้อความนี้ ให้ปิด option นี้
*   **Attachments**: เลือก **Add Attachment** เพื่อเพิ่มไฟล์แนบ ป้อน **Attachment Field Name (in Input)** เพื่อระบุว่า field ใดจาก input node ที่มีไฟล์แนบ
    *   สำหรับหลาย properties ให้ป้อนรายการที่คั่นด้วยจุลภาค
*   **BCC**: ป้อนที่อยู่อีเมลอย่างน้อยหนึ่งรายการสำหรับผู้รับสำเนาลับ แยกหลายที่อยู่อีเมลด้วยจุลภาค เช่น `jay@gatsby.com, jon@smith.com`
*   **CC**: ป้อนที่อยู่อีเมลอย่างน้อยหนึ่งรายการสำหรับผู้รับสำเนา แยกหลายที่อยู่อีเมลด้วยจุลภาค เช่น `jay@gatsby.com, jon@smith.com`
*   **Sender Name**: ป้อนชื่อที่คุณต้องการให้แสดงในอีเมลของผู้รับว่าเป็นผู้ส่ง
*   **Reply to Sender Only**: เลือกว่าจะตอบกลับทุกคน (ปิด) หรือตอบกลับเฉพาะผู้ส่ง (เปิด)

อ้างอิงเอกสาร [Gmail API Method: users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Send a message

ใช้ operation นี้เพื่อส่งข้อความ

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Message**
*   **Operation**: เลือก **Send**
*   **To**: ป้อนที่อยู่อีเมลที่คุณต้องการส่งอีเมลไปถึง
*   **Subject**: ป้อนหัวเรื่อง
*   เลือก **Email Type** เลือกจาก **Text** หรือ **HTML**
*   **Message**: ป้อนเนื้อหาของอีเมล

### Send options

ใช้ options เหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม:

*   **Append n8n attribution**: โดยค่าเริ่มต้น node จะเพิ่มข้อความ `This email was sent automatically with n8n` ต่อท้ายอีเมล หากต้องการลบข้อความนี้ ให้ปิด option นี้
*   **Attachments**: เลือก **Add Attachment** เพื่อเพิ่มไฟล์แนบ ป้อน **Attachment Field Name (in Input)** เพื่อระบุว่า field ใดจาก input node ที่มีไฟล์แนบ
    *   สำหรับหลาย properties ให้ป้อนรายการที่คั่นด้วยจุลภาค
*   **BCC**: ป้อนที่อยู่อีเมลอย่างน้อยหนึ่งรายการสำหรับผู้รับสำเนาลับ แยกหลายที่อยู่อีเมลด้วยจุลภาค เช่น `jay@gatsby.com, jon@smith.com`
*   **CC**: ป้อนที่อยู่อีเมลอย่างน้อยหนึ่งรายการสำหรับผู้รับสำเนา แยกหลายที่อยู่อีเมลด้วยจุลภาค เช่น `jay@gatsby.com, jon@smith.com`
*   **Sender Name**: ป้อนชื่อที่คุณต้องการให้แสดงในอีเมลของผู้รับว่าเป็นผู้ส่ง
*   **Send Replies To**: ป้อนที่อยู่อีเมลเพื่อตั้งเป็นที่อยู่สำหรับตอบกลับ
*   **Reply to Sender Only**: เลือกว่าจะตอบกลับทุกคน (ปิด) หรือตอบกลับเฉพาะผู้ส่ง (เปิด)

อ้างอิงเอกสาร [Gmail API Method: users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Send a message and wait for approval

ใช้ operation นี้เพื่อส่งข้อความและรอการอนุมัติจากผู้รับก่อนที่จะดำเนินการ workflow ต่อไป

/// info | ใช้ Wait สำหรับการอนุมัติที่ซับซ้อน
Operation **Send and Wait for Approval** เหมาะสำหรับกระบวนการอนุมัติที่ไม่ซับซ้อน สำหรับการอนุมัติที่ซับซ้อนกว่านี้ ให้พิจารณาใช้ [Wait node](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md)
///

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Message**
*   **Operation**: เลือก **Send and Wait for Approval**
*   **To**: ป้อนที่อยู่อีเมลที่คุณต้องการส่งอีเมลไปถึง
*   **Subject**: ป้อนหัวเรื่อง
*   **Message**: ป้อนเนื้อหาของอีเมล

### Send and wait for approval options

ใช้ options เหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม:

*   **Type of Approval**: เลือก **Approve Only** (ค่าเริ่มต้น) เพื่อใส่เฉพาะปุ่มอนุมัติ หรือ **Approve and Disapprove** เพื่อใส่ตัวเลือกไม่อนุมัติด้วย
*   **Approve Button Label**: ข้อความที่จะใช้สำหรับปุ่มอนุมัติ (ค่าเริ่มต้นคือ **Approve**)
*   **Approve Button Style**: เลือกว่าจะจัดรูปแบบปุ่มอนุมัติเป็น **Primary** (ค่าเริ่มต้น) หรือ **Secondary**
*   **Disapprove Button Label**: ข้อความที่จะใช้สำหรับปุ่มไม่อนุมัติ (ค่าเริ่มต้นคือ **Decline**) จะมองเห็นได้เฉพาะเมื่อคุณตั้งค่า **Type of Approval** เป็น **Approve and Disapprove**
*   **Disapprove Button Style**: เลือกว่าจะจัดรูปแบบปุ่มไม่อนุมัติเป็น **Primary** หรือ **Secondary** (ค่าเริ่มต้น) จะมองเห็นได้เฉพาะเมื่อคุณตั้งค่า **Type of Approval** เป็น **Approve and Disapprove**

อ้างอิงเอกสาร [Gmail API Method: users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Common issues

สำหรับข้อผิดพลาดหรือปัญหาทั่วไปและขั้นตอนการแก้ไขที่แนะนำ โปรดอ้างอิง [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md)
