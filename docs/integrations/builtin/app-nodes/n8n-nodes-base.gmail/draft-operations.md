---
#https://www.notion.so/n8n/Frontmatter-432c2b8dff1f43d4b1c8d20075510fe4
title: Gmail node Draft Operations documentation
description: Learn how to use the Draft Operations of the Gmail node in n8n. Follow technical documentation to integrate Draft Operations into your workflows.
contentType: [integration, reference]
priority: high
---

# Gmail node Draft Operations

ใช้ Draft operations เพื่อสร้าง, ลบ, หรือดึงข้อมูล draft เดียว หรือแสดงรายการ draft ใน Gmail อ้างอิง [Gmail node](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md) สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ Gmail node

## Create a draft

ใช้ operation นี้เพื่อสร้าง draft ใหม่

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Draft**
*   **Operation**: เลือก **Create**
*   **Subject**: ป้อนหัวเรื่อง
*   เลือก **Email Type** เลือกจาก **Text** หรือ **HTML**
*   **Message**: ป้อนเนื้อหาของอีเมล

### Create draft options

ใช้ options เหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม:

*   **Attachments**: เลือก **Add Attachment** เพื่อเพิ่มไฟล์แนบ ป้อน **Attachment Field Name (in Input)** เพื่อระบุว่า field ใดจาก input node ที่มีไฟล์แนบ
    *   สำหรับหลาย properties ให้ป้อนรายการที่คั่นด้วยจุลภาค
*   **BCC**: ป้อนที่อยู่อีเมลอย่างน้อยหนึ่งรายการสำหรับผู้รับสำเนาลับ แยกหลายที่อยู่อีเมลด้วยจุลภาค เช่น `jay@gatsby.com, jon@smith.com`
*   **CC**: ป้อนที่อยู่อีเมลอย่างน้อยหนึ่งรายการสำหรับผู้รับสำเนา แยกหลายที่อยู่อีเมลด้วยจุลภาค เช่น `jay@gatsby.com, jon@smith.com`
*   **From Alias Name or ID**: เลือก alias เพื่อส่ง draft จาก รายการใน field นี้จะขึ้นอยู่กับ credential ที่คุณเลือกในพารามิเตอร์
*   **Send Replies To**: ป้อนที่อยู่อีเมลเพื่อตั้งเป็นที่อยู่สำหรับตอบกลับ
*   **Thread ID**: หากคุณต้องการให้ draft นี้แนบไปกับ thread ให้ป้อน ID ของ thread นั้น
*   **To Email**: ป้อนที่อยู่อีเมลอย่างน้อยหนึ่งรายการสำหรับผู้รับ แยกหลายที่อยู่อีเมลด้วยจุลภาค เช่น `jay@gatsby.com, jon@smith.com`

อ้างอิงเอกสาร [Gmail API Method: users.drafts.create](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/create){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Delete a draft

ใช้ operation นี้เพื่อลบ draft

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Draft**
*   **Operation**: เลือก **Delete**
*   **Draft ID**: ป้อน ID ของ draft ที่คุณต้องการลบ

อ้างอิงเอกสาร [Gmail API Method: users.drafts.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/delete){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Get a draft

ใช้ operation นี้เพื่อดึงข้อมูล draft เดียว

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Draft**
*   **Operation**: เลือก **Get**
*   **Draft ID**: ป้อน ID ของ draft ที่คุณต้องการดึงข้อมูล

### Get draft options

ใช้ options เหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม:

*   **Attachment Prefix**: ป้อน prefix สำหรับชื่อของ binary property ที่ node ควรเขียนไฟล์แนบใดๆ ลงไป n8n จะเพิ่ม index ที่เริ่มต้นด้วย `0` ต่อท้าย prefix ตัวอย่างเช่น หากคุณป้อน `attachment_` เป็น prefix ไฟล์แนบแรกจะบันทึกเป็น 'attachment_0'
*   **Download Attachments**: เลือกว่าจะให้ node ดาวน์โหลดไฟล์แนบของ draft (เปิด) หรือไม่ (ปิด)

อ้างอิงเอกสาร [Gmail API Method: users.drafts.get](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/get){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

<!-- vale off -->
## Get Many drafts
<!-- vale on -->

ใช้ operation นี้เพื่อดึงข้อมูลตั้งแต่สอง draft ขึ้นไป

ป้อนพารามิเตอร์เหล่านี้:

*   เลือก **Credential to connect with** หรือสร้างใหม่
*   **Resource**: เลือก **Draft**
*   **Operation**: เลือก **Get Many**
*   **Return All**: เลือกว่าจะให้ node คืนค่า draft ทั้งหมด (เปิด) หรือจำกัดจำนวน (ปิด)
*   **Limit**: ป้อนจำนวน draft สูงสุดที่จะคืนค่า ใช้เฉพาะเมื่อคุณปิด **Return All**

<!-- vale off -->
### Get Many drafts options
<!-- vale on -->

ใช้ options เหล่านี้เพื่อปรับแต่งการทำงานของ node เพิ่มเติม:

*   **Attachment Prefix**: ป้อน prefix สำหรับชื่อของ binary property ที่ node ควรเขียนไฟล์แนบใดๆ ลงไป n8n จะเพิ่ม index ที่เริ่มต้นด้วย `0` ต่อท้าย prefix ตัวอย่างเช่น หากคุณป้อน `attachment_` เป็น prefix ไฟล์แนบแรกจะบันทึกเป็น 'attachment_0'
*   **Download Attachments**: เลือกว่าจะให้ node ดาวน์โหลดไฟล์แนบของ draft (เปิด) หรือไม่ (ปิด)
*   **Include Spam and Trash**: เลือกว่าจะให้ node ดึง draft ในโฟลเดอร์ Spam และ Trash (เปิด) หรือไม่ (ปิด)

อ้างอิงเอกสาร [Gmail API Method: users.drafts.list](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/list){:target=_blank .external-link} สำหรับข้อมูลเพิ่มเติม

## Common issues

สำหรับข้อผิดพลาดหรือปัญหาทั่วไปและขั้นตอนการแก้ไขที่แนะนำ โปรดอ้างอิง [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md)
